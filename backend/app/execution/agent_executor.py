"""
Agent Executor
==============

Coordinates one complete stage execution.

Responsibilities
----------------
• Build AgentContext
• Build / Resume StageSession
• Compose prompts
• Execute the Agent
• Run Reviewer
• Extract approved knowledge
• Return ExecutionResult

The AgentExecutor owns the runtime.

Agents remain completely stateless.
"""

from app.context.builder import ContextBuilder
from app.execution.result import ExecutionResult
from app.memory.manager import MemoryManager
from app.prompts.composer import PromptComposer
from app.review.review_engine import ReviewEngine
from app.session.session_manager import SessionManager
from app.agents.registry.agent_registry import AgentRegistry
from app.llm.manager import LLMManager
from app.llm.request import ChatRequest
class AgentExecutor:

    def __init__(self):

        self.sessions = SessionManager()

        self.context_builder = ContextBuilder()

        self.prompt_composer = PromptComposer()

        self.review = ReviewEngine()

        self.memory = MemoryManager()

        self.registry = AgentRegistry()
        self.llm = LLMManager()

    def execute(
        self,
        execution_context,
    ):

        #
        # Build Context
        #

        execution_context.context = self.context_builder.build(

            project=execution_context.project,
        
            profile=execution_context.profile,
        
            stage=execution_context.stage,
        
            task=execution_context.task,
        
        )

        #
        # Get or Create Stage Session
        #

        session = self.sessions.get_or_create(
            execution_context.project.id,
            execution_context.stage,
        )

        #
        # Compose Prompt
        #

        system_prompt, user_prompt = self.prompt_composer.compose(
            profile=execution_context.profile,
            context=execution_context.context,
            task=execution_context.task,
        )

        #
        # System prompt is added only once.
        #

        if not session.is_started:

            session.add_system(
                system_prompt,
            )

        #
        # Every execution adds a new user request.
        #

        session.add_user(
            user_prompt,
        )

        #
        # Execute Agent
        #

        agent = self.registry.create(

            stage=execution_context.stage,

            profile=execution_context.profile,

        )

        #
        # Agent lifecycle
        #

        agent.before_execute(
        
            execution_context,

            session,

        )

        
        #
        # Prepare request
        #

        messages = agent.prepare(
        
            execution_context,

            session,

        )

        #
        # Build ChatRequest
        #

        request = ChatRequest(
        
            model=execution_context.profile.model,

            messages=messages,

        )

        #
        # Execute LLM
        #

        response = self.llm.chat(
        
            request,

        )

        #
        # Process response
        #

        artifact = agent.process(
        
            response,

            execution_context,

            session,

        )

        #
        # Optional hook
        #

        artifact = agent.after_generate(
        
            artifact,

            execution_context,

            session,

        )

        #
        # Validation
        #

        agent.validate(
        
            artifact,

        )

        #
        # Review Artifact
        #

        review = self.review.review(
            reviewer_response=artifact.content,
            attempt=session.retries,
        )

        #
        # Store reviewer feedback in session
        #

        session.add_review(
            review.comments,
        )

        #
        # Approved
        #

        if review.approved:

            #
            # Extract long-term memories
            #

            self.memory.extract(
                session=session,
                artifact=artifact,
            )

            #
            # Destroy Stage Session
            #

            self.sessions.close(
                execution_context.project.id,
                execution_context.stage,
            )

        else:

            session.increment_retry()

        #
        # Return execution result
        #

        return ExecutionResult(

            stage=execution_context.stage,

            output=artifact.content,

            approved=review.approved,

            review=review.comments,

            attempt=session.retries,

            metadata={
                "artifact": artifact,
            },
        )
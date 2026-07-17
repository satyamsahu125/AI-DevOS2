# AI DevOS — Execution Framework

Version: 1.0

---

# 1. Purpose

The Execution Framework coordinates the execution of a single workflow stage.

It combines the Context Framework, Agent Framework, Review Framework, Memory Framework, and LLM Framework into one deterministic execution pipeline.

Unlike the Workflow Engine, which decides *what* to execute, the Execution Framework decides *how* a stage executes.

---

# 2. Design Philosophy

The Execution Framework follows one principle.

> One execution.
>
> One context.
>
> One agent.
>
> One artifact.

Every stage follows the exact same execution pipeline.

---

# 3. Responsibilities

The Execution Framework is responsible for:

- building execution context
- managing Stage Sessions
- composing prompts
- invoking agents
- executing the LLM
- reviewing outputs
- extracting memory
- returning execution results

It never:

- schedules workflows
- selects stages
- owns long-term memory
- indexes workspace

---

# 4. Architecture

```
Workflow Engine

↓

Execution Framework

↓

Agent Executor

↓

Agent

↓

LLM

↓

Artifact

↓

Reviewer

↓

Memory Extraction

↓

Execution Result
```

---

# 5. Core Components

The framework consists of:

```
ExecutionContext

ExecutionResult

StageSession

AgentExecutor

PromptComposer

ReviewEngine

MemoryManager
```

Each component owns exactly one responsibility.

---

# 6. ExecutionContext

ExecutionContext represents the complete runtime input for one stage.

It contains:

- project
- stage
- task
- stage profile
- AgentContext

ExecutionContext is immutable during execution.

---

# 7. ExecutionResult

ExecutionResult represents the final outcome of one execution.

Typical fields

- stage
- output
- approved
- review
- attempt
- metadata

The Workflow Engine consumes this object.

---

# 8. StageSession

StageSession stores the temporary runtime conversation.

Contents

- system prompt
- user prompts
- assistant responses
- reviewer feedback
- retry count
- generated artifacts

The StageSession is destroyed after successful completion.

---

# 9. Session Lifecycle

```
Create

↓

System Prompt

↓

User Prompt

↓

Assistant

↓

Reviewer

↓

Retry?

↓

Destroy
```

No StageSession survives beyond the active stage.

---

# 10. AgentExecutor

The AgentExecutor coordinates the complete execution lifecycle.

Responsibilities

- build context
- manage sessions
- compose prompts
- execute agents
- invoke reviewers
- extract memory
- return ExecutionResult

The AgentExecutor owns the runtime.

---

# 11. Execution Pipeline

Every execution follows the same sequence.

```
ExecutionContext

↓

ContextBuilder

↓

PromptComposer

↓

StageSession

↓

Agent

↓

LLMManager

↓

StageArtifact

↓

ReviewEngine

↓

Memory Extraction

↓

ExecutionResult
```

---

# 12. Prompt Composition

The PromptComposer creates:

- system prompt
- user prompt

Inputs

- StageProfile
- AgentContext
- task

Outputs

- system message
- user message

The composer never communicates with the LLM.

---

# 13. Agent Lifecycle

During execution the AgentExecutor invokes

```
before_execute()

↓

prepare()

↓

LLM

↓

process()

↓

after_generate()

↓

validate()
```

Every specialized agent follows this lifecycle.

---

# 14. LLM Execution

The AgentExecutor never communicates directly with providers.

Instead

```
AgentExecutor

↓

LLMManager

↓

LLMRuntime

↓

ProviderFactory

↓

Provider
```

This guarantees provider independence.

---

# 15. Artifact Generation

The agent converts the ChatResponse into a StageArtifact.

Typical artifacts include

- requirements
- architecture
- source code
- test cases
- deployment scripts

Every execution produces exactly one artifact.

---

# 16. Review Process

The StageArtifact is immediately sent to the Review Engine.

Possible outcomes

Approved

↓

Continue

Rejected

↓

Retry

The agent never reviews its own work.

---

# 17. Retry Flow

When rejected

```
Reviewer Feedback

↓

StageSession

↓

Retry Count++

↓

Prompt Updated

↓

Agent Executes Again
```

Previous conversation remains available.

---

# 18. Memory Extraction

Only approved artifacts are extracted.

```
Artifact

↓

Extraction Pipeline

↓

MemoryManager

↓

Providers
```

Rejected artifacts never enter long-term memory.

---

# 19. Runtime Memory

Runtime Memory exists only during execution.

Examples

- temporary planning
- retry metadata
- execution state

Destroyed after stage completion.

---

# 20. Error Handling

Possible failures

Provider Failure

↓

Abort Execution

Validation Failure

↓

Abort Review

Review Failure

↓

Retry

Extraction Failure

↓

Abort Completion

Errors are isolated to their owning subsystem.

---

# 21. Execution Guarantees

The Execution Framework guarantees:

✓ Exactly one ExecutionContext

✓ Exactly one StageSession

✓ Exactly one StageArtifact

✓ Review before completion

✓ Memory extraction only after approval

✓ Deterministic execution

---

# 22. Design Decisions

Execution intentionally separates

Context

↓

Generation

↓

Review

↓

Memory

↓

Workflow

Each subsystem performs one responsibility.

---

# 23. Future Improvements

Future versions may include:

- streaming execution
- multi-agent execution
- parallel execution
- human approval checkpoints
- distributed execution
- execution metrics dashboard

The execution pipeline remains unchanged.

---

# 24. Summary

The Execution Framework transforms a workflow stage into an approved project artifact through a deterministic pipeline of context construction, prompt composition, AI generation, review, and memory extraction.

By coordinating independent subsystems while preserving clear ownership boundaries, it provides a scalable, testable, and provider-independent execution model for AI DevOS.
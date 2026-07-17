# AI DevOS — Agent Framework

Version: 1.0

---

# 1. Purpose

The Agent Framework defines how every AI agent inside AI DevOS is implemented.

It provides a common lifecycle, standard interfaces, and shared execution behavior while allowing each specialized agent to focus only on its domain.

Every agent in AI DevOS inherits from `BaseAgent`.

---

# 2. Design Philosophy

AI DevOS follows one fundamental principle:

> Agents generate work.
> The framework manages everything else.

Agents are intentionally lightweight and stateless.

They never own:

- workflow
- memory
- execution
- sessions
- prompts
- provider communication

They only transform an execution context into a stage artifact.

---

# 3. Agent Architecture

```
Workflow Engine
        │
        ▼
Agent Executor
        │
        ▼
Agent Registry
        │
        ▼
Specialized Agent
        │
        ▼
BaseAgent
        │
        ▼
StageArtifact
```

---

# 4. Agent Responsibilities

Every agent is responsible for:

- interpreting the execution context
- preparing LLM messages
- processing the LLM response
- validating the generated artifact
- optionally performing post-processing

Agents never:

- call MemoryManager
- control workflow
- update workspace
- communicate with providers
- manage retries

---

# 5. BaseAgent

Every specialized agent inherits from:

```
BaseAgent
```

The BaseAgent provides:

- lifecycle hooks
- default implementations
- common processing
- artifact creation

It ensures every agent behaves consistently.

---

# 6. Agent Lifecycle

Every execution follows the same lifecycle.

```
before_execute()

↓

prepare()

↓

LLM Execution

↓

process()

↓

after_generate()

↓

validate()

↓

StageArtifact
```

Each step has a single responsibility.

---

# 7. Lifecycle Methods

## before_execute()

Purpose

Prepare the agent before generation.

Typical uses

- initialize metadata
- inspect runtime state
- prepare temporary variables

Default implementation does nothing.

---

## prepare()

Purpose

Prepare messages for the LLM.

Input

- AgentContext
- StageSession

Output

```
list[Message]
```

The default implementation returns the complete session conversation.

Agents may override this to customize prompts.

---

## process()

Purpose

Convert a ChatResponse into a StageArtifact.

Responsibilities

- store assistant message
- create StageArtifact
- attach metadata

Every successful generation produces exactly one artifact.

---

## after_generate()

Optional post-processing.

Examples

Developer Agent

↓

Format generated code

QA Agent

↓

Parse generated test cases

DevOps Agent

↓

Validate deployment scripts

Default implementation returns the artifact unchanged.

---

## validate()

Purpose

Verify artifact quality.

Examples

- empty output
- malformed JSON
- invalid code
- missing sections

Validation errors stop execution before review.

---

# 8. Stateless Design

Agents are stateless.

This means they never retain information between executions.

Instead, all required information is supplied through:

```
ExecutionContext

+

StageSession
```

Benefits

- deterministic execution
- easy testing
- provider independence
- scalability

---

# 9. Specialized Agents

Current agents include:

```
ProductOwnerAgent

ArchitectAgent

BackendDesignerAgent

FrontendDesignerAgent

BackendDeveloperAgent

FrontendDeveloperAgent

QAAgent

DevOpsAgent
```

Each agent differs only in business logic.

Execution remains identical.

---

# 10. Stage Profiles

Agents are configured using StageProfile.

StageProfile defines:

- stage name
- prompt template
- agent class
- accessible memories
- readable documents
- workspace permissions
- tools
- review requirements

This separates configuration from implementation.

---

# 11. Agent Registry

The AgentRegistry maps workflow stages to agent implementations.

Example

```
ProductOwner

↓

ProductOwnerAgent

Architect

↓

ArchitectAgent

QA

↓

QAAgent
```

The AgentExecutor never creates agents directly.

It always uses the registry.

---

# 12. StageArtifact

Every agent returns a StageArtifact.

StageArtifact represents the official output of a workflow stage.

Typical fields

- stage
- content
- metadata
- generated files
- execution metrics

Artifacts are immutable after approval.

---

# 13. Execution Context

Agents receive only one object:

```
ExecutionContext
```

ExecutionContext includes

- project
- stage
- task
- profile
- AgentContext

Agents never fetch dependencies manually.

---

# 14. AgentContext

AgentContext contains everything required for generation.

Including

- memory
- workspace index
- project documents
- review history
- runtime memory
- metadata

It is created by the ContextBuilder.

---

# 15. Interaction with the LLM

Agents never call providers directly.

Instead

```
Agent

↓

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

This allows providers to change without modifying agents.

---

# 16. Interaction with Memory

Agents never write memory.

Instead

```
StageArtifact

↓

Extraction Pipeline

↓

MemoryManager

↓

Providers
```

This prevents inconsistent memory formats.

---

# 17. Interaction with Review

Agents never decide whether their work is acceptable.

Instead

```
Artifact

↓

Review Engine

↓

Approved?

↓

Continue

or

Retry
```

Quality control remains centralized.

---

# 18. Error Handling

Agents should report only generation-related errors.

Framework-level failures are handled elsewhere.

Examples

Handled by Agent

- invalid output
- malformed response

Handled by Framework

- provider unavailable
- retry policy
- workflow progression
- persistence

---

# 19. Extension Points

Developers can extend the framework by:

- creating new agent classes
- overriding lifecycle hooks
- adding custom validation
- introducing domain-specific post-processing

No changes to BaseAgent are required.

---

# 20. Design Decisions

The Agent Framework intentionally separates:

Generation

↓

Execution

↓

Memory

↓

Workflow

↓

Review

This keeps each subsystem independent.

---

# 21. Future Improvements

Future versions may include

- Tool calling
- Multi-agent collaboration
- Streaming responses
- Self-reflection
- Planning agents
- Autonomous code repair
- Human-in-the-loop execution

The lifecycle remains unchanged.

---

# 22. Runtime Guarantees

The Agent Framework guarantees:

✓ Every agent is stateless

✓ Every agent follows the same lifecycle

✓ Every generation produces one StageArtifact

✓ Agents never own memory

✓ Agents never control workflow

✓ Providers remain interchangeable

✓ Agent implementations remain replaceable

---

# 23. Summary

The Agent Framework standardizes how AI DevOS agents behave while allowing specialized implementations for different software engineering roles.

By separating generation from orchestration, memory, review, and provider communication, the framework remains modular, testable, extensible, and provider-independent.
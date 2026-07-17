# AI DevOS — System Architecture

Version: 1.0

---

# 1. Purpose

This document defines the complete architecture of AI DevOS.

It explains every subsystem, the ownership of responsibilities, the interaction between components, and the design principles that govern the framework.

Unlike implementation documents, this specification describes **how the system is organized**, not how individual classes are implemented.

---

# 2. Architectural Philosophy

AI DevOS follows a layered architecture.

Each layer has a single responsibility.

Every layer communicates only through well-defined interfaces.

No layer bypasses another layer.

This minimizes coupling while maximizing extensibility.

---

# 3. High-Level Architecture

```text
                    +----------------------+
                    |   Workflow Engine    |
                    +----------+-----------+
                               |
                               v
                    +----------------------+
                    |   Agent Executor     |
                    +----------+-----------+
                               |
                               v
                    +----------------------+
                    |   Context Builder    |
                    +----------+-----------+
                               |
           +-------------------+------------------+
           |                   |                  |
           v                   v                  v
     Memory Selector   Workspace Selector   Document Selector
           |                   |                  |
           +-------------------+------------------+
                               |
                               v
                    +----------------------+
                    |    Agent Context     |
                    +----------+-----------+
                               |
                               v
                    +----------------------+
                    |     Base Agent       |
                    +----------+-----------+
                               |
                               v
                    +----------------------+
                    |     LLM Manager      |
                    +----------+-----------+
                               |
                               v
                    +----------------------+
                    |    LLM Runtime       |
                    +----------+-----------+
                               |
                               v
                    +----------------------+
                    | Provider Factory     |
                    +----------+-----------+
                               |
          +----------+----------+----------+----------+
          |          |          |          |          |
          v          v          v          v          v
      Gemini      Ollama     OpenAI     Claude   Future Providers

                               |
                               v

                    +----------------------+
                    |   Stage Artifact     |
                    +----------+-----------+
                               |
                               v
                    +----------------------+
                    |   Review Engine      |
                    +----------+-----------+
                               |
                 +-------------+--------------+
                 |                            |
            Approved                     Rejected
                 |                            |
                 v                            |
      Memory Extraction                  Retry Stage
                 |
                 v
          Memory Manager
                 |
                 v
        Workflow Progression
```

---

# 4. Layered Architecture

AI DevOS consists of nine architectural layers.

| Layer | Responsibility |
|-------|----------------|
| Workflow | Controls project execution |
| Execution | Executes one workflow stage |
| Context | Builds execution context |
| Agent | Generates artifacts |
| LLM | Communicates with providers |
| Review | Validates generated work |
| Memory | Owns every memory type |
| Workspace | Indexes project files |
| Prompt | Generates LLM prompts |

---

# 5. Workflow Layer

## Responsibility

Coordinates the complete software development lifecycle.

Owns:

- workflow order
- retries
- stage transitions
- completion
- dependencies

Never:

- calls LLMs
- loads memory
- modifies workspace

---

# 6. Execution Layer

The execution layer performs exactly one workflow stage.

Components

```
Execution Engine

↓

Agent Executor

↓

Execution Result
```

Responsibilities

- create session
- build context
- execute agent
- review output
- extract memory
- return execution result

---

# 7. Context Layer

The Context Layer prepares everything an agent needs.

Architecture

```
Context Builder

↓

Memory Selector

↓

Workspace Selector

↓

Document Selector

↓

Review Selector

↓

Context Budget

↓

Agent Context
```

Responsibilities

- load long-term memory
- load runtime memory
- load indexed workspace
- load project documents
- trim context

The Context Layer never communicates directly with LLM providers.

---

# 8. Agent Layer

Agents are intentionally stateless.

Each agent performs one responsibility.

Lifecycle

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

Agents never:

- create sessions
- update workflow
- store memory
- scan workspace
- call providers directly

---

# 9. LLM Layer

Architecture

```
BaseAgent

↓

LLMManager

↓

LLMRuntime

↓

ProviderFactory

↓

BaseProvider

↓

Gemini

Ollama

OpenAI

Claude
```

Only ProviderFactory knows which provider is active.

This enables provider-independent execution.

---

# 10. Review Layer

Every generated artifact passes through the reviewer.

Architecture

```
Review Engine

↓

Review Parser

↓

Change Planner

↓

Review Result
```

Possible outcomes

- Approved
- Changes Required

Only approved artifacts continue to memory extraction.

---

# 11. Memory Layer

Memory ownership is centralized.

```
Memory Manager

↓

Providers

↓

Extraction Pipeline

↓

Memory Stores
```

The Memory Manager owns every memory operation.

Nothing writes directly into memory.

This guarantees:

- consistent APIs
- auditing
- versioning
- future persistence

---

# 12. Workspace Layer

The Workspace Layer never reads source code.

It indexes metadata only.

Architecture

```
Workspace Registry

↓

Workspace Index

↓

Workspace Parser
```

Responsibilities

- file indexing
- checksum tracking
- module lookup

Future versions will include AST parsing.

---

# 13. Prompt Layer

The Prompt Layer builds prompts.

Architecture

```
Prompt Loader

↓

Prompt Composer

↓

LLM Request
```

Responsibilities

- load templates
- merge context
- create system prompt
- create user prompt

---

# 14. Data Ownership

Every major object has a single owner.

| Object | Owner |
|---------|-------|
| Workflow | Workflow Engine |
| Stage Session | Session Manager |
| Runtime Memory | Memory Manager |
| Long-Term Memory | Memory Manager |
| Workspace Index | Workspace Registry |
| Prompt Templates | Prompt Loader |
| Agent Context | Context Builder |
| Review Result | Review Engine |
| Execution Result | Agent Executor |

No object has multiple owners.

---

# 15. Dependency Rules

Allowed

```
Workflow

↓

Execution

↓

Context

↓

Agent

↓

LLM
```

Forbidden

Agent → Workflow

Agent → Memory Manager

Agent → Workspace

LLM → Memory

Review → Workflow

Workspace → LLM

Memory → LLM

These restrictions maintain loose coupling.

---

# 16. Design Principles

Every subsystem follows these principles.

## Single Responsibility

Each component performs one task.

## Dependency Inversion

High-level modules depend on abstractions.

## Stateless Agents

Agents own no persistent state.

## Centralized Memory

MemoryManager owns all memory.

## Review Before Persistence

Artifacts are reviewed before entering long-term memory.

## Provider Independence

LLM providers are interchangeable.

## Backend Independence

Execution engines are interchangeable.

---

# 17. Extension Points

AI DevOS is designed for extension.

New components can be added without modifying existing architecture.

Supported extensions

- new workflow stages
- new AI agents
- new LLM providers
- new execution engines
- new memory types
- new review strategies
- new workspace parsers

---

# 18. Architecture Summary

The architecture separates orchestration, execution, context construction, generation, review, memory, and workspace management into independent layers.

Each layer owns exactly one responsibility.

This organization minimizes coupling, improves maintainability, enables provider independence, and provides a scalable foundation for autonomous software engineering.
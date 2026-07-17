# AI DevOS Handbook

> **Version:** 2.0  
> **Project:** AI DevOS – AI Software Engineering Operating System  
> **Author:** Satyam Sahu

---

# 1. Introduction

## What is AI DevOS?

AI DevOS is an **AI Software Engineering Operating System** designed to automate and orchestrate the complete software development lifecycle using specialized AI agents.

Unlike traditional AI coding assistants that generate code from prompts, AI DevOS coordinates multiple frameworks responsible for planning, context building, execution, memory management, reviewing, and artifact generation.

The platform is built around deterministic execution, modular architecture, and provider independence, allowing different AI models and execution engines to be integrated without changing the core system.

---

## Vision

The long-term vision of AI DevOS is to transform software engineering into a structured pipeline where autonomous AI agents collaborate to convert business requirements into production-ready software.

Instead of focusing on individual code generation, AI DevOS manages the entire engineering process:

```text
Business Requirement
        │
        ▼
Product Planning
        │
        ▼
Architecture Design
        │
        ▼
Code Generation
        │
        ▼
Testing
        │
        ▼
Deployment
        │
        ▼
Continuous Improvement
```

Each stage is executed independently while remaining connected through shared context and project memory.

---

# 2. Core Design Principles

AI DevOS is built on several architectural principles that remain constant across every framework.

## Stateless Agents

Agents never own execution state.

An agent receives an `ExecutionContext`, generates a `StageArtifact`, and exits.

Agents never:

- load memory
- manage sessions
- update workflow
- communicate directly with providers
- modify workspace
- save documents

This makes every agent reusable, deterministic, and easy to test.

---

## Single Responsibility

Each framework owns exactly one responsibility.

| Framework | Responsibility |
|-----------|----------------|
| Workflow | Controls execution order |
| Execution | Executes workflow stages |
| Context | Builds execution context |
| Agent | Generates artifacts |
| Review | Validates generated artifacts |
| Memory | Stores project knowledge |
| Workspace | Indexes project files |
| LLM | Communicates with AI providers |

No framework performs responsibilities belonging to another.

---

## Review Before Approval

Generated artifacts are never considered project knowledge immediately.

Every artifact follows the same lifecycle:

```text
Generate

↓

Review

↓

Approved?

↓

Yes → Memory

No → Retry
```

Only approved artifacts become part of long-term memory.

---

## Centralized Memory Ownership

Memory is owned exclusively by the Memory Framework.

Agents never write memory directly.

Instead:

```text
Stage Artifact

↓

Extraction Pipeline

↓

Memory Manager

↓

Memory Provider
```

This guarantees consistent project knowledge.

---

## Provider Independence

AI DevOS never communicates directly with Gemini, Ollama, OpenAI, Claude, or any other provider.

Every provider implements the same interface.

```text
LLM Manager

↓

LLM Runtime

↓

Provider Factory

↓

Base Provider

↓

Gemini / Ollama / OpenAI / Claude
```

Replacing one provider requires no changes to the rest of the system.

---

## Deterministic Execution

Workflow execution always follows predefined stage dependencies.

Example:

```text
Product Owner

↓

Architect

↓

Backend

↓

Frontend

↓

QA

↓

DevOps
```

Each stage begins only after its dependencies have been successfully approved.

---

## Modular Frameworks

Every framework is isolated.

Communication occurs only through well-defined interfaces.

Benefits include:

- easier testing
- independent evolution
- minimal coupling
- clear ownership
- simpler maintenance

---

# 3. AI DevOS at a Glance

The platform is organized around a central AI Kernel that coordinates multiple independent frameworks.

```text
                        AI DevOS

                       AI Kernel
                            │
        ┌───────────────────┼───────────────────┐
        │                   │                   │
 Workflow Engine      Memory Manager     Workspace Registry
        │                   │                   │
        └──────────────┬────┴────┬──────────────┘
                       │         │
                 Context Builder Runtime Memory
                       │
                Execution Framework
                       │
                 Agent Framework
                       │
                Prompt Composer
                       │
                  LLM Framework
                       │
                Provider Factory
                       │
      Gemini • Ollama • OpenAI • Claude
```

The AI Kernel coordinates every framework while keeping them independent from one another.

Business logic resides inside individual frameworks rather than the kernel itself.

---

**Next:** Chapter 4 – AI Kernel


# 4. AI Kernel

## Overview

The **AI Kernel** is the central coordinator of AI DevOS.

It does **not** generate code, review artifacts, manage memory, or execute workflows directly.

Instead, it initializes, connects, and coordinates all independent frameworks that make up the platform.

Think of it as the operating system kernel for software engineering.

Just as an operating system kernel manages CPU scheduling, memory, devices, and processes without implementing applications itself, the AI Kernel manages the lifecycle of the AI DevOS frameworks while keeping each framework independent.

---

## Responsibilities

The AI Kernel is responsible for:

- Initializing every framework
- Registering shared services
- Managing dependency injection
- Loading configuration
- Starting and shutting down the platform
- Coordinating framework communication
- Providing extension points for future plugins

The AI Kernel never contains business logic.

Business logic always belongs to individual frameworks.

---

## High-Level Architecture

```text
                     AI DevOS

                     AI Kernel
                          │
 ┌────────────────────────┼────────────────────────┐
 │                        │                        │
Workflow Engine      Memory Manager      Workspace Registry
 │                        │                        │
 └───────────────┬────────┴────────┬──────────────┘
                 │                 │
          Context Builder   Runtime Memory
                 │
          Execution Framework
                 │
           Agent Framework
                 │
          Prompt Composer
                 │
            LLM Framework
                 │
          Provider Factory
                 │
 Gemini • Ollama • OpenAI • Claude
```

The kernel sits above every framework.

No framework owns another framework.

Instead, the kernel coordinates them.

---

## Why an AI Kernel?

Without a kernel, every framework would need to know about every other framework.

For example:

- Agents would load memory.
- Workflow would call providers directly.
- Memory would update workflows.
- Review would communicate with execution.

This creates tight coupling and makes the architecture difficult to maintain.

Instead, AI DevOS keeps every subsystem focused on one responsibility.

---

## Framework Ownership

Each framework owns exactly one responsibility.

| Framework | Owns |
|-----------|------|
| Workflow | Stage ordering |
| Execution | Stage execution |
| Context | Context construction |
| Agent | Artifact generation |
| Memory | Project knowledge |
| Review | Artifact validation |
| Workspace | File indexing |
| LLM | AI provider communication |

This separation allows every framework to evolve independently.

---

## Dependency Direction

Dependencies always flow downward.

```text
AI Kernel

↓

Workflow Framework

↓

Execution Framework

↓

Context Framework

↓

Agent Framework

↓

LLM Framework

↓

Provider
```

Shared frameworks:

```text
Memory Framework

Workspace Framework

Review Framework
```

These frameworks are services that can be used by Execution and Context but never own them.

Circular dependencies are not allowed.

---

## Startup Sequence

When AI DevOS starts, the kernel initializes the frameworks in dependency order.

```text
Load Configuration

↓

Initialize Memory

↓

Initialize Workspace

↓

Initialize Workflow

↓

Initialize Context

↓

Initialize Execution

↓

Initialize LLM

↓

System Ready
```

Every framework is initialized only once.

---

## Shutdown Sequence

When execution finishes, the kernel performs a controlled shutdown.

```text
Finish Running Stages

↓

Flush Runtime Memory

↓

Persist Approved Knowledge

↓

Close Sessions

↓

Shutdown Services
```

Only approved project knowledge survives shutdown.

Runtime state is discarded.

---

## Future Responsibilities

The current implementation focuses on orchestration.

Future versions of the AI Kernel will also manage:

- Plugin loading
- Event bus
- Scheduler
- Metrics collection
- Service discovery
- Distributed execution
- Health monitoring
- MCP integration

These additions will not change the responsibilities of the existing frameworks.

Instead, they extend the kernel while preserving the same architectural principles.

---

## Key Takeaways

- The AI Kernel is the central coordinator of AI DevOS.
- It owns lifecycle management, not business logic.
- Every framework remains independent.
- Dependencies always flow in one direction.
- New capabilities should be added through the kernel rather than by coupling frameworks together.

# 5. Runtime Architecture

## Overview

The Runtime Architecture defines how a single workflow stage is executed inside AI DevOS.

Every stage follows the same deterministic execution pipeline regardless of whether it is Product Owner, Architect, Backend Developer, QA, or DevOps.

The runtime is coordinated by the **Execution Framework**, which prepares the execution environment, invokes the appropriate AI agent, validates the generated artifact, runs the reviewer, and persists approved knowledge.

---

# Runtime Components

The runtime is composed of six primary objects.

```text
ExecutionContext

↓

StageProfile

↓

StageSession

↓

StageArtifact

↓

Review

↓

ExecutionResult
```

Each object has a single responsibility.

---

# ExecutionContext

The `ExecutionContext` is the only object consumed by an agent.

It represents everything required to execute one workflow stage.

The context is built by the **Context Builder** before execution begins.

It contains:

- Project
- Current Stage
- Task
- Context
- Runtime Memory
- Stage Profile

Agents never access MemoryManager, Workflow Engine, or Workspace directly.

Instead, they receive an `ExecutionContext`.

```text
Workflow

↓

Context Builder

↓

ExecutionContext

↓

Agent
```

---

# StageProfile

A `StageProfile` describes the capabilities of a workflow stage.

It is metadata only.

It never contains business logic.

Typical configuration includes:

- Stage name
- Prompt template
- Agent implementation
- Memory permissions
- Workspace permissions
- Document permissions
- Available tools
- Review requirements

Example:

```text
Architect

↓

Prompt: architect.md

↓

Agent: ArchitectAgent

↓

Memory:
Architecture

↓

Workspace:
Read / Write
```

Stage profiles make every stage configurable without changing the runtime.

---

# StageSession

A `StageSession` represents the temporary runtime conversation of a single stage.

It exists only while the stage is executing.

The session stores:

- Conversation history
- Reviewer feedback
- Retry count
- Runtime artifacts
- Temporary metadata

Example lifecycle:

```text
Created

↓

Agent Response

↓

Reviewer Feedback

↓

Retry

↓

Reviewer

↓

Approved

↓

Destroyed
```

Once a stage is approved, the session is destroyed.

Only approved knowledge is extracted into long-term memory.

---

# Why Stage Sessions Are Temporary

Stage sessions intentionally do **not** become permanent project knowledge.

Reasons:

- Prevent stale conversations
- Keep execution isolated
- Support deterministic retries
- Reduce memory usage
- Avoid polluting project memory

Only approved artifacts survive.

---

# Runtime Memory

Runtime Memory stores temporary information shared during execution.

Examples:

- current retry count
- temporary variables
- execution state
- intermediate calculations

Runtime Memory differs from StageSession.

| Stage Session | Runtime Memory |
|---------------|----------------|
| Conversation | Temporary state |
| Reviewer feedback | Execution variables |
| Artifacts | Runtime cache |
| Destroyed after approval | Destroyed after execution |

Neither becomes long-term knowledge.

---

# StageArtifact

A `StageArtifact` is the output generated by an agent.

Examples include:

- Requirements document
- Software architecture
- Backend code
- Frontend code
- Test cases
- Deployment configuration

A StageArtifact contains:

- Stage
- Content
- Metadata
- Generated timestamp (optional)
- Validation information (optional)

Artifacts are reviewed before they become project knowledge.

```text
Agent

↓

StageArtifact

↓

Reviewer
```

---

# Review Process

Every generated artifact follows the same review pipeline.

```text
StageArtifact

↓

Review Engine

↓

Approved?

↓

Yes

↓

Memory Extraction

↓

Next Stage

No

↓

Reviewer Feedback

↓

Retry
```

The reviewer determines whether the stage can continue.

---

# ExecutionResult

The `ExecutionResult` is returned by the Execution Framework after a stage finishes.

It summarizes the entire execution.

Typical fields include:

- Stage
- Output
- Approval status
- Review comments
- Retry count
- Generated artifact

Workflow Engine uses the `ExecutionResult` to decide whether the next stage can begin.

---

# Complete Runtime Flow

The complete runtime sequence is shown below.

```text
Workflow Engine

↓

ExecutionContext

↓

StageProfile

↓

StageSession

↓

Prompt Composer

↓

Agent

↓

LLM

↓

StageArtifact

↓

Review Engine

↓

Approved?

↓

Yes

↓

Memory Extraction

↓

ExecutionResult

↓

Next Stage
```

If rejected:

```text
Reviewer Feedback

↓

StageSession

↓

Retry

↓

Agent

↓

Reviewer
```

The cycle repeats until the reviewer approves the artifact or the retry policy is exhausted.

---

# Runtime Object Relationships

```text
ExecutionContext
        │
        │ contains
        ▼
StageProfile
        │
        ▼
StageSession
        │
        ▼
Agent
        │
        ▼
StageArtifact
        │
        ▼
Review Engine
        │
        ▼
ExecutionResult
```

Each object owns a single responsibility and communicates only through well-defined interfaces.

---

# Key Takeaways

- Every stage executes through the same runtime pipeline.
- Agents consume only `ExecutionContext`.
- `StageProfile` defines stage capabilities.
- `StageSession` is temporary and isolated.
- `StageArtifact` represents generated work.
- `ExecutionResult` summarizes the execution.
- Only approved artifacts become long-term memory.
- Runtime objects are intentionally separated to keep execution deterministic, modular, and maintainable.

# 6. Framework Interaction

## Overview

AI DevOS is built as a collection of independent frameworks.

Each framework owns exactly one responsibility and communicates only through clearly defined interfaces.

No framework contains business logic belonging to another framework.

This separation makes the platform modular, maintainable, and easy to extend.

---

# Framework Overview

The following frameworks make up the AI DevOS architecture.

| Framework | Responsibility |
|-----------|----------------|
| AI Kernel | Coordinates the platform |
| Workflow Framework | Controls stage execution order |
| Execution Framework | Executes workflow stages |
| Context Framework | Builds execution context |
| Agent Framework | Generates stage artifacts |
| LLM Framework | Communicates with AI providers |
| Review Framework | Validates generated artifacts |
| Memory Framework | Stores project knowledge |
| Workspace Framework | Indexes project files |

Each framework is independent and communicates through explicit contracts.

---

# End-to-End Framework Flow

The complete execution pipeline is shown below.

```text
                  AI Kernel
                       │
                       ▼
              Workflow Framework
                       │
                       ▼
             Execution Framework
                       │
                       ▼
              Context Framework
                       │
        ┌──────────────┼──────────────┐
        │              │              │
        ▼              ▼              ▼
 Memory Framework Workspace Framework Review History
        │              │
        └───────┬──────┘
                ▼
         ExecutionContext
                │
                ▼
         Prompt Composer
                │
                ▼
          Agent Framework
                │
                ▼
          LLM Framework
                │
                ▼
        Provider Factory
                │
                ▼
 Gemini • Ollama • OpenAI • Claude
                │
                ▼
          Stage Artifact
                │
                ▼
         Review Framework
                │
        Approved ?
         │             │
         │             │
         ▼             ▼
 Memory Extraction    Retry
         │
         ▼
 Workflow Framework
         │
         ▼
 Next Stage
```

This pipeline remains identical for every workflow stage.

---

# Workflow → Execution

The Workflow Framework decides **what should execute**.

It does not execute anything itself.

Responsibilities:

- determine next stage
- verify dependencies
- create ExecutionContext
- invoke Execution Framework

```text
Workflow

↓

Execution
```

---

# Execution → Context

The Execution Framework prepares the execution environment.

Instead of loading information directly, it delegates to the Context Framework.

```text
Execution

↓

Context Builder
```

Execution never reads memory or workspace directly.

---

# Context → Memory

The Context Framework requests only the information required by the current stage.

```text
Memory Selector

↓

Memory Manager

↓

Business Memory

Architecture Memory

Decision Memory
```

Only relevant knowledge is returned.

---

# Context → Workspace

The Context Framework retrieves project metadata through the Workspace Framework.

```text
Workspace Selector

↓

Workspace Registry

↓

Indexed Files
```

The workspace is never scanned during execution.

---

# Context → Review

Reviewer feedback from previous retries is added to the execution context.

```text
Review Selector

↓

Stage Session

↓

Reviewer Feedback
```

This allows the next attempt to improve the artifact.

---

# Context → Agent

After context construction, the Execution Framework creates an `ExecutionContext`.

```text
Memory

Workspace

Documents

Review

↓

Agent Context

↓

Agent
```

Agents receive only this object.

---

# Agent → LLM

Agents never communicate directly with providers.

Instead:

```text
Agent

↓

LLM Manager

↓

LLM Runtime

↓

Provider Factory

↓

Provider
```

This keeps providers interchangeable.

---

# Provider → Agent

The provider returns a standardized `ChatResponse`.

```text
Provider

↓

ChatResponse

↓

Agent
```

The agent converts the response into a `StageArtifact`.

---

# Agent → Review

Generated artifacts are immediately reviewed.

```text
Stage Artifact

↓

Review Engine

↓

Review Result
```

The reviewer decides whether the stage can continue.

---

# Review → Memory

Approved artifacts become project knowledge.

```text
Approved Artifact

↓

Extraction Pipeline

↓

Memory Manager

↓

Memory Providers
```

Rejected artifacts are never stored.

---

# Memory → Workflow

Once extraction finishes, the Workflow Framework receives the execution result.

```text
Execution Result

↓

Workflow

↓

Next Stage
```

The next stage starts only after successful approval.

---

# Communication Rules

Framework communication follows strict rules.

### Allowed

```text
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

---

Shared Services

```text
Memory

Workspace

Review
```

---

### Forbidden

The following interactions are intentionally prohibited.

```text
Agent

✗ Memory Manager

✗ Workflow

✗ Workspace

✗ Providers

✗ Review Engine
```

```text
Memory

✗ Workflow
```

```text
Workspace

✗ Agent
```

```text
Provider

✗ Workflow
```

Every framework communicates through the Execution Framework.

---

# Why This Design?

Separating frameworks provides several benefits.

## Loose Coupling

Changing one framework does not affect the others.

---

## Testability

Each framework can be tested independently.

---

## Replaceability

Components can be replaced without modifying the overall architecture.

Examples:

- Gemini → OpenAI
- Ollama → Claude
- Local execution → Distributed execution

---

## Scalability

Future capabilities such as distributed execution, plugin systems, semantic memory, and multi-agent collaboration can be added without redesigning the architecture.

---

# Key Takeaways

- AI DevOS is composed of independent frameworks.
- Every framework owns one responsibility.
- Frameworks communicate through explicit interfaces.
- Execution always follows the same deterministic pipeline.
- Memory is written only after review approval.
- Providers remain fully interchangeable.
- The architecture is designed for maintainability, extensibility, and long-term evolution.


# 7. Workflow Framework

## Overview

The Workflow Framework controls the execution order of every project.

It transforms a project into a sequence of executable stages while ensuring that every stage respects its dependencies.

The Workflow Framework **never executes agents** and **never communicates with AI providers**.

Its only responsibility is orchestration.

---

# Responsibilities

The Workflow Framework is responsible for:

- Creating workflow stages
- Maintaining execution order
- Validating dependencies
- Determining the next executable stage
- Tracking stage status
- Returning execution results

It is **not** responsible for:

- Generating code
- Building context
- Calling LLMs
- Reviewing artifacts
- Managing memory

---

# Workflow Components

The Workflow Framework consists of the following components.

```text
Workflow

↓

Dependency Graph

↓

Stage Profile

↓

Execution Context

↓

Execution Framework

↓

Execution Result
```

---

# Workflow Lifecycle

Every project follows the same workflow lifecycle.

```text
Project Created

↓

Workflow Generated

↓

Dependency Validation

↓

Stage Execution

↓

Stage Approved

↓

Next Stage

↓

Workflow Completed
```

Each stage must complete successfully before dependent stages begin.

---

# Stage Dependency Graph

Workflow execution is controlled through a dependency graph.

Example:

```text
Product Owner
      │
      ▼
 Architect
   ┌──┴──┐
   ▼     ▼
Backend Frontend
   └──┬──┘
      ▼
      QA
      │
      ▼
    DevOps
```

Rules:

- Architect waits for Product Owner.
- Backend waits for Architect.
- Frontend waits for Architect.
- QA waits for Backend and Frontend.
- DevOps waits for QA.

---

# Stage States

Each stage moves through a predefined lifecycle.

```text
Pending

↓

Ready

↓

Executing

↓

Review

↓

Approved

↓

Completed
```

If rejected:

```text
Review

↓

Changes Required

↓

Retry

↓

Executing
```

The Workflow Framework updates stage status based on the `ExecutionResult`.

---

# Stage Profiles

Each stage is configured using a `StageProfile`.

A profile defines **what a stage is allowed to do**, not **how it does it**.

Typical configuration includes:

- Stage name
- Prompt template
- Agent implementation
- Memory permissions
- Workspace permissions
- Document permissions
- Tools
- Review requirements

Example:

```text
Architect

↓

Prompt:
architect.md

↓

Agent:
ArchitectAgent

↓

Read Memory:
Business

↓

Write Memory:
Architecture

↓

Workspace:
Read + Write
```

The Workflow Framework loads the profile before execution begins.

---

# Workflow Execution

Once a stage becomes executable:

```text
Workflow

↓

Load Stage Profile

↓

Create ExecutionContext

↓

Execution Framework

↓

Execution Result
```

The Workflow Framework waits until execution completes before continuing.

---

# Handling Approval

If a stage is approved:

```text
Execution Result

↓

Approved

↓

Update Workflow

↓

Unlock Next Stage
```

Dependent stages become eligible for execution.

---

# Handling Rejection

If a reviewer requests changes:

```text
Execution Result

↓

Rejected

↓

Keep Stage Active

↓

Retry

↓

Execution Framework
```

The workflow never advances until the stage is approved.

---

# Why Separate Workflow and Execution?

Workflow decides:

**What should run?**

Execution decides:

**How should it run?**

This separation provides several benefits:

- Independent testing
- Easier maintenance
- Flexible execution engines
- Better scalability

The Workflow Framework never knows how an agent works.

The Execution Framework never decides which stage should execute next.

---

# Framework Interaction

```text
Workflow

↓

Execution

↓

Context

↓

Agent

↓

LLM

↓

Review

↓

Memory

↓

Workflow
```

Notice that execution returns back to the Workflow Framework after completion.

---

# Key Takeaways

- Workflow controls execution order.
- Dependency Graph defines stage relationships.
- Stage Profiles configure stages.
- Workflow never calls LLMs.
- Workflow never generates artifacts.
- Workflow advances only after approval.
- Execution is delegated to the Execution Framework.

# 8. Execution Framework

## Overview

The Execution Framework is responsible for executing a single workflow stage.

Unlike the Workflow Framework, which decides **what should execute**, the Execution Framework determines **how a stage executes**.

Every workflow stage—Product Owner, Architect, Backend, Frontend, QA, and DevOps—passes through the same execution pipeline.

The framework coordinates context construction, prompt generation, agent execution, artifact review, memory extraction, and execution results.

---

# Responsibilities

The Execution Framework is responsible for:

- Building execution context
- Creating or resuming stage sessions
- Composing prompts
- Executing AI agents
- Calling the LLM Framework
- Running artifact review
- Extracting approved knowledge
- Returning execution results

The framework never:

- decides workflow order
- stores long-term memory directly
- indexes workspace files
- communicates with providers directly

---

# Main Components

```text
Execution Framework

│

├── AgentExecutor

├── ExecutionContext

├── PromptComposer

├── StageSession

├── Review Engine

└── ExecutionResult
```

Each component owns exactly one responsibility.

---

# Execution Pipeline

Every stage follows the same execution sequence.

```text
Workflow

↓

ExecutionContext

↓

StageSession

↓

PromptComposer

↓

Agent

↓

LLM

↓

StageArtifact

↓

Review

↓

Memory Extraction

↓

ExecutionResult
```

This pipeline is identical for every stage.

---

# AgentExecutor

The **AgentExecutor** is the runtime coordinator.

It owns the complete execution lifecycle of a stage.

Responsibilities:

- Build execution context
- Create or resume StageSession
- Compose prompts
- Create the correct agent
- Execute the LLM
- Process responses
- Run reviewer
- Extract approved memory
- Return execution results

The AgentExecutor does **not** generate code itself.

It coordinates other components.

---

# ExecutionContext

The ExecutionContext contains everything required for one execution.

Typical fields include:

- Project
- Stage
- Task
- Stage Profile
- Agent Context
- Runtime Memory

It is passed through the entire execution pipeline.

```text
Workflow

↓

ExecutionContext

↓

Agent
```

Agents never communicate with other frameworks directly.

---

# StageSession

The StageSession represents the temporary runtime conversation for one stage.

It stores:

- system prompt
- user prompts
- assistant responses
- reviewer feedback
- retry count
- temporary artifacts

Lifecycle:

```text
Created

↓

Agent

↓

Reviewer

↓

Retry

↓

Approved

↓

Destroyed
```

Sessions are never persisted after approval.

---

# Prompt Composer

The Prompt Composer builds the complete prompt sent to the LLM.

It combines:

```text
System Prompt

+

Task

+

Context

↓

LLM Messages
```

The Prompt Composer never calls the LLM.

It only prepares prompts.

---

# Agent Execution

After prompts are prepared:

```text
Agent

↓

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

Each hook has a single responsibility.

---

## before_execute()

Optional initialization.

Examples:

- initialize runtime
- prepare tools
- setup execution state

---

## prepare()

Creates the message list sent to the LLM.

Usually returns:

```text
System

↓

Conversation

↓

User Request
```

---

## process()

Converts a ChatResponse into a StageArtifact.

Example:

```text
ChatResponse

↓

StageArtifact
```

---

## after_generate()

Optional post-processing.

Examples:

- format code
- execute tools
- invoke execution engine
- create files

---

## validate()

Ensures the artifact satisfies minimum requirements.

Validation may include:

- empty output
- invalid JSON
- missing sections
- syntax errors

---

# LLM Execution

The Agent never communicates directly with providers.

Instead:

```text
Agent

↓

LLM Manager

↓

LLM Runtime

↓

Provider Factory

↓

Provider
```

The provider returns a standardized ChatResponse.

---

# StageArtifact

The generated artifact becomes the output of execution.

Examples:

- requirements
- architecture
- backend code
- frontend code
- test cases
- deployment configuration

Artifacts are immediately reviewed.

---

# Review Process

Every artifact follows the same review pipeline.

```text
Artifact

↓

Review Engine

↓

Approved?
```

If approved:

```text
Artifact

↓

Memory Extraction

↓

Workflow Continues
```

If rejected:

```text
Reviewer Feedback

↓

StageSession

↓

Retry
```

The workflow remains on the same stage until approval.

---

# Retry Mechanism

Retries never create a new StageSession.

Instead, reviewer feedback is appended to the existing conversation.

```text
Attempt 1

↓

Rejected

↓

Reviewer Feedback

↓

Attempt 2

↓

Rejected

↓

Reviewer Feedback

↓

Attempt 3

↓

Approved
```

This allows the agent to improve using previous feedback.

---

# Memory Extraction

Only approved artifacts become project knowledge.

```text
Approved Artifact

↓

Extraction Pipeline

↓

Memory Manager

↓

Providers
```

Rejected artifacts are discarded with the session.

---

# ExecutionResult

After execution completes, the framework returns an ExecutionResult.

Typical information includes:

- stage
- artifact
- approval status
- review comments
- retry count
- metadata

The Workflow Framework uses this object to decide the next action.

---

# Complete Sequence

```text
Workflow

↓

ExecutionContext

↓

StageSession

↓

PromptComposer

↓

Agent

↓

LLM Manager

↓

Provider

↓

ChatResponse

↓

StageArtifact

↓

Review Engine

↓

Approved?

├── No

│     ↓

│ Reviewer Feedback

│     ↓

│ Retry

│

└── Yes

      ↓

Memory Extraction

      ↓

ExecutionResult

      ↓

Workflow
```

---

# Design Decisions

The Execution Framework follows several architectural principles.

### Single Responsibility

Execution coordinates execution only.

---

### Stateless Agents

Agents never own runtime state.

---

### Session-Based Execution

Runtime state exists only inside StageSession.

---

### Review Before Memory

Only approved artifacts become knowledge.

---

### Provider Independence

Execution never depends on Gemini, Ollama, or OpenAI.

It depends only on the LLM Framework.

---

# Key Takeaways

- The Execution Framework runs one workflow stage.
- AgentExecutor coordinates the runtime.
- StageSession stores temporary execution state.
- PromptComposer builds LLM prompts.
- Agents remain stateless.
- Every artifact is reviewed.
- Only approved artifacts become memory.
- Execution returns an ExecutionResult back to the Workflow Framework.


# 9. Agent Framework

## Overview

The Agent Framework is responsible for generating artifacts for a workflow stage.

Every workflow stage is represented by a specialized AI agent.

Examples include:

- Product Owner
- Architect
- Backend Developer
- Frontend Developer
- QA Engineer
- DevOps Engineer
- Reviewer

Although every agent performs a different task, they all follow the exact same lifecycle and execution model.

---

# Philosophy

Agents are intentionally **stateless**.

An agent should never know:

- workflow state
- project state
- memory implementation
- workspace implementation
- provider implementation
- execution order

Instead, every agent receives a fully prepared `ExecutionContext` and returns a `StageArtifact`.

```text
ExecutionContext

↓

Agent

↓

StageArtifact
```

This makes every agent reusable and deterministic.

---

# Responsibilities

Agents are responsible for:

- understanding the task
- preparing LLM messages
- processing LLM responses
- generating artifacts
- validating outputs

Agents are **not** responsible for:

- workflow orchestration
- memory management
- workspace management
- prompt construction
- provider communication
- review decisions

---

# Agent Architecture

```text
Execution Framework

↓

Agent Registry

↓

Stage Profile

↓

Agent

↓

LLM

↓

Stage Artifact
```

The Agent Framework focuses only on artifact generation.

---

# BaseAgent

Every agent inherits from `BaseAgent`.

The BaseAgent defines a common execution lifecycle.

```text
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

Every specialized agent overrides only the methods it needs.

---

# Agent Lifecycle

## 1. before_execute()

Optional initialization before the LLM request.

Typical uses:

- prepare runtime state
- initialize tools
- verify prerequisites

---

## 2. prepare()

Creates the list of messages sent to the LLM.

Default implementation:

```text
System Prompt

↓

Conversation

↓

User Request
```

Agents may customize this if necessary.

---

## 3. process()

Converts the `ChatResponse` into a `StageArtifact`.

```text
ChatResponse

↓

StageArtifact
```

Every agent ultimately produces a StageArtifact.

---

## 4. after_generate()

Optional post-processing.

Examples:

- format generated code
- invoke execution tools
- generate multiple files
- trigger code formatting

---

## 5. validate()

Performs lightweight validation before review.

Possible checks:

- empty response
- malformed JSON
- invalid markdown
- missing sections

Validation never replaces the Review Framework.

---

# StageArtifact

Every agent returns exactly one artifact.

Examples:

| Stage | Artifact |
|--------|----------|
| Product Owner | Requirements |
| Architect | Architecture |
| Backend | Backend source code |
| Frontend | Frontend source code |
| QA | Test cases |
| DevOps | Deployment configuration |

Artifacts move to the Review Framework immediately after generation.

---

# Agent Registry

The Agent Registry creates the correct agent for a workflow stage.

```text
Stage

↓

Agent Registry

↓

Agent Instance
```

Example:

```text
Architect

↓

ArchitectAgent
```

The Execution Framework never creates agents directly.

It always delegates to the registry.

---

# Stage Profiles

Agents are configured using Stage Profiles.

A Stage Profile describes:

- prompt template
- memory permissions
- workspace permissions
- documents
- tools
- agent implementation

Example:

```text
Architect

↓

ArchitectAgent

↓

architecture.md

↓

Architecture Memory

↓

Workspace Read/Write
```

This allows behavior to change through configuration rather than code.

---

# Agent Implementations

Current workflow agents include:

```text
ProductOwnerAgent

ArchitectAgent

BackendDeveloperAgent

FrontendDeveloperAgent

QAAgent

DevOpsAgent

ReviewerAgent
```

Every implementation inherits from `BaseAgent`.

Only stage-specific behavior is customized.

---

# Communication Rules

Agents communicate only through the Execution Framework.

Allowed interactions:

```text
Agent

↓

LLM Framework
```

```text
Agent

↓

ExecutionContext
```

```text
Agent

↓

StageArtifact
```

Forbidden interactions:

```text
Agent

✗ Memory Manager

✗ Workflow Engine

✗ Workspace Registry

✗ Provider Factory

✗ Review Engine
```

This keeps agents independent from the rest of the platform.

---

# Why Stateless Agents?

Stateless agents provide several advantages.

## Deterministic Execution

The same context always produces comparable results.

---

## Easier Testing

Agents can be tested independently using a mock `ExecutionContext`.

---

## Reusability

The same agent can execute multiple projects without modification.

---

## Scalability

Multiple agents can execute in parallel because they do not share internal state.

---

## Maintainability

Business logic remains inside the agent while orchestration stays inside the Execution Framework.

---

# Adding a New Agent

Adding a workflow stage requires only a few steps.

```text
Create Agent

↓

Inherit BaseAgent

↓

Implement Custom Behavior

↓

Register Agent

↓

Create Stage Profile

↓

Update Dependency Graph
```

No changes are required to the Execution Framework.

---

# Future Enhancements

Future versions may introduce:

- Tool-aware agents
- Multi-agent collaboration
- Parallel execution
- Autonomous planning
- Reflection agents
- Self-correction agents

These enhancements will continue to follow the same stateless design philosophy.

---

# Key Takeaways

- Every workflow stage is implemented as an independent agent.
- All agents inherit from `BaseAgent`.
- Agents are stateless.
- The BaseAgent defines a common lifecycle.
- Agents produce `StageArtifact` objects.
- The Agent Registry creates agents.
- Stage Profiles configure behavior.
- Agents never communicate directly with memory, workflow, workspace, or providers.


# 10. Context Framework

## Overview

The Context Framework is responsible for constructing the complete execution context required by an AI agent.

Instead of allowing agents to communicate directly with memory, workspace, documents, or review systems, the Context Framework gathers all required information and packages it into a single `AgentContext`.

This keeps agents simple, stateless, and independent from the rest of the platform.

---

# Philosophy

AI DevOS follows one important rule:

> **Agents consume context. They never build it.**

The Context Framework acts as an orchestration layer between the Execution Framework and every information source.

```text
Execution Framework

↓

Context Builder

↓

Agent Context

↓

Agent
```

Agents never need to know where the information came from.

---

# Responsibilities

The Context Framework is responsible for:

- Building AgentContext
- Selecting relevant memories
- Selecting workspace information
- Loading project documents
- Loading reviewer feedback
- Managing runtime context
- Applying context budgets

It is **not** responsible for:

- generating prompts
- executing agents
- storing memory
- reviewing artifacts
- scanning project files

---

# Framework Components

```text
Context Framework

│

├── ContextBuilder

├── AgentContext

├── MemorySelector

├── WorkspaceSelector

├── DocumentSelector

├── ReviewSelector

└── ContextBudget
```

Each component owns one responsibility.

---

# Context Builder

The Context Builder coordinates every selector.

It never loads information directly.

Instead, it delegates responsibility.

```text
Execution Framework

↓

Context Builder

├── Memory Selector

├── Workspace Selector

├── Document Selector

└── Review Selector

↓

Agent Context
```

The Context Builder is an orchestrator, not a data source.

---

# AgentContext

The AgentContext is the only object consumed by agents.

Typical contents include:

- Project
- Stage
- Task
- Memory
- Workspace
- Documents
- Review feedback
- Runtime Memory
- Metadata

```text
AgentContext

├── Project

├── Stage

├── Task

├── Memory

├── Workspace

├── Documents

├── Review

├── Runtime

└── Metadata
```

Agents receive this object and nothing else.

---

# Memory Selector

The Memory Selector retrieves only the memories required by the current stage.

Example:

```text
Architect

↓

Business Memory

↓

Architecture Memory
```

The selector never loads unrelated memories.

Benefits:

- smaller prompts
- better relevance
- lower token usage

---

# Workspace Selector

The Workspace Selector retrieves workspace metadata.

It communicates only with the Workspace Registry.

```text
Workspace Registry

↓

Workspace Selector

↓

AgentContext
```

Important:

The selector never scans the project directory.

It only queries the indexed metadata.

---

# Document Selector

The Document Selector retrieves project documentation relevant to the current stage.

Examples:

- Requirements
- Architecture
- API specifications
- Design documents

The selector filters documents using the Stage Profile permissions.

---

# Review Selector

The Review Selector retrieves reviewer feedback from the current Stage Session.

Example:

```text
Attempt 1

↓

Reviewer Comments

↓

Review Selector

↓

Attempt 2
```

This allows retries to improve previous outputs.

---

# Runtime Memory

Runtime Memory stores temporary execution information shared during the current stage.

Examples:

- retry counters
- temporary variables
- execution flags
- intermediate calculations

Unlike long-term memory, runtime memory exists only during execution.

```text
Execution

↓

Runtime Memory

↓

Execution Complete

↓

Destroyed
```

---

# Context Budget

Large contexts reduce model performance and increase token usage.

The Context Budget determines how much information can be included in an AgentContext.

Possible strategies include:

- maximum token count
- memory prioritization
- workspace filtering
- document ranking

```text
Selected Context

↓

Context Budget

↓

Trimmed Context

↓

Agent
```

Only the highest-priority information reaches the model.

---

# Complete Context Pipeline

The entire context construction process is shown below.

```text
Execution Framework

↓

Context Builder

↓

Memory Selector

Workspace Selector

Document Selector

Review Selector

↓

Context Budget

↓

Agent Context

↓

Agent
```

Every stage follows the same process.

---

# Communication Rules

The Context Framework communicates with:

```text
Memory Framework

Workspace Framework

Document Framework

Review Framework
```

It does **not** communicate with:

```text
LLM Framework

Workflow Framework

Providers

Review Engine
```

Its responsibility ends after building the AgentContext.

---

# Why Separate Context Construction?

Without a dedicated Context Framework:

- agents would load memory
- agents would scan the workspace
- agents would read documents
- agents would manage reviewer history

This would tightly couple agents to the rest of the platform.

Instead:

```text
Execution

↓

Context Builder

↓

Agent Context

↓

Agent
```

Agents remain completely independent.

---

# Design Benefits

## Stateless Agents

Agents receive complete context and never retrieve data themselves.

---

## Better Prompt Quality

Only relevant information is included.

---

## Lower Token Usage

Unused memories and documents are excluded.

---

## Independent Evolution

Memory, workspace, and document systems can evolve without modifying agents.

---

## Easier Testing

Mock AgentContext objects can be used to test agents without loading the entire platform.

---

# Future Enhancements

Future versions of the Context Framework may include:

- Semantic memory ranking
- Vector search (RAG)
- Knowledge graph traversal
- Context caching
- Dynamic token budgeting
- Multi-project context sharing
- Context compression

These enhancements will remain internal to the Context Framework.

Agents will continue consuming the same AgentContext interface.

---

# Key Takeaways

- The Context Framework prepares information for agents.
- ContextBuilder orchestrates all selectors.
- AgentContext is the only object consumed by agents.
- Selectors retrieve only relevant information.
- Runtime Memory stores temporary execution state.
- Context Budget limits prompt size.
- Agents never communicate directly with memory, workspace, or documents.
- The Context Framework enables stateless, modular, and scalable AI agents.


# 11. Memory Framework

## Overview

The Memory Framework is responsible for storing, retrieving, and organizing project knowledge throughout the software development lifecycle.

It acts as the single source of truth for persistent knowledge while ensuring that temporary execution state remains isolated from long-term memory.

Every framework that requires project knowledge communicates through the Memory Framework.

---

# Philosophy

One of the fundamental design principles of AI DevOS is:

> **Only the Memory Framework owns memory.**

No other framework writes directly to memory.

Instead, approved artifacts flow through a controlled extraction pipeline.

```text
Stage Artifact

↓

Extraction Pipeline

↓

Memory Manager

↓

Memory Provider

↓

Persistent Memory
```

This guarantees consistency and prevents invalid or incomplete information from polluting project knowledge.

---

# Responsibilities

The Memory Framework is responsible for:

- Managing project memories
- Reading persistent knowledge
- Writing approved knowledge
- Deleting obsolete memories
- Managing runtime memory
- Executing extraction pipelines
- Providing memory to the Context Framework

It is **not** responsible for:

- generating artifacts
- executing workflow stages
- reviewing artifacts
- building prompts

---

# Architecture

```text
Memory Framework

│

├── MemoryManager

├── MemoryProvider

├── RuntimeStore

├── ExtractionPipeline

└── Memory Selectors
```

---

# MemoryManager

The `MemoryManager` is the public entry point of the Memory Framework.

Every memory operation passes through it.

Responsibilities:

- read memory
- write memory
- delete memory
- retrieve runtime memory
- execute extraction pipeline

It coordinates all memory providers but never stores data directly.

---

# Memory Providers

Memory is divided into logical providers.

Typical providers include:

| Provider | Purpose |
|-----------|---------|
| Business | Requirements and business rules |
| Architecture | System design |
| Workflow | Workflow metadata |
| Decision | Important architectural decisions |
| Review | Reviewer feedback |
| Issue | Known issues and blockers |
| Artifact | Approved artifacts |
| Runtime | Temporary execution state |

Each provider owns one category of knowledge.

---

# Runtime Memory

Runtime Memory stores temporary execution data.

Examples include:

- retry count
- temporary variables
- execution flags
- intermediate state

Lifecycle:

```text
Execution Starts

↓

Runtime Store

↓

Execution Completes

↓

Destroyed
```

Runtime Memory is **never** persisted.

---

# Persistent Memory

Persistent Memory stores approved project knowledge.

Examples:

- finalized requirements
- architecture decisions
- approved APIs
- coding conventions
- project constraints

Lifecycle:

```text
Approved Artifact

↓

Extraction Pipeline

↓

Memory Provider

↓

Persistent Storage
```

Unlike Runtime Memory, persistent memories remain available throughout the project lifecycle.

---

# Runtime vs Persistent Memory

| Runtime Memory | Persistent Memory |
|---------------|-------------------|
| Temporary | Long-term |
| Stage execution only | Entire project |
| Destroyed after execution | Retained until deleted |
| Stores execution state | Stores project knowledge |
| Never reviewed | Written only after approval |

Keeping these responsibilities separate prevents execution state from contaminating project knowledge.

---

# Extraction Pipeline

The Extraction Pipeline determines what information should become long-term memory.

```text
Approved Artifact

↓

Analyze

↓

Extract Knowledge

↓

Categorize

↓

Store
```

Only approved artifacts enter the pipeline.

Rejected artifacts are discarded with the Stage Session.

---

# Reading Memory

The Context Framework retrieves knowledge through selectors.

```text
Context Builder

↓

Memory Selector

↓

Memory Manager

↓

Memory Provider
```

Only relevant memories are loaded into the AgentContext.

---

# Writing Memory

Agents never write memory directly.

Instead:

```text
Agent

↓

Stage Artifact

↓

Review

↓

Extraction Pipeline

↓

Memory Manager

↓

Memory Provider
```

This ensures all project knowledge has passed review.

---

# Communication Rules

Allowed interactions:

```text
Context Framework

↓

Memory Framework
```

```text
Execution Framework

↓

Memory Framework
```

Forbidden interactions:

```text
Agent

✗ Memory Provider
```

```text
Workflow

✗ Memory Provider
```

```text
LLM

✗ Memory Provider
```

All communication must pass through the MemoryManager.

---

# Why This Design?

Separating memory management from execution provides several advantages.

### Single Source of Truth

All project knowledge is managed in one place.

---

### Controlled Persistence

Only approved knowledge becomes permanent.

---

### Stateless Agents

Agents never own project knowledge.

---

### Easier Maintenance

Storage implementations can change without affecting other frameworks.

---

### Future Scalability

The Memory Framework can evolve independently to support:

- vector databases
- semantic search
- graph databases
- distributed memory
- external knowledge sources

without changing the rest of the platform.

---

# Future Enhancements

Planned improvements include:

- Semantic Memory
- Vector Search (RAG)
- Knowledge Graph
- Memory Versioning
- Memory Compression
- Cross-project Memory
- Memory Ranking
- Hybrid Retrieval

These enhancements remain internal to the Memory Framework.

---

# Key Takeaways

- The Memory Framework owns all project knowledge.
- MemoryManager is the single entry point.
- Runtime Memory and Persistent Memory have different responsibilities.
- Only approved artifacts become persistent knowledge.
- Agents never write memory directly.
- The Extraction Pipeline controls knowledge persistence.
- Memory can evolve independently without affecting execution or agents.

# 12. Workspace Framework

## Overview

The Workspace Framework is responsible for managing project files and their metadata throughout the software development lifecycle.

Unlike traditional AI coding systems that repeatedly scan the filesystem, AI DevOS maintains an indexed representation of the workspace.

The Workspace Framework never owns business logic or execution.

Its responsibility is to provide fast and deterministic access to project metadata.

---

# Philosophy

AI DevOS follows a simple rule:

> **Index once, query many.**

Instead of reading every file whenever an agent executes, the Workspace Framework maintains a registry containing metadata for every project file.

```text
Project Files

↓

Workspace Registry

↓

Indexed Metadata

↓

Workspace Selector

↓

Agent Context
```

Agents never access the filesystem directly.

---

# Responsibilities

The Workspace Framework is responsible for:

- Registering project files
- Tracking file metadata
- Managing file checksums
- Tracking last modification times
- Providing indexed file information
- Supporting workspace queries

It is **not** responsible for:

- reading file contents
- generating code
- parsing business logic
- executing workflow stages

---

# Architecture

```text
Workspace Framework

│

├── WorkspaceRegistry

├── WorkspaceIndex

├── WorkspaceSelector

└── WorkspaceParser
```

---

# WorkspaceRegistry

The Workspace Registry is the central index of the project workspace.

Each file is represented by a `WorkspaceIndex`.

Typical information includes:

- file path
- module
- file type
- checksum
- last modified
- metadata

The registry stores metadata only.

Actual file contents remain on disk.

---

# WorkspaceIndex

Each project file is represented by a lightweight metadata object.

Example:

```text
WorkspaceIndex

├── path

├── module

├── file_type

├── checksum

├── last_modified

└── metadata
```

This keeps the workspace lightweight and efficient.

---

# Workspace Selector

The Workspace Selector is used by the Context Framework.

Its responsibility is to retrieve only the workspace information required for the current stage.

```text
Context Builder

↓

Workspace Selector

↓

Workspace Registry

↓

Workspace Metadata
```

It never scans the filesystem.

---

# Workspace Parser

The Workspace Parser is responsible for extracting metadata from project files.

Current responsibilities:

- checksum generation

Future responsibilities:

- AST parsing
- import extraction
- class indexing
- function indexing
- dependency discovery

The parser enriches metadata without changing the execution architecture.

---

# Workspace Lifecycle

```text
File Created

↓

Register File

↓

Generate Metadata

↓

Workspace Registry

↓

Available for Context
```

When a file changes:

```text
File Updated

↓

New Checksum

↓

Registry Updated

↓

Context Uses Latest Metadata
```

---

# Workspace Communication

Allowed interactions:

```text
Execution Framework

↓

Workspace Framework
```

```text
Context Framework

↓

Workspace Framework
```

Forbidden interactions:

```text
Agent

✗ Filesystem
```

```text
LLM

✗ Filesystem
```

```text
Workflow

✗ Filesystem
```

The Workspace Framework is the only component responsible for workspace metadata.

---

# Why an Indexed Workspace?

Without a registry, every execution would require scanning the project directory.

Problems include:

- slower execution
- repeated disk access
- unnecessary token usage
- inconsistent context

Using an indexed registry provides:

- deterministic context
- faster lookups
- lower resource usage
- better scalability

---

# Future Enhancements

Planned improvements include:

- AST-based indexing
- Symbol search
- Function dependency graph
- Module relationships
- Incremental indexing
- Cross-project indexing
- Semantic code search

These enhancements will remain internal to the Workspace Framework.

---

# Key Takeaways

- The Workspace Framework owns project metadata.
- WorkspaceRegistry is the central index.
- WorkspaceIndex represents one file.
- WorkspaceSelector provides relevant metadata to the Context Framework.
- WorkspaceParser extracts metadata.
- Agents never scan the filesystem.
- Index once, query many.



# 13. LLM Framework

## Overview

The LLM Framework is responsible for all communication between AI DevOS and external Large Language Models.

Instead of allowing agents or execution components to communicate directly with providers, AI DevOS routes every request through a standardized runtime.

This abstraction allows providers to be replaced without affecting the rest of the platform.

---

# Philosophy

AI DevOS follows one simple principle:

> **The framework depends on interfaces, never providers.**

The Agent Framework never knows whether the request is executed by:

- Gemini
- Ollama
- OpenAI
- Claude
- OpenRouter

Every provider implements the same interface.

---

# Responsibilities

The LLM Framework is responsible for:

- Executing chat requests
- Selecting the active provider
- Standardizing request/response objects
- Hiding provider-specific APIs
- Supporting multiple providers

It is **not** responsible for:

- building prompts
- executing workflow stages
- managing memory
- reviewing artifacts

---

# Architecture

```text
Agent

↓

LLM Manager

↓

LLM Runtime

↓

Provider Factory

↓

Base Provider

↓

Gemini
Ollama
OpenAI
Claude
OpenRouter
```

Every request follows this exact path.

---

# LLM Manager

The **LLMManager** is the public entry point.

Every AI request enters the framework here.

Responsibilities:

- receive ChatRequest
- delegate execution
- return ChatResponse

The manager contains **no provider logic**.

```text
Agent

↓

LLMManager

↓

LLMRuntime
```

---

# LLM Runtime

The runtime executes requests.

Responsibilities:

- receive ChatRequest
- request active provider
- execute provider
- return ChatResponse

```text
LLM Runtime

↓

Provider Factory

↓

Provider
```

The runtime never knows which provider is active.

---

# Provider Factory

The Provider Factory determines which provider should execute the request.

Current flow:

```text
Settings

↓

Provider Factory

↓

Gemini

or

Ollama
```

Future providers can be added without modifying agents or execution.

---

# Base Provider

Every provider inherits from `BaseProvider`.

Required interface:

```python
chat(request) -> ChatResponse
```

Every provider must implement this method.

This ensures the rest of AI DevOS communicates through one consistent API.

---

# ChatRequest

The ChatRequest is the standardized input sent to every provider.

Typical fields:

```text
ChatRequest

├── model

├── messages

├── temperature

└── max_tokens
```

Providers convert this object into their own API format.

---

# ChatResponse

The ChatResponse is the standardized output returned by every provider.

Typical fields:

```text
ChatResponse

├── content

├── prompt_tokens

├── completion_tokens

└── finish_reason
```

The Agent Framework always receives the same response format regardless of provider.

---

# Provider Independence

The biggest advantage of this architecture is provider independence.

Example:

Today:

```text
Agent

↓

Gemini
```

Tomorrow:

```text
Agent

↓

Claude
```

Nothing changes outside the LLM Framework.

---

# Current Providers

Current implementation:

```text
GeminiProvider

OllamaProvider
```

Future implementations:

```text
OpenAIProvider

ClaudeProvider

OpenRouterProvider

AzureOpenAIProvider

LocalLLMProvider
```

Each inherits from `BaseProvider`.

---

# Request Lifecycle

```text
Agent

↓

ChatRequest

↓

LLM Manager

↓

LLM Runtime

↓

Provider Factory

↓

Provider

↓

ChatResponse

↓

Agent
```

Every provider follows the same lifecycle.

---

# Error Handling

Errors remain inside the LLM Framework.

Examples:

- authentication failure
- timeout
- rate limiting
- invalid model
- provider unavailable

The rest of AI DevOS never handles provider-specific exceptions.

---

# Why This Design?

Separating provider logic provides several benefits.

### Provider Independence

Switch providers without changing execution.

---

### Easier Testing

Mock providers can replace real APIs.

---

### Simpler Maintenance

Provider updates remain isolated.

---

### Extensibility

Adding a new provider requires:

```text
Create Provider

↓

Inherit BaseProvider

↓

Register Provider

↓

Done
```

No changes are required in agents or execution.

---

# Future Enhancements

Planned improvements include:

- Streaming responses
- Function Calling
- Tool Calling
- Vision models
- Multi-modal inputs
- Automatic provider fallback
- Cost-aware provider selection
- Load balancing across providers
- Provider health monitoring

These enhancements will remain inside the LLM Framework.

---

# Key Takeaways

- The LLM Framework owns provider communication.
- LLMManager is the public entry point.
- LLMRuntime executes requests.
- ProviderFactory selects the active provider.
- BaseProvider defines a common interface.
- ChatRequest and ChatResponse standardize communication.
- Providers are fully interchangeable.
- Agents never communicate with providers directly.


# 14. Review Framework

## Overview

The Review Framework is responsible for validating every artifact generated during workflow execution.

Instead of immediately accepting AI-generated output, AI DevOS introduces an independent review phase that verifies quality before allowing the workflow to continue.

This guarantees that only approved artifacts become part of the project's long-term knowledge.

---

# Philosophy

AI DevOS follows one important rule:

> **Generation does not equal approval.**

Every generated artifact must pass through an independent review before:

- progressing to the next workflow stage
- being stored in project memory
- becoming available to future agents

This creates a controlled software engineering pipeline rather than a simple AI chat system.

---

# Responsibilities

The Review Framework is responsible for:

- reviewing generated artifacts
- approving or rejecting stage outputs
- providing reviewer feedback
- controlling retry execution
- preventing invalid knowledge from entering memory

It is **not** responsible for:

- generating artifacts
- executing workflow stages
- building prompts
- storing memories

---

# Architecture

```text
Stage Artifact

↓

Review Engine

↓

Review Result

↓

Approved?

├── Yes
│
│   ↓
│
│ Memory Extraction
│
│ ↓
│
│ Next Stage
│
└── No
    │
    ▼
Reviewer Feedback

↓

Stage Session

↓

Retry
```

---

# Review Engine

The Review Engine coordinates the complete review process.

Responsibilities include:

- receiving StageArtifact
- evaluating artifact quality
- creating ReviewResult
- determining approval status
- generating reviewer comments

The Review Engine does not modify artifacts.

Its responsibility is evaluation.

---

# Review Result

Every review returns a standardized ReviewResult.

Typical fields include:

```text
ReviewResult

├── approved

├── comments

├── confidence

├── issues

└── metadata
```

The Execution Framework uses this object to determine the next action.

---

# Approval Lifecycle

Every artifact follows the same lifecycle.

```text
Agent

↓

Stage Artifact

↓

Review

↓

Approved?
```

If approved:

```text
Approved

↓

Memory Extraction

↓

Workflow Continues
```

If rejected:

```text
Rejected

↓

Reviewer Feedback

↓

Retry
```

---

# Reviewer Feedback

Reviewer comments become part of the active Stage Session.

Example:

```text
Attempt 1

↓

Reviewer:
Missing API validation

↓

Attempt 2

↓

Reviewer:
Authentication missing

↓

Attempt 3

↓

Approved
```

The previous conversation is preserved so the agent can improve instead of starting from scratch.

---

# Retry Mechanism

AI DevOS does not create a new execution for every retry.

Instead:

```text
Same Stage Session

↓

Reviewer Feedback Added

↓

Agent Executes Again
```

Benefits:

- conversation continuity
- lower token usage
- iterative improvement
- deterministic execution

---

# Review Before Memory

Memory extraction occurs **only after approval**.

```text
Stage Artifact

↓

Review

↓

Approved

↓

Extraction Pipeline

↓

Memory
```

Rejected artifacts are never stored.

This keeps project knowledge clean and trustworthy.

---

# Review Before Workflow

Workflow progression also depends on review.

```text
Stage

↓

Artifact

↓

Review

↓

Approved?

↓

Next Stage
```

A workflow cannot progress until the current stage has been approved.

---

# Communication Rules

The Review Framework communicates with:

```text
Execution Framework

↓

Review Framework
```

It returns:

```text
Review Result
```

It never communicates directly with:

```text
LLM Framework

Memory Framework

Workspace Framework

Workflow Framework
```

Execution coordinates all interactions.

---

# Why Separate Review?

Separating review from generation provides several advantages.

### Quality Assurance

Generated artifacts are validated before use.

---

### Reliable Memory

Only approved knowledge enters project memory.

---

### Controlled Workflow

Stages cannot skip validation.

---

### Better Agent Performance

Reviewer feedback allows iterative refinement.

---

### Cleaner Architecture

Generation and validation remain independent responsibilities.

---

# Future Enhancements

Future versions of the Review Framework may include:

- Multi-reviewer pipelines
- Human approval mode
- Confidence scoring
- Automatic regression checks
- Code quality analysis
- Security review
- Architecture review
- Style enforcement
- Test execution integration

These enhancements remain isolated within the Review Framework.

---

# Complete Review Pipeline

```text
Agent

↓

Stage Artifact

↓

Review Engine

↓

Review Result

↓

Approved?

├── No

│ ↓

│ Reviewer Feedback

│ ↓

│ Stage Session

│ ↓

│ Retry

│

└── Yes

    ↓

Memory Extraction

↓

Workflow

↓

Next Stage
```

---

# Key Takeaways

- Every generated artifact is reviewed.
- Review is independent from generation.
- ReviewEngine evaluates StageArtifacts.
- ReviewResult controls workflow progression.
- Reviewer feedback is stored in the active Stage Session.
- Rejected artifacts never enter project memory.
- Memory extraction occurs only after approval.
- Review guarantees reliable project knowledge.


# 15. Project Structure

## Overview

AI DevOS is organized into independent frameworks.

Each top-level package owns exactly one responsibility.

```text
app/

├── agents/           # AI agents and registry
├── context/          # Context Builder and selectors
├── execution/        # Stage execution runtime
├── llm/              # Provider abstraction
├── memory/           # Long-term and runtime memory
├── orchestration/    # Workflow execution
├── prompts/          # Prompt templates
├── review/           # Review engine
├── session/          # Stage sessions
├── workspace/        # Workspace registry
├── api/              # REST endpoints
├── core/             # Configuration
└── main.py
```

---

## Framework Ownership

| Folder | Responsibility |
|---------|----------------|
| agents | Generate artifacts |
| context | Build AgentContext |
| execution | Execute stages |
| llm | Communicate with AI models |
| memory | Manage project knowledge |
| orchestration | Control workflow |
| prompts | Compose prompts |
| review | Validate artifacts |
| session | Temporary conversations |
| workspace | Project indexing |

Every package owns one responsibility.

No package should duplicate another framework's logic.

---

## Dependency Direction

```text
AI Kernel

↓

Workflow

↓

Execution

↓

Context

↓

Agent

↓

LLM

↓

Provider
```

Shared services:

```text
Memory

Workspace

Review

Session
```

Circular dependencies are never allowed.


# 16. Complete Execution Flow

The following sequence illustrates how AI DevOS executes a single workflow stage.

```text
Project Created

↓

Workflow Engine

↓

Dependency Graph

↓

Stage Ready

↓

Execution Framework

↓

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

AgentContext

↓

Prompt Composer

↓

Agent

↓

LLM Manager

↓

LLM Runtime

↓

Provider Factory

↓

Provider

↓

ChatResponse

↓

StageArtifact

↓

Review Engine

↓

ReviewResult

↓

Approved?

├── No

│ ↓

│ Reviewer Feedback

│ ↓

│ Stage Session

│ ↓

│ Retry

│

└── Yes

    ↓

Extraction Pipeline

↓

Memory Manager

↓

Workflow Engine

↓

Next Stage

↓

Project Complete
```

Every workflow stage follows this identical execution pipeline.



# 17. Design Decisions

## Why Not Traditional RAG?

Many AI development platforms use Retrieval-Augmented Generation (RAG) by indexing the entire repository and retrieving similar chunks during execution.

AI DevOS intentionally follows a different architecture.

---

### Traditional RAG

```text
Project Files

↓

Embedding

↓

Vector Database

↓

Similarity Search

↓

LLM
```

Advantages:

- Works well for document search.
- Easy to implement.

Limitations:

- Large repositories increase retrieval cost.
- Retrieved context may be irrelevant.
- No distinction between temporary and approved knowledge.
- Difficult to maintain workflow state.

---

### AI DevOS Approach

```text
Approved Knowledge

↓

Memory Framework

↓

Context Builder

↓

AgentContext

↓

LLM
```

Instead of searching everything, AI DevOS builds context from structured project knowledge.

---

## Why Structured Memory?

Knowledge is divided into dedicated providers.

Examples:

- Business
- Architecture
- Workflow
- Decision
- Review
- Runtime
- Artifact

This allows every stage to receive only relevant information.

---

## Why Workspace Registry?

Instead of scanning the project every execution:

```text
Project Files

↓

Workspace Registry

↓

Metadata

↓

Context Builder
```

This improves performance and keeps execution deterministic.

---

## Why Stage Sessions?

Stage Sessions preserve temporary conversations.

They are destroyed after approval.

Only approved knowledge survives.

---

## Why Stateless Agents?

Stateless agents:

- are reusable
- are deterministic
- are easy to test
- can execute in parallel
- never own project state

---

## Why Review Before Memory?

Without review:

```text
LLM Output

↓

Memory
```

Incorrect outputs become permanent.

AI DevOS instead follows:

```text
LLM Output

↓

Review

↓

Approved

↓

Memory
```

This guarantees reliable project knowledge.





# 18. Future Roadmap

The current implementation focuses on deterministic software engineering.

Future versions will expand the platform while preserving the existing architecture.

---

## AI Kernel

- Plugin system
- Event bus
- Scheduler
- Health monitoring
- Metrics
- Distributed orchestration

---

## Workflow

- Dynamic workflows
- Parallel stage execution
- Conditional branches
- Human approval stages

---

## Context

- Semantic ranking
- Context compression
- Adaptive token budgeting
- Cross-project context

---

## Memory

- Vector memory
- Knowledge graph
- Memory versioning
- Semantic search
- Hybrid retrieval

---

## Workspace

- AST indexing
- Symbol search
- Dependency graph
- Incremental indexing

---

## LLM

- Streaming
- Tool calling
- Vision models
- Provider fallback
- Cost-aware routing

---

## Review

- Multi-reviewer pipelines
- Human review
- Security analysis
- Static analysis
- Automated testing

---

## Agents

- Multi-agent collaboration
- Planning agents
- Reflection agents
- Self-improving agents
- Autonomous debugging

---

# Final Vision

AI DevOS is designed to become an **AI Software Engineering Operating System** rather than a simple coding assistant.

The architecture is built around:

- Stateless Agents
- AI Kernel
- Workflow Engine
- Execution Framework
- Context Framework
- Memory Framework
- Workspace Framework
- LLM Framework
- Review Framework

Each framework owns exactly one responsibility.

Together they form a modular, scalable, and provider-independent platform capable of orchestrating the complete software development lifecycle.


# 19. AI Kernel Internals

## Overview

The AI Kernel is the central runtime of AI DevOS.

Every framework in the system is built around the kernel.

Unlike traditional applications where business logic is scattered across services, AI DevOS places all runtime coordination inside the AI Kernel.

The kernel is **not** responsible for software engineering tasks.

Instead, it manages the platform itself.

It is comparable to an operating system kernel.

Just as an operating system coordinates processes, memory, scheduling and devices, the AI Kernel coordinates workflows, execution, sessions, services and communication.

---

# Philosophy

The AI Kernel follows one principle:

> **Frameworks perform work. The Kernel coordinates them.**

No framework owns another framework.

Instead:

```text
AI Kernel

↓

Coordinates

↓

Workflow

Execution

Context

Memory

Workspace

LLM

Review
```

Every framework remains independent.

---

# Responsibilities

The AI Kernel is responsible for:

- Service registration
- Framework initialization
- Dependency management
- Event routing
- Lifecycle management
- Scheduling
- Configuration
- Health monitoring
- Metrics collection
- Logging
- Plugin management

The kernel never:

- generates code
- reviews artifacts
- communicates with LLM providers
- manages workflow logic

---

# Kernel Architecture

```text
                     AI Kernel

┌───────────────────────────────────────────────┐

 Configuration

 Service Registry

 Dependency Injection

 Event Bus

 Lifecycle Manager

 Scheduler

 Plugin Manager

 Metrics

 Logging

 Health Monitor

└───────────────────────────────────────────────┘

                │

                ▼

 Workflow Framework

 Execution Framework

 Context Framework

 Agent Framework

 Memory Framework

 Workspace Framework

 Review Framework

 LLM Framework
```

The AI Kernel sits above every framework.

---

# Service Registry

Every core framework registers itself with the kernel.

```text
AI Kernel

↓

Service Registry

↓

Workflow Engine

Execution Engine

Memory Manager

LLM Manager

Review Engine

Session Manager

Workspace Registry
```

Instead of creating services manually throughout the application, components retrieve them from the registry.

Benefits:

- loose coupling
- easier testing
- framework independence

---

# Dependency Injection

Frameworks never construct each other directly.

Instead:

```text
AI Kernel

↓

Service Registry

↓

Dependency Injection

↓

Framework
```

Example:

Execution Framework requests:

- MemoryManager
- ReviewEngine
- SessionManager

The kernel provides them.

---

# Event Bus

The Event Bus enables asynchronous communication between frameworks.

Instead of calling each other directly:

```text
Execution

↓

Memory
```

Frameworks publish events.

```text
Execution

↓

ArtifactApproved Event

↓

Event Bus

↓

Memory

Workflow

Metrics

Plugins
```

This removes direct dependencies.

---

# Event Examples

Typical events include:

```text
ProjectCreated

WorkflowStarted

StageStarted

StageCompleted

ArtifactGenerated

ArtifactApproved

MemoryExtracted

RetryRequested

WorkflowCompleted

ProjectCompleted
```

Future plugins may subscribe to these events without changing existing frameworks.

---

# Lifecycle Manager

The Lifecycle Manager controls framework startup and shutdown.

Startup sequence:

```text
Configuration

↓

Service Registry

↓

Memory

↓

Workspace

↓

LLM

↓

Review

↓

Execution

↓

Workflow

↓

API
```

Shutdown occurs in reverse order.

---

# Scheduler

The Scheduler determines when work should execute.

Current implementation:

```text
Workflow

↓

Ready Stage

↓

Execution
```

Future versions may support:

- delayed execution
- scheduled jobs
- background workers
- distributed queues

---

# Plugin Manager

The Plugin Manager allows AI DevOS to be extended without modifying the core platform.

Future plugins may include:

```text
Slack

GitHub

Jira

Docker

Kubernetes

Email

MCP Servers

Custom Tools
```

Plugins communicate only through the Event Bus.

---

# Configuration

The kernel loads global configuration once during startup.

Examples:

```text
LLM Provider

Workspace

Memory

Workflow

Logging

Execution

API
```

Every framework receives configuration from the kernel.

---

# Logging

Every framework logs through the kernel.

Typical events:

```text
Workflow Started

Stage Executed

Provider Called

Review Approved

Memory Written

Execution Finished
```

Centralized logging simplifies debugging.

---

# Metrics

The kernel collects platform metrics.

Examples:

- execution duration
- workflow duration
- retry count
- approval rate
- token usage
- provider latency

These metrics remain independent of business logic.

---

# Health Monitoring

The kernel continuously monitors framework health.

Examples:

```text
Memory

Workspace

LLM

Review

Workflow
```

Future versions may expose health endpoints for monitoring systems.

---

# Framework Startup

Complete startup sequence:

```text
Application

↓

AI Kernel

↓

Configuration

↓

Service Registry

↓

Dependency Injection

↓

Framework Initialization

↓

Health Check

↓

API Ready
```

Every framework is initialized exactly once.

---

# Framework Shutdown

Shutdown sequence:

```text
Stop API

↓

Finish Running Sessions

↓

Flush Memory

↓

Close Providers

↓

Destroy Services

↓

Kernel Shutdown
```

This guarantees graceful termination.

---

# Why a Kernel?

Without the kernel:

- frameworks would construct each other
- dependencies would become circular
- configuration would be duplicated
- logging would be inconsistent
- startup would be difficult

The kernel solves these problems by acting as the operating system of AI DevOS.

---

# Future Enhancements

Future versions of the AI Kernel may include:

- distributed execution
- multiple execution nodes
- cluster scheduling
- event persistence
- plugin marketplace
- distributed service registry
- runtime sandboxing
- framework hot reloading

These enhancements will remain inside the kernel.

---

# Key Takeaways

- The AI Kernel coordinates the entire platform.
- Frameworks never coordinate each other.
- The Service Registry manages shared services.
- Dependency Injection removes tight coupling.
- The Event Bus enables asynchronous communication.
- The Lifecycle Manager controls startup and shutdown.
- The Scheduler determines execution timing.
- Plugins extend the platform through events.
- The kernel acts as the operating system of AI DevOS.

# 20. Session & Runtime Architecture

## Overview

The Session Framework manages the temporary runtime state of every workflow stage.

Unlike persistent project memory, a Stage Session exists only while a stage is executing.

Its purpose is to preserve conversation history, reviewer feedback, retry information, and temporary execution state until the stage is approved.

Once approved, the session is destroyed.

Only approved knowledge survives through the Memory Framework.

---

# Philosophy

AI DevOS separates execution into two distinct types of state.

## Temporary State

Exists only while a stage is executing.

Examples:

- Conversation history
- Retry count
- Reviewer feedback
- Runtime variables
- Intermediate artifacts

---

## Persistent State

Exists for the lifetime of the project.

Examples:

- Business requirements
- Architecture
- Decisions
- Approved artifacts
- Project knowledge

This separation keeps project memory clean while allowing iterative execution.

---

# Architecture

```text
                    Execution Framework

                           │

                           ▼

                   Session Manager

                           │

             ┌─────────────┴─────────────┐

             ▼                           ▼

        Stage Session             Runtime Memory

             │                           │

             ▼                           ▼

      Conversation History      Temporary Execution State

             │                           │

             └─────────────┬─────────────┘

                           ▼

                     Agent Execution
```

---

# Stage Session

A Stage Session represents one execution lifecycle for a workflow stage.

Each stage owns exactly one active session.

Example:

```text
Project

↓

Architect Stage

↓

Architect Session
```

When Backend starts:

```text
Project

↓

Backend Stage

↓

Backend Session
```

Sessions are isolated from each other.

---

# Stage Session Contents

A session stores:

```text
Stage Session

├── System Prompt

├── User Messages

├── Assistant Messages

├── Reviewer Feedback

├── Retry Counter

├── Runtime Artifacts

├── Metadata

└── Execution State
```

Everything inside a session is temporary.

---

# Session Lifecycle

Every stage follows the same lifecycle.

```text
Stage Starts

↓

Create Session

↓

Conversation

↓

Artifact

↓

Review

↓

Approved?

├── No

│

│ Retry

│

│ Continue Same Session

│

└── Yes

     ↓

Memory Extraction

↓

Destroy Session
```

No new session is created during retries.

---

# Why Keep One Session?

Instead of restarting execution:

```text
Attempt 1

↓

Rejected

↓

Attempt 2

↓

Rejected

↓

Attempt 3
```

AI DevOS keeps the same conversation alive.

Benefits:

- previous reasoning preserved
- reviewer feedback remembered
- lower token usage
- iterative improvement

---

# Conversation Flow

Example:

```text
System

↓

User

↓

Assistant

↓

Reviewer

↓

User

↓

Assistant

↓

Reviewer

↓

User

↓

Assistant

↓

Approved
```

The conversation grows until approval.

---

# Session Manager

The Session Manager owns every Stage Session.

Responsibilities:

- create session
- retrieve session
- resume session
- close session
- destroy session

The Execution Framework never manages sessions directly.

---

# Session Operations

Typical operations include:

```text
get_or_create()

↓

add_system()

↓

add_user()

↓

add_assistant()

↓

add_review()

↓

increment_retry()

↓

close()
```

These operations encapsulate all session management.

---

# Runtime Memory

Runtime Memory stores temporary execution data.

Examples:

```text
Retry Count

Execution Flags

Current Step

Temporary Variables

Tool Results
```

Runtime Memory is shared only during the active stage.

---

# Runtime Memory Lifecycle

```text
Stage Starts

↓

Runtime Store Created

↓

Execution

↓

Review

↓

Retry

↓

Execution

↓

Approved

↓

Runtime Destroyed
```

Nothing inside Runtime Memory becomes permanent.

---

# Retry Flow

Retries reuse both:

- Stage Session
- Runtime Memory

Example:

```text
Attempt 1

↓

Reviewer

↓

Retry

↓

Attempt 2

↓

Reviewer

↓

Retry

↓

Attempt 3

↓

Approved
```

This avoids restarting the conversation.

---

# Session vs Runtime Memory

| Stage Session | Runtime Memory |
|---------------|----------------|
| Conversation | Temporary variables |
| Messages | Execution state |
| Reviewer feedback | Flags |
| Retry history | Intermediate values |
| LLM interaction | Internal runtime |

They complement each other.

---

# Session vs Project Memory

```text
Stage Session

↓

Temporary

↓

Destroyed
```

versus

```text
Memory Framework

↓

Persistent

↓

Entire Project
```

Only approved knowledge moves into project memory.

---

# Runtime Communication

The runtime communicates with:

```text
Execution Framework

↓

Session Manager

↓

Stage Session

↓

Runtime Memory
```

Agents never manage sessions directly.

---

# Approval Flow

When approved:

```text
Stage Session

↓

Extraction Pipeline

↓

Memory

↓

Session Destroyed
```

The session no longer exists.

---

# Rejection Flow

When rejected:

```text
Reviewer

↓

Session Updated

↓

Retry Counter

↓

Conversation Continues
```

No information is lost.

---

# Why Separate Sessions from Memory?

Without sessions:

- retries would restart
- reviewer comments disappear
- conversations are lost
- execution becomes inconsistent

Using Stage Sessions allows AI DevOS to behave like an experienced engineer refining work rather than restarting from scratch.

---

# Future Enhancements

Future versions may include:

- Session snapshots
- Conversation compression
- Runtime caching
- Parallel sessions
- Human collaboration
- Live execution replay
- Distributed session storage

---

# Complete Runtime Flow

```text
Workflow

↓

Create Stage Session

↓

Runtime Memory

↓

Prompt

↓

Agent

↓

LLM

↓

Artifact

↓

Review

↓

Approved?

├── No

│

│ Reviewer Feedback

│

│ Same Session

│

│ Retry

│

└── Yes

     ↓

Memory Extraction

↓

Destroy Session

↓

Next Stage
```

---

# Key Takeaways

- Every workflow stage owns one Stage Session.
- Sessions persist across retries.
- Runtime Memory stores temporary execution state.
- Sessions are destroyed after approval.
- Only approved knowledge reaches project memory.
- SessionManager owns all session operations.
- Conversations are preserved until the stage succeeds.
- Runtime architecture enables iterative, deterministic execution.


# 21. Execution Engine

## Overview

The Execution Engine is responsible for applying changes to the project workspace.

Unlike AI chat systems where the language model directly edits files, AI DevOS separates reasoning from execution.

Agents generate **what should be changed**.

The Execution Engine decides **how those changes are applied**.

This separation keeps agents stateless and allows multiple execution engines to be supported without changing the AI workflow.

---

# Philosophy

AI DevOS follows a strict architectural rule:

> **Agents generate. Execution Engines execute.**

Agents never:

- edit files
- create folders
- delete files
- execute shell commands
- modify repositories

Instead they generate a StageArtifact describing the desired output.

```text
Agent

↓

StageArtifact

↓

Execution Engine

↓

Workspace
```

---

# Responsibilities

The Execution Engine is responsible for:

- Applying generated code
- Creating files
- Updating files
- Deleting files
- Executing code tools
- Synchronizing the workspace
- Registering workspace updates
- Reporting execution results

It is **not** responsible for:

- generating requirements
- designing architecture
- reviewing artifacts
- workflow orchestration
- prompt construction

---

# Architecture

```text
Execution Framework

↓

StageArtifact

↓

Execution Engine

↓

Workspace

↓

Workspace Registry
```

The Execution Engine acts as the bridge between AI output and the real project.

---

# Why Separate Execution?

Without an Execution Engine:

```text
LLM

↓

Filesystem
```

Problems include:

- uncontrolled file edits
- provider-specific logic
- difficult testing
- poor extensibility

Instead AI DevOS follows:

```text
LLM

↓

StageArtifact

↓

Execution Engine

↓

Filesystem
```

The AI never edits the project directly.

---

# StageArtifact

The Execution Engine consumes a StageArtifact.

Typical artifact contents:

```text
StageArtifact

├── Stage

├── Content

├── Files

├── Metadata
```

The artifact describes the intended changes.

The Execution Engine decides how to apply them.

---

# Workspace Synchronization

After execution:

```text
Execution Engine

↓

Workspace

↓

Workspace Parser

↓

Workspace Registry

↓

Updated Metadata
```

The registry remains synchronized with the project.

---

# Execution Lifecycle

Every execution follows the same pipeline.

```text
StageArtifact

↓

Execution Engine

↓

Workspace Changes

↓

Registry Update

↓

Execution Result
```

This process is independent of the LLM provider.

---

# Current Execution Engine

The current architecture is designed to integrate with:

```text
Aider
```

Aider receives the generated artifact and safely applies changes to the repository.

The Agent Framework never communicates with Aider directly.

---

# Future Execution Engines

The architecture supports multiple execution engines.

Examples:

```text
Aider

Claude Code

Cursor

OpenHands

Codex

Continue.dev

Custom Engine
```

Each engine implements the same execution interface.

Changing engines does not affect the Agent Framework or Execution Framework.

---

# Execution Interface

Every execution engine should expose a common interface.

Example:

```text
ExecutionEngine

↓

execute(StageArtifact)

↓

ExecutionResult
```

This allows engines to be interchangeable.

---

# Safe Code Modification

The Execution Engine is responsible for ensuring safe modifications.

Typical responsibilities include:

- validating file paths
- preventing accidental overwrites
- creating missing directories
- applying incremental edits
- handling merge conflicts

These concerns are intentionally separated from the Agent Framework.

---

# Workspace Updates

Whenever a file changes:

```text
Execution Engine

↓

Workspace

↓

Workspace Parser

↓

Checksum

↓

Workspace Registry
```

The Context Framework automatically receives updated workspace metadata during the next execution.

---

# Tool Execution

Future execution engines may support:

- formatting code
- running linters
- compiling projects
- executing tests
- generating documentation
- dependency installation

These operations remain part of the Execution Engine rather than the agents.

---

# Communication Rules

Allowed interactions:

```text
Execution Framework

↓

Execution Engine

↓

Workspace
```

Forbidden interactions:

```text
Agent

✗ Filesystem
```

```text
Agent

✗ Shell Commands
```

```text
Agent

✗ Git
```

The Agent Framework remains purely cognitive.

---

# Why This Design?

Separating reasoning from execution provides several advantages.

### Provider Independence

Any LLM can generate artifacts.

---

### Tool Independence

Any execution engine can apply changes.

---

### Safer Execution

The AI never modifies files directly.

---

### Easier Testing

Execution engines can be tested independently from AI agents.

---

### Extensibility

New execution tools can be added without changing workflows.

---

# Future Enhancements

Future versions may support:

- Parallel execution
- Incremental patching
- Live preview
- Automatic rollback
- Git integration
- Container execution
- Remote execution
- Cloud workspaces
- Multi-repository support

These enhancements remain isolated inside the Execution Engine.

---

# Complete Execution Flow

```text
Workflow

↓

Execution Framework

↓

Agent

↓

LLM

↓

StageArtifact

↓

Execution Engine

↓

Workspace

↓

Workspace Registry

↓

Review

↓

Memory

↓

Next Stage
```

---

# Key Takeaways

- Agents never modify project files.
- The Execution Engine owns all workspace changes.
- StageArtifacts describe what should be applied.
- Execution engines are interchangeable.
- Workspace synchronization occurs after every execution.
- The architecture supports Aider today and other execution engines in the future.
- Separating reasoning from execution keeps AI DevOS modular, testable, and provider-independent.
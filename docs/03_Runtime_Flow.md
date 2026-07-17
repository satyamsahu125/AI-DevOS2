# AI DevOS — Runtime Flow

Version: 1.0

---

# 1. Purpose

This document describes the complete runtime execution lifecycle of AI DevOS.

It explains how a project moves from creation to completion, how workflow stages execute, how context is built, how AI agents generate artifacts, how reviews are performed, and how knowledge is extracted into long-term memory.

Unlike the System Architecture document, this specification focuses on **runtime behavior** rather than component structure.

---

# 2. Runtime Philosophy

AI DevOS follows a deterministic execution model.

Every stage follows the exact same lifecycle regardless of the AI provider, workflow stage, or generated artifact.

Every stage execution consists of:

1. Context Construction
2. Prompt Construction
3. Agent Execution
4. Review
5. Retry (if required)
6. Memory Extraction
7. Workflow Progression

This ensures predictable execution across every workflow.

---

# 3. Complete Runtime Lifecycle

```

Create Project

↓

Initialize Workflow

↓

Select Current Stage

↓

Create / Resume Stage Session

↓

Build Agent Context

↓

Compose Prompt

↓

Execute Agent

↓

Receive Stage Artifact

↓

Review Artifact

↓

Approved ?

↓

Yes -------------------- No

↓

Extract Memory Retry Stage

↓

Destroy Session

↓

Advance Workflow

↓

Next Stage

↓

Project Complete

```

---

# 4. Project Lifecycle

Every execution begins with project creation.

```

Project

↓

Workflow

↓

Stage Queue

↓

Execution

↓

Completion

```

The project itself contains no runtime information.

Runtime information is stored separately inside Stage Sessions and Runtime Memory.

---

# 5. Stage Lifecycle

Every workflow stage follows an identical lifecycle.

```

Waiting

↓

Running

↓

Review

↓

Approved

↓

Completed

```

or

```

Waiting

↓

Running

↓

Review

↓

Rejected

↓

Retry

↓

Running

```

Stages never skip the review process.

---

# 6. Stage Session Lifecycle

Every stage owns exactly one Stage Session.

The Stage Session stores the runtime conversation between the agent and reviewer.

```

Create Session

↓

System Prompt

↓

User Prompt

↓

Assistant Response

↓

Reviewer Feedback

↓

Retry ?

↓

Assistant Response

↓

Approved

↓

Destroy Session

```

The session is temporary.

It never becomes long-term memory.

---

# 7. Context Construction

Before execution begins, the Context Builder prepares the Agent Context.

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

Runtime Memory

↓

Context Budget

↓

Agent Context

```

The Agent receives only the final Agent Context.

It never communicates directly with memory providers.

---

# 8. Prompt Construction

The Prompt Composer converts the execution context into prompts.

Inputs

- Prompt Template
- Agent Context
- Current Task

Outputs

- System Prompt
- User Prompt

These prompts are stored inside the Stage Session.

---

# 9. Agent Execution

The AgentExecutor controls execution.

Runtime flow:

```

AgentExecutor

↓

Create Agent

↓

before_execute()

↓

prepare()

↓

LLM Manager

↓

process()

↓

after_generate()

↓

validate()

↓

Stage Artifact

```

Agents remain completely stateless.

---

# 10. LLM Execution

Every AI request follows the same path.

```

Base Agent

↓

LLM Manager

↓

LLM Runtime

↓

Provider Factory

↓

Active Provider

↓

Chat Response

```

The provider may be:

- Gemini
- Ollama
- OpenAI
- Claude
- OpenRouter
- Future Providers

The agent is unaware of which provider generated the response.

---

# 11. Artifact Creation

The AI response is converted into a StageArtifact.

StageArtifact represents the official output of one workflow stage.

Examples

Product Owner

Business Requirements

Architect

Architecture Design

Backend Developer

Source Code

QA

Test Suite

DevOps

Deployment Configuration

Artifacts are immutable once approved.

---

# 12. Review Cycle

Every artifact passes through the Review Engine.

```

Stage Artifact

↓

Review Engine

↓

Review Parser

↓

Change Planner

↓

Review Result

```

Possible results

Approved

Changes Required

No artifact bypasses the reviewer.

---

# 13. Retry Cycle

If the reviewer rejects the artifact:

```

Reviewer

↓

Feedback

↓

Stage Session

↓

Retry Count++

↓

Prompt Updated

↓

Agent Executes Again

```

The previous conversation remains inside the Stage Session.

This allows iterative refinement.

---

# 14. Memory Extraction

Only approved artifacts are extracted into long-term memory.

```

Approved Artifact

↓

Extraction Pipeline

↓

Business Extractor

↓

Architecture Extractor

↓

Decision Extractor

↓

Workflow Extractor

↓

Review Extractor

↓

Memory Manager

```

Rejected artifacts are never extracted.

---

# 15. Runtime Memory

Runtime Memory stores temporary information shared across retries within the same stage.

Examples

- intermediate plans
- generated identifiers
- temporary assumptions
- retry metadata

Runtime Memory is destroyed when the stage completes.

---

# 16. Long-Term Memory

Approved knowledge becomes permanent.

Examples

Business Memory

Architecture Memory

Workflow Memory

Review Memory

Decision Memory

Issue Memory

Artifact Memory

These memories become available to future workflow stages.

---

# 17. Session Destruction

After successful extraction:

```

Memory Extraction

↓

Stage Session Destroyed

↓

Runtime Memory Cleared

↓

Next Stage

```

No runtime conversation survives beyond the completed stage.

Only extracted knowledge remains.

---

# 18. Workflow Progression

The Workflow Engine selects the next executable stage.

The execution engine never decides workflow order.

Responsibilities remain separated.

---

# 19. Failure Handling

Possible failures

LLM Failure

Retry Provider

Context Failure

Abort Stage

Review Failure

Retry Stage

Extraction Failure

Abort Workflow

Workspace Failure

Rollback Stage

Each failure is handled independently.

---

# 20. Runtime Guarantees

AI DevOS guarantees:

- Every stage has one session.
- Every stage is reviewed.
- Memory is extracted only after approval.
- Agents remain stateless.
- Workflow controls execution.
- MemoryManager owns memory.
- Runtime Memory never becomes permanent.
- Stage Sessions never survive completion.
- Providers remain interchangeable.
- Execution is deterministic.

---

# 21. Runtime Summary

The runtime pipeline transforms business requirements into production-ready software through a controlled sequence of execution, review, memory extraction, and workflow progression.

Each subsystem performs exactly one responsibility.

This separation provides predictable execution, easier debugging, provider independence, and long-term maintainability while preserving project knowledge across the entire software development lifecycle.
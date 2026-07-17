# AI DevOS — Folder Structure

Version: 1.0

---

# 1. Purpose

This document describes the directory structure of AI DevOS and the responsibility of every package.

The project is organized according to the principle of **single responsibility**, where each package owns one subsystem of the platform.

Folder organization reflects system architecture.

---

# 2. Design Philosophy

AI DevOS is organized into independent modules.

Each module:

- owns one responsibility
- exposes a clear API
- has minimal coupling
- communicates through abstractions

No folder should contain unrelated business logic.

---

# 3. Root Structure

```
AI-DevOS/

├── app/
├── config/
├── docs/
├── prompts/
├── tests/
├── workspace/
├── scripts/
├── requirements.txt
├── README.md
└── .env
```

---

# 4. app/

The `app` directory contains the entire application.

Every runtime subsystem is implemented here.

```
app/

├── agents/
├── context/
├── execution/
├── llm/
├── memory/
├── orchestration/
├── prompts/
├── review/
├── session/
├── workspace/
├── api/
├── core/
└── main.py
```

---

# 5. agents/

Responsible for AI agent implementations.

```
agents/

base/
registry/
implementations/
```

Contains:

- BaseAgent
- specialized agents
- AgentRegistry

Never contains workflow logic.

---

# 6. context/

Responsible for context construction.

Contains

```
ContextBuilder

AgentContext

Selectors

ContextBudget
```

Never communicates directly with LLM providers.

---

# 7. execution/

Coordinates runtime execution.

Contains

```
ExecutionContext

ExecutionResult

StageArtifact

AgentExecutor
```

Acts as the execution pipeline.

---

# 8. llm/

Provides provider-independent communication with AI models.

Contains

```
LLMManager

LLMRuntime

ProviderFactory

Providers

ChatRequest

ChatResponse
```

Only this module communicates with external AI providers.

---

# 9. memory/

Owns every memory operation.

Contains

```
MemoryManager

Providers

RuntimeMemory

RuntimeStore

ExtractionPipeline

Extractors
```

No other module writes directly into memory.

---

# 10. orchestration/

Owns workflow execution.

Contains

```
WorkflowEngine

Workflow

StageProfile

DependencyGraph
```

Coordinates project execution.

---

# 11. prompts/

Contains prompt templates.

Examples

```
Product Owner

Architect

Backend

Frontend

QA

Reviewer
```

Prompt loading is handled by PromptLoader.

---

# 12. review/

Responsible for artifact evaluation.

Contains

```
ReviewEngine

ReviewParser

ReviewResult

ChangePlanner
```

No generation logic exists here.

---

# 13. session/

Owns temporary runtime conversations.

Contains

```
StageSession

SessionManager

Message
```

Sessions exist only during stage execution.

---

# 14. workspace/

Responsible for workspace indexing.

Contains

```
WorkspaceRegistry

WorkspaceIndex

WorkspaceSelector

WorkspaceParser
```

Never stores source code.

---

# 15. api/

Contains REST API endpoints.

Responsibilities

- HTTP routing
- request validation
- response serialization

Business logic remains outside this package.

---

# 16. core/

Contains shared infrastructure.

Examples

```
Configuration

Exceptions

Utilities

Logging

Constants
```

No business logic belongs here.

---

# 17. config/

Stores application configuration.

Examples

```
config.yaml

environment settings

provider configuration
```

Configuration remains external to application code.

---

# 18. docs/

Project documentation.

Includes

- architecture
- frameworks
- development guides
- ADRs
- roadmap

This folder contains no executable code.

---

# 19. prompts/

Contains Markdown prompt templates used by agents.

Prompt templates remain separate from Python code to simplify maintenance and experimentation.

---

# 20. workspace/

Represents the generated project workspace.

Contains

- generated source code
- documentation
- configuration
- deployment files

The framework indexes this directory but does not own its contents.

---

# 21. tests/

Contains automated tests.

Suggested organization

```
unit/

integration/

end_to_end/
```

Tests mirror the application structure.

---

# 22. scripts/

Contains development utilities.

Examples

- migrations
- setup scripts
- maintenance tools
- benchmarking

Scripts are not imported by the application.

---

# 23. Dependency Rules

High-level dependency flow

```
API

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

Memory, Review, and Workspace remain independent supporting services.

Circular dependencies are prohibited.

---

# 24. Folder Ownership

Every package owns exactly one subsystem.

Examples

```
memory/

↓

all memory operations

review/

↓

all review operations

workspace/

↓

all workspace indexing

llm/

↓

all provider communication
```

Responsibilities never overlap.

---

# 25. Extension Guidelines

New functionality should be added by extending existing modules rather than creating unrelated folders.

Examples

Adding a provider

```
llm/providers/
```

Adding a new agent

```
agents/implementations/
```

Adding memory

```
memory/extractors/
memory/providers/
```

---

# 26. Summary

The AI DevOS folder structure mirrors the architecture of the system itself.

Every package has a clearly defined responsibility, communicates through well-defined abstractions, and remains independent from unrelated concerns.

This organization improves maintainability, scalability, testability, and onboarding for future contributors.
# AI DevOS — Development Guide

Version: 1.0

---

# 1. Purpose

This guide explains how to develop, extend, and maintain AI DevOS.

It defines the engineering standards, development workflow, and extension patterns used throughout the project.

Every contributor should read this document before modifying the codebase.

---

# 2. Design Principles

AI DevOS follows these engineering principles.

• Single Responsibility Principle

• Dependency Inversion

• Composition over Inheritance

• Provider Independence

• Stateless Execution

• Centralized Ownership

• Explicit Interfaces

Every subsystem should own exactly one responsibility.

---

# 3. Project Philosophy

The project is designed around independent frameworks.

Instead of building one large application, AI DevOS is composed of small cooperating systems.

Example

Workflow Engine

↓

Execution Framework

↓

Agent Framework

↓

LLM Framework

↓

Provider

Each layer communicates only through public interfaces.

---

# 4. Coding Standards

General rules

- Use type hints.
- Write descriptive docstrings.
- Prefer composition over inheritance.
- Avoid global state.
- Keep functions small.
- Prefer explicit naming.

Example

Good

```
MemoryManager
```

Bad

```
Manager
```

---

# 5. Folder Ownership

Never place code into unrelated folders.

Examples

Memory logic

↓

memory/

Provider logic

↓

llm/providers/

Review logic

↓

review/

Execution logic

↓

execution/

If a class does not belong clearly to a subsystem, reconsider the design.

---

# 6. Dependency Rules

Allowed dependency direction

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

Never reverse the dependency chain.

---

# 7. Creating a New Agent

Step 1

Create a class inside

```
app/agents/implementations/
```

Example

```
SecurityReviewerAgent
```

Step 2

Inherit

```
BaseAgent
```

Step 3

Override only required lifecycle methods.

Usually

```
prepare()

process()

validate()
```

Step 4

Register inside

```
AgentRegistry
```

No additional framework changes are required.

---

# 8. Creating a New Provider

Step 1

Create provider

```
app/llm/providers/
```

Example

```
ClaudeProvider
```

Step 2

Inherit

```
BaseProvider
```

Step 3

Implement

```
chat()
```

Step 4

Register inside

```
ProviderFactory
```

Nothing else changes.

---

# 9. Creating a New Memory Type

Step 1

Create provider

```
memory/providers/
```

Step 2

Register provider inside

```
MemoryManager
```

Step 3

Create extractor

```
memory/extractors/
```

Step 4

Register extractor

```
ExtractionPipeline
```

MemoryManager API remains unchanged.

---

# 10. Creating a New Workflow Stage

Step 1

Create Agent

↓

implementations/

Step 2

Create prompt

↓

prompts/

Step 3

Create StageProfile

↓

orchestration/

Step 4

Register StageProfile

↓

StageRegistry

Step 5

Update DependencyGraph

The Execution Framework requires no changes.

---

# 11. Prompt Guidelines

Prompts should:

- describe the role
- describe the objective
- describe expected output
- avoid implementation details

Prompt templates belong in Markdown files.

Never hardcode prompts inside Python.

---

# 12. Memory Guidelines

Never write directly into memory.

Correct

```
Artifact

↓

Extraction Pipeline

↓

Memory Manager
```

Incorrect

```
Agent

↓

Memory Manager
```

Only approved artifacts become memory.

---

# 13. Context Guidelines

Agents never build context.

Always use

```
ContextBuilder

↓

AgentContext
```

Do not manually load

- memory
- workspace
- documents

inside agents.

---

# 14. Review Guidelines

Agents never approve themselves.

Every artifact must pass through

```
Review Engine
```

before workflow progression.

---

# 15. Workspace Guidelines

Never scan the workspace manually.

Always use

```
WorkspaceRegistry
```

or

```
WorkspaceSelector
```

Future implementations may change the indexing mechanism.

---

# 16. Error Handling

Every subsystem owns its own errors.

Examples

Provider

↓

API failures

Memory

↓

Storage failures

Workflow

↓

Dependency failures

Execution

↓

Runtime failures

Do not leak exceptions across subsystem boundaries.

---

# 17. Testing Strategy

Recommended structure

```
tests/

unit/

integration/

end_to_end/
```

Unit Tests

↓

Single component

Integration Tests

↓

Subsystem interaction

End-to-End Tests

↓

Complete workflow execution

---

# 18. Logging

Every subsystem should log meaningful events.

Examples

Workflow

↓

Stage Started

Execution

↓

Agent Executed

Review

↓

Artifact Approved

Memory

↓

Knowledge Extracted

Avoid excessive logging.

---

# 19. Documentation

Every public class should contain

- purpose
- responsibilities
- ownership

Every framework should have

- architecture
- lifecycle
- extension guide

Documentation should evolve alongside the code.

---

# 20. Pull Request Guidelines

Before submitting changes

✓ Tests pass

✓ Documentation updated

✓ No circular dependencies

✓ Folder ownership respected

✓ New interfaces documented

✓ Public APIs unchanged unless required

---

# 21. Things to Avoid

Do not

- call providers directly
- bypass ContextBuilder
- bypass MemoryManager
- bypass ReviewEngine
- hardcode prompts
- duplicate business logic
- introduce circular dependencies

---

# 22. Development Checklist

Before merging

✓ Code compiles

✓ Tests pass

✓ Architecture unchanged

✓ Documentation updated

✓ Naming consistent

✓ Type hints added

✓ Public APIs reviewed

---

# 23. Future Contributions

Preferred contribution areas

- new providers

- additional reviewers

- better extractors

- semantic retrieval

- execution metrics

- monitoring

- visualization

Framework changes should remain backward compatible whenever possible.

---

# 24. Summary

The AI DevOS Development Guide defines the engineering practices used throughout the project.

By following these conventions, contributors can extend the platform while preserving its modular architecture, clear ownership boundaries, and long-term maintainability.
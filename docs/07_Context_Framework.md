# AI DevOS — Context Framework

Version: 1.0

---

# 1. Purpose

The Context Framework is responsible for constructing the complete execution context required by an AI agent.

Instead of allowing agents to directly access memory, workspace files, project documents, or runtime state, the Context Framework assembles only the information required for the current workflow stage.

This makes context deterministic, reproducible, and optimized for LLM execution.

---

# 2. Design Philosophy

The Context Framework follows one principle:

> Agents consume context.
>
> They never build it.

This separation ensures that:

- agents remain stateless
- prompt size stays controlled
- memory ownership remains centralized
- execution becomes deterministic

---

# 3. Responsibilities

The Context Framework is responsible for:

- loading project memory
- loading runtime memory
- selecting workspace metadata
- selecting project documents
- selecting review history
- enforcing context budgets
- producing an AgentContext

The Context Framework never:

- calls the LLM
- updates memory
- scans the filesystem
- modifies workflow

---

# 4. Architecture

```

AgentExecutor

↓

ContextBuilder

↓

Selectors

↓

MemoryManager

WorkspaceRegistry

DocumentStore

ReviewStore

↓

ContextBudget

↓

AgentContext

↓

Agent

```

---

# 5. Context Lifecycle

Every workflow stage follows the same process.

```

Stage Starts

↓

ContextBuilder

↓

Load Memory

↓

Load Runtime

↓

Load Workspace

↓

Load Documents

↓

Load Reviews

↓

Trim Context

↓

AgentContext

↓

Agent

```

---

# 6. ContextBuilder

The ContextBuilder orchestrates the complete context creation process.

Responsibilities

- coordinate selectors
- assemble AgentContext
- apply context budget

The ContextBuilder owns no data.

It only coordinates data providers.

---

# 7. AgentContext

AgentContext is the only context object consumed by agents.

Typical contents

- project
- stage
- task
- memory
- runtime memory
- workspace index
- project documents
- review history
- metadata

The agent never communicates with any subsystem directly.

---

# 8. Context Components

The Context Framework assembles information from multiple independent sources.

```

Long-Term Memory

Runtime Memory

Workspace

Documents

Review History

Metadata

```

Each component is loaded independently.

---

# 9. Memory Selector

Purpose

Load approved project knowledge.

Reads

MemoryManager

Returns

Business Memory

Architecture Memory

Workflow Memory

Decision Memory

Issue Memory

Artifact Memory

The selector never modifies memory.

---

# 10. Runtime Memory

Runtime Memory stores temporary state for the active stage.

Examples

- retry state
- temporary assumptions
- intermediate planning
- execution metadata

Runtime Memory is isolated per stage.

---

# 11. Workspace Selector

Purpose

Load workspace metadata.

The selector communicates only with the Workspace Registry.

It never scans the project directory.

Returned information

- indexed files
- modules
- checksums
- metadata

Future versions may include dependency graphs.

---

# 12. Document Selector

Purpose

Load project documents.

Examples

- requirements
- architecture
- API specifications
- design documents

Only documents permitted by the StageProfile are included.

---

# 13. Review Selector

Purpose

Load historical reviewer feedback.

Typical contents

- previous review comments
- rejected artifacts
- quality recommendations

This enables future stages to avoid repeating earlier mistakes.

---

# 14. Metadata

Metadata contains execution information.

Examples

- project id
- workflow id
- stage name
- timestamps
- execution identifiers

Metadata is not part of business memory.

---

# 15. Context Budget

LLMs have finite context windows.

The Context Budget determines how much information may be included.

Responsibilities

- estimate token usage
- remove low-priority information
- preserve critical knowledge

Future implementations may use token-aware budgeting.

---

# 16. Context Prioritization

Information is loaded in priority order.

Highest

- current task
- runtime memory
- reviewer feedback

Medium

- architecture
- workflow
- documents

Lowest

- historical artifacts
- optional metadata

Lower-priority information is removed first when limits are reached.

---

# 17. Data Flow

```

MemoryManager

↓

MemorySelector

↓

ContextBuilder

↓

AgentContext

↓

Agent

```

The same flow applies to every selector.

---

# 18. Stage Awareness

The Context Framework is stage-aware.

Example

Product Owner receives:

- requirements
- business goals

Architect receives:

- requirements
- business memory
- review history

Backend Developer receives:

- architecture
- APIs
- workspace index
- coding decisions

QA receives:

- requirements
- architecture
- generated source metadata

Every stage receives different context.

---

# 19. Context Isolation

The Context Framework guarantees that one stage cannot access information that has not yet been approved.

Example

Backend Developer cannot access DevOps outputs because they do not yet exist.

This prevents future knowledge leakage.

---

# 20. Runtime Guarantees

The Context Framework guarantees:

✓ Context is deterministic

✓ Context is stage-aware

✓ Memory remains read-only

✓ Agents receive one AgentContext

✓ Workspace is indexed, not scanned

✓ Runtime Memory is isolated

✓ Context size is controlled

---

# 21. Future Improvements

Future versions may support:

- semantic retrieval
- vector search
- adaptive context ranking
- graph-based dependency retrieval
- incremental context updates
- token-aware optimization
- cross-project context sharing

These improvements will not require changes to agents.

---

# 22. Design Decisions

The Context Framework intentionally separates context construction from generation because:

- prompts remain consistent
- agents remain simple
- memory ownership is preserved
- execution is reproducible
- debugging becomes easier

Every subsystem performs one responsibility.

---

# 23. Summary

The Context Framework transforms distributed project knowledge into a single structured AgentContext.

By coordinating memory, runtime state, workspace metadata, project documents, and review history through dedicated selectors, it enables every AI agent to operate with the precise information required for its stage while maintaining deterministic, efficient, and scalable execution.
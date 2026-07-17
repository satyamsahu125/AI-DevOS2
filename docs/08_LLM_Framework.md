# AI DevOS — LLM Framework

Version: 1.0

---

# 1. Purpose

The LLM Framework provides a unified interface between AI DevOS and external Large Language Models (LLMs).

Its purpose is to isolate provider-specific implementations from the rest of the framework.

Every AI request passes through this framework.

No subsystem communicates with providers directly.

---

# 2. Design Philosophy

The LLM Framework follows one principle.

> The framework communicates with an abstraction,
> never with a concrete provider.

Every provider implements the same interface.

Therefore:

Gemini

↓

Ollama

↓

OpenAI

↓

Claude

↓

OpenRouter

can all be swapped without changing any business logic.

---

# 3. Responsibilities

The LLM Framework is responsible for:

- receiving chat requests
- selecting providers
- formatting requests
- executing requests
- returning normalized responses

The LLM Framework never:

- builds prompts
- loads memory
- owns workflow
- validates outputs
- stores conversations

---

# 4. Architecture

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

Concrete Provider

↓

LLM API
```

---

# 5. Layer Responsibilities

## LLMManager

Public API used by the framework.

Responsibilities

- receive ChatRequest
- delegate to runtime
- return ChatResponse

Never knows which provider is active.

---

## LLMRuntime

Coordinates execution.

Responsibilities

- request provider
- execute provider
- normalize responses

No provider-specific logic exists here.

---

## ProviderFactory

Responsible for selecting the active provider.

Input

```
settings.llm.provider
```

Output

```
GeminiProvider

or

OllamaProvider

or

OpenAIProvider

...
```

Only this class knows which provider is active.

---

## BaseProvider

Defines the provider contract.

Every provider must implement

```
chat(
    ChatRequest
)

↓

ChatResponse
```

This guarantees provider interchangeability.

---

# 6. Request Lifecycle

Every request follows the same path.

```
Agent

↓

LLMManager

↓

LLMRuntime

↓

ProviderFactory

↓

Concrete Provider

↓

LLM

↓

ChatResponse
```

The agent never sees the provider.

---

# 7. ChatRequest

Every provider receives the same request model.

Typical fields

- model
- messages
- temperature
- max_tokens

No provider-specific parameters are exposed to the framework.

---

# 8. ChatResponse

Every provider returns the same response.

Typical fields

- content
- prompt_tokens
- completion_tokens
- finish_reason

This allows every agent to process responses identically.

---

# 9. Message Model

Conversation history is represented as

```
Message

role

content
```

Possible roles

- system
- user
- assistant

Providers convert these messages into their native format.

---

# 10. Provider Independence

Internally

Gemini

↓

Gemini SDK

Ollama

↓

HTTP API

OpenAI

↓

REST API

Claude

↓

Anthropic SDK

Externally

Everything appears as

```
ChatRequest

↓

ChatResponse
```

The rest of AI DevOS never changes.

---

# 11. Why ProviderFactory?

Without ProviderFactory

Every subsystem would require

```
if provider == ...

```

This would violate the Open/Closed Principle.

Instead

```
ProviderFactory

↓

BaseProvider

↓

Concrete Provider
```

New providers require no changes elsewhere.

---

# 12. Provider Contract

Every provider must implement

```
chat(
    request: ChatRequest
)

↓

ChatResponse
```

No additional public methods are required.

Optional helper methods may exist internally.

---

# 13. Configuration

Current provider selection

```
settings.llm.provider
```

Example

```
provider = "gemini"
```

Changing this value changes the active provider.

No code modifications are required.

---

# 14. Error Handling

Provider-specific errors remain inside providers.

Framework-level errors remain inside the runtime.

Examples

Provider

- authentication
- timeout
- rate limit
- invalid model

Runtime

- provider unavailable
- unsupported provider

Agents never handle provider errors directly.

---

# 15. Token Accounting

Every provider returns

- prompt tokens
- completion tokens

Future versions may include

- cost estimation
- provider benchmarking
- token analytics
- execution dashboards

---

# 16. Streaming Support

Current Version

Blocking responses.

Future

```
Provider

↓

Streaming Tokens

↓

LLMRuntime

↓

AgentExecutor
```

The public interface remains unchanged.

---

# 17. Future Providers

Supported roadmap

- Gemini
- Ollama
- OpenAI
- Claude
- OpenRouter
- Azure OpenAI
- AWS Bedrock
- Local GGUF Models

Adding providers requires:

1. Create provider class.
2. Inherit BaseProvider.
3. Register in ProviderFactory.

Nothing else changes.

---

# 18. Security

Future improvements

- encrypted API keys
- automatic key rotation
- retry policies
- request logging
- provider failover

These remain isolated inside the framework.

---

# 19. Runtime Guarantees

The LLM Framework guarantees

✓ One public entry point

✓ Provider independence

✓ Unified request model

✓ Unified response model

✓ Centralized provider selection

✓ Replaceable providers

✓ Stateless communication

---

# 20. Design Decisions

The framework intentionally separates

Request Construction

↓

Provider Selection

↓

Execution

↓

Response Normalization

This separation allows every subsystem to remain independent from external AI vendors.

---

# 21. Summary

The LLM Framework provides a provider-independent communication layer for AI DevOS.

By standardizing requests and responses through `LLMManager`, `LLMRuntime`, `ProviderFactory`, and `BaseProvider`, the framework can integrate multiple AI providers while keeping the rest of the system completely unchanged.

This architecture enables flexibility, maintainability, and future scalability as new language models become available.
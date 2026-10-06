Enterprise AI Architect Journey
My journey from Pega Architect to Enterprise AI & Automation Architect.

Objective
Build the technical skills required to design, build, and architect enterprise AI systems outside of a single platform.

Learning Focus
- Python & Software Engineering
- LLM Engineering
- Context Engineering
- RAG & Knowledge Systems
- Agentic AI
- MCP
- Production AI Engineering
- AI Security
- AI Evaluation
- Enterprise AI Architecture

Current Progress

Python & Software Engineering Foundation

Milestone	Status
Day 1 — Python Basics	✅ Completed
Day 2 — Control Flow	✅ Completed
Day 3 — Data Structures & JSON	✅ Completed
Day 4 — Functions & Pipelines	✅ Completed
Day 5 — Modules & Packages	✅ Completed
Day 6 — Files, JSON, CSV & Configuration	✅ Completed
Day 7 — Integration Review	✅ Completed
Day 8 — Object-Oriented Programming	✅ Completed
Day 9 — Dataclasses & Type Hints	✅ Completed
Day 10 — Comprehensions, Iterators & Generators	✅ Completed
Day 11 — Decorators & Context Managers	✅ Completed
Day 12 — Logging, Debugging & Testing	✅ Completed
Day 13 — REST API Client	✅ Completed
Day 14 — Review, Refactoring, Design & Testing	✅ Completed
Day 15 — HTTP Fundamentals	✅ Completed
Day 16 — REST API Design	✅ Completed
Day 17 — API Authentication	✅ Completed

Learning Notes
- Day 15 — HTTP Fundamentals: [learning-notes/day15-http-fundamentals.md](learning-notes/day15-http-fundamentals.md)
- Day 16 — REST API Design: [learning-notes/day16_1_employee_rest_api_design.md](learning-notes/day16_1_employee_rest_api_design.md)
- Day 16 — Employee Leave API Design: [learning-notes/day16_2_employee_leave_api_design.md](learning-notes/day16_2_employee_leave_api_design.md)
- Day 16 — API Architecture Review: [learning-notes/day16_3_api_architecture_review.md](learning-notes/day16_3_api_architecture_review.md)
- Day 17 — API Authentication: [learning-notes/day17-api-authentication.md](learning-notes/day17-api-authentication.md)

Day 16 Validation
Day 16 completed the REST API design stage.

Design work completed:
- Employee CRUD API
- Resource vs collection modeling
- Path vs query design
- Employee → Leave Request relationship
- Nested collection and top-level resource decisions
- Lifecycle/state-transition modeling
- Cancellation vs physical deletion
- Error contract design
- Review and correction of a flawed enterprise API

Architectural principles reinforced:
- Resource-oriented nouns instead of RPC-style action URLs
- Correct HTTP method semantics
- Query parameters for collection filtering
- Explicit PUT vs PATCH contract
- Clarification of ambiguous business states before API design

Day 17 Validation
Day 17 completed the authentication stage of the API sequence.

Exercises completed:
- API key request
- Bearer token request
- JWT creation, verification and claim mapping
- JWT wrong-key verification failure
- OAuth Client Credentials request and protected-API-style Bearer request

Authentication mechanics practiced:
- API key in custom request header
- Authorization: Bearer <token>
- JWT HEADER.PAYLOAD.SIGNATURE structure
- PyJWT encode/decode with HS256
- Explicit allowed algorithm configuration
- JWT claim mapping: sub → employee_id, role → role, department → department, exp → expiration
- OAuth form data with grant_type and scope
- OAuth client authentication using HTTP Basic
- Access token → Bearer Authorization header

Important corrections:
- JWT decoding, signature verification, claim validation and application claim mapping are distinct concepts.
- Unverified JWT header inspection is for inspection/debugging, not a trust decision.
- The HS256 demo key was increased to 32+ bytes after the PyJWT key-length warning.
- A real OAuth authorization server and protected API were not available in the open inspection environment; the OAuth token response was simulated and is documented as such.

Real-world follow-up:
- End-to-end OAuth/JWT testing with a real authorization server and protected API remains intentionally deferred until a suitable controlled identity-provider/test environment is available.

Roadmap Alignment
Day 15 → HTTP Fundamentals
Day 16 → REST API Design
Day 17 → Authentication: API keys, OAuth basics, JWT
Day 18 → Python HTTP Clients
Day 19 → External API Integration
Day 20 → Timeouts, retries, exponential backoff, rate limits
Day 21 → Review

LLM Engineering is intentionally later in the roadmap at Day 29, after the required Python, API, and supporting engineering foundations.

Repository Structure
learning-notes/    - Learning notes and technical concepts
python/            - Python practice and exercises
ai-engineering/    - AI engineering experiments and components
architecture/      - Architecture diagrams and decisions
projects/          - Major portfolio projects

Day-based Python structure
python/
- day13_rest_api_client/
- day14_api_integration/
- day15_http_fundamentals/
- day16_rest_api_design/
- day17_api_authentication/

Day 15 and onward use numbered exercises inside the day-specific folder to keep the repository organized and easy to navigate.

Engineering Principles
This repository is not only a collection of syntax exercises.
The learning approach emphasizes:
- clear separation of responsibilities
- reusable components
- readable code
- type-aware design
- testable business logic
- isolation of external dependencies
- error handling
- refactoring
- architectural thinking
- practical enterprise-oriented design

The learning method is:
1. Understand what the concept is
2. Understand why it is useful
3. Understand how it works
4. Use small examples and predictions
5. Complete a focused exercise independently
6. Review the implementation
7. Capture the learning in repository documentation

Learning-process rule
For every new Python/API/library concept introduced in an exercise:
1. Explain the concept
2. Explain why it is needed
3. Explain how it works
4. Show the relevant Python/API syntax
5. Give a small example
6. State expected success/failure behavior
7. Then provide the focused exercise

Do not require the learner to independently discover hidden library APIs, syntax, prerequisites, or endpoint response structures.

The goal is to progress from:
Python Syntax
      ↓
Software Engineering
      ↓
API & Integration Engineering
      ↓
LLM Engineering
      ↓
RAG & Knowledge Systems
      ↓
Agentic AI / MCP
      ↓
Production AI Engineering
      ↓
Enterprise AI Architecture

About
My journey from Pega Architect to Enterprise AI & Automation Architect.

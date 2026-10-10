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
Day 18 — Python HTTP Clients & API Integration	✅ Completed
Day 19 — External API Integration	✅ Completed
Day 20 — API Resilience	✅ Completed

Learning Notes
- Day 15 — HTTP Fundamentals: [learning-notes/day15-http-fundamentals.md](learning-notes/day15-http-fundamentals.md)
- Day 16 — REST API Design: [learning-notes/day16_1_employee_rest_api_design.md](learning-notes/day16_1_employee_rest_api_design.md)
- Day 16 — Employee Leave API Design: [learning-notes/day16_2_employee_leave_api_design.md](learning-notes/day16_2_employee_leave_api_design.md)
- Day 16 — API Architecture Review: [learning-notes/day16_3_api_architecture_review.md](learning-notes/day16_3_api_architecture_review.md)
- Day 17 — API Authentication: [learning-notes/day17-api-authentication.md](learning-notes/day17-api-authentication.md)
- Day 18 — Python HTTP Clients & API Integration: [learning-notes/day18-python-http-clients.md](learning-notes/day18-python-http-clients.md)
- Day 19 — External API Integration: [learning-notes/day19-external-api-integration.md](learning-notes/day19-external-api-integration.md)
- Day 20 — API Resilience: [learning-notes/day20-api-resilience.md](learning-notes/day20-api-resilience.md)

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

Day 20 Validation
Day 20 completed the API resilience stage.

Exercises completed:
- Request timeout and Timeout exception handling
- Basic bounded retry for 503 Service Unavailable
- Exponential backoff between retries
- 429 Too Many Requests handling
- Retry-After handling
- Integrated resilient API client

Resilience mechanics practiced:
- Explicit request timeout
- requests.exceptions.Timeout
- Maximum retry attempts
- 503-specific retry decision
- Exponential delay calculation
- time.sleep() between retry attempts
- 429 rate-limit detection
- Retry-After delay handling

Failure behavior reinforced:
- Timeout -> handle transport-level timeout
- 503 -> retry with bounded exponential backoff
- 429 -> respect Retry-After when supplied
- 404 -> do not blindly retry

Engineering notes:
- Manual retry logic was used so the mechanics remain visible before introducing higher-level retry abstractions.
- The controlled 429 demonstration used separate httpbin endpoints for status and Retry-After header generation; a real API would normally supply Retry-After on the 429 response itself.
- Production code should validate auxiliary responses before consuming headers and should apply API-specific retry policies.

Day 19 Validation
Day 19 completed the external API integration stage.

Exercises completed:
- GitHub public user integration
- GitHub repository collection integration
- Multi-endpoint user summary integration
- External-to-application data normalization
- Reusable runtime GitHub user lookup

Integration capabilities demonstrated:
- Real external API calls using requests.Session()
- Object and collection response handling
- Multi-endpoint data composition
- Derived application-level values such as total stars
- External schema → application schema mapping
- Controlled 404 handling without a traceback

Engineering note:
- The final lookup exercise was accepted as completed with one recorded production refinement: the current HTTPError handler labels every HTTPError as USER NOT FOUND; production code should distinguish 404 from other 4xx/5xx responses.
- GitHub/httpbin values are external-system data and can change over time.

Day 18 Validation
Day 18 completed the Python HTTP client and API integration stage.

Exercises completed:
- requests.Session fundamentals
- Session-level headers and request-level header override
- Authenticated reusable Session with Bearer token
- GET with query parameters
- HTTP response validation with raise_for_status()
- HTTPError handling for a deliberate 404
- POST with JSON request body
- Combined GET + POST employee API integration

Key Python HTTP client mechanics practiced:
- requests.Session() for reusable client configuration
- session.headers.update(...) for common headers/authentication
- params={...} for query parameters
- json={...} for JSON request bodies
- response.raise_for_status() for HTTP error handling
- response.json() for response payload parsing

Important engineering note:
- Session-level configuration is reused across multiple endpoints, while request-specific headers/parameters remain local to the individual call.
- HTTP response validation should occur before processing a business payload when the payload is only meaningful after a successful operation.
- httpbin.org was used as an echo/inspection service, not as a real authentication server or protected enterprise API.

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
Day 18 → Python HTTP Clients & API Integration
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
- day18_python_http_clients/
- day19_external_api_integration/
- day20_api_resilience/

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

# DAY 16 — EXERCISE 3
# API Architecture Review

## 1. Review Summary

The design supplied by the team is not a clean REST design. It mixes resource-oriented URIs with RPC-style action endpoints and uses `POST` for nearly every operation. This introduces ambiguity, weakens the contract, and makes the API harder to understand, test, and evolve.

The root problem is that the design is driven by client convenience rather than HTTP semantics and resource modeling. A good API should use:

- nouns for resources
- standard HTTP methods for operations
- query parameters for filtering
- explicit status transitions for lifecycle changes

The corrected design should model Employee as a resource, and approval/rejection as a business state transition, not as ad-hoc action endpoints.

---

## 2. Endpoint-by-Endpoint Review

### `/createEmployee`

1. What is wrong?
   - It uses an RPC-like name instead of a resource-oriented URI.
   - The operation is not a standard REST action on a resource.

2. Why is it problematic?
   - It does not signal that an Employee resource is being created.
   - It makes the API less consistent and less discoverable.
   - It is harder to reason about than `POST /employees`.

3. What should it become?
   - `POST /employees`

4. Why is this better?
   - It matches the standard collection pattern.
   - The client creates a new resource in the employee collection.
   - It is clearer and consistent with other REST APIs.

---

### `/getEmployee`

1. What is wrong?
   - It is action-oriented and uses `POST` for retrieval.
   - It does not identify a resource in a standard way.

2. Why is it problematic?
   - GET is the standard method for reading data.
   - Using `POST` for reads hides the fact that this is a simple resource lookup.
   - It is difficult to cache and less consistent with HTTP semantics.

3. What should it become?
   - `GET /employees/{employeeId}`

4. Why is this better?
   - It clearly retrieves one employee resource by identity.
   - It uses the correct HTTP verb for retrieval.
   - It matches the resource model and is easier for clients to understand.

---

### `/updateEmployee`

1. What is wrong?
   - This is also RPC-style naming.
   - It uses `POST` even though update is a resource modification.

2. Why is it problematic?
   - It hides the fact that the API is updating a specific resource.
   - It is less clear than an update against a unique resource URI.

3. What should it become?
   - `PUT /employees/{employeeId}`
   - Or, in a partial-update design, `PATCH /employees/{employeeId}` if only part of the employee record changes.

4. Why is this better?
   - It directly links the update to a specific employee resource.
   - It follows REST semantics and makes the contract easy to reason about.

---

### `/deleteEmployee`

1. What is wrong?
   - It is an action name rather than a resource operation.
   - It uses `POST` for a delete operation.

2. Why is it problematic?
   - Clients cannot rely on standard HTTP semantics.
   - It is less expressive and weaker than standard delete behavior.

3. What should it become?
   - `DELETE /employees/{employeeId}`

4. Why is this better?
   - It communicates deletion directly.
   - It aligns with the resource identity and HTTP methods.
   - It is a consistent contract for clients.

---

### `/employee/EMP001`

1. What is wrong?
   - It uses singular resource naming, while the REST design should model the collection as plural.
   - It is not consistent with the rest of the design.

2. Why is it problematic?
   - The API mixes `/employee` and `/employees` without a clear strategy.
   - It makes the contract inconsistent and confusing.

3. What should it become?
   - `/employees/EMP001`

4. Why is this better?
   - It follows standard collection/item design.
   - The collection is a meaningful resource group, and the item is a specific employee within it.

---

### `/employee?department=IT`

1. What is wrong?
   - It is a singular resource path for a collection-like query.
   - It is not clear whether `/employee` is a single resource or a collection.

2. Why is it problematic?
   - Filtering should be done on a collection resource, not a singular resource path.
   - This creates confusion about API structure and maintainability.

3. What should it become?
   - `GET /employees?department=IT`

4. Why is this better?
   - Filtering belongs in query parameters on the collection resource.
   - It keeps the URI stable and scalable.
   - It supports multiple filters cleanly.

---

### `/employees/EMP001/approve`

1. What is wrong?
   - It hard-codes a business action into the URL.
   - It creates a custom endpoint for a state change rather than representing the actual resource lifecycle.

2. Why is it problematic?
   - This is not a resource; it is an operation disguised as a path.
   - It is harder to extend and less consistent with a clean resource model.
   - It creates custom endpoints for each action, which is difficult to scale.

3. What should it become?
   - A state update on the employee resource, such as:
   - `PATCH /employees/EMP001` with `{ "status": "ACTIVE" }` or a specific state transition contract.
   - For a stronger resource-state model, an explicit status transition could also be modeled through a dedicated lifecycle operation, but it should still be clearly tied to the resource, not buried as a custom action path.

4. Why is this better?
   - It keeps the contract around the employee resource itself.
   - It is easier to reason about and extend.
   - It matches the idea that status is part of the resource lifecycle and not just an ad-hoc action.

---

### `/employees/EMP001/reject`

1. What is wrong?
   - Same issue as the approve endpoint: a custom action URL instead of a resource-oriented state transition.

2. Why is it problematic?
   - It treats a state change as a distinct endpoint rather than a change in a resource field.
   - It is harder to standardize and less consistent with the rest of the API.

3. What should it become?
   - `PATCH /employees/EMP001` with a status change, or a resource-specific transition endpoint if the business requires stronger validation.

4. Why is this better?
   - It makes the state transition part of the resource contract.
   - It is simpler and more coherent architecture-wise.

---

### `/employees/department/IT`

1. What is wrong?
   - This is a custom path hierarchy for a filter.
   - It embeds search criteria into the path instead of using query parameters.

2. Why is it problematic?
   - It makes the API less uniform and less scalable.
   - It mixes filtering concerns into the resource path.
   - It becomes awkward when there are multiple filters.

3. What should it become?
   - `GET /employees?department=IT`

4. Why is this better?
   - Filters belong in the query string.
   - It works for both single and multiple filters.
   - It preserves a clean REST shape.

---

## 3. Resource Naming

I would standardize on:

```text
/employees
```

rather than:

```text
/employee
```

Why?

- The API is dealing with a collection of employee resources.
- Collection naming is more consistent with REST and common API design patterns.
- It allows clean use of patterns such as:
  - `GET /employees`
  - `GET /employees/{employeeId}`
  - `POST /employees`
  - `DELETE /employees/{employeeId}`

The singular form feels like a procedure name or a custom endpoint, not a resource model.

---

## 4. Employee Retrieval

The current design uses:

```http
POST /getEmployee
```

This should be replaced with a proper read operation:

```http
GET /employees/{employeeId}
```

Example:

```http
GET /employees/EMP001
```

Response:

```json
{
  "employeeId": "EMP001",
  "name": "Ashok",
  "department": "IT",
  "status": "ACTIVE"
}
```

This is better because it expresses retrieval as a read of a resource, not an RPC call.

---

## 5. Filtering

The current design:

```http
GET /employees/department/IT
```

should become:

```http
GET /employees?department=IT
```

This is better because:
- filtering is a query concern, not a path concern
- it is easy to combine filters
- it remains consistent with collection semantics

Example:

```http
GET /employees?department=IT&status=ACTIVE
```

This is a clear and scalable pattern.

---

## 6. Approval / Rejection

The business design is not wrong to say that approval/rejection is a meaningful state transition; that is actually the correct architectural question. The problem is not the business concept itself. The problem is the API shape that exposes it as a custom action endpoint.

A better model is to treat approval/rejection as a state change on the employee resource itself, because those are lifecycle transitions.

### Recommended model
Use a partial update on the resource:

```http
PATCH /employees/EMP001
```

Request body:

```json
{
  "status": "APPROVED"
}
```

and for rejection:

```json
{
  "status": "REJECTED"
}
```

### Why this is better
- It keeps the contract centered on the employee resource.
- It clearly represents a state transition.
- It supports lifecycle operations without custom action URIs.
- It is consistent with the distinction we saw in the leave-request exercise: a partial update or explicit state-change contract should match the business operation, not mimic a custom procedure.

If the business needs stronger validation around approval or rejection (for example, permission checks, duplicate approval rules, or audit trails), an explicit business-action endpoint could still be considered. But the default and cleaner model is a resource-state update.

---

## 7. HTTP Method Design

The team says:

> "POST is easier."

This is a poor API design principle because it chooses convenience over semantics.

HTTP methods have meaning:

- `GET` -> retrieve a resource or collection
- `POST` -> create a new resource or submit a command
- `PUT` -> full replacement of a resource
- `PATCH` -> partial update
- `DELETE` -> remove a resource

When a team uses `POST` for everything, the API loses clarity. Clients can no longer infer the contract from the method. The result is:

- inconsistent semantics
- poor discoverability
- weaker tooling
- harder maintenance
- harder testing and troubleshooting

A good API does not choose methods based solely on client ease; it chooses them based on the resource model and business behavior.

---

## 8. Corrected API

Here is the corrected, clean API design:

```text
GET    /employees
GET    /employees/{employeeId}
POST   /employees
PUT    /employees/{employeeId}
PATCH  /employees/{employeeId}
DELETE /employees/{employeeId}
GET    /employees?department=IT
GET    /employees?status=ACTIVE
GET    /employees?department=IT&status=ACTIVE
```

This design is consistent, simple, and resource-oriented. It preserves the employee as a first-class resource and moves filtering to the collection query string.

---

## 9. Architectural Principles

1. Use nouns for resources, not action names.
2. Use HTTP methods for their intended purpose, not for client convenience.
3. Keep collection and item resources distinct.
4. Keep filtering in query parameters.
5. Treat lifecycle state changes as resource-state transitions, not arbitrary custom endpoints, unless business rules require a more explicit command model.
6. Keep API contracts consistent so clients can reason about them without special-case knowledge.

This is a much stronger enterprise API contract than the original design and represents the type of architectural review a working API team should perform before implementation.

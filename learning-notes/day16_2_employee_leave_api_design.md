# DAY 16 — EXERCISE 2
# Employee Leave Management API

## 1. Resource Model

Employee
--------
employeeId : string
name       : string
department : string

Leave Request
-------------
leaveRequestId : string
employeeId     : string
leaveType      : string
fromDate       : string (ISO date)
toDate         : string (ISO date)
reason         : string
status         : string

Example leave request:

```json
{
  "leaveRequestId": "LR001",
  "employeeId": "EMP001",
  "leaveType": "ANNUAL",
  "fromDate": "2026-10-15",
  "toDate": "2026-10-17",
  "reason": "Personal work",
  "status": "PENDING"
}
```

The system has two resources:

- Employee: the person who works in the company
- Leave Request: a business record created by an employee and later approved or rejected

Leave Request is not just a simple embedded field inside Employee. It is a separate resource because it has its own identity (`leaveRequestId`), lifecycle (`PENDING`, `APPROVED`, `REJECTED`, `CANCELLED`), and operational history. It is associated with an Employee, but it is not just a property of the Employee record.

---

## 2. Employee → Leave Request Relationship

A leave request belongs to an employee, but it should still be modeled as a distinct resource. This is because:

- a leave request has its own business identity
- it has a lifecycle and status transitions
- it can be fetched, approved, rejected, or cancelled independently
- multiple leave requests can exist for one employee

The relationship is therefore:

- One Employee has many Leave Requests
- One Leave Request belongs to one Employee

This suggests a clear nested collection model for employee-scoped queries, but a top-level resource model for standalone leave request operations.

---

## 3. Employee Leave Collection

### Primary design
`GET /employees/EMP001/leave-requests`

Purpose: return every leave request for employee `EMP001`.

This is the primary design because it matches the domain relationship naturally:

- the resource is scoped to one employee
- the URL expresses ownership clearly
- the collection name is meaningful
- it is easy to reason about as “the leave requests belonging to this employee”

Example response:

```json
[
  {
    "leaveRequestId": "LR001",
    "employeeId": "EMP001",
    "leaveType": "ANNUAL",
    "fromDate": "2026-10-15",
    "toDate": "2026-10-17",
    "reason": "Personal work",
    "status": "PENDING"
  }
]
```

Alternative design:

```http
GET /leave-requests?employeeId=EMP001
```

This is valid and useful for cross-employee search or reporting. However, the nested collection is more natural when the main use case is “show me all leave requests for this employee.”

---

## 4. Individual Leave Request

### Primary design
`GET /leave-requests/LR001`

This is the better design for a single leave request because the leave request has its own identity and lifecycle. It can be treated as a first-class resource.

The employee relationship is already carried in the payload:

```json
{
  "leaveRequestId": "LR001",
  "employeeId": "EMP001",
  "leaveType": "ANNUAL",
  "fromDate": "2026-10-15",
  "toDate": "2026-10-17",
  "reason": "Personal work",
  "status": "PENDING"
}
```

Alternative nested design:

```http
GET /employees/EMP001/leave-requests/LR001
```

This is also valid if the API strongly emphasizes the employee hierarchy. However, once the resource has a global identity and business meaning outside the employee context, the top-level resource endpoint is cleaner and more scalable.

---

## 5. Create Leave Request

### Endpoint
`POST /employees/EMP001/leave-requests`

### Purpose
Submit a new leave request for employee `EMP001`.

### Request body
```json
{
  "leaveType": "ANNUAL",
  "fromDate": "2026-10-15",
  "toDate": "2026-10-17",
  "reason": "Personal work"
}
```

### Success status
`201 Created`

### Example response
```json
{
  "leaveRequestId": "LR001",
  "employeeId": "EMP001",
  "leaveType": "ANNUAL",
  "fromDate": "2026-10-15",
  "toDate": "2026-10-17",
  "reason": "Personal work",
  "status": "PENDING"
}
```

Why this is the right endpoint:
- the request is created in the employee’s leave collection
- the employee is already known from the URI
- the server assigns the leave request ID and status

---

## 6. Approve / Reject Design

This is the most important decision in the exercise.

### Chosen model
Use a status update on the leave request resource:

```http
PUT /leave-requests/LR001
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

### Why this is better than action endpoints
I would not use:

```http
POST /leave-requests/LR001/approve
POST /leave-requests/LR001/reject
```

because these action-style endpoints create a custom command model that is harder to keep consistent. Approving or rejecting a leave request is fundamentally a state change on a resource, not a brand-new resource or a special action object.

The resource already exists, and the business outcome is simply: `status` changes from `PENDING` to `APPROVED` or `REJECTED`.

This design keeps the contract consistent:
- fetch resource: `GET /leave-requests/LR001`
- update resource: `PUT /leave-requests/LR001`
- change status: update the `status` field

> Contract note: `PUT` is being used within this exercise to model the state update, but a status-only request body is not a full resource replacement. In a production API, a partial-update mechanism or explicit business action/command model should be evaluated.

This is a clean and standard approach for a workflow resource.

---

## 7. Filtering Design

### Pending leave requests
`GET /leave-requests?status=PENDING`

This is a good and common design for requesting a filtered collection of leave requests. It is sufficient when the requirement is simply:

- “show all pending requests”

The API can also support additional filters by adding query parameters:

```http
GET /leave-requests?status=PENDING&employeeId=EMP001
GET /leave-requests?status=PENDING&leaveType=ANNUAL
GET /leave-requests?employeeId=EMP001&status=PENDING
```

When more filters are needed, such as date range, the API can extend naturally with parameters like:

```http
GET /leave-requests?status=PENDING&fromDate=2026-10-01&toDate=2026-10-31
```

This keeps filtering flexible without inventing special path structures or custom endpoints.

---

## 8. Cancel / Delete Design

### Decision
Cancellation is not the same as deleting the resource.

I would model this as:

```http
PUT /leave-requests/LR001
```

with:

```json
{
  "status": "CANCELLED"
}
```

### Why not delete?
Deleting a leave request removes the historical record. In many business processes, a leave request is important to retain for audit and reporting. A cancellation is a lifecycle state change, not a complete removal.

This is more accurate for operational reality:
- the request existed
- it was submitted
- it was later cancelled
- it remains traceable

So the design treats cancellation as a status transition, not as destruction of the record.

> Contract note: `PUT` is being used within this exercise to model the state update, but a status-only request body is not a full resource replacement. In a production API, a partial-update mechanism or explicit business action/command model should be evaluated.

There may still be a separate hard-delete endpoint in a future administrative API, but for normal business operations, a cancellation state is the correct model.

---

## 9. Error Handling

Use one consistent error envelope for all invalid or missing resources.

Example:

```json
{
  "error": {
    "code": "LEAVE_REQUEST_NOT_FOUND",
    "message": "Leave request LR999 does not exist",
    "details": {
      "leaveRequestId": "LR999"
    }
  }
}
```

This should be used for:
- unknown leave request ID
- employee not found for a scoped request
- invalid date range
- invalid leave type or status transition

Typical HTTP status codes:
- `404 Not Found` when the resource is missing
- `400 Bad Request` for invalid payload or invalid dates
- `409 Conflict` for invalid business state transition, such as approving an already rejected leave request

---

## 10. Design Decisions

1. Leave Request is a separate resource associated with an Employee, not merely an embedded field.
2. The employee-scoped collection endpoint is the natural place for “list all leave requests for this employee.”
3. The individual leave request should have its own top-level identity as `/leave-requests/{leaveRequestId}`.
4. Creation is best modeled in the employee’s leave collection: `POST /employees/{employeeId}/leave-requests`.
5. Approval/rejection is modeled as a state update on the leave request, not a special action endpoint.
6. Filtering belongs in query parameters, with common filters such as `status`, `employeeId`, and `leaveType`.
7. Cancellation is represented as a status change, not physical deletion, because records often need to remain auditable.
8. The API keeps a simple and consistent contract without mixing in security, pagination, or versioning concerns.

This design balances business realism, clean URI structure, and consistent REST semantics, while keeping the API understandable for clients and maintainers.

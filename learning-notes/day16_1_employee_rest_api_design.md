# DAY 16 EXERCISE 1
# Employee REST API Design

## 1. Resource Model

Employee
---------
employeeId : string
name       : string
email      : string
department : string
role       : string
status     : string

Example:

```json
{
  "employeeId": "EMP001",
  "name": "Ashok",
  "email": "ashok@example.com",
  "department": "IT",
  "role": "Pega Developer",
  "status": "ACTIVE"
}
```

The employee resource is a first-class domain object. It is represented as a single record with a stable business identifier, `employeeId`, which is used in the URI for individual access.

`employeeId` ownership:
The client supplies `employeeId` during `POST`, and it must be unique.

For `PUT`, `employeeId` is identified by the URI and is not included in the request body.

---

## 2. API Endpoint Design

| Operation | Method | Endpoint | Purpose |
|---|---|---|---|
| Get all employees | GET | `/employees` | Return the collection of all employees |
| Get one employee | GET | `/employees/{employeeId}` | Return one employee by ID |
| Create employee | POST | `/employees` | Create a new employee |
| Update employee | PUT | `/employees/{employeeId}` | Replace employee data completely |
| Delete employee | DELETE | `/employees/{employeeId}` | Remove an employee |
| Filter by department | GET | `/employees?department=IT` | Return employees in a specific department |
| Filter by status | GET | `/employees?status=ACTIVE` | Return employees with a given status |
| Filter by both | GET | `/employees?department=IT&status=ACTIVE` | Return employees matching both filters |

This design keeps the collection and item resource separate and reflects the standard REST pattern:

- `/employees` = collection of employees
- `/employees/{employeeId}` = one employee in that collection

---

## 3. Collection vs Individual Resource

### `/employees`
This is the employee collection resource. It is used for operations that affect many employees.

Examples:
- `GET /employees` -> list employees
- `POST /employees` -> create a new employee

### `/employees/{employeeId}`
This is the individual employee resource. It identifies one employee in the collection.

Examples:
- `GET /employees/EMP001` -> fetch one employee
- `PUT /employees/EMP001` -> replace/update one employee
- `DELETE /employees/EMP001` -> remove one employee

Why this split is better:
- The collection endpoint is the place for listing and creating
- The item endpoint is the place for specific resource identity and single-record operations
- It is clear, predictable, and consistent with common REST conventions

---

## 4. Filtering Design

### Department filter
`GET /employees?department=IT`

### Status filter
`GET /employees?status=ACTIVE`

### Combined filter
`GET /employees?department=IT&status=ACTIVE`

This is a reasonable design because both are independent query filters on the same collection. The API should treat them as a logical AND condition: return employees where department = IT AND status = ACTIVE.

This makes the endpoint flexible without introducing a custom path structure like `/employees/department/IT` or `/employees/status/ACTIVE`, which is less consistent and harder to scale.

For example:

```http
GET /employees?department=IT&status=ACTIVE
```

returns only employees that match both values.

If no filters are supplied, the endpoint returns the full employee list.

---

## 5. Create Employee

### Endpoint
`POST /employees`

### Request body
```json
{
  "employeeId": "EMP002",
  "name": "Priya",
  "email": "priya@example.com",
  "department": "HR",
  "role": "HR Manager",
  "status": "ACTIVE"
}
```

### Expected success status
`201 Created`

### Example success response
```json
{
  "employeeId": "EMP002",
  "name": "Priya",
  "email": "priya@example.com",
  "department": "HR",
  "role": "HR Manager",
  "status": "ACTIVE"
}
```

The API should return the created resource, and the response should include a `201 Created` status to indicate the resource was successfully created.

---

## 6. Update Employee

### Endpoint
`PUT /employees/EMP001`

### Purpose
Update the employee record for `EMP001`.

### Example request body
```json
{
  "name": "Ashok",
  "email": "ashok@example.com",
  "department": "IT",
  "role": "Senior Pega Developer",
  "status": "ACTIVE"
}
```

This updates the role from:

```text
Pega Developer
```

to:

```text
Senior Pega Developer
```

### Expected success status
`200 OK`

### Example success response
```json
{
  "employeeId": "EMP001",
  "name": "Ashok",
  "email": "ashok@example.com",
  "department": "IT",
  "role": "Senior Pega Developer",
  "status": "ACTIVE"
}
```

`PUT` is appropriate here because we are updating the full resource representation for a known employee identity.

---

## 7. Delete Employee

### Endpoint
`DELETE /employees/EMP001`

### Expected success behavior
- Return `204 No Content` when the delete succeeds
- The server should not return a body for a successful delete

Example:

```http
DELETE /employees/EMP001
```

Response:

```http
HTTP/1.1 204 No Content
```

This keeps the delete operation simple and avoids returning a deleted object that is no longer valid.

---

## 8. Error Response

Use one consistent error structure for all not-found or validation problems.

Example error for missing employee:

```json
{
  "error": {
    "code": "EMPLOYEE_NOT_FOUND",
    "message": "Employee EMP999 does not exist",
    "details": {
      "employeeId": "EMP999"
    }
  }
}
```

### Suggested fields
- `code`: machine-readable error code
- `message`: clear human-readable description
- `details`: optional structured details such as the missing ID or invalid field

### Typical status codes
- `404 Not Found` for unknown employee
- `400 Bad Request` for invalid input
- `409 Conflict` for duplicate employeeId or state conflict
- `500 Internal Server Error` for unexpected failures

---

## 9. Design Decisions

1. Use resource-based URIs: `/employees` and `/employees/{employeeId}`
2. Use standard HTTP methods: `GET`, `POST`, `PUT`, `DELETE`
3. Keep filtering in the query string, not in the path, because department and status are attributes of the collection, not separate resources
4. Use `PUT` to replace the full employee resource for a known ID, which makes the update contract predictable and explicit
5. Use one consistent error envelope so clients can build a single error-handling pattern
6. Keep the design simple and focused: no authentication, versioning, pagination, or extra infrastructure concerns yet

This gives a clean, scalable contract for an employee management service while staying easy for clients to understand and use.

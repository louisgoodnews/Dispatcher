# 🎟️ `DispatcherEvent` Class Documentation

The `DispatcherEvent` class defines the structure of an event that can be dispatched using the `Dispatcher` system. Events are immutable and carry structured metadata that is used to identify and process them during dispatch.

## 🧱 Class Definition

```python
class DispatcherEvent:
    id: int
    uuid: str
    name: str
    code: str
    data: dict[str, Any]
```

## 🧠 Attributes

| Attribute | Type         | Description                                                  |
|-----------|--------------|--------------------------------------------------------------|
| `id`      | `int`        | A unique numeric identifier for the event.                   |
| `uuid`    | `str`        | A universally unique identifier string.                      |
| `name`    | `str`        | A human-readable name for the event.                         |
| `code`    | `str`        | An optional machine-readable code associated with the event. |
| `data`    | `dict`       | A dictionary carrying arbitrary payload data for the event.  |

---

## 🛡️ Immutability

This class is declared as `frozen=True`, meaning:

- Once an instance is created, its fields cannot be modified.
- This ensures event integrity across multiple dispatches and handlers.

---

## 🏗️ Creation

While you can instantiate a `DispatcherEvent` manually, it is **strongly recommended** to use the `DispatcherEventBuilder` or `DispatcherEventFactory` to ensure proper initialization of `id`, `uuid`, and field formatting.

```python
event = DispatcherEventBuilder()\
    .with_name("UserLoggedIn")\
    .with_data(user_id=42)\
    .build()
```

---

## 📌 Notes

- `DispatcherEvent` objects are used as input for the `Dispatcher.dispatch()` method.
- Events are deeply introspectable and include unique identifiers for traceability.
- Designed for consistent and testable usage in distributed or modular systems.

---

## 🧑‍💻 Author

**Louis Goodnews**  
2025-08-03 · Düsseldorf

---

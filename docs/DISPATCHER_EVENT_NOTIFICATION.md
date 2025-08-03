# 📢 `DispatcherEventNotification` Class Documentation

The `DispatcherEventNotification` class encapsulates the outcome of dispatching a `DispatcherEvent`. It provides access to the results returned by event handlers, timestamps for tracking, and flags for success or failure.

## 🧱 Class Definition

```python
@dataclass(frozen=True)
class DispatcherEventNotification:
    id: int
    uuid: str
    event: DispatcherEvent
    success: bool
    errors: list[str]
    results: list[Any]
    dispatched_at: float
    finished_at: float
```

---

## 🧠 Attributes

| Attribute       | Type              | Description                                                  |
|-----------------|-------------------|--------------------------------------------------------------|
| `id`            | `int`             | Unique identifier for the notification.                      |
| `uuid`          | `str`             | Universally unique identifier.                               |
| `event`         | `DispatcherEvent` | The dispatched event that triggered this notification.       |
| `success`       | `bool`            | Indicates if all handlers executed without error.            |
| `errors`        | `list[str]`       | List of error messages from failed handlers.                 |
| `results`       | `list[Any]`       | Results returned from event handlers.                        |
| `dispatched_at` | `float`           | Timestamp when the event was dispatched.                     |
| `finished_at`   | `float`           | Timestamp when all handlers completed execution.             |

---

## 🧪 Methods

### `get_one_and_only_result() → Any`

Returns the first result if only one handler returned a value.  
Raises an error if:

- No results were returned.
- More than one result exists.

#### Raises:

- `ValueError` if the result list is empty or contains more than one element.

---

### `__repr__() → str`

Returns a formatted string representation of the notification, including status, timestamps, and event metadata.

---

## 🧩 Usage Example

```python
notification = dispatcher.dispatch(event, "greet")

if notification.success:
    print("Result:", notification.get_one_and_only_result())
else:
    print("Errors:", notification.errors)
```

---

## 📌 Notes

- This class is immutable (`frozen=True`) for consistency and integrity.
- Used as the return type for `Dispatcher.dispatch()`.
- Helpful for debugging, logging, and monitoring event handling outcomes.

---

## 🧑‍💻 Author

**Louis Goodnews**  
2025-08-03 · Düsseldorf

---

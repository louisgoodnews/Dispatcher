# 📎 `DispatcherEventSubscription` Class Documentation

The `DispatcherEventSubscription` class manages subscriptions to a specific event namespace. It stores and manages a list of handler functions that can be triggered when an event is dispatched under the associated namespace.

## 🧱 Class Definition

```python
class DispatcherEventSubscription:
    def __init__(self, namespace: str, persistent: bool = False):
        ...
    def subscribe(self, function: Callable) -> None:
        ...
    def unsubscribe(self, function: Callable) -> None:
        ...
    def get_subscribers(self) -> list[Callable]:
        ...
    def __repr__(self) -> str:
        ...
```

---

## 🧠 Attributes

| Attribute     | Type      | Description                                                  |
|---------------|-----------|--------------------------------------------------------------|
| `namespace`   | `str`     | The name of the event namespace associated with the subscription. |
| `persistent`  | `bool`    | Whether the subscription should persist beyond a single session. |
| `_subscribers`| `list`    | Internal list of callable handler functions.                |

---

## 🛠️ Methods

### `__init__(namespace: str, persistent: bool = False)`

Initializes the subscription object.

#### Parameters:

- `namespace` (`str`): The event namespace.
- `persistent` (`bool`, optional): Whether the subscription is persistent. Defaults to `False`.

---

### `subscribe(function: Callable) → None`

Adds a callable to the list of subscribed functions.

#### Parameters:

- `function` (`Callable`): The function to be subscribed.

#### Raises:

- `TypeError` if the function is not callable.

---

### `unsubscribe(function: Callable) → None`

Removes a function from the subscription list.

#### Parameters:

- `function` (`Callable`): The function to be unsubscribed.

---

### `get_subscribers() → list[Callable]`

Returns the list of currently subscribed functions.

---

### `__repr__() → str`

Returns a human-readable string representation of the subscription object.

---

## 📌 Notes

- Subscriptions are grouped by namespaces, allowing multiple event categories.
- This class is used internally by the `Dispatcher` to manage per-namespace handlers.
- Use in conjunction with `Dispatcher` for best results.

---

## 🧑‍💻 Author

**Louis Goodnews**  
2025-08-03 · Düsseldorf

---

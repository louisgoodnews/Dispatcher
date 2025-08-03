# 📬 `Dispatcher` Class Documentation

The `Dispatcher` is the central class for managing event dispatching and handler subscriptions. It provides mechanisms for defining custom namespaces, subscribing handler functions, and dispatching `DispatcherEvent` objects to receive `DispatcherEventNotification` responses.

## 🧱 Class Definition

```python
class Dispatcher:
    def __init__(self):
        ...
    def dispatch(self, event: DispatcherEvent, namespace: str) -> DispatcherEventNotification:
        ...
    def subscribe(self, namespace: str, function: Callable) -> None:
        ...
    def unsubscribe(self, namespace: str, function: Callable) -> None:
        ...
    def get_subscribers(self, namespace: str) -> list[Callable]:
        ...
```

## 🎯 Responsibilities

- Manage **event handlers** (subscriptions) per `namespace`.
- Dispatch events to the **appropriate handlers** and collect their results.
- Provide a **notification object** with success status, results, and metadata.
- Enforce **validation** of input types for events and handler functions.

---

## 🧠 Internal Structure

- `_subscribers`:  
  A `defaultdict(list)` mapping namespaces to lists of handler functions.

---

## 🧪 Methods

### `__init__()`

Initializes an empty dispatcher with no registered subscribers.

---

### `dispatch(event: DispatcherEvent, namespace: str) → DispatcherEventNotification`

Dispatches an event to all handlers subscribed to the given namespace.

#### Parameters:

- `event` (`DispatcherEvent`): The event to dispatch.
- `namespace` (`str`): The namespace whose handlers should be triggered.

#### Returns:

- `DispatcherEventNotification`: Contains results from handlers, timestamps, and error information.

#### Raises:

- `TypeError` if `event` is not a `DispatcherEvent`.

---

### `subscribe(namespace: str, function: Callable) → None`

Registers a function as an event handler for the given namespace.

#### Parameters:

- `namespace` (`str`): The namespace to subscribe to.
- `function` (`Callable`): The function to execute when an event is dispatched.

#### Raises:

- `TypeError` if `function` is not callable.

---

### `unsubscribe(namespace: str, function: Callable) → None`

Removes a previously subscribed function from the given namespace.

#### Parameters:

- `namespace` (`str`): The namespace to unsubscribe from.
- `function` (`Callable`): The handler function to remove.

---

### `get_subscribers_for_namespace(namespace: str) → list[Callable]`

Retrieves all subscriber functions for a specific namespace.

#### Parameters:

- `namespace` (`str`): The namespace to query.

#### Returns:

- `list[Callable]`: A list of handler functions registered under the namespace.

---

## 💡 Example

```python
dispatcher = Dispatcher()

def my_handler(event):
    return f"Received {event.name}"

dispatcher.subscribe("test", my_handler)

event = DispatcherEventBuilder().with_name("Ping").build()
notification = dispatcher.dispatch(event, "test")

print(notification.get_one_and_only_result())  # Output: Received Ping
```

---

## 📌 Notes

- Each namespace can have multiple subscribers.
- Subscriptions are not persistent across sessions unless externally saved.
- `DispatcherEventNotification` includes detailed metadata (timestamps, error handling, etc.).

---

## 🧑‍💻 Author

**Louis Goodnews**  
2025-08-03 · Düsseldorf

---

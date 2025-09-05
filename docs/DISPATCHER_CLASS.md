# Dispatcher Class

The `Dispatcher` class is the central component of the event dispatching system. It manages event subscriptions, dispatches events to subscribers, and handles the entire event lifecycle.

## Table of Contents

- [Class Overview](#class-overview)
- [Key Features](#key-features)
- [Initialization](#initialization)
- [Core Methods](#core-methods)
- [Subscription Management](#subscription-management)
- [Event Dispatching](#event-dispatching)
- [Best Practices](#best-practices)
- [Examples](#examples)

## Class Overview

```python
class Dispatcher:
    def __init__(self) -> None:
        self._subscriptions: dict[str, list[DispatcherEventSubscription]] = {}
```

## Key Features

- **Event Subscription**: Subscribe functions to specific events
- **Namespace Support**: Organize events into logical groups
- **Priority Handling**: Control the order of event handler execution
- **Bulk Operations**: Subscribe/unsubscribe multiple functions at once
- **Persistent Subscriptions**: Create subscriptions that persist across application restarts
- **Thread Safety**: Safe to use in multi-threaded environments

## Initialization

```python
# Create a new Dispatcher instance
dispatcher = Dispatcher()
```

## Core Methods

### subscribe

Subscribes a function to an event.

```python
def subscribe(
    self,
    event: Union[DispatcherEvent, str],
    function: Callable[..., Any],
    namespace: str = "global",
    persistent: bool = False,
    priority: int = 0,
) -> str:
    ...
```

### unsubscribe

Unsubscribes a function from an event.

```python
def unsubscribe(
    self,
    event: Union[DispatcherEvent, str],
    function: Callable[..., Any],
    namespace: str = "global",
) -> None:
    ...
```

### dispatch

Dispatches an event to all subscribed functions.
Please note: The event is dispatched to all subscribed functions in the specified namespace.
Thus subscriptions will have to accept the event as a parameter. The event's data can be acessed in the subscription function using the event's data attribute.

```python
def dispatch(
    self,
    event: DispatcherEvent,
    namespace: str = "global",
    *args: Iterable[Any],
    **kwargs: dict[str, Any],
) -> DispatcherEventNotification:
    ...
```

### bulk_subscribe

Subscribes multiple functions to multiple events.

```python
def bulk_subscribe(
    self,
    events: Iterable[Union[DispatcherEvent, str]],
    functions: Union[Callable[..., Any], Iterable[Callable[..., Any]]],
    namespaces: str = "global",
    persistents: bool = False,
    priorities: int = 0,
) -> list[str]:
    ...
```

## Subscription Management

### Finding Subscriptions

- `get_subscriptions_by_event(event)`: Get all subscriptions for an event
- `get_subscriptions_by_function(function)`: Get all subscriptions for a function
- `get_subscriptions_by_namespace(namespace)`: Get all subscriptions in a namespace
- `get_subscription_by_code(code)`: Get a subscription by its unique code

### Unsubscribing

- `unsubscribe_by_code(code)`: Unsubscribe using a subscription code
- `unsubscribe_by_function(function)`: Unsubscribe all subscriptions for a function
- `unsubscribe_by_namespace(namespace)`: Unsubscribe all subscriptions in a namespace
- `unsubscribe_all()`: Remove all subscriptions

## Event Dispatching

When an event is dispatched, the Dispatcher:

1. Creates a notification with the event details
2. Finds all matching subscriptions
3. Sorts them by priority (highest first)
4. Executes each subscriber function
5. Collects results and errors
6. Returns a notification with the outcome

## Best Practices

1. **Use Meaningful Event Names**: Choose clear, descriptive names for events
2. **Organize with Namespaces**: Use namespaces to group related events
3. **Set Appropriate Priorities**: Use priorities to control execution order
4. **Handle Errors**: Always include error handling in your event handlers
5. **Clean Up**: Unsubscribe from events when they're no longer needed
6. **Use Bulk Operations**: For multiple subscriptions, use bulk methods for better performance
7. **Consider Thread Safety**: The Dispatcher is thread-safe, but your handlers should be too

## Examples

### Basic Usage

```python
# Create a dispatcher
dispatcher = Dispatcher()

# Define an event handler
def handle_user_created(event: DispatcherEvent, user_data):
    print(f"User created: {user_data}")

# Subscribe to an event
subscription_code = dispatcher.subscribe(
    event="user_created",
    function=handle_user_created,
    namespace="user_management"
)

# Dispatch an event
notification = dispatcher.dispatch(
    event=DispatcherEvent(
        code="user_created",
        id=123,
        name="UserCreated",
        data={"user_id": 456}
    ),
    namespace="user_management"
)

# Unsubscribe when done
dispatcher.unsubscribe_by_code(subscription_code)
```

### Bulk Subscriptions

```python
# Define multiple handlers
def log_event(event: DispatcherEvent, user_data):
    print(f"Event received: {user_data}")

def process_event(event: DispatcherEvent, user_data):
    # Process the event
    return {"status": "processed", "data": user_data}

# Subscribe multiple functions to multiple events
subscription_codes = dispatcher.bulk_subscribe(
    events=["user_created", "order_processed"],
    functions=[log_event, process_event],
    namespaces=["user_management", "order_processing"],
    priorities=[0, 10]  # process_event will run before log_event
)
```

### Error Handling

```python
try:
    notification = dispatcher.dispatch(
        event=DispatcherEvent(
            code="critical_operation",
            id=789,
            name="CriticalOperation",
            data={"param": "value"}
        )
    )
    
    if notification.has_errors():
        print(f"Errors occurred: {notification.errors}")
    else:
        print(f"Operation successful: {notification.get_one_and_only_result()}")
        
except Exception as e:
    print(f"Failed to dispatch event: {e}")
```

## Author

**Louis Goodnews**  
2025-09-05 · Düsseldorf

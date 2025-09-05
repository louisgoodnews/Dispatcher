# Dispatcher Event Subscription System

This document provides comprehensive documentation for the subscription-related classes in the Dispatcher system: `DispatcherEventSubscription`, `DispatcherEventSubscriptionFactory`, and `DispatcherEventSubscriptionBuilder`.

## Table of Contents

- [DispatcherEventSubscription](#dispatchereventsubscription)
- [DispatcherEventSubscriptionFactory](#dispatchereventsubscriptionfactory)
- [DispatcherEventSubscriptionBuilder](#dispatchereventsubscriptionbuilder)
- [Usage Examples](#usage-examples)

## DispatcherEventSubscription

The `DispatcherEventSubscription` class represents a subscription to an event in the Dispatcher system. It encapsulates the details of a subscription, including the event, function, namespace, and other metadata.

### Class Definition

```python
class DispatcherEventSubscription:
    def __init__(
        self,
        code: str,
        event: DispatcherEvent,
        function: Callable[..., Any],
        namespace: str,
        persistent: bool,
        priority: int,
    ) -> None:
        ...
```

### Properties

- `code` (str): A unique code identifying the subscription
- `event` (DispatcherEvent): The event being subscribed to
- `function` (Callable): The function to be called when the event is dispatched
- `namespace` (str): The namespace of the subscription
- `persistent` (bool): Whether the subscription persists across restarts
- `priority` (int): The priority of the subscription (higher numbers are called first)

### Key Methods

- `__call__`: Calls the subscribed function with the provided arguments
- `__eq__`: Compares subscriptions for equality
- `__hash__`: Returns a hash of the subscription
- `__repr__` and `__str__`: String representations of the subscription

## DispatcherEventSubscriptionFactory

The `DispatcherEventSubscriptionFactory` class is responsible for creating `DispatcherEventSubscription` instances with unique codes.

### Class Definition

```python
class DispatcherEventSubscriptionFactory:
    _base_id: int = 10000
    
    @classmethod
    def create_dispatcher_subscription(
        cls,
        event: DispatcherEvent,
        function: Callable[..., Any],
        namespace: str,
        persistent: bool = False,
        priority: int = 0,
    ) -> DispatcherEventSubscription:
        ...
```

### Key Methods

- `create_dispatcher_subscription()`: Creates a new `DispatcherEventSubscription` with the specified parameters

## DispatcherEventSubscriptionBuilder

The `DispatcherEventSubscriptionBuilder` class provides a fluent interface for constructing `DispatcherEventSubscription` instances.

### Class Definition

```python
class DispatcherEventSubscriptionBuilder:
    def __init__(self) -> None:
        self._configuration: dict[str, Any] = {}
    
    def with_event(self, value: DispatcherEvent) -> Self:
        ...
        
    def with_function(self, value: Callable[..., Any]) -> Self:
        ...
        
    def with_namespace(self, value: str) -> Self:
        ...
        
    def with_persistent(self, value: bool) -> Self:
        ...
        
    def with_priority(self, value: int) -> Self:
        ...
        
    def build(self) -> DispatcherEventSubscription:
        ...
```

### Key Methods

- `with_event(value)`: Sets the event to subscribe to
- `with_function(value)`: Sets the function to be called
- `with_namespace(value)`: Sets the namespace for the subscription
- `with_persistent(value)`: Sets whether the subscription is persistent
- `with_priority(value)`: Sets the priority of the subscription
- `build()`: Constructs and returns a new `DispatcherEventSubscription` instance

## Usage Examples

### Creating a Subscription with DispatcherEventSubscriptionFactory

```python
from dispatcher.core import DispatcherEvent, DispatcherEventSubscriptionFactory

def handle_user_created(user_data):
    print(f"User created: {user_data}")

# Create an event
event = DispatcherEvent(
    code="user_created",
    id=123,
    name="UserCreated",
    data={"user_id": 456}
)

# Create a subscription
subscription = DispatcherEventSubscriptionFactory.create_dispatcher_subscription(
    event=event,
    function=handle_user_created,
    namespace="user_management",
    persistent=True,
    priority=10
)
```

### Creating a Subscription with DispatcherEventSubscriptionBuilder

```python
from dispatcher.core import DispatcherEvent, DispatcherEventSubscriptionBuilder

def handle_order_processed(order_data):
    print(f"Order processed: {order_data}")

# Using the builder pattern
subscription = (DispatcherEventSubscriptionBuilder()
    .with_event(DispatcherEvent(
        code="order_processed",
        id=789,
        name="OrderProcessed",
        data={"order_id": 101112}
    ))
    .with_function(handle_order_processed)
    .with_namespace("order_processing")
    .with_persistent(True)
    .with_priority(5)
    .build()
)
```

### Working with Subscriptions

```python
# Call the subscription directly
subscription({"user_id": 123, "username": "johndoe"})

# Access subscription properties
print(f"Subscription code: {subscription.code}")
print(f"Event name: {subscription.event.name}")
print(f"Namespace: {subscription.namespace}")
print(f"Priority: {subscription.priority}")
print(f"Persistent: {subscription.persistent}")
```

## Best Practices

1. **Use Builders for Complex Subscriptions**: When creating subscriptions with multiple parameters, use `DispatcherEventSubscriptionBuilder` for better readability.

2. **Choose Appropriate Namespaces**: Use meaningful namespaces to organize and manage subscriptions effectively.

3. **Set Priorities Carefully**: Higher priority subscriptions are called first. Use priorities to control the order of execution.

4. **Consider Persistence**: Mark subscriptions as persistent if they should survive application restarts.

5. **Handle Errors Gracefully**: Always include error handling in your subscription callbacks.

6. **Clean Up Unused Subscriptions**: Unsubscribe from events when they're no longer needed to prevent memory leaks.

## Author

**Louis Goodnews**  
2025-09-05 · Düsseldorf

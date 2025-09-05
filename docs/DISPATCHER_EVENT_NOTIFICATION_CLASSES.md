# Dispatcher Event Notification System

This document provides comprehensive documentation for the notification-related classes in the Dispatcher system: `DispatcherEventNotification`, `DispatcherEventNotificationFactory`, and `DispatcherEventNotificationBuilder`.

## Table of Contents

- [DispatcherEventNotification](#dispatchereventnotification)
- [DispatcherEventNotificationStatus](#dispatchereventnotificationstatus)
- [DispatcherEventNotificationFactory](#dispatchereventnotificationfactory)
- [DispatcherEventNotificationBuilder](#dispatchereventnotificationbuilder)
- [Usage Examples](#usage-examples)

## DispatcherEventNotification

The `DispatcherEventNotification` class represents a notification in the Dispatcher system. It encapsulates the details of a notification, including its content, duration, associated event, and status.

### Class Definition

```python
class DispatcherEventNotification:
    def __init__(
        self,
        content: dict[str, Any],
        end: datetime,
        errors: Iterable[dict[str, Any]],
        event: DispatcherEvent,
        id: int,
        namespace: str,
        start: datetime,
        status: DispatcherEventNotificationStatus,
    ) -> None:
        ...
```

### Properties

- `content` (dict[str, Any]): The content of the notification
- `duration` (float): The duration of the notification in seconds
- `end` (datetime): The end time of the notification
- `errors` (Iterable[dict[str, Any]]): A list of errors associated with the notification
- `event` (DispatcherEvent): The associated event for this notification
- `id` (int): A unique identifier for the notification
- `namespace` (str): The namespace associated with the notification
- `start` (datetime): The start time of the notification
- `status` (DispatcherEventNotificationStatus): The status of the notification

### Key Methods

- `get_function_names()`: Returns the function names from the notification's content
- `get_function_results()`: Returns the function results from the notification's content
- `get_one_and_only_result()`: Returns the single result if there's only one in the content
- `handle()`: Handles the notification
- `has_errors()`: Checks if the notification has any errors
- `__contains__`: Checks if a key exists in the notification's content
- `__getitem__`: Gets a value from the notification's content
- `__repr__` and `__str__`: String representations of the notification

## DispatcherEventNotificationStatus

An enumeration that represents the possible statuses of a notification.

### Values

- `SUCCESS`: Indicates that the notification was successful
- `FAILURE`: Indicates that the notification failed

## DispatcherEventNotificationFactory

The `DispatcherEventNotificationFactory` class is responsible for creating `DispatcherEventNotification` instances with unique IDs.

### Class Definition

```python
class DispatcherEventNotificationFactory:
    _base_id: int = 10000
    
    @classmethod
    def create_dispatcher_notification(
        cls,
        end: datetime,
        event: DispatcherEvent,
        namespace: str,
        start: datetime,
        status: DispatcherEventNotificationStatus,
        content: Optional[dict[str, Any]] = None,
        errors: Optional[Iterable[dict[str, Any]]] = None,
    ) -> DispatcherEventNotification:
        ...
```

### Key Methods

- `create_dispatcher_notification()`: Creates a new `DispatcherEventNotification` with the specified parameters

## DispatcherEventNotificationBuilder

The `DispatcherEventNotificationBuilder` class provides a fluent interface for constructing `DispatcherEventNotification` instances.

### Class Definition

```python
class DispatcherEventNotificationBuilder:
    def __init__(self) -> None:
        self._configuration: dict[str, Any] = {}
    
    def with_content(self, **kwargs: Any) -> Self:
        ...
        
    def with_end(self, value: datetime) -> Self:
        ...
        
    def with_errors(self, *args: Iterable[dict[str, Any]]) -> Self:
        ...
        
    def with_event(self, value: DispatcherEvent) -> Self:
        ...
        
    def with_namespace(self, value: str) -> Self:
        ...
        
    def with_start(self, value: datetime) -> Self:
        ...
        
    def with_status(self, value: DispatcherEventNotificationStatus) -> Self:
        ...
        
    def build(self) -> DispatcherEventNotification:
        ...
```

### Key Methods

- `with_content(**kwargs)`: Adds content to the notification
- `with_end(value)`: Sets the end time of the notification
- `with_errors(*args)`: Adds errors to the notification
- `with_event(value)`: Sets the associated event
- `with_namespace(value)`: Sets the namespace
- `with_start(value)`: Sets the start time
- `with_status(value)`: Sets the status
- `build()`: Constructs and returns a new `DispatcherEventNotification` instance

## Usage Examples

### Creating a Notification with DispatcherEventNotificationFactory

```python
from datetime import datetime
from dispatcher.core import DispatcherEvent, DispatcherEventNotificationStatus, DispatcherEventNotificationFactory

# Create an event
event = DispatcherEvent(
    code="user_created",
    id=123,
    name="UserCreated",
    data={"user_id": 456}
)

# Create a notification
start_time = datetime.now()
end_time = datetime.now()

notification = DispatcherEventNotificationFactory.create_dispatcher_notification(
    content={"message": "User created successfully"},
    end=end_time,
    event=event,
    namespace="user_management",
    start=start_time,
    status=DispatcherEventNotificationStatus.SUCCESS
)
```

### Creating a Notification with DispatcherEventNotificationBuilder

```python
from datetime import datetime
from dispatcher.core import DispatcherEvent, DispatcherEventNotificationStatus, DispatcherEventNotificationBuilder

# Create an event
event = DispatcherEvent(
    code="order_processed",
    id=789,
    name="OrderProcessed",
    data={"order_id": 101112, "status": "completed"}
)

# Using the builder pattern
notification = (DispatcherEventNotificationBuilder()
    .with_content(message="Order processed successfully", order_id=101112)
    .with_event(event)
    .with_namespace("order_processing")
    .with_start(datetime.now())
    .with_end(datetime.now())
    .with_status(DispatcherEventNotificationStatus.SUCCESS)
    .build()
)
```

### Working with Notifications

```python
# Check if notification has errors
if notification.has_errors():
    print(f"Notification failed with {len(notification.errors)} errors")
    for error in notification.errors:
        print(f"Error: {error}")

# Access notification data
print(f"Notification ID: {notification.id}")
print(f"Event: {notification.event.name}")
print(f"Duration: {notification.duration:.2f} seconds")

# Get notification results
if not notification.has_errors():
    result = notification.get_one_and_only_result()
    print(f"Result: {result}")
```

## Best Practices

1. **Use Builders for Complex Notifications**: When creating notifications with multiple fields, use `DispatcherEventNotificationBuilder` for better readability.

2. **Handle Errors Gracefully**: Always check `has_errors()` before processing notification results.

3. **Use Meaningful Namespaces**: Choose clear, descriptive namespaces to categorize notifications.

4. **Include Relevant Context**: Add sufficient context in the notification content to make it useful for consumers.

5. **Monitor Notification Duration**: Track and log notification durations to identify performance issues.

6. **Use Appropriate Status**: Always set the correct status to indicate success or failure.

## Author

**Louis Goodnews**  
2025-09-05 · Düsseldorf

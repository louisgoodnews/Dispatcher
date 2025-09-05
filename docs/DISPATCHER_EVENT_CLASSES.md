# Dispatcher Event System

This document provides comprehensive documentation for the core event-related classes in the Dispatcher system: `DispatcherEvent`, `DispatcherEventFactory`, and `DispatcherEventBuilder`.

## Table of Contents

- [DispatcherEvent](#dispatcherevent)
- [DispatcherEventFactory](#dispatchereventfactory)
- [DispatcherEventBuilder](#dispatchereventbuilder)
- [Usage Examples](#usage-examples)

## DispatcherEvent

The `DispatcherEvent` class represents an event in the Dispatcher system. It encapsulates the details of an event, including its code, ID, name, and optional data.

### Class Definition

```python
class DispatcherEvent:
    def __init__(
        self,
        code: str,
        id: int,
        name: str,
        data: Optional[dict[str, Any]] = None,
    ) -> None:
        ...
```

### Properties

- `code` (str): A unique code for the event
- `data` (dict[str, Any]): Optional dictionary containing additional data
- `id` (int): A unique identifier for the event
- `last_notified` (Optional[datetime]): The last time the event was notified
- `name` (str): The name of the event

### Key Methods

- `clear()`: Clears the data dictionary
- `compare_to(other)`: Compares this event with another for equality
- `is_empty()`: Checks if the event has no data
- `__contains__(key)`: Checks if a key exists in the event's data
- `__getitem__(key)`: Gets a value from the event's data
- `__setitem__(key, value)`: Sets a value in the event's data
- `__eq__`: Compares events for equality
- `__repr__` and `__str__`: String representations of the event

## DispatcherEventFactory

The `DispatcherEventFactory` class is responsible for creating `DispatcherEvent` instances with unique IDs and codes.

### Class Definition

```python
class DispatcherEventFactory:
    _base_id: int = 10000
    
    @classmethod
    def create_dispatcher_event(
        cls,
        name: str,
        data: Optional[dict[str, Any]] = None,
    ) -> DispatcherEvent:
        ...
```

### Key Methods

- `create_dispatcher_event(name, data=None)`: Creates a new `DispatcherEvent` with a unique ID and code

## DispatcherEventBuilder

The `DispatcherEventBuilder` class provides a fluent interface for constructing `DispatcherEvent` instances with a more readable syntax.

### Class Definition

```python
class DispatcherEventBuilder:
    def __init__(self) -> None:
        self._configuration: dict[str, Any] = {}
    
    def with_data(self, **kwargs: Any) -> Self:
        ...
        
    def with_name(self, value: str) -> Self:
        ...
        
    def build(self) -> DispatcherEvent:
        ...
```

### Key Methods

- `with_data(**kwargs)`: Adds data to the event
- `with_name(value)`: Sets the name of the event
- `build()`: Constructs and returns a new `DispatcherEvent` instance

## Usage Examples

### Creating an Event with DispatcherEventFactory

```python
# Create a simple event
event = DispatcherEventFactory.create_dispatcher_event(
    name="UserLoggedIn",
    data={"user_id": 123, "timestamp": datetime.now()}
)
```

### Creating an Event with DispatcherEventBuilder

```python
# Using the builder pattern
event = (DispatcherEventBuilder()
    .with_name("OrderPlaced")
    .with_data(
        order_id=456,
        items=["item1", "item2"],
        total=99.99
    )
    .build()
)
```

### Working with Event Data

```python
# Check if data exists
if "user_id" in event:
    print(f"User ID: {event['user_id']}")

# Access data using dictionary syntax
for key, value in event.data.items():
    print(f"{key}: {value}")

# Clear event data
event.clear()
```

## Best Practices

1. **Use Builders for Complex Events**: When creating events with multiple data fields, use `DispatcherEventBuilder` for better readability.

2. **Keep Event Data Light**: Only include essential data in the event to minimize memory usage and serialization overhead.

3. **Use Meaningful Event Names**: Choose clear, descriptive names for events that indicate their purpose.

4. **Handle Event Data Safely**: Always check if a key exists before accessing it to avoid KeyError exceptions.

5. **Consider Immutability**: While the event data can be modified, it's generally better to treat events as immutable once created.

## Author

**Louis Goodnews**  
2025-09-05 · Düsseldorf

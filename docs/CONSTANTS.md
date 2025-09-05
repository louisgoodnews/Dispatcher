# Constants Module

This module defines the core constants used throughout the Dispatcher system, primarily for namespace management.

## Table of Contents

- [Overview](#overview)
- [Available Constants](#available-constants)
- [Usage Examples](#usage-examples)
- [Best Practices](#best-practices)

## Overview

The `constants` module provides essential string literals that are used to identify and manage namespaces within the Dispatcher system. These constants ensure consistency and prevent typos when working with event namespaces.

## Available Constants

### `GLOBAL`

- **Type**: `Final[Literal["global"]]`
- **Value**: `"global"`
- **Purpose**: Identifies the global namespace for events that should be accessible across all processes.
- **Usage**: 
  ```python
  from dispatcher.utils.constants import GLOBAL
  
  # Subscribe to a global event
  dispatcher.subscribe("user_created", handle_user, namespace=GLOBAL)
  ```

### `LOCAL`

- **Type**: `Final[Literal["local"]]`
- **Value**: `"local"`
- **Purpose**: Identifies the local namespace for events that should only be accessible within the current process.
- **Usage**:
  ```python
  from dispatcher.utils.constants import LOCAL
  
  # Subscribe to a local event
  dispatcher.subscribe("process_complete", handle_completion, namespace=LOCAL)
  ```

## Usage Examples

### Basic Namespace Usage

```python
from dispatcher import Dispatcher
from dispatcher.utils.constants import GLOBAL, LOCAL

# Create a dispatcher instance
dispatcher = Dispatcher()

# Function to handle global events
def handle_global_event(data):
    print(f"Global event received: {data}")

# Function to handle local events
def handle_local_event(data):
    print(f"Local event received: {data}")

# Subscribe to events with different namespaces
dispatcher.subscribe("system_event", handle_global_event, namespace=GLOBAL)
dispatcher.subscribe("internal_event", handle_local_event, namespace=LOCAL)

# Dispatch events
dispatcher.dispatch("system_event", GLOBAL, {"message": "System is starting"})
dispatcher.dispatch("internal_event", LOCAL, {"status": "Processing complete"})
```

### Checking Namespace in Event Handlers

```python
from dispatcher import Dispatcher, DispatcherEvent
from dispatcher.utils.constants import GLOBAL, LOCAL

dispatcher = Dispatcher()

def event_handler(event: DispatcherEvent, namespace: str):
    if namespace == GLOBAL:
        print(f"Handling global event: {event.name}")
    elif namespace == LOCAL:
        print(f"Handling local event: {event.name}")
    else:
        print(f"Handling custom namespace event: {namespace}.{event.name}")

# Subscribe the handler to multiple namespaces
for namespace in [GLOBAL, LOCAL, "custom_namespace"]:
    dispatcher.subscribe("user_action", event_handler, namespace=namespace)
```

## Best Practices

1. **Always Use Constants**:
   Always import and use these constants instead of hardcoding string literals to prevent typos and ensure consistency.

   ```python
   # Good
   from dispatcher.utils.constants import GLOBAL
   dispatcher.subscribe("event", handler, namespace=GLOBAL)
   
   # Avoid
   dispatcher.subscribe("event", handler, namespace="global")  # Typo-prone
   ```

2. **Namespace Selection**:
   - Use `GLOBAL` for events that need to be accessible across different parts of your application or between processes.
   - Use `LOCAL` for events that should only be handled within the current process or module.

3. **Custom Namespaces**:
   While you can use custom namespace strings, it's recommended to define them as constants in your application for consistency.

4. **Type Checking**:
   The constants are typed using `Final` and `Literal` to enable static type checking. This helps catch potential issues at development time.

## Author

**Louis Goodnews**  
2025-09-05 · Düsseldorf

# Utils Module

This module provides utility functions that simplify common operations with the Dispatcher system. These functions offer convenient wrappers around the core Dispatcher functionality.

## Table of Contents

- [Overview](#overview)
- [Functions](#functions)
  - [subscribe_to_events](#subscribe_to_events)
  - [unsubscribe_from_events](#unsubscribe_from_events)
- [Usage Examples](#usage-examples)
- [Best Practices](#best-practices)

## Overview

The `utils` module contains helper functions that make it easier to work with the Dispatcher system, particularly for common operations like subscribing to and unsubscribing from multiple events at once.

## Functions

### `subscribe_to_events`

Subscribes to multiple events with a single function call.

```python
def subscribe_to_events(subscriptions: list[dict[str, Any]]) -> list[str]:
    """
    Subscribes to multiple events.

    Args:
        subscriptions: A list of subscription dictionaries, where each dictionary
                     should contain:
                     - 'event': The event to subscribe to (str or DispatcherEvent)
                     - 'function': The callback function
                     - 'namespace': (Optional) The event namespace (default: GLOBAL)
                     - 'persistent': (Optional) Whether the subscription persists (default: False)
                     - 'priority': (Optional) The subscription priority (default: 0)

    Returns:
        A list of subscription IDs for the created subscriptions.

    Raises:
        Exception: If there's an error during subscription.
    """
```

### `unsubscribe_from_events`

Unsubscribes from multiple events with a single function call.

```python
def unsubscribe_from_events(function_ids: list[str]) -> None:
    """
    Unsubscribes from multiple events.

    Args:
        function_ids: A list of subscription IDs to unsubscribe from.

    Raises:
        Exception: If there's an error during unsubscription.
    """
```

## Usage Examples

### Subscribing to Multiple Events

```python
from dispatcher.utils import subscribe_to_events
from dispatcher.utils.constants import GLOBAL

def handle_user_created(event: DispatcherEvent, data):
    print(f"User created: {data}")

def handle_order_processed(event: DispatcherEvent, data):
    print(f"Order processed: {data}")

# Define subscriptions
subscriptions = [
    {
        'event': 'user_created',
        'function': handle_user_created,
        'namespace': GLOBAL,
        'persistent': True,
        'priority': 10
    },
    {
        'event': 'order_processed',
        'function': handle_order_processed,
        'namespace': 'orders',
        'priority': 5
    }
]

# Subscribe to all events at once
subscription_ids = subscribe_to_events(subscriptions)
```

### Unsubscribing from Multiple Events

```python
from dispatcher.utils import unsubscribe_from_events

# Later, when you want to unsubscribe
unsubscribe_from_events(subscription_ids)
```

### Error Handling

```python
try:
    subscription_ids = subscribe_to_events(subscriptions)
    # ... your code ...
    
except Exception as e:
    print(f"Failed to subscribe to events: {e}")
    # Handle the error appropriately
    
finally:
    # Always clean up when done
    if 'subscription_ids' in locals():
        try:
            unsubscribe_from_events(subscription_ids)
        except Exception as e:
            print(f"Warning: Failed to clean up subscriptions: {e}")
```

## Best Practices

1. **Use Context Managers**:
   Consider creating a context manager for managing subscriptions to ensure proper cleanup.

   ```python
   from contextlib import contextmanager
   
   @contextmanager
   def managed_subscriptions(subscriptions):
       """Context manager for managing subscriptions."""
       try:
           ids = subscribe_to_events(subscriptions)
           yield ids
       finally:
           if 'ids' in locals():
               unsubscribe_from_events(ids)
   
   # Usage
   with managed_subscriptions(subscriptions) as sub_ids:
       # Your code here
       pass  # Subscriptions are automatically cleaned up
   ```

2. **Batch Operations**:
   Group related subscriptions together to make management easier.

   ```python
   def setup_notification_subscriptions():
       """Set up all notification-related subscriptions."""
       return subscribe_to_events([
           {'event': 'email_sent', 'function': log_email_sent},
           {'event': 'sms_sent', 'function': log_sms_sent},
           {'event': 'push_sent', 'function': log_push_sent},
       ])
   ```

3. **Error Handling**:
   Always implement proper error handling when working with subscriptions.

4. **Documentation**:
   Document the purpose of each subscription and any special handling requirements.

5. **Testing**:
   Test subscription and unsubscription logic to ensure resources are properly managed.

## Author

**Louis Goodnews**  
2025-09-05 · Düsseldorf

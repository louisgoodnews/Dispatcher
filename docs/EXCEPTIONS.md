# Exceptions

This module defines the custom exception hierarchy used throughout the Dispatcher system. These exceptions provide detailed error information and help with debugging and error handling.

## Table of Contents

- [Exception Hierarchy](#exception-hierarchy)
- [Exception Reference](#exception-reference)
- [Usage Examples](#usage-examples)
- [Best Practices](#best-practices)

## Exception Hierarchy

```
Exception
└── DispatcherError
    ├── DispatcherDispatchingError
    │   └── DispatcherDispatchingFormatError
    ├── DispatcherSubscriptionError
    ├── DispatcherSubscriptionLookupError
    └── DispatcherUnsubscriptionError
```

## Exception Reference

### `DispatcherError`

**Base Class**: `Exception`

Base exception class for all Dispatcher-related exceptions. This should be caught when you want to handle any exception from the Dispatcher system.

### `DispatcherDispatchingError`

**Base Class**: `DispatcherError`

Raised when there is an error during event dispatching. This is a general exception for dispatching-related issues.

### `DispatcherDispatchingFormatError`

**Base Class**: `DispatcherDispatchingError`

Raised when there is an error in the format of the event being dispatched. This typically indicates invalid or malformed event data.

### `DispatcherSubscriptionError`

**Base Class**: `DispatcherError`

Raised when there is an error during subscription to an event. This is a general exception for subscription-related issues.

### `DispatcherSubscriptionLookupError`

**Base Class**: `DispatcherError`

Raised when a subscription cannot be found during a lookup operation. This typically occurs when trying to unsubscribe from a non-existent subscription.

### `DispatcherUnsubscriptionError`

**Base Class**: `DispatcherError`

Raised when there is an error during unsubscription from an event. This could be due to invalid parameters or other unsubscription failures.

## Usage Examples

### Basic Error Handling

```python
from dispatcher.core.exceptions import (
    DispatcherError,
    DispatcherSubscriptionError,
    DispatcherSubscriptionLookupError
)

try:
    # Attempt to subscribe or dispatch
    subscription_code = dispatcher.subscribe("some_event", some_handler)
    
    # Later, try to unsubscribe
    dispatcher.unsubscribe_by_code(subscription_code)
    
except DispatcherSubscriptionLookupError as e:
    print(f"Subscription not found: {e}")
    
except DispatcherSubscriptionError as e:
    print(f"Subscription error: {e}")
    
except DispatcherError as e:
    print(f"Dispatcher error: {e}")
    
except Exception as e:
    print(f"Unexpected error: {e}")
```

### Custom Exception Handling

```python
from dispatcher.core.exceptions import DispatcherDispatchingError

class CustomDispatchingError(DispatcherDispatchingError):
    """Custom exception for application-specific dispatching errors."""
    pass

# Usage
try:
    result = dispatcher.dispatch("critical_event", data=critical_data)
    if not result:
        raise CustomDispatchingError("Failed to process critical event")
        
except CustomDispatchingError as e:
    # Handle custom dispatching error
    logger.error(f"Critical event processing failed: {e}")
    
except DispatcherDispatchingError as e:
    # Handle other dispatching errors
    logger.warning(f"Dispatching error: {e}")
```

## Best Practices

1. **Catch Specific Exceptions**:
   Always catch the most specific exception possible before more general ones.

   ```python
   try:
       # Dispatcher operation
   except DispatcherSubscriptionLookupError:
       # Handle specific case
   except DispatcherError:
       # Handle general Dispatcher errors
   ```

2. **Log Exceptions with Context**:
   Include relevant context when logging exceptions to aid in debugging.

   ```python
   try:
       dispatcher.dispatch("process_data", data=data)
   except DispatcherDispatchingError as e:
       logger.error(f"Failed to dispatch process_data with data: {data}", exc_info=True)
       raise
   ```

3. **Create Custom Exceptions**:
   For application-specific error handling, create custom exceptions that inherit from the base Dispatcher exceptions.

   ```python
   class PaymentProcessingError(DispatcherDispatchingError):
       """Raised when there's an error in payment processing."""
       pass
   ```

4. **Preserve Stack Traces**:
   When re-raising exceptions, use `raise` without arguments to preserve the original traceback.

   ```python
   try:
       dispatcher.dispatch("critical_operation")
   except DispatcherError:
       logger.exception("Critical operation failed")
       raise  # Re-raise with original traceback
   ```

5. **Document Exception Conditions**:
   Clearly document in your code which exceptions each function can raise.

   ```python
   def process_order(order_data):
       """
       Process an order.
       
       Args:
           order_data: The order data to process
           
       Raises:
           DispatcherDispatchingError: If there's an error dispatching the order event
           ValueError: If the order data is invalid
       """
       if not order_data:
           raise ValueError("Order data cannot be empty")
           
       return dispatcher.dispatch("order_processed", data=order_data)
   ```

## Author

**Louis Goodnews**  
2025-09-05 · Düsseldorf

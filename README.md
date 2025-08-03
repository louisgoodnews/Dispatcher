# Dispatcher System 🛰️

A modular and extensible event-dispatching system for Python, built around core principles of immutability, separation of concerns, and observable state transitions. Designed for flexible, type-safe use in medium to large-scale applications.

## 🧠 Overview

The Dispatcher system implements a structured way to emit and react to custom events. It includes:

- `DispatcherEvent`: Represents a unique event with metadata.
- `DispatcherEventNotification`: Tracks the result and metadata of dispatched events.
- `Dispatcher`: Central manager to dispatch events and manage subscriptions.
- `Subscription` and `Builder` classes to facilitate object creation and maintain clean architecture.

## 🔧 Features

- 📦 Event creation via `DispatcherEventFactory` and `DispatcherEventBuilder`
- 🔄 Notification tracking with success/error handling
- 🧪 Subscription management per namespace (with persistence toggle)
- 🧱 Fluent builder interfaces for both events and notifications
- 🔍 Full introspection and traceable lifecycle via detailed string representations
- 🛑 Immutability where appropriate (e.g., notification content)

## 🚀 Usage Example

```python
from dispatcher import Dispatcher, DispatcherEventBuilder

# Create dispatcher
dispatcher = Dispatcher()

# Define a sample handler
def greet_handler(event):
    name = event.data.get("name", "world")
    return f"Hello, {name}!"

# Subscribe handler to namespace
dispatcher.subscribe(namespace="greet", function=greet_handler)

# Build an event
event = DispatcherEventBuilder().with_name("greeting_event").with_data(name="Alice").build()

# Dispatch the event
notification = dispatcher.dispatch(event=event, namespace="greet")

# Check result
print(notification.get_one_and_only_result())  # → Hello, Alice!

📦 Installation

This module is standalone and has no external dependencies beyond the standard library.

To use it in your project, simply include dispatcher.py in your codebase.
🧩 Components
Component	Description
DispatcherEvent	Immutable event structure with name, id, code, and data.
DispatcherEventNotification	Read-only result container with execution metadata and errors.
Dispatcher	Manages all events and subscriptions.
Builder classes	Provide clean, chainable object creation.
Factory classes	Central ID management and construction logic.
Subscription classes	Namespace-based subscription storage and dispatching logic.
🧪 Tests

Tests are currently not included but recommended using pytest or unittest.
👤 Author

Louis Goodnews

If you use this module in your own project or research, feel free to reach out or cite the author!
"""
Author: Louis Goodnews
Date: 2025-08-03
"""

from core.core import (
    Dispatcher,
    DispatcherEventBuilder,
    DispatcherEvent,
    DispatcherEventNotification,
)


def main() -> None:
    """
    Main function to demonstrate the usage of the Dispatcher.
    It creates an event, subscribes to it, dispatches the event, and then unsubscribes from it.
    """

    # Create an event with a comment and a name
    # The event is built using the DispatcherEventBuilder
    # The event contains data that can be processed by subscribers
    # The name of the event is set to "TestEvent"
    # The event can be used to trigger actions in the system
    # The comment is a simple message that can be used for logging or debugging purposes
    event: DispatcherEvent = (
        DispatcherEventBuilder()
        .with_data(**{"comment": "Hello World!"})
        .with_name(value="TestEvent")
        .build()
    )

    # Print the created event to the console
    print(f"Event created: {event}")

    # Create an instance of the Dispatcher
    # The Dispatcher is responsible for managing events and subscriptions
    # It allows you to subscribe to events, dispatch them, and unsubscribe from them
    # The Dispatcher can handle multiple namespaces, allowing for organized event management
    # The Dispatcher can also handle persistent subscriptions, which means that subscribers can receive events even if
    # they are not currently active
    # The Dispatcher can be used to decouple components in a system, allowing for flexible event-driven architecture
    # The Dispatcher can be used to implement publish-subscribe patterns, where publishers send events and subscribers
    # receive them without needing to know about each other
    dispatcher: Dispatcher = Dispatcher()

    # Subscribe to the event with a lambda function that simply returns the event data
    subscription: str = dispatcher.subscribe(
        event=event,
        function=lambda x: x,
        namespace="test",
        persistent=True,
    )

    # Dispatch the event to the subscribers in the "test" namespace
    # The dispatch method will call the subscribed functions with the event data
    # The subscribers can process the event data and perform actions based on it
    # The dispatch method will return the results of the subscribers' processing
    # If there are no subscribers for the event, it will simply return an empty list
    # The dispatch method can also handle multiple events at once, allowing for batch processing of events
    # The dispatch method can be used to trigger actions in the system based on events
    # The dispatch method can also be used to implement event-driven workflows, where events trigger a series of actions
    # The dispatch method can be used to implement reactive programming patterns, where the system reacts to events
    # The dispatch method can be used to implement event sourcing, where the state of the system is derived from a sequence of events
    # The dispatch method can be used to implement CQRS (Command Query Responsibility Segregation) patterns,
    # where commands trigger events
    # and queries retrieve the current state of the system based on those events
    notification: DispatcherEventNotification = dispatcher.dispatch(
        event=event,
        namespace="test",
    )

    # Print the notification received from the dispatch method
    # The notification contains the results of the subscribers' processing of the event
    # The notification can be used to log the results, trigger further actions, or simply inform
    # the system about the outcome of the event processing
    print(f"Notification received: {notification}")

    # Unsubscribe from the event using the subscription code
    # The unsubscribe method will remove the subscription from the Dispatcher
    # This means that the subscriber will no longer receive events for this subscription
    # Unsubscribing is useful when the subscriber is no longer interested in receiving events
    # or when the subscriber is being removed from the system
    dispatcher.unsubscribe(code=subscription)


if __name__ == "__main__":
    main()

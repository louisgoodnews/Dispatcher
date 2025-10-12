"""
Author: Louis Goodnews
Date: 2025-09-05

This module contains utility functions using the dispatcher.
"""

from typing import Any, Final

from dispatcher.core.core import Dispatcher


def subscribe_to_events(
    dispatcher: Dispatcher,
    subscriptions: list[dict[str, Any]],
) -> list[str]:
    """
    Subscribes to events.

    This method subscribes to events and returns a list of function IDs.
    It is a convenience function that allows you to subscribe to multiple events at once.

    Args:
        dispatcher (Dispatcher): The dispatcher to subscribe to.
        subscriptions (list[dict[str, Any]]): The subscriptions to subscribe to.

    Returns:
        list[str]: The function IDs of the subscribed events.

    Raises:
        Exception: If an error occurs while subscribing to an event.
    """

    # Initialize a list to store the results
    result: list[str] = []

    # Iterate over the subscriptions
    for subscription in subscriptions:
        try:
            # Subscribe to the event
            function_id: str = dispatcher.subscribe(
                event=subscription["event"],
                function=subscription["function"],
                namespace=subscription.get("namespace", "global"),
                persistent=subscription.get("persistent", False),
                priority=subscription.get("priority", 0),
            )

            # Add the function ID to the result list
            result.append(function_id)
        except Exception as e:
            # Re-raise the exception to the caller
            raise e

    # Return the result list
    return result


def unsubscribe_from_events(
    dispatcher: Dispatcher,
    function_ids: list[str],
) -> None:
    """
    Unsubscribes from events.

    This method unsubscribes from events.
    It is a convenience function that allows you to unsubscribe from multiple events at once.

    Args:
        dispatcher (Dispatcher): The dispatcher to unsubscribe from.
        function_ids (list[str]): The function IDs to unsubscribe from.

    Returns:
        None

    Raises:
        Exception: If an error occurs while unsubscribing from an event.
    """

    # Iterate over the function IDs
    for function_id in function_ids:
        try:
            # Unsubscribe from the event
            dispatcher.unsubscribe(function_id=function_id)
        except Exception as e:
            # Re-raise the exception to the caller
            raise e

    # Clear the function IDs list
    function_ids.clear()


__all__: Final[list[str]] = [name for name in globals() if not name.startswith("_")]

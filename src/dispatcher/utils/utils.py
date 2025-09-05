"""
Author: Louis Goodnews
Date: 2025-09-05

This module contains utility functions using the dispatcher.
"""

from typing import Final, List

from core.core import DISPATCHER


__all__: Final[List[str]] = [
    "subscribe_to_events",
    "unsubscribe_from_events",
]


def subscribe_to_events(subscriptions: list[dict[str, Any]]) -> list[str]:
    """
    Subscribes to events.

    This method subscribes to events and returns a list of function IDs.
    It is a convenience function that allows you to subscribe to multiple events at once.

    Args:
        subscriptions (list[dict[str, Any]]): The subscriptions to subscribe to.

    Returns:
        list[str]: The function IDs of the subscribed events.
    """

    # Initialize a list to store the results
    result: list[str] = []

    # Iterate over the subscriptions
    for subscription in subscriptions:
        try:
            # Subscribe to the event
            function_id: str = DISPATCHER.subscribe(
                event=subscription["event"],
                function=subscription["function"],
                namespace=subscription.get("namespace", GLOBAL),
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


def unsubscribe_from_events(function_ids: list[str]) -> None:
    """
    Unsubscribes from events.

    This method unsubscribes from events.
    It is a convenience function that allows you to unsubscribe from multiple events at once.

    Args:
        function_ids (list[str]): The function IDs to unsubscribe from.
    """

    # Iterate over the function IDs
    for function_id in function_ids:
        try:
            # Unsubscribe from the event
            DISPATCHER.unsubscribe(function_id=function_id)
        except Exception as e:
            # Re-raise the exception to the caller
            raise e

"""
Author: Louis Goodnews
Date: 2025-08-19
"""

from typing import Final, List, Literal

from .core.core import (
    Dispatcher,
    DispatcherEvent,
    DispatcherEventBuilder,
    DispatcherEventFactory,
    DispatcherEventNotification,
    DispatcherEventNotificationBuilder,
    DispatcherEventNotificationFactory,
    DispatcherEventSubscription,
    DispatcherEventSubscriptionBuilder,
    DispatcherEventSubscriptionFactory,
    DISPATCHER,
)

from .utils.utils import subscribe_to_events, unsubscribe_from_events


__all__: Final[List[str]] = [
    "Dispatcher",
    "DispatcherEvent",
    "DispatcherEventBuilder",
    "DispatcherEventFactory",
    "DispatcherEventNotification",
    "DispatcherEventNotificationBuilder",
    "DispatcherEventNotificationFactory",
    "DispatcherEventSubscription",
    "DispatcherEventSubscriptionBuilder",
    "DispatcherEventSubscriptionFactory",
    "DISPATCHER",
    "subscribe_to_events",
    "unsubscribe_from_events",
]

__version__: Final[Literal["0.1.0"]] = "0.1.0"

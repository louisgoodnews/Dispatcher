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
)


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
]

__version__: Final[Literal["0.1.0"]] = "0.1.0"

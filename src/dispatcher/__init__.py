"""
Author: Louis Goodnews
Date: 2025-09-05
"""

from typing import Final, List, Literal

from .core.core import (
    DISPATCHER,
    Dispatcher,
    DispatcherEvent,
    DispatcherEventBuilder,
    DispatcherEventFactory,
    DispatcherEventNotification,
    DispatcherEventNotificationBuilder,
    DispatcherEventNotificationFactory,
    DispatcherEventNotificationStatus,
    DispatcherEventSubscription,
    DispatcherEventSubscriptionBuilder,
    DispatcherEventSubscriptionFactory,
)

from .utils.constants import GLOBAL, LOCAL

from .utils.utils import subscribe_to_events, unsubscribe_from_events


__all__: Final[List[str]] = [
    "DISPATCHER",
    "Dispatcher",
    "DispatcherEvent",
    "DispatcherEventBuilder",
    "DispatcherEventFactory",
    "DispatcherEventNotification",
    "DispatcherEventNotificationBuilder",
    "DispatcherEventNotificationFactory",
    "DispatcherEventNotificationStatus",
    "DispatcherEventSubscription",
    "DispatcherEventSubscriptionBuilder",
    "DispatcherEventSubscriptionFactory",
    "GLOBAL",
    "LOCAL",
    "subscribe_to_events",
    "unsubscribe_from_events",
]


__version__: Final[Literal["0.1.0"]] = "0.1.0"

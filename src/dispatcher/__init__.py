"""
Author: Louis Goodnews
Date: 2025-09-05
"""

from typing import Final, List, Literal

from .common.constants import GLOBAL, LOCAL

from .core.core import (
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

from .utils.utils import subscribe_to_events, unsubscribe_from_events


__all__: Final[List[str]] = [
    "DISPATCHER",
    "GLOBAL",
    "LOCAL",
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
    "subscribe_to_events",
    "unsubscribe_from_events",
]


__version__: Final[Literal["0.1.0"]] = "0.1.0"

"""
Author: Louis Goodnews
Date: 2025-09-05

This module contains custom exceptions used by the dispatcher.
"""

from typing import Final, List


__all__: Final[List[str]] = [
    "DispatcherError",
    "DispatcherDispatchingError",
    "DispatcherDispatchingFormatError",
    "DispatcherSubscriptionError",
    "DispatcherSubscriptionLookupError",
    "DispatcherUnsubscriptionError",
]


class DispatcherError(Exception):
    """
    Base exception class for Dispatcher errors.
    """


class DispatcherDispatchingError(DispatcherError):
    """
    Exception class for dispatching errors.
    """


class DispatcherDispatchingFormatError(DispatcherDispatchingError):
    """
    Exception class for dispatching format errors.
    """


class DispatcherSubscriptionError(DispatcherError):
    """
    Exception class for subscription errors.
    """


class DispatcherSubscriptionLookupError(DispatcherError):
    """
    Exception class for subscription lookup errors.
    """


class DispatcherUnsubscriptionError(DispatcherError):
    """
    Exception class for unsubscription errors.
    """

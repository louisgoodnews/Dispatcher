"""
Author: Louis Goodnews
Date: 2025-09-05

This module contains custom exceptions used by the dispatcher.
"""

from typing import Final


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


__all__: Final[List[str]] = [name for name in globals() if not name.startswith("_")]

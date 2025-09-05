"""
Author: Louis Goodnews
Date: 2025-09-05

This module contains constants used by the dispatcher.
The constants are used to identify namespaces in which events are dispatched.
"""

from typing import Final, List, Literal


__all__: Final[List[str]] = [
    "GLOBAL",
    "LOCAL",
]


# The global namespace is used to identify events that are accessible across all processes.
GLOBAL: Final[Literal["global"]] = "global"

# The local namespace is used to identify events that are only accessible within the current process.
LOCAL: Final[Literal["local"]] = "local"

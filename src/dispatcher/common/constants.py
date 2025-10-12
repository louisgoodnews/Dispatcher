"""
Author: Louis Goodnews
Date: 2025-10-10
"""

from typing import Final, Literal


# ------ Constants ------

# ----- Namespace Constants -----

# Global namespace.
GLOBAL: Final[Literal["global"]] = "global"

# Local namespace.
LOCAL: Final[Literal["local"]] = "local"


__all__: Final[list[str]] = [name for name in globals() if not name.startswith("_")]

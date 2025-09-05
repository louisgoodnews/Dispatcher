"""
Author: Louis Goodnews
Date: 2025-08-03

Minimal setup.py for backward compatibility with tools that expect it.

This project uses pyproject.toml for configuration. This file exists only for
backward compatibility with tools that don't yet support PEP 517/518.
"""

import setuptools

if __name__ == "__main__":
    setuptools.setup()

"""Mock utilities."""

from unittest.mock import ANY, AsyncMock, MagicMock, Mock, create_autospec, patch


def CoroutineMock(*args, **kwargs):
    """Return an AsyncMock that returns a MagicMock, unless return_value is set."""
    if "return_value" in kwargs:
        return AsyncMock(*args, **kwargs)
    return AsyncMock(*args, **kwargs, return_value=MagicMock())


__all__ = [
    "CoroutineMock",
    "AsyncMock",
    "MagicMock",
    "patch",
    "create_autospec",
    "Mock",
    "ANY",
]

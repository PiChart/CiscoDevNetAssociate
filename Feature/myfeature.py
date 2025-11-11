from __future__ import annotations
from dataclasses import dataclass
from typing import Callable, Optional, ContextManager
import contextlib
import logging
import argparse

"""
Basic feature module.

File: /Users/marshall/Desktop/Code/CiscoDevNetAssociate/Feature/myfeature.py
Provides a simple Feature class to enable/disable behavior and a small CLI demo.
"""


logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


@dataclass
class Feature:
    """Simple feature toggle with context manager support."""
    name: str
    enabled: bool = False

    def enable(self) -> None:
        """Enable the feature."""
        if not self.enabled:
            logger.info("Enabling feature: %s", self.name)
            self.enabled = True

    def disable(self) -> None:
        """Disable the feature."""
        if self.enabled:
            logger.info("Disabling feature: %s", self.name)
            self.enabled = False

    def toggle(self) -> None:
        """Toggle the feature on/off."""
        self.enabled = not self.enabled
        logger.info("Feature %s set to %s", self.name, self.enabled)

    def run(self, action: Callable[[], None], *, when_disabled: Optional[Callable[[], None]] = None) -> None:
        """
        Run `action` only if the feature is enabled.
        If disabled and `when_disabled` is provided, call it instead.
        """
        if self.enabled:
            logger.info("Running action for feature: %s", self.name)
            action()
        elif when_disabled:
            logger.info("Feature %s disabled, running fallback", self.name)
            when_disabled()
        else:
            logger.info("Feature %s disabled, skipping action", self.name)

    def temporary_enabled(self) -> ContextManager["Feature"]:
        """
        Context manager that temporarily enables the feature for the context block.
        Usage:
            with feature.temporary_enabled():
                feature.run(...)
        """
        @contextlib.contextmanager
        def _mgr():
            was_enabled = self.enabled
            try:
                self.enable()
                yield self
            finally:
                if not was_enabled:
                    self.disable()
        return _mgr()


def _demo_action() -> None:
    logger.info("Demo action executed.")


def _fallback_action() -> None:
    logger.info("Fallback action executed.")


def main() -> None:
    parser = argparse.ArgumentParser(description="Demo the Feature toggle.")
    parser.add_argument("--enable", action="store_true", help="Start with the feature enabled.")
    args = parser.parse_args()

    feature = Feature(name="myfeature", enabled=args.enable)
    logger.info("Feature %s initial state: %s", feature.name, feature.enabled)

    feature.run(_demo_action, when_disabled=_fallback_action)

    # Temporarily enable for a block
    with feature.temporary_enabled():
        feature.run(_demo_action)

    logger.info("Feature %s final state: %s", feature.name, feature.enabled)


if __name__ == "__main__":
    main()
print ("Welcoem to DevAsc!")
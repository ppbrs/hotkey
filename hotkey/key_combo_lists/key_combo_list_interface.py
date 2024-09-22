"""Interface that is common to all hotkeys configurations."""

import abc
import logging

from hotkey.key_combo import KeyCombo

_logger = logging.getLogger(__name__)


class KeyComboListInterface(abc.ABC):  # pylint: disable=too-few-public-methods
    """Interface class."""

    WEIGHT_NORMAL = 1
    WEIGHT_ELEVATED = 100  # for learning
    LEGEND_PREFIX = "DEFAULT_PREFIX"

    @abc.abstractmethod
    def _get(self) -> list[KeyCombo]:
        pass

    def get(self) -> list[KeyCombo]:
        """Return all hotkeys in the list. Insert a specific prefix."""
        key_combo_list = self._get()
        for _, key_combo in enumerate(key_combo_list):
            for i, _ in enumerate(key_combo.legend):
                key_combo.legend[i] = self.LEGEND_PREFIX + ": " + key_combo.legend[i]
        return key_combo_list

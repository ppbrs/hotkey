""" Interface that is common to all hotkeys configurations.
"""
# pylint: disable=import-error

# Standard library imports
import abc
# Third party imports
from hotkey.key_combo import Key_combo
from pybp.log import Log
# Local application imports


class KeyComboListInterface(abc.ABC):
    """ Interface class. """

    WEIGHT_NORMAL = 1
    WEIGHT_ELEVATED = 100  # for learning
    LEGEND_PREFIX = "DEFAULT_PREFIX"

    @abc.abstractmethod
    def _get(self, log: Log) -> list[Key_combo]:
        pass

    def get(self, log: Log) -> list[Key_combo]:
        """ Return all hotkeys in the list. Insert a specific prefix. """
        key_combo_list = self._get(log)
        for _, key_combo in enumerate(key_combo_list):
            for i, _ in enumerate(key_combo.legend):
                key_combo.legend[i] = self.LEGEND_PREFIX + ': ' + key_combo.legend[i]
        return key_combo_list

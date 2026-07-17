"""
Base Selector

Every selector inside the Context Framework inherits
from this class.

Responsibilities
----------------
- Provide a common interface.
- Hide implementation details.
- Allow selectors to be replaced independently.

Examples
--------
MemorySelector
WorkspaceSelector
ReviewSelector
DocumentSelector
"""

from abc import ABC, abstractmethod


class BaseSelector(ABC):

    @abstractmethod
    def load(
        self,
        stage: str,
        project: str,
    ):
        """
        Load data required by the current stage.

        Returns
        -------
        Any
            Context data for this selector.
        """
        pass
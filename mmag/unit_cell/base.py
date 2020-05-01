from abc import ABC, abstractmethod
import numpy as np

class AbstractCell(ABC):
    """
    An abstract class to predict in a model
    """

    def __init__(self, position: np.ndarray):
        self.__position = position
        assert self.__position.shape == (3,), "Position must be ndarray of shape (3,)"

    @property
    def position(self):
        return self.__position

    @abstractmethod
    def face_positions(self, *args, **kwargs):
        pass

    @abstractmethod
    def unit_field(self):
        pass

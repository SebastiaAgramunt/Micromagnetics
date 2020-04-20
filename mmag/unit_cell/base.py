from abc import ABC, abstractmethod
import numpy as np

class AbstractCell(ABC):
    """
    An abstract class to predict in a model
    """

    def __init__(self, position: np.float64):
        self.__position = position

    @property
    def position(self):
        return self.__position

    @abstractmethod
    def face_positions(self, *args, **kwargs):
        pass

    @abstractmethod
    def unit_field(self):
        pass

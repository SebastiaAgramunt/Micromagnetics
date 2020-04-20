from .base import AbstractCell
import numpy as np


class Cuboid(AbstractCell):

    def __init__(self, position: np.array, delta: np.array):

        super().__init__(position)
        self.__delta = delta

        # perpendicular vectors to the cuboid faces
        self.__unit_vector_faces = {0: np.asarray([1.0, 0, 0]),
                                    1: np.asarray([-1.0, 0, 0]),
                                    2: np.asarray([0.0, 1.0, 0]),
                                    3: np.asarray([0.0, -1.0, 0]),
                                    4: np.asarray([0.0,  0.0, 1.0]),
                                    5: np.asarray([0.0,  0.0, -1.0])}

        self.__face_positions = {}
        for face in self.__unit_vector_faces.keys():
            self.__face_positions[face] = self.position + self.__unit_vector_faces[face]*self.__delta/2.0

    @property
    def face_positions(self):
        return self.__face_positions

    def unit_field(self):
        pass

    def __str__(self):
        m = f"Cuboid of center [{self.position[0]}, {self.position[1]}, {self.position[2]}]"
        for elem in self.__face_positions:
            m += f"\n\tFace {elem}: {self.__face_positions[elem][0]}, {self.__face_positions[elem][1]}, {self.__face_positions[elem][2]}"
        return m


# class MicromagenticCell(Cuboid):
#     def __init__(self, center, delta, m):
#         Cuboid.__init__(self, center, delta)
#         self.__m = m
#
#         norm = np.linalg.norm(m)
#         if norm > 1.01 or norm < 0.99:
#             raise Exception('Cannot create MicromagneticCell object, norm is not 1: {}'.format(norm))
#
#     def Renormalize(self):
#         norm = np.linalg.norm(self.__m)
#         self.__m = self.__m/norm
#
#     def __str__(self):
#         m = super(MicromagenticCell, self).__str__()
#         m += "\n\t Micromagnetic cell m = [{},{},{}]".format(self.__m[0],
#                                                              self.__m[1],
#                                                              self.__m[2])
#         return m





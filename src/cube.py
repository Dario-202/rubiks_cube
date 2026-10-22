
import random
import numpy as np


class Rubiks_cube:
    colors = ['W', 'Y', 'G', 'B', 'O', 'R']
    faces = ['U', 'D', 'F', 'B', 'L', 'R']
    def __init__(self):
        self.cube = self.create_solved_cube()

    def create_solved_cube(self):
        cube = {
            'U': np.full((3, 3), 'W'),  # White
            'D': np.full((3, 3), 'Y'),  # Yellow
            'F': np.full((3, 3), 'G'),  # Green
            'B': np.full((3, 3), 'B'),  # Blue
            'L': np.full((3, 3), 'O'),  # Orange
            'R': np.full((3, 3), 'R')   # Red
            }
        return cube

    def display_cube(self):
        for face in self.faces:
            print(f"{face} face:")
            print(f"{self.cube[face]}\n")
# -*- coding: utf-8 -*-
from math import sqrt, sin, cos, atan2


# immutable 2d vector representation
class vector2d():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def length(self):
        return sqrt(self.x**2 + self.y**2)

    def to_polar(self):
        angle = atan2(self.y, self.x)
        return (self.length(self), angle)

    def to_tuple(self):
        return (self.x, self.y)

    def add(self, v):
        return vector2d(self.x + v.x, self.y + v.y)

    def subtract(self, v):
        return vector2d(self.x - v.x, self.y - v.y)

    def distance(self, v):
        return self.length(self.subtract(v))

    def scale(self, scalar):
        return vector2d(scalar * self.x, scalar * self.y)

    def rotate(self, angle):
        polar = self.to_polar()
        self.from_polar((polar[0], polar[1] + angle))

    # class method, convenience using
    def translate(t, vectors):
        return [v.add(t) for v in vectors]

    def sum(vectors):
        return vector2d(sum([v.x for v in vectors]), sum([v.y for v in vectors]))

    def perimeter(vectors):
        distances = [vector2d.distance(vectors[i], vectors[(i + 1) % len(vectors)]) for i in range(0, len(vectors))]
        return sum(distances)

    def from_polar(polar_vector):
        length, angle = polar_vector[0], polar_vector[1]
        return vector2d(length * cos(angle), length * sin(angle))

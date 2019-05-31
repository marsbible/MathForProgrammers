#!/usr/bin/env python
# -*- coding: utf-8 -*-
from vector.draw2d import Polygon, Points, draw
from vector.vector2d import vector2d
from random import uniform

dino_vectors = [(6, 4), (3, 1), (1, 2), (-1, 5), (-2, 5), (-3, 4), (-4, 4), (-5, 3), (-5, 2), (-2, 2), (-5, 1), (-4, 0),
                (-2, 1), (-1, 0), (0, -3), (-1, -4), (1, -4), (2, -3), (1, -2), (3, -1), (5, 1)]


def hundred_dinos():
    translations = [vector2d(12 * x, 10 * y) for x in range(-5, 5) for y in range(-5, 5)]
    ndv = [vector2d(*t) for t in dino_vectors]
    dinos = [Polygon(*vector2d.translate(t, ndv), color='blue') for t in translations]
    draw(*dinos, grid=None, axes=None, origin=None)


def big_dinos(offset):
    ndv = [vector2d(*x).add(offset) for x in dino_vectors]
    draw(Points(*ndv), Polygon(*ndv, color='red'))


def square_curve():
    draw(
        Points(*[vector2d(x, x**2) for x in range(-10, 11)]),
        grid=(1, 10),
        nice_aspect_ratio=False  # don't require x scale to match y scale
    )


# Suppose u = (-1,1) and v = (1,1) and suppose r and s are real numbers.
# Specifically, let’s assume -1 < r < 1 and -3 < s < 3.
# Where are the possible points on the plane where the vector r ∙ u + s ∙ v could end up?
def linear_two(u, v, r_range, s_range):
    r = lambda: uniform(*r_range)
    s = lambda: uniform(*s_range)
    possibilities = [vector2d.sum([u.scale(r()), v.scale(s())]) for i in range(0, 500)]
    draw(Points(*possibilities))


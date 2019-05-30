#!/usr/bin/env python
# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
from vector.draw2d import *
from mpl_toolkits.mplot3d import Axes3D
import math

dino_vectors = [(6, 4), (3, 1), (1, 2), (-1, 5), (-2, 5), (-3, 4), (-4, 4), (-5, 3), (-5, 2), (-2, 2), (-5, 1), (-4, 0),
                (-2, 1), (-1, 0), (0, -3), (-1, -4), (1, -4), (2, -3), (1, -2), (3, -1), (5, 1)]

# draw by segments
# segs = [Segment(dino_vectors[i], dino_vectors[(i+1)%len(dino_vectors)], color='blue') for i in range(0, len(dino_vectors))]
# draw(*segs)

# draw by points
# draw(Points(*dino_vectors), Polygon(*dino_vectors))

draw(
     Points(*[(x,x**2) for x in range(-10,11)]),
     grid=(1,10),
     nice_aspect_ratio=False # don't require x scale to match y scale
 )
# draw(Points(*dino_vectors))
# draw(Arrow((2, -2), (0, 0), color='blue'))
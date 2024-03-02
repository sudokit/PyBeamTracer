from typing import TypeAlias
import glm

class Point(glm.vec3): pass

class Color(glm.vec3):
  def __init__(self, r: float, g: float, b: float):
    super().__init__(255.99 * r, 255.99 * g, 255.99 * b)
from .types import Point
import glm

class Ray:
  def __init__(self, origin: Point, direction: glm.vec3) -> None:
    self.orig = origin
    self.dir = direction
  
  def at(self, t: float) -> glm.vec3:
    return self.orig + t * self.dir
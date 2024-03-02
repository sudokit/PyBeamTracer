import glm
from .types import Color, Point
import numpy as np
from .ray import Ray
from .settings import CAMERA_CENTER, FOCAL_LENGTH, VIEWPORT_HEIGHT, VIEWPORT_WIDTH, WIDTH, HEIGHT

def hit_sphere(center: Point, radius: float, r: Ray) -> bool:
  oc = r.orig - center
  a = glm.dot(r.dir, r.dir)
  half_b = glm.dot(oc ,r.dir)
  c = glm.length(oc)**2 - radius**2
  discrim = half_b**2 - a * c
  return -1.0 if discrim < 0 else (-half_b - np.sqrt(discrim)) / a

def ray_color(r: Ray) -> Color:
  t = hit_sphere(Point(0, 0, -1), 0.5, r)
  if (t > 0.0):
    N = glm.normalize(r.at(t) - glm.vec3(0, 0, -1))
    return 0.5 * Color(N.x+1, N.y+1, N.z+1)

  unit_dir = glm.normalize(r.dir)
  a = 0.5 * (unit_dir.y + 1.0)
  return (1.0-a)*Color(1.0, 1.0, 1.0) + a*Color(0.5, 0.7, 1.0)

def process_pixels(pixels: np.ndarray) -> list[tuple[tuple[int, int], Color]]: # so a list of (x, y) and (r, g, b)
  viewport_u = glm.vec3(VIEWPORT_WIDTH, 0, 0)
  viewport_v = glm.vec3(0, -VIEWPORT_HEIGHT, 0)
  
  pixel_delta_u = viewport_u / WIDTH
  pixel_delta_v = viewport_v / HEIGHT
  
  viewport_upper_left = CAMERA_CENTER - glm.vec3(0, 0, FOCAL_LENGTH) - viewport_u/2 - viewport_v/2
  pixel00_loc = viewport_upper_left + 0.5 * (pixel_delta_u + pixel_delta_v)

  res: list[tuple[tuple[int, int], Color]] = []
  for pos in pixels:
    x, y = (int(pos[0]), int(pos[1]))
    pixel_center = pixel00_loc + (x * pixel_delta_u) + (y * pixel_delta_v)
    ray_dir = pixel_center - CAMERA_CENTER
    ray = Ray(CAMERA_CENTER, ray_dir)
    color = ray_color(ray)
    res.append(((x, y), color))
  return res
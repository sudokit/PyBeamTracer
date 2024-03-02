import numpy as np
from matplotlib import pyplot as plt
from tracer.settings import *
from tracer.utils import displayImg, imgParts, splitImg
from tqdm import tqdm
import glm
from tracer.trace import process_pixels
import time

#TODO: figure out how to split the image for n amount of threads

def main():

  # blah blah
  pool = mp.Pool(processes=NUM_THREADS)  
  
  split_img = splitImg(WIDTH, HEIGHT, NUM_THREADS)
  
  start = time.time()
  
  array = np.zeros((WIDTH, HEIGHT, 3))
  
  fig, ax = plt.subplots()
  img = ax.imshow(array, interpolation='nearest', extent=(0, WIDTH, HEIGHT, 0))
  plt.ion()
  
  # actual calculations
  
  res = pool.map_async(process_pixels, split_img) 
  
  for e in tqdm(res.get()):
    for pos, color in tqdm(e):
      array[pos[0], pos[1]] = color.to_list()
    # img.set_data(array.astype(np.uint8))
    img.set_data(np.transpose(array.astype(np.uint8), (1, 0, 2)))
    fig.canvas.draw_idle()
    plt.pause(0.01)
  plt.ioff()
  plt.show()
  print(f"took: {time.time() - start}")
  # print(array.astype(np.uint8).shape)
if __name__ == '__main__':
  main()
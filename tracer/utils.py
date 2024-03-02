import numpy as np
from matplotlib import pyplot as plt

def displayImg(array: np.ndarray) -> None:
  # img =  ImageTk.PhotoImage(image=Image.fromarray(array))

  print(array.shape)
  plt.imshow(array.astype(np.uint8), interpolation='nearest')
  plt.show()
  

def splitImg(width: int, height: int, n_threads: int) -> list[np.ndarray]:
  parts = imgParts(width, height, n_threads)
  pixels: list[np.ndarray] = []
  y_offset = 0
  for i, part in enumerate(parts):
    # each part we want to give it its own array of pixel coords
    # it will house part * width arrays of [x, y]
    curr = np.zeros((part*width, 2))
    j = 0
    for y in range(y_offset, y_offset+part):
      for x in range(width):
        # np.append(curr, [x, y])
        curr[j] = [x, y]
        j += 1
    # each pass we append it to the pixels array
    pixels.append(curr)
    y_offset += part
  return pixels

# splits into n_threads amount of strips
def imgParts(width: int, height: int, n_threads: int) -> list[float]:
  """
  so i return how many rows (height basically) each thread should have. return an array like [25, 25, 27]
  """
  # NOTE: idfk what im doiiing
  rows, remainder = divmod(height, n_threads)
  res = [rows + 1 if i < remainder else rows for i in range(n_threads)]
  return res
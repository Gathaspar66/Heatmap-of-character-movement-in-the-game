import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib import image as mpimg
from skimage import io
import seaborn as sns

img = io.imread('mapa.png')
x_dim, y_dim, z_dim = np.shape(img)
heatmap = np.zeros((y_dim, x_dim), dtype=float)
skala=10.12

for y in range(1,19):
    data = pd.read_csv("wynik"+str(y)+".txt")

    for i in range(0,len(data)):
        a = int((data.x[i] * skala) + 930)
        b = int((data.z[i] * skala * -1) + 1340)
        heatmap[a][-b]+=10

heatmap=np.rot90(heatmap)
plt.figure(figsize=(15, 15))
h = sns.heatmap(heatmap, vmin=0, vmax=30,cmap='rocket')
my_image = mpimg.imread("mapa.png")
h.imshow(my_image,aspect=h.get_aspect(),extent= h.get_xlim() + h.get_ylim(),zorder=1,alpha=0.1)
plt.show()


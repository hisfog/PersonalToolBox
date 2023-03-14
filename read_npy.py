from PIL import Image
import numpy as np
import os
from matplotlib import pyplot as plt
import glob

data = np.load('./1Weights_and_npzs/res50_192x640_weights_19/disps_eigen_split.npy', allow_pickle=True)
save_dir = './1Weights_and_npzs/res50_192x640_weights_19/depth_maps_raw/'
print(data.shape)
if not os.path.exists(save_dir):
    os.makedirs(save_dir)
print("converting npy to images ...")
for i in range(len(data)):
    # plt.imshow(data[i])
    plt.imsave(save_dir+str(i)+'.png', data[i], cmap='gray')
print("done.")
    # plt.imshow(data[i], cmap='gray')
    # plt.show()


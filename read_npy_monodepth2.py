from PIL import Image
import numpy as np
import os
from matplotlib import pyplot as plt
import glob


def read_monodepth2_npys(origin_disp_dir, output_disp_dir):
    all_disps = glob.glob(origin_disp_dir + '/*.npy')
    if not os.path.exists(output_disp_dir):
      os.makedirs(output_disp_dir)
    print('reading npys')
    i = 0
    for disp in all_disps:
        data = np.load(disp, allow_pickle=True)
        # print(data.shape)
        # print(len(data))
        # res = Image.fromarray(data[0])
        # res.show()
        # plt.imshow(np.squeeze(data[0]), cmap='gray')
        plt.imsave(output_disp_dir+str(i)+'.png', np.squeeze(data[0]), cmap='gray')
        i = i + 1
    print("done.")

if __name__ == '__main__':
    read_monodepth2_npys('./1Weights_and_npzs/monodepth2_npys_disp_320x1024/', 
                         './1Weights_and_npzs/1monodepth2_disp_320x1024/')


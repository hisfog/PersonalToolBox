import os
import glob
import numpy as np
from PIL import Image
import matplotlib as mpl
import matplotlib.cm as cm

if __name__ == '__main__': 
    all_src_dir = './EPC_320x1024/'
    all_files = glob.glob(all_src_dir + '/*.png')
    out_dir = './vis_assets/EPC_320x1024_resized/'
    if not os.path.exists(out_dir):
      os.makedirs(out_dir)
    print('resizing ...')
    for x in all_files:
        # print('colorlize ',x)
        img = Image.open(x)
        # im.show()
        #save image
        res_resized = img.resize((640, 192), Image.BILINEAR)
        res_resized.save(os.path.join(out_dir, os.path.basename(x)))

    print('done.')

import PIL.Image as pil
import glob
import cv2
import numpy as np
import os
import matplotlib as mpl
import matplotlib.cm as cm

def convert_array_to_pil(name):
    # Input: depth_map -> HxW numpy array with depth values 
    # Output: colormapped_im -> HxW numpy array with colorcoded depth values
    # [256:, 192:1856]
    img = pil.open(name)
    width, height = img.size
    # print(width, height)
# Setting the points for cropped image
    left = 192*width/2048
    top = 256*height/768
    right = 1856*width/2048
    bottom = height # for cityscapes, crop the image
    # left = (width - 0.5*width)/2
    # top = (height - 0.25*height)/2
    # right = (width + 0.5*width)/2
    # bottom = (height + 1.0*height)/2
# Cropped image of above dimension
# (It will not change original image)
    res = img.crop((left, top, right, bottom))
    return res

if __name__ == '__main__': 
    origin_disp_dir = './disps_cityscapes_split/'
    all_disps = glob.glob(origin_disp_dir + '/*.png')
    output_disp_dir = './disps_cityscapes_split_crop/'
    if not os.path.exists(output_disp_dir):
      os.makedirs(output_disp_dir)
    print('resizing ...')
    for disp in all_disps:
        res = convert_array_to_pil(disp)
        # res = pil.fromarray(res)
        # im.show()
        #save image
        res_resized = res.resize((640, 192), pil.BILINEAR)
        res_resized.save(os.path.join(output_disp_dir, os.path.basename(disp)))
    print('done.')


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
    img = pil.open(name)
    # img = pil.open(name).convert('L')
    depth_map = np.asarray(img)
    # disp_map = depth_map
    # # disp_map = 1 / depth_map
    # vmax = np.percentile(depth_map, 95)
    # normalizer = mpl.colors.Normalize(vmin=disp_map.min(), vmax=vmax)
    # mapper = cm.ScalarMappable(norm=normalizer, cmap='magma')
    # colormapped_im = (mapper.to_rgba(disp_map)[:, :, :3] * 255).astype(np.uint8)
    # return colormapped_im
    return depth_map

if __name__ == '__main__': 
    origin_disp_dir = './src_eigen_benchmark_split/'
    all_disps = glob.glob(origin_disp_dir + '/*.png')
    output_disp_dir = './src_eigen_benchmark_split_192x640/'
    if not os.path.exists(output_disp_dir):
      os.makedirs(output_disp_dir)
    print('resizing ...')
    for disp in all_disps:
        res = convert_array_to_pil(disp)
        res = pil.fromarray(res)
        # im.show()
        #save image
        res_resized = res.resize((640, 192), pil.BILINEAR)
        res_resized.save(os.path.join(output_disp_dir, os.path.basename(disp)))
    print('done.')


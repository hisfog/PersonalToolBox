# This script is to visualize disparity maps.
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
    img = pil.open(name).convert('L')
    depth_map = np.asarray(img)
    disp_map = 1 / (depth_map + 1e-8)
    disp_map = (disp_map - disp_map.min()) / (disp_map.max() - disp_map.min())
    # disp_map = 0.4 - depth_map
    # disp_map = 0.85 - depth_map
    # vmin = np.percentile(disp_map, 20)
    vmax = np.percentile(disp_map, 90)
    # normalizer = mpl.colors.Normalize(vmin=vmin, vmax=vmax)
    # normalizer = mpl.colors.Normalize(vmin=vmin, vmax=disp_map.max())
    # normalizer = mpl.colors.Normalize(vmin=disp_map.min(), vmax=disp_map.max())
    normalizer = mpl.colors.Normalize(vmin=disp_map.min(), vmax=vmax)
    mapper = cm.ScalarMappable(norm=normalizer, cmap='plasma_r')
    colormapped_im = (mapper.to_rgba(disp_map)[:, :, :3] * 255).astype(np.uint8)
    return colormapped_im

if __name__ == '__main__': 
    origin_disp_dir = './1Weights_and_npzs/1monodepth2_disp_320x1024/'
    all_disps = glob.glob(origin_disp_dir + '/*.png')
    output_disp_dir = './1monodepth2_npys_320x1024_mono_disp_color/'
    if not os.path.exists(output_disp_dir):
      os.makedirs(output_disp_dir)
    print('colorlizing')
    for disp in all_disps:
        res = convert_array_to_pil(disp)
        res = pil.fromarray(res)
        # im.show()
        #save image
        res_resized = res.resize((1024, 320), pil.BILINEAR)
        res_resized.save(os.path.join(output_disp_dir, os.path.basename(disp)))
    print('done.')



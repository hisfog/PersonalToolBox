# This script is to visualize depth maps.
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
    disp_map = depth_map
    # disp_map = 1 / depth_map
    vmax = np.percentile(depth_map, 95)
    normalizer = mpl.colors.Normalize(vmin=disp_map.min(), vmax=vmax)
    mapper = cm.ScalarMappable(norm=normalizer, cmap='plasma_r')
    colormapped_im = (mapper.to_rgba(disp_map)[:, :, :3] * 255).astype(np.uint8)
    return colormapped_im

if __name__ == '__main__': 
    origin_disp_dir = './1Weights_and_npzs/res50_192x640_weights_19/depth_maps_raw/'
    all_disps = glob.glob(origin_disp_dir + '/*.png')
    output_disp_dir = './1Weights_and_npzs/res50_192x640_weights_19/SQLdepth_res50_kitti_192x640/'
    if not os.path.exists(output_disp_dir):
      os.makedirs(output_disp_dir)
    print('colorlizing')
    for disp in all_disps:
        res = convert_array_to_pil(disp)
        res = pil.fromarray(res)
        # im.show()
        #save image
        res_resized = res.resize((640, 192), pil.BILINEAR)
        res_resized.save(os.path.join(output_disp_dir, os.path.basename(disp)))
    print('done.')

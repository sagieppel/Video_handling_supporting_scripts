# Interactive Demo of material segmentation net, select point in the image and display the similarity of
# This should display the segmentation map and material similarity map for a selected point in the image (the segment of the point and how similart the rest of the materials in the rest  of the image to the point.)
# image, segment contour, similarity map, selected point marked blue, Arrows: move dot, +/- change dot size, PageUp/PageDown change threshold
import os.path

import numpy as np
import torch
import cv2
import argparse

import Desnet

###############################################################################################
# input parameters
parser = argparse.ArgumentParser(description='Apply segmentation, find similarity of materials in the image to a selected point in the image')
parser.add_argument('--in_main_dir', default="/media/deadcrow/6TB/python_project/MatSeg-Synthethic-Dataset-Generation-Script-main/out_generated_data_extracted_Pbrs_cycles/", type=str, help='target image')
parser.add_argument('--out_dir', default="/media/deadcrow/6TB/python_project/MatSeg-Synthethic-Dataset-Generation-Script-main/out_videos/", type=str, help='output folder')
#parser.add_argument('--image_path', default="samples/MatSegBenchMark/images_selected/20230913_185027.jpg", type=str, help='target image')

args = parser.parse_args()

#---------------------------------------------------------------------------------
out_dir = args.out_dir
if out_dir == "":
    out_dir = args.in_dir
if not os.path.exists(out_dir): os.mkdir(out_dir)


if __name__ == "__main__":
            for dr in os.listdir(args.in_main_dir):
                in_dir= args.in_main_dir+"/"+dr+"//"
                if not os.path.isdir(in_dir): continue
                out_vid = out_dir + "/" + dr +".mp4"
                print("   in dir:",in_dir,"   out dir:",out_dir)
                frame=0
                for iii in range(10000):
                    im_file= in_dir+"/RGB_"+str(iii)+"_RGB.jpg"
                    if not os.path.exists(im_file): continue
                    im= cv2.imread(im_file)
                    print(im_file)

                    if frame == 0:
                        fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # 'mp4v' for MP4 files
                        video_writer = cv2.VideoWriter(out_vid, fourcc, 23, (im.shape[1], im.shape[0]))
                    frame+=1
                    video_writer.write(im)
                    print("write",frame, " path ", out_vid)


                video_writer.release()

import os
import cv2
import shutil
import numpy as np

from Demo_Interactive_Video import out_vid

indr="/media/deadcrow/6TB/python_project/MatSeg-Synthethic-Dataset-Generation-Script-main/out_videos/Selected2x2/"
outvd="/media/deadcrow/6TB/python_project/MatSeg-Synthethic-Dataset-Generation-Script-main/out_videos/Selected2x2_merged_Fast_Small.mp4"


for ii,fl in enumerate(os.listdir(indr)):
    cap = cv2.VideoCapture(indr+"/"+fl)
    if not cap.isOpened():
        print("Error: Could not open video.")
        exit()

    for frm in range(100000000):
        ret, im = cap.read()

        if ret == False: break
        im = cv2.resize(im, [1080, 1080])
        if frm % 2 == 1: continue
        print(ii, frm)
        if frm==0 and ii==0:
            fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # 'mp4v' for MP4 files
            out_vid = outvd
            sx=im.shape[1]
            sy = im.shape[0]

            video_writer = cv2.VideoWriter(out_vid, fourcc, 23, (sx, sy))
        if  sx!=im.shape[1] or sy!= im.shape[0]:
             im = cv2.resize(im,[sx,sy])
        video_writer.write(im)
    cap.release()

video_writer.release()


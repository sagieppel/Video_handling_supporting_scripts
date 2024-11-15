import os
import cv2
import shutil
import numpy as np

from Demo_Interactive_Video import out_vid

indr="/media/deadcrow/6TB/python_project/MatSeg-Synthethic-Dataset-Generation-Script-main/out_videos/Selected/"
outdr="/media/deadcrow/6TB/python_project/MatSeg-Synthethic-Dataset-Generation-Script-main/out_videos/Selected7x7/"
if not os.path.exists(outdr): os.mkdir(outdr)
grd_sz=7

in_vids=os.listdir(indr)
sz_im=1080
max_size=1080*4
vid_group=[]
grp=[]
for ii,fl in enumerate(os.listdir(indr)):
    if ii%(grd_sz**2)==0:

        if len(grp)==grd_sz**2:
            vid_group.append(grp)
        grp = []

    grp.append(indr+"/"+fl)
# videos--------------------------------------------------------------------------------------
for ii,grp in enumerate(vid_group):
    caps=[]
    for vd in grp:
      caps.append(cv2.VideoCapture(vd))
      if not caps[-1].isOpened():
        print("Error: Could not open video.")
        exit()
    finish = False
    #----------------Frames----------------------------------------------------------------------------
    frm = 0
    while(True):
        xx=0
        yy=0
        ll=0

#--------panels--------------------------------------------------------------------------------------
        stack_frame= np.zeros([sz_im*grd_sz,sz_im*grd_sz,3],dtype=np.uint8)
        for ff, cap in enumerate(caps):
            ret, im = cap.read()

            if ret == False:
                finish = True
                break
            ll+=1
            if ff%grd_sz==0 and ff>0:
                yy+=1
                xx=0
            stack_frame[yy*sz_im:(yy+1)*sz_im, xx*sz_im:(xx+1)*sz_im]=im
            xx+=1
        # cv2.imshow("",stack_frame)
        # cv2.waitKey()
        if stack_frame.shape[0]>max_size:
            stack_frame=cv2.resize(stack_frame,[max_size,max_size])
        if finish:
             if frm>0:
                 video_writer.release()
             break
        if frm==0:
            fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # 'mp4v' for MP4 files
            out_vid= outdr +"/" + str(ii)+".mp4"
            video_writer = cv2.VideoWriter(out_vid, fourcc, 23, (stack_frame.shape[1],stack_frame.shape[0]))
        video_writer.write(stack_frame)
        print(out_vid,"   frame ",frm)
        frm+=1
    video_writer.release()








    #
    #
    # if os.path.exists(indr+"/"+sdr+"/v.txt"):
    #      shutil.copytree(indr+"/"+sdr,outdr+"/"+sdr)
    #      print(indr+"/"+sdr,outdr+"/"+sdr)
    #
    #      fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # 'mp4v' for MP4 files
    #      video_writer = cv2.VideoWriter(out_vid, fourcc, 23, (comb_im.shape[1], comb_im.shape[0]))
from ImageFrame import Frame
from EdgeFinder import EdgeFinder as ef
import numpy as np
from PIL import Image
from scipy.ndimage import filters
from auto_drive_functions import *

def retrieve_angle(s1,hd,img,frame,plot = False):
    data = frame.get_data(img,5)
    edges = perform_3sig(data,s1,hd,False)
    points = np.empty((0,2),float)
    for key in edges.keys():
        points = np.append(points,[edges[key][0:2]],axis=0)
    #print(mids_point[:,2])
    mid_points = mid_angle(points,frame.width,frame.height)
    if plot : plot_on_img(img,edges,frame,mid_points)
    return mid_points[:,2]
    
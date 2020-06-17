#!/pkg/python/3.6.8/bin/python3.6
import numpy as np
import cv2
from scipy.ndimage import gaussian_filter

def extract_subhalo(data, outpath):
    # Load and Resize image as needed
    img = cv2.resize(data, (512,512), interpolation=cv2.INTER_CUBIC)
    # Gaussian filter
    imgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    imgray = gaussian_filter(imgray,sigma=5)
    # Threshold
    ret, thresh = cv2.threshold(imgray,255,255,255)
    # Find contours
    img2, contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    # Generate binary mask
    h,w,_ = img.shape
    fill = np.zeros((h,w,3), np.float64)
    cv2.drawContours(fill, contours, -1, (1,1,1), cv2.FILLED)
    mask = np.zeros((h,w,3),np.float64)
    mask[21:476,60:422] = fill[21:476,60:422]
    # Crop image along contours
    img_cropped = np.zeros((h,w,3), np.uint8)
    img_cropped = mask*img
    img_cropped = img_cropped.astype(int)
    # Save image
    cv2.imwrite(str(outpath), img_cropped)
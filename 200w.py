# Copyright (C) 2021  wfxzf

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

###############################################################################################################
##  使用方法  :   仅需修改输入输出的文件名即可，注意文件路径，要求输入图像为正方形或接近正方形                    ##                                        
###############################################################################################################
import cv2
import numpy as np
pic = cv2.imread('mi.jpg')
side = len(pic) if len(pic)<len(pic[0]) else len(pic[0])
alpha_channel = np.ones( pic[0:side,0:side][:,:,0].shape, dtype='uint8') * 255
for i in range(0,side):
    for j in range(0,side):
        alpha_channel[i][j] = 0 if (abs(i-int(side/2))**3+abs(j-int(side/2))**3) > int(side/2)**3 else 255
img_BGRA = cv2.merge((pic[0:side,0:side], alpha_channel))
cv2.imwrite("200w.png", img_BGRA)




#!/usr/bin/env python
# above line to execute in linux

import numpy as np
import cv2
import random
import string
import os
from PIL import ImageFont, ImageDraw, Image
from random import randrange, uniform, randint
#from Tutorial_Random_numbers_strings_etc import *

"""WORKFLOW: Training and Testdata generator
1. label size definition
2. 4K/ FullHD 
3. loop for original image or augmentation
4. random VDA label integration (yellow and white)  including random strings/ labels AND LABELS for YOLOv3
5. save all images with specific label names"""

# TODO while loop which creates random labels in an image
# todo create label boxes around createt labels for YOLO including random colours (rgb 0-255) = 8 bit
# TODO all open cv image operations/ data augementator ops and randomly choose a few inside a while loop for a label position ( for each label ==> picture in different variations)

""" label and picture size definition"""
## yellow label:
yl_label_width = 225
yl_label_height = 50
## white label
wh_label_width = 190
wh_label_height = 150
# Image Size's 4K 16:9 UHDTV standard and Full HD
fourK_width = 3840
fourK_height = 2160
FullHD_width = 1920
FullHD_height = 1080
""" Define distance of white and yellow pixels ==> use in defining random start pixel area """
wh_dstnc_l_t_x = 25
wh_dstnc_l_t_y = 100

"Dateaset creation loops"
count = 0
while count < 1:

# for i in range(50):
#     print("Some thing")

    """ Localization Parameter""" #TODO make random and start with yellow label
    """ Start Pixel (random) of labels """

    #Todo: random start of yellow label ===> decide whether 4K/FullHD ===> 4k between 0 and 3840-yl_label

    # area of yellow label 4K or FullHD
    """ SET 4K or FullHD"""
    four_K = 0

    if four_K == 1:
        start_pxl_lft_tp_x = fourK_height - randint(0, (fourK_width - yl_label_width))
        start_pxl_lft_tp_y = fourK_height - randint(0, (fourK_height - (yl_label_height + wh_dstnc_l_t_y + wh_label_height)))
    else:
        start_pxl_lft_tp_x = FullHD_width - randint(0, (FullHD_width - yl_label_width))
        start_pxl_lft_tp_y = FullHD_height - randint(0, (FullHD_height - (yl_label_height + wh_dstnc_l_t_y + wh_label_height)))
    print("start pixel x is: {} and start pixel in y is: {}".format(start_pxl_lft_tp_x , start_pxl_lft_tp_y))

    #Todo yellow label standalone
    """Yellow label  dependend on random image pixels in range of image pixels"""
    def yellow_box():
        pass
    yl_pxl_l_t_x = start_pxl_lft_tp_x
    yl_pxl_l_t_y = start_pxl_lft_tp_y
    yl_pxl_r_b_x = yl_pxl_l_t_x + yl_label_width
    yl_pxl_r_b_y = yl_pxl_l_t_y + yl_label_height
    yl_col_R = 255
    yl_col_G = 255
    yl_col_B = 0
    ## black box inside yellow label depends on yellow label
    bb_pxl_l_t_x = yl_pxl_r_b_x - yl_label_height
    bb_pxl_l_t_y = yl_pxl_r_b_y - yl_label_height
    bb_pxl_r_b_x = yl_pxl_r_b_x
    bb_pxl_r_b_y = yl_pxl_r_b_y
    # img = cv2.rectangle(img, (yl_pxl_l_t_x , yl_pxl_l_t_y), (yl_pxl_r_b_x, yl_pxl_r_b_y), (yl_col_B, yl_col_G,yl_col_R), -1)
    # img = cv2.rectangle(img, (bb_pxl_l_t_x , bb_pxl_l_t_y), (bb_pxl_r_b_x, bb_pxl_r_b_y), (0, 0, 0), -1)

    """white label dependend on independend start pixel"""
    ## white  label referenced on random start pixel size of top left pixel

    wh_pxl_l_t_x = start_pxl_lft_tp_x + wh_dstnc_l_t_x                      # pixel left top white box
    wh_pxl_l_t_y = start_pxl_lft_tp_y + wh_dstnc_l_t_y
    wh_pxl_r_b_x = wh_pxl_l_t_x + wh_label_width
    wh_pxl_r_b_y = wh_pxl_l_t_y + wh_label_height
    wh_col_R = 255
    wh_col_G = 255
    wh_col_B = 255

    #TODO upload/ read image and print box on top
    """ DRAW Backround with Box"""
    def print_labels_on_image():
        img = cv2.imread('../Image1_realsense_test.png')
        #img = np.ones((1080, 1920, 3), np.uint8)*255                                                # create image with FullHD resolution in white = np.ones * 255
        #img = cv2.rectangle(img, (pxl_l_t_x, pxl_l_t_y), (pxl_r_b_x, pxl_r_b_y), (bb_col_B, bb_col_G, bb_col_R), -1)                       # thicknes  = -1 to fill rectangle                    # draw brown box BGR!!!
        img = cv2.rectangle(img, (yl_pxl_l_t_x , yl_pxl_l_t_y), (yl_pxl_r_b_x, yl_pxl_r_b_y), (yl_col_B, yl_col_G,yl_col_R), -1)
        img = cv2.rectangle(img, (bb_pxl_l_t_x , bb_pxl_l_t_y), (bb_pxl_r_b_x, bb_pxl_r_b_y), (0, 0, 0), -1)
        img = cv2.rectangle(img, (wh_pxl_l_t_x, wh_pxl_l_t_y), (wh_pxl_r_b_x, wh_pxl_r_b_y), (wh_col_B, wh_col_G, wh_col_R), -1)

        """ random label text generator"""
        label_1st_pos = random_text_gen(2, randomascii=False, uppercase=True)
        label_2nd_pos = random_text_gen(1, randomascii=False, uppercase=False, lowercase=False)
        label_3rd_pos = '-'
        label_4th_pos = random_text_gen(3, randomascii=False, uppercase=False, lowercase=False)
        label_5th_pos = random_text_gen(1, randomascii=False, uppercase=True)
        label_text_comb = '%s%s %s %s%s' % (label_1st_pos, label_2nd_pos, label_3rd_pos, label_4th_pos, label_5th_pos)
        print(label_text_comb)
        label_white_number = random_text_gen(10, randomascii=False, uppercase=False, lowercase=False)
        print(label_white_number)
        label_white_str = '%s' % (label_white_number)

        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(img, label_text_comb, (txt_pos_blyl_x, txt_pos_blyl_y), font, 0.5, (0, 0, 0), 2, cv2.LINE_AA)
        cv2.putText(img, random_text_gen(2, randomascii=False, uppercase=False, lowercase=False),
                    (txt_pos_ylbl_x, txt_pos_ylbl_y), font, 1, (yl_col_B, yl_col_G, yl_col_R), 2, cv2.LINE_AA)
        cv2.putText(img, label_white_number, (txt_pos_wh_x, txt_pos_wh_y), font, 0.8, (0, 0, 0), 2, cv2.LINE_AA)

        # Todo write  more variables in string in filename for picture name and opencv operation
        """ show and write image """
        # print(img)
        filename_str = '%s --- %s.jpg' % (label_text_comb, label_white_str)
        print(filename_str)
        cv2.imshow('Dataset_VDA_labels', img)
        cv2.waitKey(0) & 0xFF
        cv2.destroyAllWindows()

        return img


    """ Labels text positions"""
    #text position inside yellow label
    txt_distance_x = 40
    txt_distance_y = 5
    txt_pos_blyl_x = yl_pxl_l_t_x + txt_distance_x                      # pixel left bottom x
    txt_pos_blyl_y = yl_pxl_l_t_y + yl_label_height - txt_distance_y    # pixel left bottom y
    # on black box
    txt_distance_yellow_x = 6
    txt_distance_yellow_y = 12
    txt_pos_ylbl_x = bb_pxl_l_t_x + txt_distance_yellow_x
    txt_pos_ylbl_y = bb_pxl_l_t_y + yl_label_height - txt_distance_yellow_y
    # on white label
    txt_wh_dstnc_x = 20
    txt_wh_dstnc_y = 60
    txt_pos_wh_x = wh_pxl_l_t_x + txt_wh_dstnc_x
    txt_pos_wh_y = wh_pxl_l_t_y + txt_wh_dstnc_y

    """ text generator"""
    def random_text_gen(length=32, randomascii=True, uppercase=True, lowercase=True, numbers=True):
        character_set = ''  # lowercase, uppercase, digits etc. possile
        if randomascii:
            character_set += string.ascii_letters
        elif uppercase:
            character_set += string.ascii_uppercase
        elif lowercase:
            character_set += string.ascii_lowercase
        elif numbers:
            character_set += string.digits

        return ''.join(random.choice(character_set) for i in range(length))

    # """ random label text generator"""
    # label_1st_pos = random_text_gen(2,randomascii=False, uppercase=True)
    # label_2nd_pos = random_text_gen(1, randomascii=False, uppercase=False, lowercase=False)
    # label_3rd_pos = '-'
    # label_4th_pos = random_text_gen(3, randomascii=False, uppercase=False, lowercase=False)
    # label_5th_pos = random_text_gen(1,randomascii=False, uppercase=True)
    # label_text_comb = '%s%s %s %s%s' %(label_1st_pos, label_2nd_pos, label_3rd_pos, label_4th_pos, label_5th_pos)
    # print(label_text_comb)
    # label_white_number = random_text_gen(10, randomascii=False, uppercase=False, lowercase=False)
    # print(label_white_number)
    # label_white_str = '%s' %(label_white_number)
    #
    # font = cv2.FONT_HERSHEY_SIMPLEX
    # cv2.putText(img, label_text_comb, (txt_pos_blyl_x, txt_pos_blyl_y), font, 0.5, (0, 0, 0), 2, cv2.LINE_AA)
    # cv2.putText(img, random_text_gen(2, randomascii=False, uppercase=False, lowercase=False), (txt_pos_ylbl_x, txt_pos_ylbl_y), font, 1, (yl_col_B,yl_col_G, yl_col_R), 2, cv2.LINE_AA)
    # cv2.putText(img, label_white_number, (txt_pos_wh_x, txt_pos_wh_y), font, 0.8, (0, 0, 0), 2, cv2.LINE_AA)
    #
    # #Todo write  more variables in string in filename for picture name and opencv operation
    # """ show and write image """
    # #print(img)
    # filename_str = '%s --- %s.jpg' %(label_text_comb, label_white_str)
    # print(filename_str)
    #cv2.imwrite(filename_str, img)
    # cv2.imshow('Dataset_VDA_labels', img)
    # cv2.waitKey(0) & 0xFF
    # cv2.destroyAllWindows()

    count = count + 1


if __name__ == "__main__":
    print_labels_on_image()

""" text generator"""
# def random_text_gen(length=32, randomascii=True, uppercase=True, lowercase=True, numbers=True):
#     character_set = ''                                                                          # lowercase, uppercase, digits etc. possile
#     if randomascii:
#         character_set += string.ascii_letters
#     elif uppercase:
#         character_set += string.ascii_uppercase
#     elif lowercase:
#         character_set += string.ascii_lowercase
#     elif numbers:
#         character_set += string.digits
#
#     return ''.join(random.choice(character_set) for i in range(length))

"""Brown box """
# """brown box hardcoded at startpixel"""
# pxl_l_t_x = 300                                             # pixel left top x
# pxl_l_t_y = 200
# brown_width = 600
# brown_height = 400                                          # left top y
# pxl_r_b_x = pxl_l_t_x + brown_width                         # right bottom x
# pxl_r_b_y = pxl_l_t_y + brown_height                        # right bottom y
# bb_col_R = 222
# bb_col_G = 184
# bb_col_B = 135
# """"yellow label referenced on size of top left pixel of brown box /// in range of image pixels  ###"""
# # yl_dstnc_l_t_x = 100
# # yl_dstnc_l_t_y = 40
# # yl_pxl_l_t_x = pxl_l_t_x + yl_dstnc_l_t_x                      # pixel left top
# # yl_pxl_l_t_y = pxl_l_t_y + yl_dstnc_l_t_y#

"""diagonal blue line with thickness of 5px2"""
    # img3 = cv2.line(img3, (0,0), (511,511), (255,0,0), 5)


    ### write into image  Adding Text to Images:

    # To put texts in images, you need specify following things.
    #
    #         Text data that you want to write
    #         Position coordinates of where you want put it (i.e. bottom-left corner where data starts).
    #         Font type (Check cv2.putText() docs for supported fonts)
    #         Font Scale (specifies the size of font)
    #         regular things like color, thickness, lineType etc. For better look, lineType = cv2.LINE_AA is recommended.
#
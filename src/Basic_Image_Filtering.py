import os
import cv2
import matplotlib.pyplot as plt
import numpy as np

url = input("Please enter the image path you want to process: ")
if url == "":
    url = '../media/input/input.jpg'

if os.path.exists(url):
    og_image = cv2.imread(url)
    height = og_image.shape[0]
    width = og_image.shape[1]
else:
    print("Please re-enter the path")
    exit(0)


def channelassign(input):
    if input.lower() == 'r':
        inp = 2
        return inp
    elif input.lower() == 'g':
        inp = 1
        return inp
    elif input.lower() == 'b':
        inp = 0
        return inp
    else:
        print("You've selected " + str(
            input) + ". Incorrect option selected. Select between R, G and B")


def checkuserinput(input, min, max):
    try:
        input = int(input)
    except ValueError:
        print("You've selected " + str(
            input) + ". Incorrect option selected. Select an integer between " + str(min) + " and " + str(max))
    if input in range(min, max):
        return True
    else:
        print("You've selected " + str(
            input) + ". Incorrect option selected. Select an integer between " + str(min) + " and " + str(max))
        return False


def plot_RGB(og_image, row):
    row = int(row)
    b_val = og_image[:, row - 1, 0]
    g_val = og_image[:, row - 1, 1]
    r_val = og_image[:, row - 1, 2]
    x_axis = range(len(list(r_val)))
    plt.scatter(x_axis, b_val, s=7, color="blue", label="Blue pixel values")
    plt.scatter(x_axis, g_val, s=7, color="green", label="Green pixel values")
    plt.scatter(x_axis, r_val, s=7, color="red", label="Red pixel values")
    plt.xlabel("Pixel")
    plt.ylabel("Value")
    plt.legend(loc="lower left")
    plt.savefig('../media/output/1_scanline.png')
    plt.show()


def verticalRBGstack(og_image):
    zero_val = np.zeros(og_image[:, :, 0].shape)
    blue = og_image.copy()
    blue[:, :, 1] = zero_val
    blue[:, :, 2] = zero_val

    red = og_image.copy()
    red[:, :, 0] = zero_val
    red[:, :, 1] = zero_val

    green = og_image.copy()
    green[:, :, 0] = zero_val
    green[:, :, 2] = zero_val

    conc = np.concatenate((red, green, blue), axis=0)
    return conc


def swapColor(og_image, ch1, ch2):
    ch1 = channelassign(ch1)
    ch2 = channelassign(ch2)
    if ch1 != ch2:
        swap = og_image.copy()
        swap[:, :, 1] = og_image[:, :, ch1]
        swap[:, :, 2] = og_image[:, :, ch2]
        return swap
    else:
        print("You've selected same channels, please reselect")
        exit(0)


def RGB2Gray(og_image):
    gray = ((0.114 * og_image[:, :, 0]) + 0.587 * (og_image[:, :, 1]) + 0.299 * (og_image[:, :, 2])).astype(np.uint8)
    return gray


def channelaverage(og_image):
    red_avg = np.mean(og_image[:, :, 2])
    green_avg = np.mean(og_image[:, :, 1])
    blue_avg = np.mean(og_image[:, :, 0])
    avg_image = og_image.copy()
    avg_image[:, :, 0] = blue_avg
    avg_image[:, :, 1] = green_avg
    avg_image[:, :, 2] = red_avg
    avg_image = avg_image.astype(np.uint8)
    return avg_image


def pixelaverage(og_image):
    avg = ((((1 / 3) * og_image[:, :, 0])) + ((1 / 3) * (og_image[:, :, 1])) + ((1 / 3) * (og_image[:, :, 2]))).astype(
        np.uint8)
    return avg


def channelaverage(og_image):
    avg = og_image.copy()
    avg[:, :, 0] = np.mean(og_image[:, :, 0])
    avg[:, :, 1] = np.mean(og_image[:, :, 1])
    avg[:, :, 2] = np.mean(og_image[:, :, 2])
    avg = avg.astype(np.uint8)
    return avg


def colornegative(og_image):
    neg = og_image.copy()
    neg[:, :, 0] = abs(255 - og_image[:, :, 0])
    neg[:, :, 1] = abs(255 - og_image[:, :, 1])
    neg[:, :, 2] = abs(255 - og_image[:, :, 2])
    return neg


def gray2negative(og_image):
    gray = RGB2Gray(og_image)
    neg = abs(255 - gray)
    return neg


def cropandrotate(og_image, orient, crop_val):
    crop = og_image.copy()
    crop = crop[int((height / 2) - (crop_val / 2)):int((height / 2) + (crop_val / 2)),
           int((width / 2) - (crop_val / 2)):int((width / 2) + (crop_val / 2))]
    if orient in range(1, 3):
        if orient == 1:
            crop_90 = np.rot90(crop, k=3)
            crop_180 = np.rot90(crop, k=2)
            crop_270 = np.rot90(crop, k=1)
        elif orient == 2:
            crop_90 = np.rot90(crop, k=1)
            crop_180 = np.rot90(crop, k=2)
            crop_270 = np.rot90(crop, k=3)
        else:
            print("You've selected " + str(orient) + ". Incorrect option selected. Select an integer between 1 and 2")
        rot = np.concatenate((crop, crop_90, crop_180, crop_270), axis=1)
        return rot
    else:
        print("You've selected " + str(orient) + ". Incorrect option selected. Select an integer between 1 and 2")


def maskImage(og_image, thresh):
    mask = np.zeros(og_image.shape)
    mask[og_image[:, :, 0] > thresh, 0] = 255
    mask[og_image[:, :, 1] > thresh, 1] = 255
    mask[og_image[:, :, 2] > thresh, 2] = 255
    mask = mask.astype(np.uint8)
    return mask


def maskedAvg(og_image, thresh):
    mask = maskImage(og_image, thresh)
    m_red_avg = np.mean(mask[:, :, 2])
    print("Masked red channel average: ", m_red_avg)
    m_green_avg = np.mean(mask[:, :, 1])
    print("Masked green channel average: ", m_green_avg)
    m_blue_avg = np.mean(mask[:, :, 0])
    print("Masked blue channel average: ", m_blue_avg)


def nonMax(og_image, step, win_size):
    gray = RGB2Gray(og_image)
    nonmax = np.zeros(gray.shape)
    copy = gray.copy()
    for i in range(0, height, step):
        for j in range(0, width, step):
            win = copy[i:(i + win_size), j:(j + win_size)]
            max_val = np.max(win)
            index_val = win == max_val
            n_win = nonmax[i:(i + win_size), j:(j + win_size)]
            n_win[index_val] = 255
    return nonmax


opt = (input("Please select the suitable option:\n"
             "1) Plot R, G, B values of a certain row\n"
             "2) Stack R, G, B channels vertically \n"
             "3) Swap channels \n"
             "4) Convert image to grayscale \n"
             "5) Average pixel color \n"
             "6) Obtain negative of grayscale image \n"
             "7) Rotate and stack horizontally the cropped image \n"
             "8) Mask image \n"
             "9) Print the RGB mean of the masked image \n"
             "10) Put a non-max filter on the image \n\n"))
name = ""
if checkuserinput(opt, 1, 11):
    opt = int(opt)
if (type(opt) == int):
    if opt in range(1, 11):
        if opt == 1:
            row = input("Please enter the row of the image: ")
            if checkuserinput(row, 1, height + 1):
                plot_RGB(og_image, row)
        elif opt == 2:
            result = verticalRBGstack(og_image)
            name = "2_concat"
        elif opt == 3:
            ch1 = input("Select the first channel: ")
            ch2 = input("Select the second channel: ")
            result = swapColor(og_image, ch1, ch2)
            name = "3_swapchannel"
        elif opt == 4:
            result = RGB2Gray(og_image)
            name = "4_grayscale"
        elif opt == 5:
            choice = input("\nSelect type of average\n"
                           "1. Pixel Average\n"
                           "2. Channel Average\n\n")
            if checkuserinput(choice, 1, 3):
                choice = int(choice)

                if choice == 1:
                    result = pixelaverage(og_image)
                    name = "5_average"
                elif choice == 2:
                    result = channelaverage(og_image)
                    name = "5_average"
        elif opt == 6:
            img = input("\nSelect type of negative:\n"
                        "1. Grayscale Negative\n"
                        "2. Color Negative\n\n")
            if checkuserinput(img, 1, 3):
                img = int(img)
                if img == 1:
                    result = gray2negative(og_image)
                    name = "6_negative"
                elif img == 2:
                    result = colornegative(og_image)
                    name = "6_negative"
        elif opt == 7:
            orient = input("\nSelect type of rotation\n"
                           "1. Clockwise\n"
                           "2. Anticlockwise\n\n")
            if checkuserinput(orient, 1, 3):
                orient = int(orient)
                crop_val = input("\nPlease enter the crop value: ")
                if checkuserinput(crop_val, 1, min(height, width)):
                    crop_val = int(crop_val)
                    result = cropandrotate(og_image, orient, crop_val)
                    name = "7_rotation"
        elif opt == 8:
            thresh = input("Please input the minimum threshold value: ")
            if checkuserinput(thresh, 0, 255):
                thresh = int(thresh)
                result = maskImage(og_image, thresh)
                name = "8_mask"
        elif opt == 9:
            thresh = input("Please input the minimum threshold value: ")
            if checkuserinput(thresh, 0, 255):
                thresh = int(thresh)
                maskedAvg(og_image, thresh)
        elif opt == 10:
            win_size = input("\nPlease enter the window size: ")
            step = input("\nSelect step size for window translation: ")
            if step <= win_size:
                if checkuserinput(win_size, 1, min(height, width)):
                    win_size = int(win_size)
                    if checkuserinput(step, 1, min(height, width)):
                        val = int(step)
                        result = nonMax(og_image, val, win_size)
                        name = "10_nonmax"
            else:
                print("Incorrect step size, please make sure it is less than window size")

if name != "":
    cv2.imshow(name, result)
    cv2.imwrite("../media/output/" + name + ".png", result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

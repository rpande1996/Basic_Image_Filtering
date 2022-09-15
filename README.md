## Basic_Image_Filtering
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
---

## Overview



## Softwares

* Recommended IDE: PyCharm 2021.2

## Libraries

* Numpy 1.21.4
* OpenCV 4.6.0
* Matplotlib 3.5.0

## Programming Languages

* Python 3.10.7

## License 

```
MIT License

Copyright (c) 2022 Rajan Pande

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE 
SOFTWARE.
```
## Demo

- R, G, B values of the 250th row:

![img1](https://github.com/rpande1996/Basic_Image_Filtering/blob/main/media/output/1_scanline.png)

- R, G, B channels stacked vertically

![img2](https://github.com/rpande1996/Basic_Image_Filtering/blob/main/media/output/2_concat.png)

- Swapped R and G channels

![img3](https://github.com/rpande1996/Basic_Image_Filtering/blob/main/media/output/3_swapchannel.png)

- Grayscale

![img4](https://github.com/rpande1996/Basic_Image_Filtering/blob/main/media/output/4_grayscale.png)

- Pixel Average of the image

![img5](https://github.com/rpande1996/Basic_Image_Filtering/blob/main/media/output/5_average.png)

- Grayscale negative

![img6](https://github.com/rpande1996/Basic_Image_Filtering/blob/main/media/output/6_negative.png)

- 372x372 central crop rotated at an angle of 90 deg

![img7](https://github.com/rpande1996/Basic_Image_Filtering/blob/main/media/output/7_rotation.png)

- Masked image

![img8](https://github.com/rpande1996/Basic_Image_Filtering/blob/main/media/output/8_mask.png)

- Average pixel values of masked channels

```
Masked red channel average:  53.95040509259259
Masked green channel average:  77.4486255787037
Masked blue channel average:  150.74698350694445
```

- Non-maxima suppression

![img10](https://github.com/rpande1996/Basic_Image_Filtering/blob/main/media/output/10_nonmax.png)

## Build

```
git clone https://github.com/rpande1996/Basic_Image_Filtering
cd Basic_Image_Filtering/src
python Basic_Image_Filtering.py
```

## Steps

Please choose appropriate image path

Please choose the appropriate option
```
Please select the suitable option:
1) Plot R, G, B values of a certain row
2) Stack R, G, B channels vertically
3) Swap channels
4) Convert image to grayscale
5) Average pixel color
6) Obtain negative of grayscale image
7) Rotate and stack horizontally the cropped image
8) Mask image
9) Print the RGB mean of the masked image
10) Put a non-max filter on the image
```
Please choose the appropriate sub-option

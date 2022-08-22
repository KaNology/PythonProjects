"""
Python Image Manipulation Empty Template by Kylie Ying (modified from MIT 6.865)

YouTube Kylie Ying: https://www.youtube.com/ycubed 
Twitch KylieYing: https://www.twitch.tv/kylieying 
Twitter @kylieyying: https://twitter.com/kylieyying 
Instagram @kylieyying: https://www.instagram.com/kylieyying/ 
Website: https://www.kylieying.com
Github: https://www.github.com/kying18 
Programmer Beast Mode Spotify playlist: https://open.spotify.com/playlist/4Akns5EUb3gzmlXIdsJkPs?si=qGc4ubKRRYmPHAJAIrCxVQ 
"""

from re import L
from image import Image
import numpy as np

def adjust_brightness(image, factor):
    # when we brighten, we just want to make each channel higher by some amount 
    # factor is a value > 0, how much you want to brighten the image by (< 1 = darken, > 1 = brighten)

    x_pixels, y_pixels, num_channels = image.array.shape # Get the parameters of the image

    new_img = Image(x_pixels, y_pixels, num_channels) # Create a blank image first

    for x in range(x_pixels):
        for y in range(y_pixels):
            for c in range(num_channels):
                new_img.array[x, y, c] = image.array[x, y, c] * factor

    # Or you can simply use
    # new_img.array = image.array * factor

    return new_img

def adjust_contrast(image, factor, mid):
    # adjust the contrast by increasing the difference from the user-defined midpoint by factor amount
    
    x_pixels, y_pixels, num_channels = image.array.shape # Get the parameters of the image

    new_img = Image(x_pixels, y_pixels, num_channels) # Create a blank image first

    for x in range(x_pixels):
        for y in range(y_pixels):
            for c in range(num_channels):
                new_img.array[x, y, c] = mid + (image.array[x, y, c] - mid) * factor

    # new_img.array = mid + (image.array - mid) * factor

    return new_img

def blur(image, kernel_size):
    # kernel size is the number of pixels to take into account when applying the blur
    # (ie kernel_size = 3 would be neighbors to the left/right, top/bottom, and diagonals).
    # kernel size should always be an *odd* number
    
    x_pixels, y_pixels, num_channels = image.array.shape # Get the parameters of the image

    new_img = Image(x_pixels, y_pixels, num_channels) # Create a blank image first

    neighbor_range = kernel_size // 2 # How many neighbors to one side the center has

    for x in range(x_pixels):
        for y in range(y_pixels):
            for c in range(num_channels):
                total = 0
                for x_i in range(max(0, x - neighbor_range), min(x_pixels - 1, x + neighbor_range) + 1):
                    for y_i in range(max(0, y - neighbor_range), min(y_pixels - 1, y + neighbor_range) + 1):
                        total += image.array[x_i, y_i, c]
            
                new_img.array[x, y, c] = total / (kernel_size ** 2)

    return new_img

def apply_kernel(image, kernel):
    # the kernel should be a 2D array that represents the kernel we'll use!
    # for the sake of simiplicity of this implementation, let's assume that the kernel is SQUARE
    # for example the sobel x kernel (detecting horizontal edges) is as follows:
    # [1 0 -1]
    # [2 0 -2]
    # [1 0 -1]
    x_pixels, y_pixels, num_channels = image.array.shape  # represents x, y pixels of image, # channels (R, G, B)
    new_img = Image(x_pixels=x_pixels, y_pixels=y_pixels, num_channels=num_channels)  # making a new array to copy values to!
    
    neighbor_range = kernel.shape[0] // 2  # this is a variable that tells us how many neighbors we actually look at (ie for a 3x3 kernel, this value should be 1)
    
    for x in range(x_pixels):
        for y in range(y_pixels):
            for c in range(num_channels):
                total = 0

                for x_i in range(max(0,x-neighbor_range), min(new_img.x_pixels-1, x+neighbor_range)+1):
                    for y_i in range(max(0,y-neighbor_range), min(new_img.y_pixels-1, y+neighbor_range)+1):
                        x_k = x_i + neighbor_range - x
                        y_k = y_i + neighbor_range - y
                        kernel_val = kernel[x_k, y_k]
                        total += image.array[x_i, y_i, c] * kernel_val

                new_img.array[x, y, c] = total

    return new_img

def combine_images(image1, image2):
    # let's combine two images using the squared sum of squares: value = sqrt(value_1**2, value_2**2)
    # size of image1 and image2 MUST be the same
    
    x_pixels, y_pixels, num_channels = image1.array.shape # Get the parameters of the image

    new_img = Image(x_pixels, y_pixels, num_channels) # Create a blank image first
        
    for x in range(x_pixels):
        for y in range(y_pixels):
            for c in range(num_channels):
                new_img.array[x, y, c] = (image1.array[x, y, c] ** 2 + image2.array[x, y, c] ** 2) ** 0.5

    return new_img
    
if __name__ == '__main__':
    lake = Image(filename='lake.png')
    city = Image(filename='city.png')

    # adjust_brightness(lake, 2).write_image('brightened_lake.png')
    # adjust_contrast(lake, 2, 1).write_image('contrasted_lake.png')
    # blur(lake, 5).write_image('blurred_lake.png')
    # blur(city, 5).write_image('blurred_city.png')
    # apply_kernel(city, np.array([[1, 2, 1], [0, 0, 0], [-1, -2, -1]])).write_image('sobel_x_city.png')
    # apply_kernel(city, np.array([[1, 0, -1], [2, 0, -2], [1, 0, -1]])).write_image('sobel_y_city.png')

    sobel_x = apply_kernel(city, np.array([[1, 2, 1], [0, 0, 0], [-1, -2, -1]]))
    sobel_y = apply_kernel(city, np.array([[1, 0, -1], [2, 0, -2], [1, 0, -1]]))
    combine_images(sobel_x, sobel_y).write_image('combined_sobel_city.png') # Edge detection!
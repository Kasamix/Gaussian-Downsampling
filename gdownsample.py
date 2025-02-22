"""
Gaussian Downsampling of Images from CSV
"""

"""
This module provides functions to load an image from a CSV file, perform Gaussian downsampling,
and print the resulting downsampled image.
Functions:
----------
- load_image_from_csv(file_path):
    Loads an image from a CSV file and returns it as a 2D list of integers.
- gdownsample(input_image):
    Performs Gaussian downsampling on the input image by applying horizontal and vertical passes,
    followed by downsampling the array.
- horizontal_pass(array, array_width, height):
    Applies a horizontal Gaussian blur to the input array.
- vertical_pass(array, array_width, height):
    Applies a vertical Gaussian blur to the input array.
- downsample_array(arr):
    Downsamples the input array by sampling every other row and every third column.
Usage:
------
1. Load an image from a CSV file using `load_image_from_csv`.
2. Perform Gaussian downsampling using `gdownsample`.
3. Print the resulting downsampled image and its dimensions.
Example:
--------
"""
import csv

def load_image_from_csv(file_path):
    with open(file_path, mode='r') as file:
        reader = csv.reader(file)
        image = [list(map(int, row)) for row in reader]
    return image

def gdownsample(input_image):

    # Placeholder implementation
    array_width = len(input_image[0])
    width = array_width//3
    height = len(input_image)

    blurred_horizontal = horizontal_pass(input_image, array_width, height)
    blurred = vertical_pass(blurred_horizontal, array_width, height)
    return downsample(blurred)
    
def horizontal_pass(array, array_width, height):
    new_array = [row[:] for row in array]  # Create a copy of the array
    for i in range(height):
        for j in range(9, array_width - 9):

            blurred_pixel = (array[i][j] * 6 +
                             array[i][j-3] * 4 +
                             array[i][j+3] * 4 +
                             array[i][j-6] * 1 +
                             array[i][j+6] * 1) // 16
            
            print(f"Row: {i:<3} Column: {j:<3} Value: {array[i][j]:<3} Blurred: {blurred_pixel:<3} Horizontal | Neighbors: {array[i][j-6]:<3} {array[i][j-3]:<3} {array[i][j]:<3} {array[i][j+3]:<3} {array[i][j+6]:<3}")

            new_array[i][j] = blurred_pixel

    return new_array
            

def vertical_pass(array, array_width, height):
    new_array = [row[:] for row in array]
    for i in range(array_width):
        for j in range(3, height - 3):
            blurred_pixel = (array[j][i] * 6 +
                             array[j-1][i] * 4 +
                             array[j+1][i] * 4 +
                             array[j-2][i] * 1 +
                             array[j+2][i] * 1) // 16
            
            print(f"Row: {j:<3} Column: {i:<3} Value: {array[j][i]:<3} Blurred: {blurred_pixel:<3} Vertical | Neighbors: {array[j-2][i]:<3} {array[j-1][i]:<3} {array[j][i]:<3} {array[j+1][i]:<3} {array[j+2][i]:<3}")
            
            new_array[j][i] = blurred_pixel

    return new_array
    
def downsample(arr):
    result = []
    for i in range(0, len(arr), 2):  # Sample every other row
        sampled_row = []
        for j in range(0, len(arr[i]), 6):  # Sample 3, skip 3
            sampled_row.extend(arr[i][j:j+3])
        result.append(sampled_row)
    return result
   
if __name__ == "__main__":
    input_image = load_image_from_csv('input_image.csv')
    output_image = gdownsample(input_image)

    print("=============================================")
    print("Output image:")
    for row in output_image:
        print(row)

    input_width = len(input_image[0])
    input_height = len(input_image)
    output_width = len(output_image[0])
    output_height = len(output_image)

    print("=============================================")
    print(f"Input Image - Width: {input_width}, Height: {input_height}")
    print(f"Output Image - Width: {output_width}, Height: {output_height}")


import cv2
import numpy as np
import os
from scipy.spatial.distance import cosine
from itertools import combinations

def extract_color_histogram(image_path):
    image = cv2.imread(image_path)
    histogram = cv2.calcHist([image], [0, 1, 2], None, [8, 8, 8], [0, 256, 0, 256, 0, 256])
    cv2.normalize(histogram, histogram)
    return histogram.flatten()

def compare_histograms(hist1, hist2):
    return cosine(hist1, hist2)

# Specify the folder path
folder_path = 'path/to/your/image/folder'

# Retrieve and filter image files
image_extensions = ['.jpg', '.jpeg', '.png', '.bmp']
image_paths = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if os.path.splitext(f)[1].lower() in image_extensions]

# Extract histograms
histograms = [extract_color_histogram(path) for path in image_paths]

# Compare each pair of images
pairs = combinations(range(len(histograms)), 2)
similarities = {pair: compare_histograms(histograms[pair[0]], histograms[pair[1]]) for pair in pairs}

# Find the most similar pair
most_similar_pair = min(similarities, key=similarities.get)
print(f"The most similar images are: {image_paths[most_similar_pair[0]]} and {image_paths[most_similar_pair[1]]} with a similarity score of {similarities[most_similar_pair]}")
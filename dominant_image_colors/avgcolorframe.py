import cv2
import numpy as np
from sklearn.cluster import KMeans

# Cluster analysis: grouping a set of objects that are more similar to one
# k-means clustering: partition the n observations into k clusters where each observation belongs
# to a cluster with the nearest mean

def visualize_colors(cluster, centroids):
    ### Get the number of different clusters, create histogram, and normalize

    # get a range of values within an interval (np.arange)
    # get sorted array of unique elements (np.unique) -> +1 because len doesn't include last number
    labels = np.arange(0, len(np.unique(cluster.labels_)) + 1) # gets an array of numbers
    (hist, _) = np.histogram(cluster.labels_, bins = labels) # returns values of histogram
    hist = hist.astype("float")
    hist /= hist.sum()

    # Create frequency rect and iterate through each cluster's color and percentage
    rect = np.zeros((50, 300, 3), dtype=np.uint8)
    colors = sorted([(percent, color) for (percent, color) in zip(hist, centroids)])
    start = 0
    for (percent, color) in colors:
        print(color, "{:0.2f}%".format(percent * 100))
        end = start + (percent * 300)
        cv2.rectangle(rect, (int(start), 0), (int(end), 50), \
                      color.astype("uint8").tolist(), -1)
        start = end
    return rect

# Load image and convert to a list of pixels
image = cv2.imread('1917snip.jpg')
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB) # convert from BGR colorspace to RGB colorspace
reshape = image.reshape((image.shape[0] * image.shape[1], 3)) # size, channels for reshape

# Find and display most dominant colors
cluster = KMeans(n_clusters=5).fit(reshape)
visualize = visualize_colors(cluster, cluster.cluster_centers_)
visualize = cv2.cvtColor(visualize, cv2.COLOR_RGB2BGR)
cv2.imshow('visualize', visualize)
cv2.waitKey()


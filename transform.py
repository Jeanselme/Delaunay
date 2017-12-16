import sys
import numpy as np
import scipy.misc
from scipy.spatial import Delaunay

def centroid(listPixel, dim):
	"""
		Computes the centroid of the given points given as [r, g, b]
	"""
	center = np.zeros(dim)
	for pixel in listPixel:
		center = np.add(center, pixel/len(listPixel))
	return center

def randomPoints(image, k):
	"""
		Creates k+16 "randomPoints" contained in the image
	"""
	randis = np.random.randint(low = 0, high = image.shape[0], size = k)
	randjs = np.random.randint(low = 0, high = image.shape[1], size = k)
	points = [[i,j] for i, j in zip(randis, randjs)]

	# For aesthetic - Not totally random : + 16
	points +=  [[0, 0], [0, image.shape[1]], [image.shape[0], 0], [image.shape[0], image.shape[1]]]
	points +=  [[0, j] for j in np.random.randint(low = 0, high = image.shape[1], size = 3)]
	points +=  [[i, 0] for i in np.random.randint(low = 0, high = image.shape[0], size = 3)]
	points +=  [[image.shape[0], j] for j in np.random.randint(low = 0, high = image.shape[1], size = 3)]
	points +=  [[i, image.shape[1]] for i in np.random.randint(low = 0, high = image.shape[0], size = 3)]
	
	return points

def delaunayTransform(image, points):
	"""
	Computes the SLIC algorithm on an image with k**2 superpixels
	"""
	# Computes triangulation
	triangulation = Delaunay(points)

	# Assign each pixel to the triangle
	pixelTriangle = np.zeros((image.shape[0], image.shape[1]))
	assignements = {key: [] for key in range(-1, len(triangulation.simplices))}

	for i in range(image.shape[0]):
		for j in range(image.shape[1]):
			pixel = image[i][j]
			pixelTriangle[i, j] = triangulation.find_simplex((i,j))
			assignements[pixelTriangle[i, j]].append(pixel)

	# Computes color
	centroids = {}
	for key in assignements:
		centroids[key] = centroid(assignements[key],image.shape[2])

	# Result image
	res = np.zeros(image.shape)
	for i in range(image.shape[0]):
		for j in range(image.shape[1]):
			res[i, j] = centroids[pixelTriangle[i, j]]

	return res

def help():
	print("python3.5 delaunay.py FileName.png -k int [-o resultFileName]")
	quit()

def main():
	arg = sys.argv
	if len(arg) < 4:
		help()
	elif ".png" in arg[1] or ".jpg" in arg[1] :
		fileName = arg[1]
		output = ""
		i = 2
		# Parse the command line
		while i+1 < len(arg):
			if arg[i] == "-k":
				k = int(arg[i+1])
				i+=2
			elif arg[i] == "-o":
				output = arg[i+1]
				i+=2
			else :
				help()

		if (k <= 0):
			help()
		else:
			image = scipy.misc.imread(fileName)
			points = randomPoints(image, k)
			res = delaunayTransform(image, points)
			scipy.misc.imshow(res)
			if (output != ""):
				scipy.misc.imsave(output, res)
	else:
		help()

if __name__ == '__main__':
	main()
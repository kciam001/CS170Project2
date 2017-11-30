import math
import struct
import numpy as np
import random





								#data, currentSet, featureToAdd
def leaveOneOutCrossValidation(data, currentSet, featureToAdd):
	

	myFeatures = currentSet.copy()
	myFeatures.append(featureToAdd)

	numPoints = data.shape[0]
	#iterate through all points

	#for i in range(0, numPoints):
	nearestNeighbor(data, data[0], myFeatures, numPoints)

	return(random.randint(0, 101))



def euclideanDistance(point, neighbor):

	x = np.array(point)
	y = np.array(neighbor)

	return np.linalg.norm(x-y)


#returns class that it guesses the points
def nearestNeighbor(data, point, features, numPoints):
	pointFeatures = []
	neighbors = []


	for j in features:
		pointFeatures.append(point[j])

	#iterate through every point finding neighbors
	for i in range(0, numPoints):

		neighborFeatures = []
		if not np.array_equal(data[i], point):
			for j in features:
				neighborFeatures.append(data[i][j])


			#now calculate distance
			dist = euclideanDistance(pointFeatures, neighborFeatures)

			neighbor = [data[i][0], dist]

			neighbors.append(neighbor)

	theNearestNeighbor = min(neighbors, key = lambda item: item[1])
	prediction = theNearestNeighbor[0]
	
	return prediction









			# print("point features")
			# print(pointFeatures)
			# print("neighborFeatures")
			# print(neighborFeatures)









	#x = np.array()
	#print(features)


def forwardSelection(data):
	#get number of columns in data

	numOfFeatures = 3 #data.shape[1]

	#tracks current features in the set
	currentFeatures = []
	#stores the highest accuracy
	maxAccuracy = 0
	#stores the set with the highest accuracy
	bestSet = []
	

	#outer loop, iterate for each level of the search tree
	for i in range(1, numOfFeatures):
		print("On the " + str(i) + "th level of the search tree:\n ")
		#tracks the accuracy along with the feature that gave that accuracy
		accuracyList = []
		#inner loop, iterate for every feature
		for j in range(1, numOfFeatures):
			#if we havent added this feature yet
			if j not in currentFeatures:
				#get the accuracy if we add this feature to the current features
				accuracy = leaveOneOutCrossValidation(data, currentFeatures, j)
				#add it to a list
				accuracyList.append((j,accuracy))

				print("Consider adding the " + str(j) + " feature")
				
				print("Using previous feature(s) ", end ='')
				print(currentFeatures, end ='')
				print(" and the new feature " + str(j), end ='')
				print(" the accuracy is " + str(accuracy) + "%\n")

		#get the feature that improved the accuracy the most
		if len(accuracyList) != 0:
			mostAccurate = max(accuracyList, key = lambda item: item[1])
		
		####if mostAccurate[0] not in currentFeatures:
		#add that feature to our set of current features

		currentFeatures.append(mostAccurate[0])
		currentFeatures.sort()

		print ("On level " + str(i) + " I added feature "  + str(currentFeatures[-1]) + " to the current set: ", end='')
		print(currentFeatures)
		print ("----------------------------------------------------------------------------------")

		#update max accuracy
		if maxAccuracy < mostAccurate[1]:
			maxAccuracy = mostAccurate[1]
			bestSet = currentFeatures.copy()

	print("The feature set with the highest accuracy is ", end ='')
	print(bestSet, end = '')
	print(" with an accuracy of " + str(maxAccuracy) + "%")






def main():


	smallDataName = 'CS170Smalltestdata__68.txt'
	smallData = np.genfromtxt(smallDataName)

	bigDataName = 'CS170BIGtestdata__29.txt'
	bigData = np.genfromtxt(bigDataName)
	

	numOfInstances, numOfFeatures = smallData.shape
	numOfFeatures -= 1 #one column is the class attribute

	print("This dataset has " + str(numOfFeatures) + 
	" features (not including the class attirubute), with " 
	+ str(numOfInstances) + " instances.\n")


	
	#leaveOneOutCrossValidation(smallData,0,0)
	forwardSelection(smallData)
	#forwardSelection(bigData)





if __name__ == "__main__":
	main()
import math
import struct
import numpy as np
import random

								#data, currentSet, featureToAdd
def leaveOneOutCrossValidation(data, currentSet, featureToAdd):
	
	index = featureToAdd-1
	myData = data
	myCurrentSet = currentSet
	myFeatureToAdd = featureToAdd
	return(random.randint(0, 101))


def featureSearch(data):
	numOfInstances, numOfFeatures = data.shape

	currentFeatures = []
	accuracyList = []
	maxAccuracy = 0
	bestSet = []
	


	for i in range(1, numOfFeatures):
		print("On the " + str(i) + "th level of the search tree:\n ")
		accuracyList = []
		for j in range(1, numOfFeatures):
			

			if j not in currentFeatures:
				accuracy = leaveOneOutCrossValidation(data, currentFeatures, j)
				accuracyList.append((j,accuracy))

				print("Consider adding the " + str(j) + " feature")
				
				print("Using previous feature(s) ", end ='')
				print(currentFeatures, end ='')
				print(" and the new feature " + str(j), end ='')
				print(" the accuracy is " + str(accuracy) + "%\n")

		mostAccurate = max(accuracyList, key = lambda item: item[1])
		if mostAccurate[0] not in currentFeatures:
			currentFeatures.append(mostAccurate[0])
			currentFeatures.sort()

			print ("On level " + str(i) + " I added feature "  + str(currentFeatures[-1]) + " to the current set: ", end='')
			print(currentFeatures)
			print ("----------------------------------------------------------------------------------")

		if maxAccuracy < mostAccurate[1]:
			maxAccuracy = mostAccurate[1]
			bestSet = currentFeatures.copy()

	print("The feature set with the highest accuracy is ", end ='')
	print(bestSet, end = '')
	print(" with an accuracy of " + str(maxAccuracy) + "%")






def main():


	smallDataName = 'CS170Smalltestdata__68.txt'
	smallData = np.genfromtxt(smallDataName)
	

	numOfInstances, numOfFeatures = smallData.shape
	numOfFeatures -= 1 #one column is the class attribute

	print("This dataset has " + str(numOfFeatures) + 
	" features (not including the class attirubute), with " 
	+ str(numOfInstances) + " instances.\n")


	featureSearch(smallData)





if __name__ == "__main__":
	main()
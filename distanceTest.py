import math
import struct
import numpy as np
import random


def main():


	a = np.array((1,2,3,10,20))
	b = np.array((4,5,6,-5,3))

	dist = np.linalg.norm(a-b)

	print(dist)





if __name__ == "__main__":
	main()
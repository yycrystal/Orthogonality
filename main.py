import random
import math
LOWER = -1
UPPER = 1

#START OF Vector class
class Vector:
    def __init__(self, values):
        self.__values = values
        self.__dim = len(values)
    

    def __mul__(self, other):
        """
        Multiplies itself by another vector;
        Providing that both have same dimension;
        Returns new vector object of the result

        Args:
            self (Vector) : own vector object
            other (Vector) : other vector object

        Returns:
            spare_vector (Vector): new vector object representing result
        """
        if type(self) == Vector: #type(other)?
            spare_vector = []
            if self.__dim == other.getDimension():
                for i in range(self.__dim):
                    summation = self.__values[i] * other.getValues()[i]
                    spare_vector.append(summation)
            #if dimensions are not the same then...
                    
            return Vector(spare_vector)

    def getValues(self):
        return(self.__values)
    
    def getDimension(self):
        return(self.__dim)

    def getMagnitude(self):
        """
        Gets magnitude of own vector

        Args:
            self (Vector) : own vector object

        Returns:
            summation (float) : magnitude of the vector
        """
        summation = 0
        for i in self.__values:
            summation += i**2
            
        summation = math.sqrt(summation)
        return summation


    def getSumOf(self):
        """
        Gets sum of all values in the vector

        Args:
            self (Vector) : own vector object

        Returns:
            summation (float) : sum of the vector
        """
        summation = 0
        for i in self.__values:
            summation += i
        return summation

    def getInnerProduct(self, other):
        """
        Gets inner product of itself and some other vector

        Args:
            self (Vector) : own vector object
            other (Vector) : other vector object

        Returns:
            (float) inner product
        """
        vector3 = self * other      #Gets dot product
        return vector3.getSumOf()   #Sum of dot product
#END OF Vector class


def randomVectors(number, dimension):
    """
    Generates a list of n random vectors with dimension d. The range of values generated are (-1,1).

    Args:
        number (int) : number of vectors generated
        dimension (int) : dimension of each vector

    Returns:
        vectors (List[Vector]) : list containing the randomly generated vectors
    """
    vectors = []
    for j in range(number):
        addedVector = []
        for i in range(dimension):
            addedVector.append(random.uniform(LOWER, UPPER))
        vectors.append(Vector(addedVector))
    return vectors


def __main__(n=0,d=0):
    sumIPlist = []
    sumIP = 0
    if (n, d) == (0, 0):
        n, d = int(input('Number of vectors: ')), int(input('Dimension: '))
    vectors = randomVectors(n, d)
    
    for i in range(n):
        for j in range(i, n):
            if i != j:
                sumIP += vectors[i].getInnerProduct(vectors[j])
                print(f'<x{i},x{j}> = {vectors[i].getInnerProduct(vectors[j])}')
                
    sumIPlist.append(sumIP)
    #print(f'Inner product sum: {sumIP}')
    return sumIP


__main__()
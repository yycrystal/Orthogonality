import random
import math
LOWER = -1
UPPER = 1

class Vector:
    def __init__(self, values):
        self.values = values
        self.dim = len(values)
        
    def __mul__(self, other):
        if type(self) == Vector:
            spare_vector = []
            if self.dim == other.dim:
                for i in range(self.dim):
                    summation = self.values[i] * other.values[i]
                    spare_vector.append(summation)
                    
            return Vector(spare_vector)
        
    def magnitude(self):
        summation = 0
        for i in self.values:
            summation += i**2
            
        summation = math.sqrt(summation)
        return summation

    def sumOf(self):
        summation = 0
        for i in self.values:
            summation += i
        return summation

    def innerProduct(self, other):
        vector3 = self * other
        return vector3.sumOf()


def randomVector(number, dimension):
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
    vectors = randomVector(n, d)
    
    for i in range(n):
        for j in range(i, n):
            if i != j:
                sumIP += vectors[i].innerProduct(vectors[j])
                print(f'<x{i},x{j}> = {vectors[i].innerProduct(vectors[j])}')
                
    sumIPlist.append(sumIP)
    #print(f'Inner product sum: {sumIP}')
    return sumIP

__main__()
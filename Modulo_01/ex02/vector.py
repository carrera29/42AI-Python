import importlib
import vector

class Vector:
    def __init__(self, elements):
        if not isinstance(elements, list):
            print ("is not a list")
        else:
            if len(elements) is 1:
                self.size = len(elements[0])
                self.shape = (1, self.size)
                self.type = "fila"
            elif len(elements) > 1:
                self.size = len(elements)
                self.shape = (self.size, 1)
                self.type = "colum"
            else:
                print ("error")
            self.values = []
            for i in elements:
                self.values.append(i)
        
    def __str__(self):
        return f""" 
        Vector type:    {self.type}
        Shape:          {self.shape}
        Values:         {self.values}\n"""

    def doc(v1, v2):
        if v1.shape == v2.shape:
            res = 0
            for i in range(v1.shape[0]):
                for j in range(v1.shape[1]):
                    res += v1.values[i][j] * v2.values[i][j]
            return res
        else: 
            print ("vectors have different shape")
    
    def __add__(v1, v2):
        if v1.shape == v2.shape:
            result = [[0] * v1.shape[1] for _ in range(v1.shape[0])]
            for i in range(v1.shape[0]):
                for j in range(v1.shape[1]):
                    result[i][j] = v1.values[i][j] + v2.values[i][j]
            return Vector(result)
        else: 
            print ("vectors have different shape")

    def __rmul__(v1, e):
            result = [[0] * v1.shape[1] for _ in range(v1.shape[0])]
            for i in range(v1.shape[0]):
                for j in range(v1.shape[1]):
                    result[i][j] = v1.values[i][j] * e
            return Vector(result)

    def T(v1):
        result = []
        for i in range(v1.shape[1]):
            temp = []
            for j in range(v1.shape[0]):
                temp.append(v1.values[j][i])
            result.append(temp)
        return Vector(result)

importlib.reload(vector)
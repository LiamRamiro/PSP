from random import randint

class Matriz:
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.matrix = [[randint(0, 9) for _ in range(columns)] for _ in range(rows)]

    def get_number_rows(self):
        return self.rows

    def get_number_columns(self):
        return self.columns

    def set_element(self, x, y, element):
        if 0 <= x < self.rows and 0 <= y < self.columns:
            self.matrix[x][y] = element
        else:
            print("Índices fuera de rango")

    def add_matrix(self, other_matrix):
        if self.get_number_rows() == other_matrix.get_number_rows() and self.get_number_columns() == other_matrix.get_number_columns():
            for i in range(self.get_number_rows()):
                for j in range(self.get_number_columns()):
                    self.set_element(i, j, self.matrix[i][j] + other_matrix[i, j])
        else:
            print("No se pueden sumar matrices que no son del mismo tamaño")

    def mult_matrix(self, matrix):
        if self.get_number_columns() == matrix.get_number_rows():
            result = [[0 for _ in range(matrix.get_number_columns())] for _ in range(self.get_number_rows())]
            for i in range(self.get_number_rows()):
                for j in range(matrix.get_number_columns()):
                    sum = 0
                    for k in range(self.get_number_columns()):
                        sum += self.matrix[i][k] * matrix[k, j]  # Utilizar __getitem__
                    result[i][j] = sum
            self.matrix = result
            self.columns = matrix.get_number_columns()
        else:
            print("No se pueden multiplicar matrices con dimensiones incompatibles")

    def __getitem__(self, index):
        return self.matrix[index[0]][index[1]]

matriz1 = Matriz(3, 3)
matriz2 = Matriz(4, 2)
matriz3 = Matriz(3, 2)
matriz4 = Matriz(3, 3)
print('matriz1', matriz1.matrix)
print('matriz2', matriz2.matrix)
print('matriz3', matriz3.matrix)
print('matriz4', matriz4.matrix)
matriz1.add_matrix(matriz2)
print('matriz1.add2',matriz1.matrix)
matriz1.add_matrix(matriz3)
print('matriz1.add3',matriz1.matrix)
matriz1.add_matrix(matriz4)
print('matriz1.add4',matriz1.matrix)
matriz1.mult_matrix(matriz2)
print('matriz1.multi2',matriz1.matrix)
matriz1.mult_matrix(matriz3)
print('matriz1.multi3',matriz1.matrix)
matriz1.mult_matrix(matriz4)
print('matriz1.multi4',matriz1.matrix)
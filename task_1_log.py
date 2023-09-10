#Создайте класс Матрица. 
#Добавьте методы для: вывода на печать, сравнения, сложения, *умножения матриц

import logging

logging.basicConfig(filename= 'logger_matrix.log', encoding= 'utf-8', level= logging.INFO, filemode= 'w')
logger = logging.getLogger(__name__)



class Matrix:  
    def __init__(self, rows: int, columns: int):  
        self.rows = rows  
        self.columns = columns  
        self.value = [[0 for _ in range(columns)] for _ in range(rows)] 
    
    def comparison_size(self, other): 
        """checking matrices by size""" 
        if self.rows != other.rows or self.columns != other.columns:
            logger.error(f'Матрицы разные по размеру, математические действия с ними не возможны')
            raise Exception
        return logger.info('Матрицы одинаковые по размеру, операции сложения и умножения матриц возможны')          
        
        # if self.rows != other.rows or self.columns != other.columns:
        #     raise Exception('Матрицы разные по размеру, математические действия с ними не возможны')  
        # return ('Матрицы одинаковые по размеру, операции сложения и умножения матриц возможны')      
    
    def comparison_el(self, other):  
        """checking matrices by element values"""  
         
        for i in range(self.rows):  
            for j in range(self.columns):  
                if self.value[i][j] != other.value[i][j]:
                    return logger.info('Значения элементов матриц разные')
                else:
                    return logger.info('Значения элементов матриц одинаковые')  
            
   
    def add(self, other):
        """addition of matrix elements"""  
        result_matrix = Matrix(self.rows, self.columns)  
        for i in range(self.rows):  
            for j in range(self.columns):  
                result_matrix.value[i][j] = self.value[i][j] + other.value[i][j] 
        logger.info(f'Результат сложения двух матриц \n{mat1} и \n{mat2} равен \n{result_matrix}') 
        return result_matrix  
    
   
    
    def multiplication(self, other): 
        """multiplication of matrix elements""" 
        result_matrix = Matrix(self.rows, other.columns)  
        for i in range(self.rows):  
            for j in range(other.columns):  
                for k in range(self.columns):  
                    result_matrix.value[i][j] += self.value[i][k] * other.value[k][j] 
        logger.info(f'Результат умножения двух матриц \n{mat1} и \n{mat2} равен \n{result_matrix}')             
        return result_matrix  
          
    def __str__(self): 
        """user-readable representation method""" 
        output = ""  
        for row in self.value:  
            output += "\t".join(str(element) for element in row)  
            output += "\n"  
        return output  

# Создание экземпляров класса Matrix  

# mat1 = Matrix(3, 3)
# mat1.value = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]  
# mat1.value = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
mat1 = Matrix(2, 3)
mat1.value = [[9, 8, 7], [6, 5, 4]]
#print(f'Матрица 1: {mat1.value}')
mat2 = Matrix(3, 3)
mat2.value = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]  
# print(f'Матрица 2: {mat2.value}')
# print()
print(f'Сравнение размеров двух матриц: {mat1.comparison_size(mat2)}\n')
print(f'Сравнение значений элементов двух матриц: {mat1.comparison_el(mat2)}\n')
print(f'Сложение матриц: \n{mat1.add(mat2)}') 
print(f'Умножение матриц: \n{mat1.multiplication(mat2)}')
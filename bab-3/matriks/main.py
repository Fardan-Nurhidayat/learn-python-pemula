matriks = [
    [
        1 , 2  , 4 , 5 , 6
    ]
]

matriks_2 = [
    [1 , 2 ,3],
    [4 , 5 ,6],
    [7 , 8 ,9]
]

print(matriks_2)

print(matriks)

# Membuat matriks 2x2
var_mat = [[5, 0],
          [1, -2]]
def_mat = [[0 for j in range(2)] for i in range(2)]

for i in range(len(var_mat)):
  for j in range(len(var_mat[0])):
    def_mat[i][j] = var_mat[i][j]*2

print(def_mat)
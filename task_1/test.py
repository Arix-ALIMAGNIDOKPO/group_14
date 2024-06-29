from numpy import Matrice

# Test complet

# Création de matrices 1D et 2D
mat1d = Matrice([1, 2, 3, 4, 5])
mat2d = Matrice([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Affichage des matrices
print("Matrice 1D:", mat1d)
print("Matrice 2D:", mat2d)

# Test de l'addition
print("Addition 1D:", mat1d + Matrice([5, 4, 3, 2, 1]))
print("Addition 2D:", mat2d + Matrice([[9, 8, 7], [6, 5, 4], [3, 2, 1]]))
print("Addition 1D avec un scalaire:", mat1d + 2)
print("Addition 2D avec un scalaire:", mat2d + 1)

# Test de la soustraction
print("Soustraction 1D:", mat1d - Matrice([5, 4, 3, 2, 1]))
print("Soustraction 2D:", mat2d - Matrice([[9, 8, 7], [6, 5, 4], [3, 2, 1]]))
print("Soustraction 1D avec un scalaire:", mat1d - 2)
print("Soustraction 2D avec un scalaire:", mat2d - 1)

# Test de la multiplication
print("Multiplication 1D:", mat1d * Matrice([5, 4, 3, 2, 1]))
print("Multiplication 2D:", mat2d * Matrice([[9, 8, 7], [6, 5, 4], [3, 2, 1]]))
print("Multiplication 1D avec un scalaire:", mat1d * 2)
print("Multiplication 2D avec un scalaire:", mat2d * 2)

# Test de la division
print("Division 1D:", mat1d / Matrice([5, 4, 3, 2, 1]))
print("Division 2D:", mat2d / Matrice([[9, 8, 7], [6, 5, 4], [3, 2, 1]]))
print("Division 1D avec un scalaire:", mat1d / 2)
print("Division 2D avec un scalaire:", mat2d / 2)

# Test de la multiplication avec un scalaire (@)
print("Multiplication 1D avec un scalaire (@):", mat1d @ 2)
print("Multiplication 2D avec un scalaire (@):", mat2d @ 2)

# Test de la recherche d'un élément
print("Recherche d'élément 1D (3):", 3 in mat1d)
print("Recherche d'élément 2D (5):", 5 in mat2d)

# Test de l'indexage
print("Indexage 1D (2ème élément):", mat1d[1])
print("Indexage 2D (2ème ligne, 3ème colonne):", mat2d[1, 2])

# Test du slicing
print("Slicing 1D (2ème au 4ème éléments):", mat1d[1:4])
print("Slicing 2D (1ère et 2ème lignes):", mat2d[0:2])
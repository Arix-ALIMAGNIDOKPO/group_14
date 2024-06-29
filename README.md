## Tache 1 : Implémentation d'un sous-ensemble de NumPy en Python pur

Ce repository contient une implémentation d'une classe `Matrice` en Python pur, qui offre des fonctionnalités similaires à la bibliothèque NumPy, sans dépendre de bibliothèques externes.

La classe `Matrice` permet de créer des tableaux 1D et 2D et de réaliser des opérations de base telles que :

- **Création de tableaux** à partir de listes Python.
- **Opérations éléments par éléments** : addition (+), soustraction (-), multiplication (\*), division (/).
- **Multiplication avec un scalaire** avec l'opérateur '@'.
- **Recherche d'éléments** avec l'opérateur 'in'.
- **Indexage et Slicing** comme dans NumPy.

## Installation

Vous pouvez installer le package Python `matrice-ifri` via pip :

````bash
pip install matrice-ifri
```
## Utilisation

```python
from matrice_ifri import Matrice

# Créer un tableau 1D
array1d = Matrice([1, 2, 3, 4, 5])

# Créer un tableau 2D
array2d = Matrice([[1, 2], [3, 4]])

# Opérations de base
print(array1d + Matrice([5, 4, 3, 2, 1]))  # Addition
print(array1d * 2)  # Multiplication par un scalaire
print(array1d @ 2)  # Multiplication avec un scalaire (@)
print(5 in array1d)  # Recherche d'élément
print(array2d[0, 1])  # Indexage
print(array1d[1:4])  # Slicing

```

## Code source

Le code source de la classe `Matrice` est disponible dans le fichier `numpy.py` du dossier `task_1`.

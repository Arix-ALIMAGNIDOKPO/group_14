library(dplyr)
library(ggplot2)

#charger le dataset
data <- read_csv("Housing.csv")

# Afficher les premières lignes
head(data)

# Vérifier les types de données et les valeurs manquantes
str(data)
sum(is.na(data))
sum(duplicated(data))

# Statistiques descriptives

# Statistiques descriptives pour les variables numériques
summary(data %>% select_if(is.numeric))

# Statistiques descriptives pour les variables catégorielles
summary(data %>% select_if(is.character))


#Visualisation 

# Histogramme du nombre de chambres
ggplot(data, aes(x = bedrooms)) +
  geom_histogram(binwidth = 1, fill = "skyblue", color = "black") +
  labs(title = "Distribution du nombre de chambres", x = "Nombre de chambres", y = "Fréquence")

# Graphique de dispersion : Prix en fonction de la surface
ggplot(data, aes(x = area, y = price)) +
  geom_point(color = "blue") +
  geom_smooth(method = "lm", se = FALSE, color = "red") +
  labs(title = "Prix en fonction de la surface", x = "Surface (pi²)", y = "Prix")


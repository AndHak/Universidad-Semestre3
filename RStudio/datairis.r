# Cargar y dejar disponibles los datos llamados iris
data(iris)
print(head(iris)) # Visualizar las primeras filas para confirmar la carga

# Descripción de los datos y significado de cada variable
# Este comando abrirá la ayuda donde se describe el dataset Iris en detalle
?iris

# Clasificación de variables - ver estructura del dataset
str(iris)

# Análisis unidimensional de cada variable
# Esto proporcionará estadísticas descriptivas básicas para cada variable
summary(iris)

# Análisis bidimensional para establecer relaciones entre las variables
# Generando una matriz de scatterplots para visualizar relaciones potenciales
pairs(iris[1:4], main = "Matrix de Dispersión para Iris", pch = 21, bg = c("#1b9e77", "#d95f02", "#7570b3")[unclass(iris$Species)])

# Mejorando el gráfico de dispersión con ggplot2
library(ggplot2)
ggplot(iris, aes(x = Sepal.Length, y = Sepal.Width, color = Species)) + 
  geom_point(alpha = 0.5, size = 3) +  # Ajustando transparencia y tamaño del punto
  labs(title = "Relación entre Sepal Length y Sepal Width por Especie de Iris",
       x = "Longitud del Sépalo (cm)", 
       y = "Ancho del Sépalo (cm)") + 
  theme_minimal() + # Usando un tema minimalista
  scale_color_manual(values = c("setosa" = "#1b9e77", "versicolor" = "#d95f02", "virginica" = "#7570b3")) # Colores personalizados por especie

#Desarrollado por Yenny Marcela Guerra
#Universidad de Nariño 2024

#Instalamos la libreria ggplot2 y la llamamos
install.packages("ggplot2")
library(ggplot2)

##################### Punto 1: Importacion de datos #####################
#Cargamos los datos con read table que nos entrega un data frame que nos servira para analizar los datos
datos_ratones <- read.table("C:/Programacion Universidad/Semestre 3/RStudio/Ratones.txt", header = TRUE, quote="\"")
#Verificamos que los datos se esten cargando correctamente
datos_ratones
head(datos_ratones)
attach(datos_ratones)

#################### Punto 2: Resumen y analisis unidimensional #####################
# Mostramos el resumen de cada una de las variables
summary(datos_ratones)

#Creamos un histograma para cada una de las las variables tratamiento, celulas, wbc, y rbc
hist(datos_ratones$trat, main = "Histograma de Tratamientos", xlab = "Número de tratamientos", ylab = "Frecuencia", col = "yellow")
hist(datos_ratones$celulas, main = "Histograma de Células", xlab = "Número de Células Cancerosas", ylab = "Frecuencia", col = "blue")
hist(datos_ratones$wbc, main = "Histograma de WBC (Células Blancas)", xlab = "Número de Células Blancas", ylab = "Frecuencia", col = "green")
hist(datos_ratones$rbc, main = "Histograma de RBC (Células Rojas)", xlab = "Número de Células Rojas", ylab = "Frecuencia", col = "red")


##################### Punto 3: Graficos bidimensionales #####################
#Relación entre células cancerosas y células blancas (WBC)
plot(datos_ratones$celulas, datos_ratones$wbc, main = "Relación entre Células Cancerígenas y WBC",
     xlab = "Células Cancerígenas", ylab = "WBC", pch = 19, col = "red")
cor_cel_wbc <- cor(datos_ratones$celulas, datos_ratones$wbc)

#Relación entre células cancerosas y células rojas (RBC)
plot(datos_ratones$celulas, datos_ratones$rbc, main = "Relación entre Células Cancerígenas y RBC",
     xlab = "Células Cancerígenas", ylab = "RBC", pch = 19, col = "blue")
cor_cel_rbc <- cor(datos_ratones$celulas, datos_ratones$rbc)

#Gráfico de cajas para visualizar la distribución de células por tratamiento
ggplot(datos_ratones, aes(x = as.factor(trat), y = celulas)) +
  geom_boxplot(color = "black", fill = "lightblue") + 
  labs(title = "Células cancerosas por tratamiento",
       x = "Tratamiento",
       y = "Número de células cancerosas")

##################### Punto 4: Gráficos con mas de dos variables #####################
#Gráfico de dispersión con facetas según tratamiento y color según RBC
ggplot(datos_ratones, aes(x = wbc, y = celulas, color = as.factor(rbc))) +
  geom_point() +
  facet_wrap(~ trat) +
  labs(title = "Relación de Células Cancerosas y Células Blancas", x = "WBC", y = "C élulas cancerígenas") +
  scale_color_discrete(name = "Número de células rojas")

#Gráfico de burbujas para células vs WBC, tamaño según RBC y color según tratamiento
ggplot(datos_ratones, aes(x = wbc, y = celulas, size = rbc, color = as.factor(trat))) +
  geom_point(alpha = 0.5) +
  labs(title = "Gráfico de Burbujas Células vs WBC", x = "WBC", y = "Células Cancerígenas", size = "RBC") +
  scale_color_discrete(name = "Tratamiento")

#Gráfico de líneas para el número de colonias de células vs WBC, coloreado por tratamiento 
ggplot(datos_ratones, aes(x = wbc, y = celulas, color = as.factor(trat), group = trat)) +
  geom_line() +
  geom_point() +
  labs(title = "Células cancerosas vs. Células blancas por tratamiento",
       x = "Células blancas (WBC)",
       y = "Células cancerosas",
       color = "Tratamiento")

##################### Punto 5: Análisis de promedios y gráfico de perfiles medios #####################
#Calculamos los promedios de colonias de celulas para cada tratamiento y cada tiempo
medias_celulas <- aggregate(celulas ~ trat + id, data = datos_ratones, mean)
#Convertimos id de tiempo en una variable cualitativa para que nos aparezca cada una de las id
medias_celulas$id <- factor(medias_celulas$id)
#Creamos un gráfico de líneas para mostrar los perfiles medios de células por tratamiento
ggplot(medias_celulas, aes(x = id, y = celulas, group = trat, color = as.factor(trat))) +
  geom_line() +
  geom_point() +
  labs(title = "Perfiles Medios de Células por Tratamiento", x = "Observación", y = "Número Medio de Células") +
  scale_color_discrete(name = "Tratamiento")

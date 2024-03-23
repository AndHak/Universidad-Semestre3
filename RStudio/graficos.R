set.seed(1998)
muestra <- sample(18:40, 1000, replace=TRUE)
muestra 
barplot(muestra)
hist(muestra, main = "Histograma para edades", xlab = "Categoria",
     ylab = "Valor", col = "lightblue")

muestra_1 <- sample(1:7,10, replace=TRUE)
barplot(muestra_1)
install.packages("ggplot2")
library(ggplot2)
datos_barras <- data.frame(
  categoria = c(17, 18, 19, 20, 22, 23, 24, 25, 26, 27),
  frecuencia = c(2, 4, 5, 4, 1, 5, 4, 5, 5, 5))
g1 <- ggplot(datos_barras, aes(x = categoria, y = frecuencia)) +
  geom_bar(stat = "identity", fill = "steelblue") + 
  labs(title = "Grafico de barras")

g1

g2 <- ggplot(datos_barras, aes(x = "", y = frecuencia, fill)) +
  geom_bar(stat = "identity") + coord_polar("y", start = 0) + labs(title = "Grafico de paste")

g2
boxplot(muestra)
table(muestra)

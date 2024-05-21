# Desarrollado por Yenny Marcela Guerra
# Universidad de Nariño 2024

# Cargar los paquetes necesarios
library(ggplot2)
library(knitr)
library(dplyr)

# Leer los datos desde el archivo
datos_vinos <- read.table("C:/Programacion Universidad/Semestre 3/RStudio/vinos.txt", header = TRUE, quote="\"")

# Renombrar las variables
names(datos_vinos) <- c("claridad", "aroma", "cuerpo", "sabor", "aromac", "calidad", "region")

# Mostrar el encabezado de los datos usando kable
kable(head(datos_vinos), caption = "Encabezado de los datos de vinos")

# Tablas de frecuencia unidimensionales
freq_region <- datos_vinos %>%
  count(region) %>%
  rename(Frecuencia = n)

freq_calidad <- datos_vinos %>%
  count(calidad) %>%
  rename(Frecuencia = n)

# Tablas de frecuencia bidimensionales
freq_region_calidad <- datos_vinos %>%
  count(region, calidad) %>%
  rename(Frecuencia = n)

# Mostrar tablas usando kable
kable(freq_region, caption = "Frecuencia de Región")
kable(freq_calidad, caption = "Frecuencia de Calidad")
kable(freq_region_calidad, caption = "Frecuencia de Región vs. Calidad")

# Gráficos asociados usando ggplot2

# Gráfico de barras para frecuencia de región
ggplot(freq_region, aes(x = factor(region), y = Frecuencia)) +
  geom_bar(stat = "identity", fill = "skyblue") +
  labs(title = "Frecuencia de Región", x = "Región", y = "Frecuencia")

# Gráfico de barras para frecuencia de calidad
ggplot(freq_calidad, aes(x = factor(calidad), y = Frecuencia)) +
  geom_bar(stat = "identity", fill = "lightblue") +
  labs(title = "Frecuencia de Calidad", x = "Calidad", y = "Frecuencia")

# Gráfico de barras para frecuencia de región vs. calidad
ggplot(freq_region_calidad, aes(x = factor(region), y = Frecuencia, fill = factor(calidad))) +
  geom_bar(stat = "identity", position = "dodge") +
  labs(title = "Frecuencia de Región vs. Calidad", x = "Región", y = "Frecuencia", fill = "Calidad") +
  scale_fill_brewer(palette = "Blues")

# Agrupar los datos por 'region' y calcular la media de 'calidad'
calidad_media_region <- datos_vinos %>%
  group_by(region) %>%
  summarise(calidad_media = mean(calidad, na.rm = TRUE))

# Mostrar la tabla de calidad media por región usando kable
kable(calidad_media_region, caption = "Calidad Media por Región")

# Gráfico de barras de la calidad media por región
ggplot(calidad_media_region, aes(x = factor(region), y = calidad_media)) +
  geom_bar(stat = "identity", fill = "skyblue") +
  labs(title = "Calidad Media por Región", x = "Región", y = "Calidad Media") +
  theme_minimal()

# Convertir claridad a factor
datos_vinos$claridad <- as.factor(datos_vinos$claridad)

# Calcular la calidad media agrupada por región y claridad
calidad_media_claridad_region <- datos_vinos %>%
  group_by(region, claridad) %>%
  summarise(calidad_media = mean(calidad, na.rm = TRUE))

# Mostrar la tabla usando kable
kable(calidad_media_claridad_region, caption = "Calidad Media por Claridad y Región")

# Gráfico de perfiles medios
ggplot(calidad_media_claridad_region, aes(x = claridad, y = calidad_media, color = factor(region), group = region)) +
  geom_line(size = 1) +
  geom_point(size = 2) +
  labs(title = "Calidad Media por Claridad y Región", x = "Claridad (como factor)", y = "Calidad Media") +
  scale_color_manual(values = c("red", "blue", "green"), name = "Región") +
  theme_minimal() +
  theme(legend.title = element_text(color = "blue"))

# Gráfico de dispersión para relacionar calidad, sabor y aroma
ggplot(datos_vinos, aes(x = sabor, y = calidad, color = aroma, size = aroma)) +
  geom_point(alpha = 0.7) +
  labs(title = "Relación entre Calidad, Sabor y Aroma", x = "Sabor", y = "Calidad") +
  theme_minimal() +
  scale_color_gradient(low = "yellow", high = "red")

# Conclusiones generales
conclusiones <- "
Las siguientes conclusiones se derivan del análisis de los datos de vinos:
1. La región con la mayor calidad media de vinos es la región X, mientras que la región Y tiene la menor calidad media.
2. Existe una variación notable en la calidad de los vinos dependiendo de la región y la claridad del vino.
3. La calidad del vino está positivamente correlacionada con el sabor y el aroma, como se muestra en el gráfico de dispersión.
4. Los vinos con mejor calidad tienden a tener altos valores en sabor y aroma.

Estas conclusiones pueden ayudar a identificar las características de los mejores y peores vinos y guiar futuras decisiones en la producción y selección de vinos.
"

cat(conclusiones)

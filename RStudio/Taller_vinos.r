# Desarrollado por Yenny Marcela Guerra
# Universidad de Nariño 2024

# Cargar los paquetes necesarios
library(ggplot2)
library(knitr)
library(dplyr)

# Leer los datos desde el archivo
vinos <- read.table("C:/Programacion Universidad/Semestre 3/RStudio/vinos.txt", header = TRUE, quote="\\")

# 1. Renombrar las variables
names(vinos) <- c("claridad", "aroma", "cuerpo", "sabor", "aromac", "calidad", "region")

# Mostrar el encabezado de los datos usando kable
kable(head(vinos), caption = "Encabezado de los datos de vinos")

# 2. Tablas de frecuencia unidimensionales y bidimensionales

# Tabla de frecuencia unidimensional para la variable calidad
tabla_calidad <- table(vinos$calidad)
kable(tabla_calidad, caption = "Tabla de frecuencia de la calidad del vino")

# Tabla de frecuencia bidimensional para las variables region y calidad
tabla_region_calidad <- table(vinos$region, vinos$calidad)

# Convertir la tabla a un data frame ordenado
df_tabla_region_calidad <- data.frame(tabla_region_calidad) %>%
  rename(Region = Var1, Calidad = Var2, Frecuencia = Freq) %>%
  arrange(desc(Frecuencia))

# Gráfico de barras para la tabla de frecuencia de calidad por región
ggplot(df_tabla_region_calidad, aes(x = Calidad, y = Frecuencia, fill = Region)) +
  geom_bar(stat = "identity") +
  labs(x = "Calidad", y = "Frecuencia", fill = "Región", title = "Distribución de la calidad del vino por región",
       subtitle = "Frecuencia de los vinos según su índice de calidad y región") +
  scale_fill_manual(values = c("#FFA07A", "#00FA9A", "#4169E1"), name = "Región",
                    labels = c("Región 1", "Región 2", "Región 3")) +
  theme(plot.title = element_text(hjust = 0.5, color = "#800080", family = "Arial", size = 20, face = "bold"),
        plot.subtitle = element_text(hjust = 0.5, family = "Arial", color = "#8B008B"))

# Tabla de frecuencia bidimensional para las variables region y calidad
tabla_region_calidad <- table(vinos$region, vinos$calidad)
kable(tabla_region_calidad, caption = "Tabla de frecuencia de la region y calidad del vino")

# Gráfico de barras apiladas para la tabla de frecuencia de "calidad" por región
data.frame(tabla_region_calidad) %>%
  ggplot(aes(x = Var1, y = Freq, fill = Var2)) +
  geom_bar(stat = "identity") +
  labs(x = "Region", y = "Frecuencia", fill = "Calidad", title = "Distribución de la calidad del vino por region",
       subtitle = "Grafico de barras que indica la frecuencia de la calidad por la region") +
  theme(plot.title = element_text(hjust = 0.5, color = "#006400", family = "Arial", size = 20, face = "bold"),
        plot.subtitle = element_text(hjust = 0.5, family = "Arial", color = "#556B2F"))

# Calidad media del vino por región
vinos %>%
  group_by(region) %>%
  summarise(calidad = mean(calidad)) %>%
  ggplot(aes(x = region, y = calidad)) +
  geom_bar(stat = "identity", fill = "#DC143C") +
  labs(x = "Region", y = "Calidad media", title = "Calidad media del vino por region") +
  theme(plot.title = element_text(hjust = 0.5, color = "#8B0000", family = "Arial", size = 20, face = "bold"),
        plot.subtitle = element_text(hjust = 0.5, family = "Arial", color = "#B22222"))

# Perfiles medios de calidad por claridad y región
vinos %>%
  ggplot(aes(x = factor(claridad), y = calidad, color = factor(region), group = factor(region))) +
  geom_line() +
  geom_point() +
  labs(x = "Claridad", y = "Calidad media", color = "Región", title = "Perfiles medios de calidad por claridad y región",
       subtitle = "Calidad media según la claridad del vino por cada región") +
  scale_color_manual(values = c("#4169E1", "#00FA9A", "#FFA07A"), name = "Región") +
  theme(plot.title = element_text(hjust = 0.5, color = "#00008B", family = "Arial", size = 20, face = "bold"),
        plot.subtitle = element_text(hjust = 0.5, family = "Arial", color = "#00688B"),
        legend.title = element_text(color = "blue"))

# Gráfico creativo para relacionar "calidad", "sabor" y "aroma"
vinos %>%
  ggplot(aes(x = sabor, y = calidad, color = factor(sabor), size = aroma, shape = factor(region))) +
  geom_point(alpha = 0.6) +
  labs(x = "Sabor", y = "Calidad", color = "Calidad", size = "Aroma", shape = "Region",
       title = "Relación entre calidad, sabor y aroma del vino") +
  theme_bw() +
  theme(plot.title = element_text(hjust = 0.5, color = "#8A2BE2", family = "Arial", size = 20, face = "bold")) +
  theme(axis.title.x = element_text(size = 13,
                                    color = "#DC143C",
                                    face = "italic"),
        axis.title.y = element_text(size = 13,
                                    color = "#DC143C",
                                    face = "italic")) 






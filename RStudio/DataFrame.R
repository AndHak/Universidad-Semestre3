series <- data.frame(
  nombre = c("Avatar", "Patos 2", "The office", "Los increibles", "Dumb 2"),
  imdb = c(10.0, 8.9, 7.5, 7.6, 9.6),
  duracion = c(120, 100, 90, 95, 130),
  concluida = c(FALSE,TRUE,TRUE,FALSE,FALSE)
)

write.csv(series,
          file = "C:/Programacion Universidad/Semestre 3/RStudio/Tabla_series.csv",
          row.names = FALSE)

series <- read.csv("C:/Programacion Universidad/Semestre 3/RStudio/Tabla_series.csv")

View(series)
nrow(series)
ncol(series)
str(series)
summary(series)

#Agregar nueva informacion
nueva_peli <- data.frame(nombre = "Sinse",
                         imdb = 9.4,
                         duracion = 100,
                         concluida = FALSE)
series <- rbind(series, nueva_peli)

#Extraer info
series[c(TRUE,FALSE,FALSE,FALSE,FALSE,TRUE),]
series[series$imdb >= 9,]
series[series$duracion <= 100,]



















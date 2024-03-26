#Histograma

videogames <- read.csv("C:\\Programacion Universidad\\Semestre 3\\RStudio\\all_games.csv")

hist(videogames$meta_score,
     #Ancho de la barra
     breaks = 40,
     
     #Color
     col = "blue",
     
     #Xlab para modificar el nombre del eje x
     xlab = "Meta score",
     
     #main nombre de la grafica
     main = "Histograma del metascore")






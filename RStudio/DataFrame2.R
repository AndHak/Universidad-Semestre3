videogames <- read.csv("C:\\Programacion Universidad\\Semestre 3\\RStudio\\all_games.csv")

nrow(videogames)
ncol(videogames)

View(head(videogames, 10)) 


str(videogames, strict.width = "cut")

#Valores faltantes
colSums(is.na(videogames))

#Cual es el juego con menor meta_score
which.min(videogames$meta_score)
View(videogames[18799, ])

which.max(videogames$meta_score)
View(videogames[1,])

#Juegos por cada plataforma
videogames$platform <- trimws(videogames$platform)
sort(table(videogames$platform), decreasing = TRUE)


#Cuantos juegos de PC tienen meta_score mayor a 100
nrow(videogames[videogames$platform == "PC"
                & videogames$meta_score > 90,])


#Cuantos juegos hay de GameCube o de PSP
nrow(videogames[videogames$platform %in% c("GameCube","PSP"),])


#Cuantos juegos hay de Switch que tengan meta_score
nrow(videogames[videogames$platform == "Switch" &
                  videogames$meta_score <= 70 &
                  videogames$meta_score >= 50, ])



















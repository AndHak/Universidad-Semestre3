install.packages("stringr")

library(stringr)

#Contar comas de una oracion
sum(strsplit("Primero,Segundo,Tercero","")[[1]]==",")

str_count(string = "Primero,Segundo,Tercero",
          pattern = ",")

install.packages("tidyverse")

library(tidyverse)

videogames <- read.csv("C:\\Programacion Universidad\\Semestre 3\\RStudio\\all_games.csv")
videogames$platform <- trimws(videogames$platform)
videogames$user_review <- as.numeric(videogames$user_review)*10
str(videogames, strick.wifth = "cut")

#Cuantos juegos hay de gamecube
nrow(filter(videogames, platform == "GameCube"))

#usando pipe 
videogames %>%
  filter(platform == "GameCube") %>%
  nrow()

#Cuantos juegos tienen meta score entre 90 y 100
videogames %>%
  filter(meta_score >= 90 & meta_score <= 100) %>%
  nrow()




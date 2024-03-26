install.packages("stringr")

library(stringr)

#Contar comas de una oracion
sum(strsplit("Primero,Segundo,Tercero","")[[1]]==",")

str_count(string = "Primero,Segundo,Tercero",
          pattern = ",")

install.packages("tidyverse")
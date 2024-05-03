setwd("C:\\Users\\Udenar\\Desktop")
ejercicio <- read.table("datos.txt", header = TRUE)
tabla_pisos <- table(ejercicio$Andar)


prob_piso_4_7 <- sum(tabla_pisos[4:7])/sum(tabla_pisos)
prob_piso_4_7

tabla_bloque <- table(ejercicio$Bloco)
prob_bloque_b <- sum(tabla_bloque["B"])/sum(tabla_bloque)
prob_bloque_b

tabla_racha_infil <- table(ejercicio$Rachadura, ejercicio$Infiltr)
prob_ambas1 <- tabla_racha_infil["1", "0"] / sum(tabla_racha_infil)
prob_ambas2 <- tabla_racha_infil["0", "1"] / sum(tabla_racha_infil)
prob_ambas3 <- tabla_racha_infil["1", "1"] / sum(tabla_racha_infil)
prob_total <- prob_ambas1 + prob_ambas2 + prob_ambas3
prob_total

prob_todo_table <- table(ejercicio$Bloco, ejercicio$Andar)
prob_bloque_b_4_7 <- sum(prob_todo_table["B", 4:7])/sum(prob_todo_table)
prob_bloque_b_4_7

prob_racha_infil_blo_b <- mean(ejercicio$Rachadura[ejercicio$Bloco == "B"] == 1 |
                                ejercicio$Infiltr[ejercicio$Bloco == "B"] == 1)
prob_racha_infil_blo_b


#52 cartas y salga
prob_carta_as <- 4/52
prob_carta_as

tipo <- c("Corazones", "Diamantes", "Picas", "Treboles")
color <- c("Roja", "Negra")
baraja <- expand.grid(Tipo = tipo, Color = color,  Numeros = c(2:10, "AS", "J", "Q", "K"))
baraja

prob_as_roja <- mean(baraja$Numeros == "AS" & (baraja$Tipo == "Corazones" | baraja$Tipo == "Diamantes"))
prob_as_roja
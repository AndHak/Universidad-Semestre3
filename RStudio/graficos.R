set.seed(1998)
muestra <- sample(18:40, 1000, replace=TRUE)
muestra 
barplot(muestra)
hist(muestra, main = "Histograma para edades", xlab = "Categoria",
     ylab = "Valor", col = "lightblue")

muestra_1 <- sample(1:7,10, replace=TRUE)
barplot(muestra_1)
library(ggplot2)
datos_barras <- data.frame(
  categoria = c(17, 18, 19, 20, 22, 23, 24, 25, 26, 27),
  frecuencia = c(2, 4, 5, 4, 1, 5, 4, 5, 5, 5))
g1 <- ggplot(datos_barras, aes(x = categoria, y = frecuencia)) +
  geom_bar(stat = "identity", fill = "steelblue") + 
  labs(title = "Grafico de barras")


primer_digito_decimal <- function(numero){
  cadena <- as.character(numero)
  posicion_decimal <- stringr::str_locate(cadena, "\\.")[[1,1]]
  
  if (is.na(posicion_decimal)){
    return(0)
  }
  primer_digito <- substr(cadena, posicion_decimal+1, posicion_decimal+1)
  return(as.numeric(primer_digito))
}

aproximar <- function(numero){
  digito <- primer_digito_decimal(numero)
  if (digito %% 2 == 0){
    return(ceiling(numero))
  } else {
    return(floor(numero))
  }
}

tabla_agrupados <- function(lista){
  k <- 1+3.322*log10(length(lista))
  k_new <- aproximar(k)
  rango <- max(lista)-min(lista)
  amplitud <- rango/k_new
  L <- min(lista)+amplitud*(0:k_new)
  mc <- numeric(length(L)-1)
  for (i in 1:(length(L)-1)){
    mc[i] <- (L[i]+L[i+1])/2
  }
  #Cut es para hacer los intervalos
  intervalos <- cut(lista, breaks = k_new, right = FALSE, include.lowest = TRUE)
  tabla_frec <- as.data.frame(table(intervalos))
  
  names(tabla_frec) <- c("Edades", "fi", "Marca clase")
  tabla_frec$
  
  # Calcular mc
  marca_clase <- (intervalos[-length(intervalos)] + intervalos[-1]) / 2
  
return(tabla_frec)
}
tabla_agrupados(muestra)









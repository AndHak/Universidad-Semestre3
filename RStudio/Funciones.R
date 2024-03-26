cuadrado <- function(num){
  return(num**2)
}

cuadrado(10)


exponente <- function(num, exp){
  return(num**exp)
}

exponente(2,8)

celcius_a_farenheit <- function(temp){
  return(temp*9/5+32)
}

celcius_a_farenheit(25)

usuario_valido <- function(nombre){
  val_long <- nchar(nombre) < 10
  val_riot <- !grepl("RIOT", nombre)
  val_ocupados <- !nombre %in% c("ElVaipa", "Txtli")
  
  validacion <- val_long & val_riot & val_ocupados
  return(validacion)
}

usuario_valido("ELJOJO")



cuenta_vocales <- function(string){
  
  
  letras <- strsplit(string, split = "")[[1]]
  letras <- tolower(letras)
  
  vocales <- c("a", "e", "i", "o", "u")
  
  
  sum(letras %in% vocales)
  
  
}

cuenta_vocales("juanito")

mueve_punto <- function(pos_i){
  dado1 <- sample(1:6, size = 1)
  dado2 <- sample(1:6, size = 1)
  pos_f <- pos_i + 2*dado1 - dado2
  paste0("Posicion inicial", pos_i, ", posicion final", pos_f)
}


mueve_punto(5)


siglo <- function(year){
  ceiling(year/100)
}


siglo(2024)


#Primos
es_primo <- function(numero) {
  divisores <- 0
  for (i in 1:sqrt(numero)) {
    if (numero %% i == 0) {
      divisores <- divisores + 1
    }
  }
  if (divisores == 1) {
    return(TRUE)
  } else {
    return(FALSE)
  }
}

es_primo(4)

es_primo <- Vectorize(es_primo)

es_primo(c(2,4,5))























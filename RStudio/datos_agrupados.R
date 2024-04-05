################################################################################
# script para agrupar datos y hacer un análisis descriptivo.
# 
# Probabilidad y estadística
# Universidad de Nariño
# 
# Realizado por: Santigo Jiménez Ramos
#
# Uso libre
################################################################################


# Función para obtener el primer dígito decimal de un número real
primer_digito_decimal <- function(numero) {
  # Convertir el número a una cadena
  cadena <- as.character(numero)
  
  # Encontrar la posición del punto decimal
  posicion_decimal <- stringr::str_locate(cadena, "\\.")[[1,1]]
  
  # Si no hay punto decimal, devolver 0
  if (is.na(posicion_decimal)) {
    return(0)
  }
  
  # Obtener el primer dígito después del punto decimal
  primer_digito <- substr(cadena, posicion_decimal + 1, posicion_decimal + 1)
  
  # Devolver el dígito como número
  return(as.numeric(primer_digito))
}

# Función para aproximar k al techo o al piso según el primer dígito decimal
aproximar <- function(k) {
  if (as.numeric(substr(k, 1, 1)) %% 2 == 0) {
    return(ceiling(k))
  } else {
    return(floor(k))
  }
}

tabla_agrupada <- function(datos) {
  # Calcular el número de intervalos de clases según la regla de Sturges
  n <- length(datos)
  k <- 1 + 3.322 * log10(n)
  # Aproximar k al techo o al piso según el primer dígito decimal
  k_new <- aproximar(k)
  
  # Calcular rango, amplitud e intervalos
  rango <- diff(range(datos))
  amplitud <- rango / k_new 
  
  # Crear una nueva lista con la marca de clase
  L <- seq(min(datos), max(datos), by = amplitud)
  mc <- (L[-1] + L[-length(L)]) / 2
  
  # Crear la tabla de frecuencias de datos agrupados
  intervalos <- cut(datos, breaks = k_new, right = FALSE, include.lowest = TRUE) 
  freq_table <- as.data.frame(table(intervalos)) 
  names(freq_table) <- c("Intervalo", "fi_abs") 
  
  # Calcular frecuencia acumulada absoluta
  freq_table$Fi_abs <- cumsum(freq_table$fi_abs)
  
  # Calcular frecuencia relativa
  freq_table$fi_rel <- freq_table$fi_abs/n
  
  # Calcular frecuencia acumulada relativa
  freq_table$Fi_rel <- cumsum(freq_table$fi_rel)
  
  # Calcular porcentajes
  freq_table$Porcentaje <- freq_table$fi_rel * 100
  
  # Calcular grados
  freq_table$Grados <- freq_table$fi_rel * 360
  
  # Agregar marca de clase a la tabla
  freq_table$Marca_de_Clase <- mc
  
  # Imprimir resumen de estadísticas
  cat("x_(1):", min(datos), "\n")
  cat("x_(n):", max(datos), "\n")
  cat("k    :", k_new, "\n")
  cat("r(x) :", rango, "\n")
  cat("A    :", amplitud, "\n\n")
  
  # Devolver la tabla de frecuencias y la lista L
  return(list(freq_table = freq_table, L = L))
}


# Calcular la media para datos agrupados
calcular_media <- function(datos_agrupados){
  
  media <- sum((datos_agrupados$Mc*datos_agrupados$fi_abs))/(length(muestra))
  
  return(media)
}

#funcion para calcular la mediana
calcular_mediana <- function(datos_agrupados) {
  # Tamaño total de la muestra
  n <- sum(datos_agrupados$freq_table$fi_abs)
  
  # Calcular la posición de la mediana
  mediana_pos <- n / 2
  
  # Encontrar el intervalo que contiene la mediana
  intervalo <- which.max(datos_agrupados$freq_table$Fi_abs >= mediana_pos)
  if(intervalo == 1){
    Fi_1 <- 0
  } else{
    Fi_1 <- datos_agrupados$freq_table$Fi_abs[intervalo - 1]
  }  
  
  # Obtener los datos del intervalo que contiene la mediana
  Li <- datos_agrupados$L[intervalo]
  fi <- datos_agrupados$freq_table$fi_abs[intervalo]
  A <- (datos_agrupados$L[2]-datos_agrupados$L[1])
  
  # Calcular la mediana
  mediana <- Li + ((mediana_pos - Fi_1) / fi) * A
  
  return(mediana)
}

calcular_modas <- function(datos_agrupados){
  modas <- c() # Vector para almacenar las modas
  
  # Encontrar los intervalos que contienen modas
  intervalos_moda <- which(datos_agrupados$freq_table$fi_abs == max(datos_agrupados$freq_table$fi_abs))
  
  # Calcular la moda para cada intervalo
  for (intervalo in intervalos_moda) {
    if (intervalo == 1) {
      fi_a <- 0
    } else {
      fi_a <- datos_agrupados$freq_table$fi_abs[intervalo - 1]
    }
    
    if (intervalo == length(datos_agrupados$L)-1) {
      fi_s <- 0
    } else {
      fi_s <- datos_agrupados$freq_table$fi_abs[intervalo + 1]
    }
    
    Li <- datos_agrupados$L[intervalo]
    fi <- datos_agrupados$freq_table$fi_abs[intervalo]
    A <- datos_agrupados$L[2] - datos_agrupados$L[1]
    
    moda <- Li + ((fi - fi_a) / ((fi - fi_a) + (fi - fi_s))) * A
    
    modas <- c(modas, moda) # Almacenar la moda calculada
  }
  
  return(modas)
}

calcular_cuantiles <- function(datos_agrupados, q, k) {
  # Verificar que q sea un valor válido
  if (!(q %in% c(4, 10, 100))) {
    stop("El valor de q debe ser un entero y debe ser 4, 10 o 100.")
  }
  
  # verificar que k sea un entero y este estre 1 y q
  if (!(k %in% seq(1:q))) {
    stop(paste("El valor de k debe ser un entero entre 1 y ", q, ".", sep=""))
  }
  
  # Tamaño total de la muestra
  n <- sum(datos_agrupados$freq_table$fi_abs)
  
  # Calcular la posición del cuantil
  quantile_pos <- (k * n) / q
  
  # Encontrar el intervalo que contiene el cuantil
  intervalo <- which.max(datos_agrupados$freq_table$Fi_abs >= quantile_pos)
  if(intervalo == 1){
    Fi_1 <- 0
  } else{
    Fi_1 <- datos_agrupados$freq_table$Fi_abs[intervalo - 1]
  }  
  
  # Obtener los datos del intervalo que contiene el cuantil
  Li <- datos_agrupados$L[intervalo]
  fi <- datos_agrupados$freq_table$fi_abs[intervalo]
  A <- (datos_agrupados$L[2]-datos_agrupados$L[1])
  
  # Calcular el cuantil
  cuantil <- Li + ((quantile_pos - Fi_1) / fi) * A
  
  return(cuantil)
}
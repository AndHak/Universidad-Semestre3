
calcular_varianza <- function(datos_agrupados) {
  n <- sum(datos_agrupados$freq_table$fi_abs) 
  media <- calcular_media(datos_agrupados)   
  suma <- sum(datos_agrupados$freq_table$fi_abs * (datos_agrupados$freq_table$Mc - media)^2)
  varianza <- suma / n
  
  return(varianza)
}

condicion <- TRUE

if (condicion) {
  print("TRUE")
} else {
  print("FALSO")
}

elo <- 1500
if(elo >= 1200){
  rango <- "Profesional"
} else if(elo >= 1800){
  rango <- "Gran Maestro"
} else if(elo >= 600){
  rango <- "Aprendiz"
} else {
  rango <- "Novato"
}
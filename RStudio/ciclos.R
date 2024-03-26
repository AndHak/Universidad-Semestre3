
#ciclo for
for (i in 1:10){
  texto <- paste0("Iteracion", i)
  print(texto)
}

for (i in letters){
  print(i)
}

numero <- 5
while(numero <= 10){
  texto <- paste0("El numero es: ", numero)
  numero <- numero + 1
  print(texto)
}
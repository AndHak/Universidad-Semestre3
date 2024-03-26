usuario <- "AndresGuerra"

#Numero de caracteres
x <- nchar(usuario)

#Convertir a Mayusculas
toupper(usuario)

#Cnvertir a minusculas
tolower(usuario)

#Obtener desde un punto a otro
substr(usuario, 1, 6)

substr(usuario, 7, x)

#Sustituir una ocurriencia
sub("e", "E", usuario)

#Sustituir todas las ocurrencias
gsub("r", "R", usuario)
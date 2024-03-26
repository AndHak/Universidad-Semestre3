#Vector numerico
vistas <- c(8321, 2974, 5792, 4932, 4889, 7433, 6651)

#Vector strings
nombres <- c("Video 1", "Video 2", "Video 3", "Video 4",
             "Video 5", "Video 6", "Video 7")

#Tamaño de la lista
length(vistas)
#Max de la lista
max(vistas)
#Min de la lista
min(vistas)
#Promedio
mean(vistas)
#Suma total
sum(vistas)

#Se aplica a todo el vector
vistas + 1000

#Agregar
vistas <- c(vistas, 5600)
nombres <- c(nombres, "Video 8")

names(vistas) <- nombres

sort(vistas)
sort(vistas, decreasing = TRUE)

vistas > 6000


#Regresa las posiciones de TRUE
which(vistas < 5000)


#Extraer info
vistas[c(2,4)]
vistas[3]

vistas[-4]
vistas[-c(2,4)]

vistas[vistas > 7000]
vistas[vistas > 4000 & vistas < 5000]

#Cambiar valores
vistas[1] <- 500
vistas[c(2,3,4)] <- c(0,0,0)
vistas[vistas > 7000] = 7000



yo <- c("GTA V", "Mortal Kombat", "Zelda", "Skyrim")
amigo <- c("Mario Kart", "Zelda", "Devil May Cry", "GTA V")

#Unir
union(yo, amigo)

#Cosas en comun
intersect(yo, amigo)

#que tengo yo que el no
setdiff(yo, amigo)

#Mismos videojuegos
setequal(yo, amigo)

#Buscar elemento
"Zelda" %in% amigo

c("Age of empires", "Mario Kart") %in% amigo

#Con operadores
1:50
20:1
-5:5

#Utilizando seq(donde inicia, donde termina, de cuanto aumenta)
seq(from=10, to=100, by=2)
seq(from=0, to=10, by=0.5)


#Separar string
juego <- "Mortal Kombat"

split <- strsplit(juego, "")[[1]]
class(split)

#Cosas de manera aleatoria

resultados <- c("victoria", "derrota")
sample(resultados, size=1, replace = TRUE, prob = c(0.05, 0.95))

#Distribuciones de probabilidad
runif(n=20, min = 0, max = 2)
rnorm(n=20, mean=15, sd=2)
rbinom(n=20, size=1, p=0.5)
rbinom(n=20, size=5, p=0.5)

#Fijar semilla
set.seed(123)
runif(n=1)

ejemplo <- c(3.1415, TRUE, "God of War")


numeros <- 1:1000000

sum(numeros %% 6 == 0 & numeros %% 8 == 0)


set.seed(123)
compras <- rnorm(n = 10000, mean = 5000, sd = 1000)

#Monto de las compras 435 y 678
compras[c(435, 678)]

#Cuales fueron mayores a 8000
sum(compras > 8000)

#Cuales fueron el monto maximo y minimo
max(compras)
min(compras)

#que porcentaje de compras fue entre 4000 y 6000
porcentaje <- sum(compras >= 4000 & compras <= 6000)/length(compras)
porcentaje*100



usuario = "NoobSlayer9"

#True si tiene al menos un numero
any(strsplit(usuario, split = "")[[1]] %in% 1:9)

#True si contiene solo numeros
all(strsplit(usuario, split = "")[[1]] %in% 1:9)



#Conversion


as.character(5.6)
as.character(-6)


as.logical(100)
as.logical(0)

as.numeric(TRUE)
as.numeric("123")

as.logical("TRUE")

vec <- c("1", "2", "3", "4", "5")
as.numeric(vec)



















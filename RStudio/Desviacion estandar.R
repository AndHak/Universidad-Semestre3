A <- c(20, 25, 23, 24)
B <- c(0.5, 2.2, 3.5)
C <- c("azul", "amarillo", "rojo", "verde")
set.seed(123)
datos_edades <- sample(17:30,30, replace = TRUE)
datos_edades
mean(datos_edades)
mode(datos_edades)
summary(datos_edades)
sd(datos_edades)

md <- function(x){
  n <- length(x)
  media <- mean(x)
  d <- sum(abs(x-media))
  return(d/n)
}

md(datos_edades)

dk <- function(x){
  n <- length(x)
  media <- mean(x)
  des <- sd(x)
  suma <- sum((x-media)^3)
  return((1/des^3)*(1^n)*suma)
}

dk(datos_edades)

frec_absoluta <- table(datos_edades)
frec_aa <- cumsum(frec_absoluta)
frec_relativa <- prop.table(frec_absoluta)
frec_ra <- cumsum(frec_relativa)
df_frec <- data.frame(edad = as.numeric(names(frec_absoluta)),
                      Fa = as.numeric(frec_absoluta),
                      fa = as.numeric(frec_aa),
                      Fr = as.numeric(frec_relativa),
                      fr = as.numeric(frec_ra))
print(df_frec)

max(datos_edades)

min(datos_edades)

1+3.322*log(datos_edades)

sort(datos_edades)

frec_absoluta <- table(datos_edades)
frec_aa <- cumsum(frec_absoluta)
frec_relativa <- prop.table(frec_absoluta)
frec_ra <- cumsum(frec_relativa)
df_frec <- data.frame(edad = as.numeric(names(frec_absoluta)),
                      Fa = as.numeric(frec_absoluta),
                      fa = as.numeric(frec_aa),
                      Fr = as.numeric(frec_relativa),
                      fr = as.numeric(frec_ra))

View(df_frec)



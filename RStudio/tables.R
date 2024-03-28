library(tidyverse)

#Tabla
series <- data.frame(
  nombre = c("Los 100", "Sense 8", "One Piece", "Death Note"),
  imdl = c(9.4, 8.9, 9.5, 10.0),
  episodios = c(400, 100, 1200, 46),
  concluida = c(FALSE,TRUE,FALSE,TRUE)
)

series2 <- tibble(
  nombre = c("Los 100", "Sense 8", "One Piece", "Death Note"),
  imdl = c(9.4, 8.9, 9.5, 10.0),
  episodios = c(400, 100, 1200, 46),
  concluida = c(FALSE,TRUE,FALSE,TRUE)
)

#Convertir un data frame a tibble
videogames <- as_tibble(videogames)


#Maniular datos
zelda_filter <- videogames %>%
  filter(str_detect(name,"Zelda"))

zelda_select <- zelda_filter %>%
  select(name,platform,meta_score,release_date)

#Sustituir
zelda_select %>%
  mutate(new_var = case_when(
    meta_score >= 90 ~ "excelente",
    meta_score >= 80 ~ "bueno",
    TRUE ~ "Regular"
  ),
  release_year = as.numeric(str_sub(release_date,
                         str_length(release_date) -3,
                         str_length(release_date)))
  )

zelda_arrange <- zelda_mutate %>%
  arrange(desc(release_year))

#Calculos agrupados
zelda_mutate %>%
  group_by(platform) %>%
  summarise(meta_score = mean(meta_score),
            ultimo_juego = max(release_year)) %>%
  arrange(desc(meta_score))

#Contar
zelda_filter %>%
  count(platform) %>%
  arrange(desc(n))

#Otra manera de extraer filas
zelda_filter %>%
  #Filas entre 1 y 3, no cuenta el 3
  slice(c(1,3))
zelda_filter %>%
  #Primeras filas
  slice_head(n = 10)
zelda_filter %>%
  #Ultimas filas
  slice_tail(n = 3)


#Extraer fila con valor mayor
zelda_filter %>%
  slice_max(meta_score)

#Fila con el menor
zelda_filter %>%
  slice_min(meta_score)


#Extraer filas al azar
zelda_filter %>%
  slice_sample(n = 2)


#Extraer un juego al azar de cada plataforma
zelda_filter %>%
  group_by(platform) %>%
  slice_sample(n = 1) %>%
  ungroup()

#Extraer el mejor juego de zelda para cada plataforma
zelda_filter %>%
  group_by(platform) %>%
  slice_max(meta_score)


#Otra manera de extraer columnas como vectores
zelda_filter %>%
  pull(meta_score)

#Obtener columnas que tengan cierto patron
zelda_filter %>%
  select(contains("score") | contains("re"))












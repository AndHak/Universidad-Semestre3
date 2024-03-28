library(tidyverse)
videogames <- read.csv("C:\\Programacion Universidad\\Semestre 3\\RStudio\\all_games.csv")

#Histograma
videogames %>%
  ggplot(aes(x = meta_score)) + 
  geom_histogram(bins = 40, fill = "steelblue") +
  labs(x = "Meta score", title = "Histrograma del metascore") +
  theme_minimal() + 
  theme(plot.title = element_text(hjust = 0.5))


#Scatterplot

videogames %>%
  filter(platform == "PlayStation 4") %>%
  ggplot(aes(x = meta_score, y = user_review)) + 
  geom_point(size = 5, color = "red", alpha = 0.8) +
  labs(x = "MetaScore", y = "User review",
       title = "Comparacion Metascore y user review para N64") +
  theme_bw() + 
  theme(plot.title = element_text(hjust = 0.5))


#Boxplot
videogames %>%
  filter(platform %in% c("PSP", "Nintendo 64", "PC", "Switch"
                         , "PlayStation 4")) %>%
  ggplot(aes(x = platform, y = meta_score)) +
  geom_boxplot(fill = "purple") + 
  labs(x = "", y = "Metascore",
       title = "Distribución del metascore por plataforma") +
  theme_minimal() +
  theme(plot.title = element_text(hjust = 0.5))









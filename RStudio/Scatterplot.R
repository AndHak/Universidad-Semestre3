#Scatterplot
videogames <- read.csv("C:\\Programacion Universidad\\Semestre 3\\RStudio\\all_games.csv")
n64 <- videogames[videogames$platform == "Nintendo 64",]

plot(n64$meta_score,
     n64$user_review,
     col = "steelblue",
     pch = 19,
     lwd = 5,
     xlab = "MetaScore",
     ylab = "UserReview",
     main = "Comparación Metascore y user riview para N64",
     frame = FALSE)


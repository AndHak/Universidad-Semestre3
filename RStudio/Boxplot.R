#Boxplot
videogames <- read.csv("C:\\Programacion Universidad\\Semestre 3\\RStudio\\all_games.csv")
videogames$platform <- trimws(videogames$platform)
videogames$user_review <- as.numeric(videogames$user_review)*10
str(videogames, strick.wifth = "cut")
boxplot(videogames$meta_score)

boxplot(meta_score = platform,
        data = videogames,
        col = "purple",
        subset = platform %in% c("PSP", "Nintendo 64", "PC",
                                 "Switch", "PlayStation 4"),
        xlab = "",
        ylab = "Meta Score",
        frame = FALSE)






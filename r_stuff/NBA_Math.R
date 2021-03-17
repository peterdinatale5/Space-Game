raptors_scores <- read.csv("raptors_scores.csv")
# Total points scored in each Toronto Raptors (Rapters?) game over the last
# three seasons

player_sizes <- read.csv("players.csv")
# Heights and weights of NBA players. Someone from the 11am sent me 
# a link to this data. To that student, thank you!

hist(raptors_scores$Total,
     main="Total Score In Rapters Games",
     xlab= "Points",
     breaks=55)
hist(player_sizes$weight,
     main="NBA Players Weight",
     xlab = "Weight")
hist(player_sizes$height,
     main="NBA Players Height",
     xlab="Height")

#print(player_sizes$height)
#print(player_sizes)[player_sizes["player_name"]=="Dennis Rodman"]


six_sided_die <- function()
{
        result <- sample(c(1,2,3,4,5,6),1)
        return(result)
}

n_sided_die <- function(n=6) {
        # this function allows us to roll a die with a number of sides
        # of our choosing. The n=6 means that it will default to 6, but you
        # can enter any positive number you want!
        
        # here we create a vector to sample from using the "range" function. Google it!
        sample_vector <- range(1,n)
        
        result <- sample(sample_vector)
        return(result)
}

x = c(1,2,3,4,2,3,5,7,4,3,9,8,1)
sd(x)

plot(players$age, players$weight,
     col = "#cc0000", #col = color
     pch = 20,
     main = "Iris: Petal Length vs. Petal Width",
     xlab = "Player Age",
     ylab = "Player Weight")


library(datasets)
head(iris)

?plot

plot(iris$Species) #catagorical
plot(iris$Petal.Length)
plot(iris$Species, iris$Petal.Width)

plot(iris$Petal.Length, iris$Pedal.Width,
     col = "#cc0000", #col = color
     pch = 20,
     main = "Iris: Petal Length vs. Petal Width",
     xlab = "Petal length",
     ylab = "Petal Width")

plot(cos, 0, 2*pi)
plot(dnorm, -3, +3)



problem_one <- pnorm(40,mean= 30, sd = 4, lower.tail = TRUE)
problem_two <- pnorm(21,mean= 30, sd = 4, lower.tail = FALSE)
problem_three <- pnorm(35,mean= 30, sd = 4, lower.tail = TRUE) - pnorm(30,mean= 30, sd = 4, lower.tail = FALSE)
round(problem_one, digits = 3)
round(problem_two, digits = 3)
round(problem_three, digits = 3)

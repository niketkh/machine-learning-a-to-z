# Data Preprocessing
dataset = read.csv("Salary_Data.csv")

library(caTools)
set.seed(42)
split = sample.split(dataset$Salary, SplitRatio = 2/3)
training_set = subset(dataset, split==TRUE)
test_set = subset(dataset, split==FALSE)

# Fitting Linear Regression into Training Set
regressor = lm(formula = Salary ~ YearsExperience, data = training_set )
# summary(regressor)

# Predicting the Test Results
y_pred = predict(regressor, newdata = test_set)

# Visualising Training Set Results
# install.packages('ggplot2')
library(ggplot2)
ggplot() +
  geom_point(aes(x = training_set$YearsExperience, y = training_set$Salary),
             colour = 'red') + 
  geom_line(aes(x = training_set$YearsExperience, y = predict(regressor, newdata = training_set)),
            colour = 'blue') +
  ggtitle('Salary vs Years Experience (Training Set)') + 
  xlab('Years of Experience') +
  ylab('Salary') 

# Visualising Test Set Results
ggplot() +
  geom_point(aes(x = test_set$YearsExperience, y = test_set$Salary),
           colour = 'red') + 
  geom_line(aes(x = training_set$YearsExperience, y = predict(regressor, newdata = training_set)),
            colour = 'blue') +
  ggtitle('Salary vs Years Experience (Test Set)') + 
  xlab('Years of Experience') +
  ylab('Salary') 
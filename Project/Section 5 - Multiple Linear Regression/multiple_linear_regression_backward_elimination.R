# Importing the dataset
dataset = read.csv('50_Startups.csv')

# Encoding the state column
dataset$State = factor(dataset$State,
                       levels = c('New York', 'California', 'Florida'),
                       labels = c(1, 2, 3))

# Splitting Dataset into Training Set and Test Set
library(caTools)
set.seed(0)
split = sample.split(dataset$Profit, SplitRatio = 0.8)
training_set = subset(dataset, split == TRUE)
test_set = subset(dataset, split == FALSE)

# Fitting Multiple Linear Regression into Training Set
regressor = lm(formula = Profit ~ ., data = training_set)
summary(regressor)

# Predicting the Test Set Results
y_pred = predict(regressor, newdata = test_set)

# Building the Optimal Model using Backward Elimination
regressor = lm(formula = Profit ~ R.D.Spend + Administration + Marketing.Spend + State, data = dataset)
summary(regressor)

regressor = lm(formula = Profit ~ R.D.Spend + Administration + Marketing.Spend, data = dataset)
summary(regressor)

regressor = lm(formula = Profit ~ R.D.Spend  + Marketing.Spend, data = dataset)
summary(regressor)

regressor = lm(formula = Profit ~ R.D.Spend, data = dataset)
summary(regressor)



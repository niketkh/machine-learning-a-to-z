# Data Preprocessing
dataset = read.csv('50_Startups.csv')

# Encoding State Column
dataset$State = factor(dataset$State, 
                       levels = c('New York', 'California', 'Florida'), 
                       labels = c(1, 2, 3))

# Splitting dataset into Training Set and Test Set
library(caTools)
set.seed(0)
split = sample.split(dataset$Profit, SplitRatio = 0.8)
training_set = subset(dataset, split == TRUE)
test_set = subset(dataset, split==FALSE)

# Fitting Multiple Regression to the Training Set
# Profit ~ . , where . indicates all the independent variables 
# Equivalent to Profit ~ R.D.Spend + Administration + Marketing.Spend + State
regressor = lm(formula = Profit ~ ., data = training_set)
summary(regressor)
# From Summary its clear that only independent variable that has significant impact is R.D.Spend
# regressor = lm(formula = Profit ~ R.D.Spend, data = training_set)
# summary(regressor)

# Predicting the test results
y_pred = predict(regressor, newdata = test_set)

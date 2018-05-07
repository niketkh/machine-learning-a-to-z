# Data Preprocessing Template

# Importing the libraries
import pandas 

# Importing the dataset
dataset = pandas.read_csv('Data.csv')

# Independent Variable Vector
X = dataset.iloc[:,:-1].values

# Dependent Variable Vector
Y = dataset.iloc[:,-1].values

# Handling Missing Data
from sklearn.preprocessing import Imputer

imputer = Imputer(missing_values = 'NaN', strategy = 'mean', axis = 0) 
imputer.fit(X[:,1:3])
X[:,1:3] = imputer.transform(X[:,1:3])

# Encoding Categorical Data
from sklearn.preprocessing import LabelEncoder, OneHotEncoder

oneHotEncoder = OneHotEncoder(categorical_features = [0]) 
labelEncoder_X = LabelEncoder()

X[:,0] = labelEncoder_X.fit_transform(X[:,0])
X = oneHotEncoder.fit_transform(X).toarray()

labelEncoder_Y = LabelEncoder()
Y = labelEncoder_Y.fit_transform(Y)

# Splitting the dataset into training set and test set
from sklearn.cross_validation import train_test_split

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.2, random_state = 0)


# Feature Scaling
from sklearn.preprocessing import StandardScaler

sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)

print(X_train)


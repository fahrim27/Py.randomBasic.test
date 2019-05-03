from pydoc import describe

from fuzzywuzzy import fuzz
from fuzzywuzzy import process
import pandas

# Load dataset

url = "http://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"

names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']

dataset = pandas.read_csv(url, names=names)

print(dataset.shape)

print(dataset.head())
print(50*'=')

print(dataset.describe)
print(50*'=')

print(dataset.groupby('class').size())
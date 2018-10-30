#Create daaframe from data in x_train
# lable the columns using the Strings in feature_name
# example
iris_dataframe= pd.DataFrame(x_train, columns=iris_dataset.feature_name)
# create scatte matrix from the dataframe, color by y_train
pd.plotting.scatter_matrix(iris_dataframe, c=y_train, figsize=(15,15), marker="0", hist_kwds={'bins': 20}, s=60, apha=8, cmap=mglearn.cm3)

#code to print out png I run this in terminal
$ dot -Tpng mytree.dot -o mytree.png
# now come to jupyter notebook and change the cell to markdown
![](mytree.png)


import graphviz
from sklearn.tree import export_graphviz

 
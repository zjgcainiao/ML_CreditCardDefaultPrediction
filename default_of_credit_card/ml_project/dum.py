import graphviz
from sklearn import export_graphviz

export_graphviz(tree, out_file="cancer.dot", class_names=['malignant', 'begign'], feature_names=X, impurity=False, filled=True)
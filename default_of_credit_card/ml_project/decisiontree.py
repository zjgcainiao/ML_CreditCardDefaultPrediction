# cd ml_project
# mkdir credit_default
# cd credit_default
# jupyter notebook
# you see 88888

import pandas as pd
import numpy as np

from sklearn import tree
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from matplotlib import pyplot as plt
import seaborn as sns

import graphviz
import pydotplus
from scipy import misc

%matplotlib inline



# go to kaggle and download it
 # download it and go to your teminal
 # and cd to your dir and in that dir make another dir can data
    #    mkdir data
# go to download and move that file to data
    # mv ~/Downloads/spotifyclassification.zip ./data
    # cd data
    # unzip spotifyclassification.zip
    # ls
    # backe to jupyter notebook

# Sporty Song Attributes EDA
    # Import the data
    # EDA to visualize data and observe srurcture
    # Train a classifier (Decision Tree clasaifier)
    # Predict traget using the trained classifier

    data = pd.read_csv("data/data.csv")

    data.describe()
    data.head()
    data.info()
    # split the data into training and testing set
    train, test = train_test_split(data, test_size =0.15)
    print("Traning size: {}; Test size {}".format(len(train), len(test)))
    train.shape # to see # of row and col

    pos_tempo = data[data['target']==1]['tempo']
    neg_tempo = data[data['target']==0]['tempo']
#    ------------
#custom color palette
red_blue =["#19B5FE", "#EF4836"]
palette = sns.color_palette(red_blue)
sns.set_palette(palette)
sns.set_style("white")
# -----
pos_tempo = data[data['target'] == 1]['tempo']
neg_tempo = data[data['target'] == 0]['tempo']

pos_dance = data[data['target'] == 1]['danceability']
neg_dance = data[data['target'] == 0]['danceability']

pos_duration = data[data['target'] == 1]['duration_ms']
neg_duration = data[data['target'] == 0]['duration_ms']

pos_loudness = data[data['target'] == 1]['loudness']
neg_loudness = data[data['target'] == 0]['loudness']

pos_speechiness = data[data['target'] == 1]['speechiness']
neg_speechiness = data[data['target'] == 0]['speechiness']

pos_valence = data[data['target'] == 1]['valence']
neg_valence = data[data['target'] == 0]['valence']

pos_energy = data[data['target'] == 1]['energy']
neg_energy = data[data['target'] == 0]['energy']

pos_acousticness = data[data['target'] == 1]['acousticness']
neg_acousticness = data[data['target'] == 0]['acousticness']

pos_key = data[data['target'] == 1]['key']
neg_key = data[data['target'] == 0]['key']

pos_instrumentalness = data[data['target'] == 1]['instrumentalness']
neg_instrumentalness = data[data['target'] == 0]['instrumentalness']
# ------
pos_tempo
# ----

   fig = plt.figure(figsize=(12,8))
   plt.title("Song Tempo Like /Dislike Distribution")
   pos_tempo.hist(alpha=0.7, bins = 30, label='positive')
   neg_tempo.hist(alpha=0.7, bins = 30, label='negative')
   plt.legend(loc='upper right')

# -----------

fig2 = plt.figure(figsize=(15, 15))

# Danceability
ax3 = fig2.add_subplot(331)
ax3.set_xlabel("Danceability")
ax3.set_ylabel("Count")
ax3.set_title("Song Danceability Like Distribution")
pos_dance.hist(alpha=0.5, bins=30)
ax4 = fig2.add_subplot(331)
neg_dance.hist(alpha=0.5, bins=30)

# Duration
ax5 = fig2.add_subplot(332)
ax5.set_xlabel("Duration (ms)")
ax5.set_ylabel("Count")
ax5.set_title("Song Duration Like Distribution")
pos_duration.hist(alpha=0.5, bins=30)
ax6 = fig2.add_subplot(332)
neg_duration.hist(alpha=0.5, bins=30)

# Loudness
ax7 = fig2.add_subplot(333)
ax7.set_xlabel("Loudness")
ax7.set_ylabel("Count")
ax7.set_title("Song Loudness Like Distribution")
pos_loudness.hist(alpha=0.5, bins=30)
ax8 = fig2.add_subplot(333)
neg_loudness.hist(alpha=0.5, bins=30)
# Speechiness
ax7 = fig2.add_subplot(334)
ax7.set_xlabel("Speechiness")
ax7.set_ylabel("Count")
ax7.set_title("Song Speechiness Like Distribution")
pos_speechiness.hist(alpha=0.5, bins=30)
ax8 = fig2.add_subplot(334)
neg_speechiness.hist(alpha=0.5, bins=30)

# Valence
ax7 = fig2.add_subplot(335)
ax7.set_xlabel("Valence")
ax7.set_ylabel("Count")
ax7.set_title("Song Valence Like Distribution")
pos_valence.hist(alpha=0.5, bins=30)
ax8 = fig2.add_subplot(335)
neg_valence.hist(alpha=0.5, bins=30)

# Energy
ax7 = fig2.add_subplot(336)
ax7.set_xlabel("Energy")
ax7.set_ylabel("Count")
ax7.set_title("Song Energy Like Distribution")
pos_energy.hist(alpha=0.5, bins=30)
ax8 = fig2.add_subplot(336)
neg_energy.hist(alpha=0.5, bins=30)

# Acousticness
ax7 = fig2.add_subplot(337)
ax7.set_xlabel("Acousticness")
ax7.set_ylabel("Count")
ax7.set_title("Song Acousticness Like Distribution")
pos_acousticness.hist(alpha=0.5, bins=30)
ax8 = fig2.add_subplot(337)
neg_acousticness.hist(alpha=0.5, bins=30)

# Key
ax7 = fig2.add_subplot(338)
ax7.set_xlabel("Key")
ax7.set_ylabel("Count")
ax7.set_title("Song Key Like Distribution")
pos_key.hist(alpha=0.5, bins=30)
ax8 = fig2.add_subplot(338)
neg_key.hist(alpha=0.5, bins=30)

# Instrumentalness
ax7 = fig2.add_subplot(339)
ax7.set_xlabel("Instrumentalness")
ax7.set_ylabel("Count")
ax7.set_title("Song Instrumentalness Like Distribution")
pos_instrumentalness.hist(alpha=0.5, bins=30)
ax8 = fig2.add_subplot(339)
neg_instrumentalness.hist(alpha=0.5, bins=30)


# -------

cc  ==  DecisionTreeClassifierDecision (min_samples_split=100)
# ---
features  = ["danceability", "loudness", "valence", "energy", "instrumentalness", "acousticness", "key", "speechiness", "duration_ms"]
# ----

x_trainx_train  ==  traintrain[[featuresfeatures]
y_train = train["target"]

x_test = test[features]
y_test = test["target"]

# ------
dt = c.fit(x_train,y_train)
def show_tree(tree,features,path):
    f = io.StringIO()
    export_graphviz(tree, out_file=f , feature_names=features)
    pydotplus.graph_from_dot_data(f.getvalue()).write_png(path)
    img = misc.imread(path)
    plt.rcParams["figure.figsize"]= (20,20)
    plt.imshow(img)
# ---
show_tree(dt, features, 'dec_tree_01.png')
#----
y_pred = c.predict(x_test)
y_pred

# ----
from sklearn.metrics import accuracy_score
score = accuracy_score(y_test,y_pred)*100

# ----
print("Accuracy (Using Decision Tree) : ", round(score,1), "%")
# ----


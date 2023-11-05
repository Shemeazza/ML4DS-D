
import numpy as np
import pandas as pd
from sklearn.model_selection import StratifiedShuffleSplit, train_test_split
import hashlib
import os


TRAINING_PATH = os.path.join("datasets", "train.csv")

def load_training_data(training_path=TRAINING_PATH):
    csv_path = training_path
    return pd.read_csv(csv_path)

training = load_training_data()


def test_set_check(identifier, test_ratio, hash=hashlib.md5):
    return hash(np.int64(identifier)).digest()[-1] < 256 * test_ratio

def train_test_split_by_id(data, test_ratio, id_column):
    ids = data[id_column]
    in_test_set = ids.apply(lambda id_: test_set_check(id_, test_ratio))
    return data.loc[~in_test_set], data.loc[in_test_set]

training_with_id = training.reset_index()   # adds an `index` column
train_set, test_set = train_test_split_by_id(training_with_id, 0.2, "index")

training_with_id["id"] = training["Year"] * 1000 + training["Month"]
train_set, test_set = train_test_split_by_id(training_with_id, 0.2, "id")


train_set, test_set = train_test_split(training, test_size=0.2, random_state=69)

training["Consumer_type"] = pd.cut(training["Consumption"],
                               bins=[0, 2, 4, 5, 6., np.inf],
                               labels=[1, 2, 3, 4, 5])


split = StratifiedShuffleSplit(n_splits=1, test_size=0.2, random_state=69)
for train_index, test_index in split.split(training, training["Consumer_type"]): # this line of code is broken on my machine becouse i don't have a latest pandas version and i cant update it for whatever reason
    stratifiedfd_train_set = training.loc[train_index]
    stratified_test_set = training.loc[test_index]
        
def consumer_type_proportions(data):
    return data["Consumer_type"].value_counts() / len(data)

train_set, test_set = train_test_split(training, test_size=0.2, random_state=69)

compare_props = pd.DataFrame({
    "Overall": consumer_type_proportions(training),
    "Stratified": consumer_type_proportions(stratified_test_set),
    "Random": consumer_type_proportions(test_set),
}).sort_index()
compare_props["Rand. %error"] = 100 * compare_props["Random"] / compare_props["Overall"] - 100
compare_props["Strat. %error"] = 100 * compare_props["Stratified"] / compare_props["Overall"] - 100

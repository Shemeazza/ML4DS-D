import sys
assert sys.version_info >= (3, 5)

import sklearn 
assert sklearn.__version__ >= "0.20"

import numpy as np
import os
import urllib.request
import pandas as pd
import matplotlib
import numpy
import matplotlib as mpl
import matplotlib.pyplot as plt

# %matplotlib inline
mpl.rc('axes', labelsize = 14)
mpl.rc('xtick', labelsize = 12)
mpl.rc('ytick', labelsize = 12)

PROJECT_ROOT_DIR = "."
CHAPTER_ID  = "Water Bill Usage"
IMAGES_PATH = os.path.join(PROJECT_ROOT_DIR, "images", CHAPTER_ID)
os.makedirs(IMAGES_PATH, exist_ok=True)

def save_fig(fig_id, tight_layout=True, fig_extension="png", resolution=300 ):
    path = os.path.join(IMAGES_PATH, fig_id + "." + fig_extension)
    print("Saving figure", fig_id)
    if tight_layout:
        plt.tight_layout()
    plt.savefig(path, format = fig_extension, dpi = resolution)

TRAINING_PATH = os.path.join("datasets", "train.csv")

def load_training_data(training_path=TRAINING_PATH):
    csv_path = TRAINING_PATH
    return pd.read_csv(csv_path)

training = load_training_data()

training.head()
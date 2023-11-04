import sys
assert sys.version_info >= (3, 5)
import sklearn 
assert sklearn.__version__ >= "0.20"
import os
import matplotlib
import matplotlib as mpl
import matplotlib.pyplot as plt
import Training

    """
    Im really bad a python so a lot of code was 'borrowed' from our proffesors if you think you can improve it give it a go 
    also im never again writing a code at 5am 
    """









# %matplotlib inline                    #uncomment this line if using Jupyter or google collab
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



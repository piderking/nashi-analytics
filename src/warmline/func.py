import os
import matplotlib.pyplot as plt



def save(fo: __file__):
    plt.savefig("images/warmline/{}.png".format(os.path.basename(fo).split(".py")[0]))

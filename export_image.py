import plotly.graph_objects as go
import os
from datetime import datetime
import pytz


def create_folder():
    folder = "images"
    if not os.path.exists(folder):
        os.mkdir(folder)
       
    now = datetime.now(pytz.timezone('Europe/Berlin'))
    dt_string = now.strftime("%d_%m_%Y-%H_%M_%S")
    complete_path = folder + '/' + dt_string

    os.makedirs(complete_path)
    return complete_path

def export(fig, current_path, filename):
    #display chart
    fig.show()

    #export chart
    #fig.write_image(current_path + "/" + filename + ".svg")
#Visualization for project
from create_image import *
from export_image import *

current_path = create_folder()

#fig = create_random_chart()
fig = create_gauge_chart(110, "Gauge Chart Example", 100, 0, 200, 0.05, 0.2, 0.8)

filename = "fig1"
export(fig, current_path, filename)
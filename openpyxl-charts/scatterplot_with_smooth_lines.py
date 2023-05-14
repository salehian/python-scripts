import matplotlib.pyplot as plt
from openpyxl import Workbook
from openpyxl.drawing.image import Image

# create some data
x_data = [i for i in range(1, 51)]
y_data = [i**0.5 for i in range(1, 51)]

# create a scatter plot with smooth lines
fig, ax = plt.subplots()
ax.plot(x_data, y_data, linestyle='-', linewidth=1, color='blueviolet')

# add labels and title
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_title('Scatter Plot with Smooth Lines')

# save the plot as an image
fig.savefig('scatter_plot.png')

# create a new workbook and worksheet
wb = Workbook()
ws = wb.active

# insert the image into the worksheet
img = Image('scatter_plot.png')
ws.add_image(img, 'A1')

# save the workbook
wb.save('scatter_plot_with_smooth_lines.xlsx')
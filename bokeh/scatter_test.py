from bokeh.plotting import figure, output_file, show, save, ColumnDataSource
from bokeh.models.tools import HoverTool
from bokeh.transform import factor_cmap
from bokeh.palettes import mpl
from bokeh.embed import components
import pandas

# Read in csv
df = pandas.read_csv("cars.csv")

# Create ColumnDataSource from data frame
source = ColumnDataSource(df)

# Use for basic data input:
#cars = df["Car"]
#hps = df["Horsepower"]

# Car list variables
car_list = source.data["Car"].tolist()
hp_list = source.data["Horsepower"].tolist()

# p = Scatter(df, x="X", y="Y", title="Tempterature Observations", xlabel="Date", ylabel="Temperature")

output_file("cars.html")

# Add plot
p = figure(
	title="Cars with Top Horsepower",
	x_axis_label="Horsepower",
	y_axis_label="Car",
	y_range=car_list,
	plot_width=800,
	plot_height=600,
	tools="box_select,reset,save"
)

# Render glyph
# NOTES:
# - Using "source=ColumnDataSource(pandas.dataframe)" allows for reading directly from CSV titles
# - Enables ____
p.hbar(
	y="Car",
	right="Horsepower",
	left=0,
	height=0.4,
	fill_color=factor_cmap("Car", palette=mpl['Plasma'][len(car_list)], factors=car_list),
	fill_alpha=0.8,
	source=source,
	legend="Car"
)

# Add Legend
p.legend.orientation = "vertical"
p.legend.location = "top_right"
p.legend.label_text_font_size = "10px"

# Add Hover Tooltips
# NOTES:
# - Access CSV attributes with "@title" within HTML
hover = HoverTool()
hover.tooltips = """
	<div>
		<h3>@Car</h3>
		<div><strong>Price: </strong>@Price</div>
		<div><strong>Horsepower: </strong>@Horsepower</div>
		<div><img src="@Image" alt="" width="200" /></div>
	</div>
"""

p.add_tools(hover)

# Show results
#show(p)

# Save results
save(p)

# Print out components as HTML and Javascript
script, div = components(p)

#print(script)

#print(div)
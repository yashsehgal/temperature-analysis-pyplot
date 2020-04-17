# importing modules
import io
import numpy as np
import matplotlib.pyplot as plotter
import pandas as pandas

# opening data CSV File
WEATHER_INDEX_DATA = pandas.read_csv("weather_1.csv")
INDIA_DATA = WEATHER_INDEX_DATA[WEATHER_INDEX_DATA.country == "India"]
PAKISTAN_DATA = WEATHER_INDEX_DATA[WEATHER_INDEX_DATA.country == "Pakistan"]
AUSTRALIA_DATA = WEATHER_INDEX_DATA[WEATHER_INDEX_DATA.country == "Australia"]
# plotting graphs
plotter.scatter(AUSTRALIA_DATA.Date, AUSTRALIA_DATA.temp, color="yellow")
plotter.scatter(INDIA_DATA.Date, INDIA_DATA.temp, color="red")
plotter.scatter(PAKISTAN_DATA.Date, PAKISTAN_DATA.temp, color="blue")
plotter.title("Temperature Rate Index")
plotter.xlabel("Time")
plotter.ylabel("Temperature in Celcius")
plotter.legend(["India", "Pakistan", "Australia"])
plotter.show()

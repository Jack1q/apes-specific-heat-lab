# -*- coding: utf-8 -*-
import matplotlib.pyplot as plot

# X var
times = [x for x in range(0, 630, 30)] # 0 - 600, incremented by 30
# Y vars
water_temps = [20, 20.9, 21.5, 21.9, 22.4, 22.8, 23.4, 23.9, 24.5, 25.1, 25.7, 26.3, 26.9, 27.6, 28.2, 28.8, 29.5, 30, 30.8, 31.1, 31.7]
black_sand_temps = [21.9, 35, 45.6, 53.6, 60.9, 67.4, 73, 78, 82.5, 86.8, 90, 93.6, 96.7, 99.2, 101.9, 105, 105, 106, 109, 110, 111.5]
white_sand_temps = [21.7, 22.1, 22.8, 23.1, 25, 26.5, 28.2, 30, 32, 33.1, 35.5, 37.5, 39.5, 41.2, 43, 44.8, 46.5, 61.7, 62, 62.7, 64.6]
soil_temps = [21.4, 21.7, 22.2, 23, 23.8, 24.8, 25.8, 26.8, 27.8, 28.9, 30, 31, 32, 32.8, 33.7, 34.8, 35.8, 36.3, 37.3, 37.7, 38.3]

plot.scatter(x=times, y=water_temps, label='Water', color='blue')
plot.scatter(x=times, y=black_sand_temps, label='Black Sand', color='black')
plot.scatter(x=times, y=white_sand_temps, label='White Sand', color='tan')
plot.scatter(x=times, y=soil_temps, label='Soil', color='brown')
plot.xlabel('Time (s)')
plot.ylabel("Temperature (\N{DEGREE SIGN}C)")
plot.ylim(bottom=10, top=120)
plot.grid('on',alpha=0.25, linewidth=2)

plot.legend()
plot.show()

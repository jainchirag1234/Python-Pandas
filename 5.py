import pandas as pd

colors = pd.read_csv('C:\\Users\\Book1.csv')  # Make sure this path and file name are correct
colors.to_html('NiceColor.html')  # Corrected 'color' to 'colors' and added .html extension


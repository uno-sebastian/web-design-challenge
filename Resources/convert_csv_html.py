import pandas as pd 
  
# read csv file named "cities" 
cities = pd.read_csv("cities.csv") 

# save as html file 
cities.to_html("cities.html", index = False) 
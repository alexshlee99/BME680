import matplotlib.pyplot as plt
import pandas as pd

file = "/home/pi/firstsensor/pollution_data.csv"

# Initialize data file into dataframe
df_data = pd.read_csv(file, header=0, names=["Date", "Temperature", "Humidity", "Resistance"], delimiter=";", error_bad_lines=False)


# Weekly data date vs. Voc
df_date = df_data.loc[df_data["Date"].str.contains("2020-02-27")] 
print(df_date)

#plt.plot(list(df_date["Date"]), list(df_data["Resistance"]))
#plt.show()

import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter
import pandas as pd
from datetime import datetime

file = "/Users/sang-hyunlee/PycharmProjects/bme680/BME680/pollution_data.csv"

# Initialize data file into dataframe
df_data = pd.read_csv(file, header=0, names=["Date", "Temperature", "Humidity", "Resistance"], delimiter=";",
                      error_bad_lines=False
                      , skiprows=12)

# Initialize DataFrames for sensor data per day
df_date1 = df_data.loc[df_data["Date"].str.contains("2020-02-27")]
df_date1["Date"] = pd.to_datetime(df_date1["Date"], format='%Y-%m-%d %H:%M:%S.%f')
df_date1["Date"] = df_date1["Date"].dt.time

df_date2 = df_data.loc[df_data["Date"].str.contains("2020-02-28")]
df_date2["Date"] = pd.to_datetime(df_date2["Date"], format='%Y-%m-%d %H:%M:%S.%f')
df_date2["Date"] = df_date2["Date"].dt.time


df_date3 = df_data.loc[df_data["Date"].str.contains("2020-02-29")]
df_date3["Date"] = pd.to_datetime(df_date3["Date"], format='%Y-%m-%d %H:%M:%S.%f')
df_date3["Date"] = df_date3["Date"].dt.time

df_date4 = df_data.loc[df_data["Date"].str.contains("2020-03-01")]
df_date4["Date"] = pd.to_datetime(df_date4["Date"], format='%Y-%m-%d %H:%M:%S.%f')
df_date4["Date"] = df_date4["Date"].dt.time

df_date5 = df_data.loc[df_data["Date"].str.contains("2020-03-02")]
df_date5["Date"] = pd.to_datetime(df_date5["Date"], format='%Y-%m-%d %H:%M:%S.%f')
df_date5["Date"] = df_date5["Date"].dt.time

df_date6 = df_data.loc[df_data["Date"].str.contains("2020-03-03")]
df_date6["Date"] = pd.to_datetime(df_date6["Date"], format='%Y-%m-%d %H:%M:%S.%f')
df_date6["Date"] = df_date6["Date"].dt.time

df_date7 = df_data.loc[df_data["Date"].str.contains("2020-03-04")]
df_date7["Date"] = pd.to_datetime(df_date7["Date"], format='%Y-%m-%d %H:%M:%S.%f')
df_date7["Date"] = df_date7["Date"].dt.time

df_date8 = df_data.loc[df_data["Date"].str.contains("2020-03-05")]
df_date8["Date"] = pd.to_datetime(df_date8["Date"], format='%Y-%m-%d %H:%M:%S.%f')
df_date8["Date"] = df_date8["Date"].dt.time

df_date9 = df_data.loc[df_data["Date"].str.contains("2020-03-06")]
df_date9["Date"] = pd.to_datetime(df_date9["Date"], format='%Y-%m-%d %H:%M:%S.%f')
df_date9["Date"] = df_date9["Date"].dt.time

# Plot Time of Day vs. Resistance
ax = plt.gca()
ax.xaxis.set_major_formatter(DateFormatter('%H:%M:%S.%f'))
pd.plotting.register_matplotlib_converters()
ax.xaxis_date()


ay = df_date2.plot(x="Date", y="Resistance")
df_date1.plot(ax=ay, x="Date", y="Resistance")
df_date3.plot(ax=ay, x="Date", y="Resistance")
df_date4.plot(ax=ay, x="Date", y="Resistance")
df_date5.plot(ax=ay, x="Date", y="Resistance")
df_date6.plot(ax=ay, x="Date", y="Resistance")
df_date7.plot(ax=ay, x="Date", y="Resistance")
df_date8.plot(ax=ay, x="Date", y="Resistance")
df_date9.plot(ax=ay, x="Date", y="Resistance")


plt.legend(["2020-02-28", "2020-02-27", "2020-02-29", "2020-03-01", "2020-03-02", "2020-03-03", "2020-03-04",
            "2020-03-05", "2020-03-06"], loc='lower left', prop={'size': 6})
plt.xlabel("Time of Day")
plt.ylabel("Resistance")
plt.title("Time of Day vs. Resistance")

plt.savefig("timeofdayvsrez.png")

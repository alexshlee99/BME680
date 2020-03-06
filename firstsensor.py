import bme680
import time
import csv 
import datetime 

try: 
	sensor = bme680.BME680(bme680.I2C_ADDR_PRIMARY)
except IOError: 
	sensor = bme680.BME680(bme680.I2C_ADDR_SECONDARY)
	print("Im using secondary") 

sensor.set_humidity_oversample(bme680.OS_2X)
sensor.set_pressure_oversample(bme680.OS_4X)
sensor.set_temperature_oversample(bme680.OS_8X)
sensor.set_filter(bme680.FILTER_SIZE_3)

sensor.set_gas_status(bme680.ENABLE_GAS_MEAS)
sensor.set_gas_heater_temperature(320)
sensor.set_gas_heater_duration(150)
sensor.select_gas_heater_profile(0)

start = -1

csv_file = open("pollution_data.csv", "a")
csv_writer = csv.writer(csv_file, delimiter=";")
while True:
	if sensor.get_sensor_data():
		output = "{0:.2f} C,{1:.2f} hPa,{2:.2f} %RH".format(sensor.data.temperature, sensor.data.pressure, sensor.data.humidity)
		if sensor.data.heat_stable:
			print("{0},{1} Ohms".format(output, sensor.data.gas_resistance))
			csv_writer.writerow([datetime.datetime.now(), sensor.data.temperature, sensor.data.humidity, sensor.data.gas_resistance]) 
		else:
			print(output)
		# update the time 
		if start== -1:
			print("first value")
		else:
               		print(time.time() - start)
		# get updated time
		start = time.time()  
	time.sleep(1) 





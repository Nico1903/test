import requests 
import json
import csv
import os

response = requests.get("http://api.openweathermap.org/data/2.5/forecast?q=Augsburg,De&APPID=ca9d175f389c46b262b56ef51ef64436")

if response.status_code == 200:
    print("alles ok")

else:
    print ("nicht ok") 


#fs= open("test.json", "w+")
#json.dump(response.json(), fs)
#fs.close()

weather_json =response.json()

#print(weather_json["city"]["name"])
#print(weather_json["city"]["country"])

#print(weather_json['list'][2]['dt'])
#print(weather_json['list'][2]['main']['temp'])

#print(weather_json['list'][3]['dt'])
#print(weather_json['list'][3]['main']['temp'])

for datapoint in weather_json["list"]:
    print("ID: " + str(weather_json["list"].index(datapoint)))   
    print("Date: " + str(datapoint["dt_txt"]))
    print("Temp: " + str(datapoint["main"]["temp"]))
    print("Weatherdata " + str(datapoint["weather"]))
    print("Weatherdata " + str(datapoint["weather"][0]["id"]))
    print("Weatherdata " + str(datapoint["weather"][0]["main"]))
    print("Weatherdata " + str(datapoint["weather"][0]["description"]))
    print("Weatherdata " + str(datapoint["weather"][0]["icon"]))


#single_car = {"doors": "6",
              #"color": "green"}


#cars = [{"doors": "4",
 #          "color": "black"},
  #        {"doors": "5",
   #        "color": "white"},
    #      {"doors": "6",
     #      "color": "green"}]
#print(cars[2])


#index = cars.index(single_car)
#print(index)

#for car in cars:
 #   print(car["doors"])





#header = "id;date;temp;weather-id"
#print(header)
#for datapoint in weather_json['list']:
 #   print(str(weather_json['list'].index(datapoint)) + ";" + str(datapoint['dt_txt']) + ";" + str(datapoint['main']['temp']) + ";" + str(datapoint['weather'][0]['id']))



f = open("data.csv" , "w+" , newline="")

header = ["id" , "date" , "temp" , "weather-id"] 
writer = csv.writer(f, delimiter=";")
writer.writerow(header)

for datapoint in weather_json['list']:
    #datapointrow = ["str(weather_json['list'].index(datapoint)) +" , "str(datapoint['dt_txt'])" , "str(datapoint['main']['temp']) +" , "str(datapoint['weather'][0]['id'])" ]
    list = [str(weather_json['list'].index(datapoint))]
    dt_txt = [str(datapoint['dt_txt'])]
    main = [str(datapoint['main']['temp'])]
    id= [str(datapoint['weather'][0]['id'])]
    
    writer.writerow(list + dt_txt + main + id)

f.close()

############################################################
    
os.remove("data.csv")


f = open("data.csv" , "w+" , newline="")

header = ["id" , "date" , "temp" , "weather-id"] 
writer = csv.writer(f, delimiter=";")
writer.writerow(header)

for datapoint in weather_json['list']:
    #datapointrow = ["str(weather_json['list'].index(datapoint)) +" , "str(datapoint['dt_txt'])" , "str(datapoint['main']['temp']) +" , "str(datapoint['weather'][0]['id'])" ]
    list = [str(weather_json['list'].index(datapoint))]
    dt_txt = [str(datapoint['dt_txt'])]
    main = [str(datapoint['main']['temp'])]
    id= [str(datapoint['weather'][0]['id'])]
    
    writer.writerow(list + dt_txt + main + id)

f.close()





#employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
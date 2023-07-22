import urllib.request as request
import json
import csv
import re
src = "https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json"

def saveAttraction(url):
    with request.urlopen(url) as response:
        data = json.load(response)
    with open("attraction.csv", mode="w", newline="") as file:
        writer = csv.writer(file)
        districts = ["中正區", "萬華區", "中⼭區", "⼤同區", "⼤安區", "松⼭區", "信義區", "⼠林區", "文⼭區", "北投區", "內湖區", "南港區"]    
        for item in data["result"]["results"]:
            for district in districts:
                if re.search(district, item["address"]):
                    foundDistrict = district
            attraction = [item["stitle"], foundDistrict, item["longitude"], item["latitude"],"https" + item["file"].split("https")[1]]
            writer.writerow(attraction)    
saveAttraction(src)

def MrtAttraction(url):
    with request.urlopen(url) as response:
        data = json.load(response)
    with open("mrt.csv", mode="w", newline="") as file:
        writer = csv.writer(file)
        MRT={}
        for item in data["result"]["results"]:
            if item["MRT"] not in MRT:
                MRT[item["MRT"]] = [item["stitle"]]
            else:
                MRT[item["MRT"]].append(item["stitle"])
        
        for key, value in MRT.items():
                writer.writerow([key] + value) 

MrtAttraction(src)

            


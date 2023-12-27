import socket
import requests
from ip2geotools.databases.noncommercial import DbIpCity
from geopy.distance import distance

def printDetails(ip):
    res = DbIpCity.get(ip, api_key="free")
    print(f"IP ADDRESS :  {res.ip_address}")
    print(f"LOCATION : {res.city}, {res.region},{res.country}")
    
    
ipadd=input("Enter IP : ")
printDetails(ipadd)
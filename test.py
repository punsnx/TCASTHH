import random 
import sys
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import tkinter as tk
import time
import python_weather
import asyncio

async def getweather(c):
    # declare the client. format defaults to metric system (celcius, km/h, etc.)
    client = python_weather.Client(format=python_weather.METRIC)

    # fetch a weather forecast from a city
    weather = await client.find(c)

    # returns the current day's forecast temperature (int)
    print(weather.current.temperature)


    # close the wrapper once done
    await client.close()


named_tuple = time.localtime() # get struct_time
time_string = time.strftime("%m/%d/%Y %H:%M:%S", named_tuple)

ask = str(input("Do you want to have some food [yes/no]: "))
if ask == "yes" :
    askcity = str(input("Your City : "))
    if len(askcity) > 0 :
        print(time_string)
        if __name__ == "__main__":
            loop = asyncio.get_event_loop()
            loop.run_until_complete(getweather(ask))

else :
    print(time_string + " Sad hmmm :) thanks ")

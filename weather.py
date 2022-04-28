# import the module
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

ask
if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(getweather())


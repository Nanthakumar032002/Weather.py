import tkinter as tk
import requests
import time

def getweather(event):
    city = textfield.get()
    api_key = '1482db6750598e48abd1172b84a0c8ad'
    api_url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'

    try:
        json_data = requests.get(api_url).json()
        if json_data.get('cod') != 200:
            raise ValueError(f"Error: {json_data.get('message', 'Unable to retrieve weather data')}")
        
        condition = json_data['weather'][0]['main']
        temp = int(json_data['main']['temp'] - 273.15)
        min_temp = int(json_data['main']['temp_min'] - 273.15)
        max_temp = int(json_data['main']['temp_max'] - 273.15)
        pressure = json_data['main']['pressure']
        humidity = json_data['main']['humidity']
        wind = json_data['wind']['speed']
        sunrise = time.strftime('%H:%M:%S', time.gmtime(json_data['sys']['sunrise']))
        sunset = time.strftime('%H:%M:%S', time.gmtime(json_data['sys']['sunset']))

        final_info = f"{condition}\n{temp}°C"
        final_data = (
            f"\nMin Temp: {min_temp}°C\nMax Temp: {max_temp}°C\n"
            f"Pressure: {pressure} hPa\nHumidity: {humidity}%\n"
            f"Wind: {wind} m/s\nSunrise: {sunrise}\nSunset: {sunset}"
        )
        label1.config(text=final_info)
        label2.config(text=final_data)
    except Exception as e:
        label1.config(text="Error")
        label2.config(text=str(e))

# Setup the main Tkinter window
canvas = tk.Tk()
canvas.geometry('600x500')
canvas.title('WEATHER APP')

f = ('poppins', 15, 'bold')
t = ('poppins', 35, 'bold')

textfield = tk.Entry(canvas, font=t)
textfield.pack(pady=20)
textfield.focus()
textfield.bind('<Return>', getweather)

label1 = tk.Label(canvas, font=t)
label1.pack()

label2 = tk.Label(canvas, font=f)
label2.pack()

canvas.mainloop()

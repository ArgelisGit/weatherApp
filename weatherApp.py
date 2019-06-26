import tkinter as tk
from tkinter import font
import requests

HEIGHT = 700
WIDTH = 800


def test_function(entry):
    print("This is your entry, ", entry)


def format_response(weather):
    try:
        name = (weather['name'])
        description = (weather['weather'][0]['description'])
        temp = (weather['main']['temp'])

        final_str = 'City: %s \nCondition: %s \nTemperature (F): %s' % (name, description, temp)
    except:
        final_str = 'There was a problem with your entry'

    return final_str


def get_weather(city):
    weather_key = '1497791cfd25c958e405af23b8087fac'
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {'APPID': weather_key, 'q': city, 'units': 'imperial'}
    response = requests.get(url, params=params)
    weather = response.json()

    label['text'] = format_response(weather)


# 1497791cfd25c958e405af23b8087fac
# api.openweathermap.org/data/2.5/forecast?q={city name},{country code}
root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

# background_image = tk.PhotoImage(file='pexels-photo-132037.jpeg')
# background_label1 = tk.Label(root, image=background_image)
# background_label1.place(relwidth=1, relheight=1)

frame = tk.Frame(root, bg='#80c1ff', bd=4)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry = tk.Entry(frame, font=40)
entry.place(relwidth=0.65, relheight=1)

button = tk.Button(frame, text="Get Weather", font=40, command=lambda: get_weather(entry.get()))
button.place(relx=0.7, rely=0, relwidth=0.3, relheight=1)

lower_frame = tk.Frame(root, bg='#80c1ff', bd=4)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

label = tk.Label(lower_frame, font=('Courier', 16))
label.place(relwidth=1, relheight=1)

root.mainloop()

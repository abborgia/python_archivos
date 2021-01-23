from tkinter import *
import requests
import json

# 64ca9e0aa3b548976ee5e53e7dc49c7b
# api.openweathermap.org/data/2.5/weather?q={city name},{state code},{country code}&appid={API key}

def mostrar_respuestas(clima):
    nombre_ciudad =clima["name"]
    desc =clima["weather"][0]["description"]
    temp =clima["main"]["temp"]

    ciudad["text"] = nombre_ciudad
    temperatura["text"] = str(int(temp))+°C #temp con °C
    descripcion["text"] = desc



def clima_JSON(ciudad):
    try:
        APIkey= "64ca9e0aa3b548976ee5e53e7dc49c7b"
        URL="http://api.openweathermap.org/data/2.5/weather"
        parametros={"APPID" : APIkey, "q" : ciudad, "units" : "metric", "lang" : "es"}
        response = requests.get(URL, params = parametros)
        clima = response.json()
        datos = json.dumps(clima, indent=4)
        #datos2 = json.loads(clima)
        print(clima)
        print(datos)
        #print(datos2)
        print(clima["name"])
        print(clima["weather"][0]["description"])
        print(clima["main"]["temp"])
        mostrar_respuestas(clima)
    except:
        ciudad["text"] = "Intenta nuevamente"


    mostrar_respuestas(clima)

ventana = Tk()
ventana.geometry("350x550")

texto_ciudad = Entry(ventana, font=("Courier",20, "normal"), justify= "center")
texto_ciudad.pack(padx=30, pady=30)

obtener_clima = Button(ventana, text="Obtener Clima" ,font=("Courier",20, "normal"), command = lambda: clima_JSON(texto_ciudad.get()))
obtener_clima.pack()

ciudad = Label(ventana, font=("Courier",20, "normal"))
ciudad.pack(padx=30, pady=30)

temperatura = Label(ventana,font=("Courier",50, "normal"))
temperatura.pack(padx=10, pady=10)

descripcion = Label(ventana,font=("Courier",20, "normal"))
descripcion.pack(padx=10, pady=10)


ventana.mainloop()






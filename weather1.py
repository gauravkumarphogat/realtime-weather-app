from tkinter import *
from tkinter import ttk
import requests

# Function to get data
def data_get():
    city = city_name.get()  # Retrieve the actual city name from the StringVar
    data = requests.get(f"YOUR_WEATHER_API").json()

    w_label1.config(text=data["weather"][0]["main"])
    temp_label1.config(text=str(int(data["main"]["temp"]-273.15)))

win = Tk()
win.title("Gaurav Weather Forecast App")
win.config(bg="light blue")
win.geometry("500x500")

name_label = Label(win, text="Gaurav Weather Forecast App",font=("TIME NEW ROMAN",20,"bold"))
name_label.place(x=25,y=50,height=50,width=450)

# Combo box (multiple boxes that we use for locations)
city_name = StringVar()
list_name = ["Andhra Pradesh","Arunachal Pradesh ","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal","Andaman and Nicobar Islands","Chandigarh","Dadra and Nagar Haveli","Daman and Diu","Lakshadweep","National Capital Territory of Delhi","Puducherry"]
com = ttk.Combobox(win, text="Gaurav Weather Forecast App", values=list_name, font=("TIME NEW ROMAN",15,"bold"), textvariable=city_name)
com.place(x=45,y=120,height=50,width=400)

# Climate description
w_label = Label(win, text="Weather Climate", font=("TIME NEW ROMAN",12,"bold"))
w_label.place(x=25,y=300,height=35,width=200)
w_label1 = Label(win, text="", font=("TIME NEW ROMAN",12,"bold"))
w_label1.place(x=235,y=300,height=35,width=200)

# Temperature
temp_label = Label(win, text="Temperature", font=("TIME NEW ROMAN",12,"bold"))
temp_label.place(x=25,y=350,height=35,width=200)
temp_label1 = Label(win, text="", font=("TIME NEW ROMAN",10,"italic"))
temp_label1.place(x=235,y=350,height=35,width=200)

# Button
done_button = Button(win, text="Done", font=("TIME NEW ROMAN",15,"bold"), command=data_get)
done_button.place(y=190, height=50, width=100, x=200)

win.mainloop()

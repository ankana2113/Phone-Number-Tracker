from tkinter import *
import phonenumbers
import folium
import webbrowser
from phonenumbers import carrier, geocoder
from opencage.geocoder import OpenCageGeocode

root = Tk()
root.title('Phone Number Tracker')
root.geometry('500x400+400+200')
root.resizable(width=True, height=True)
root.configure(bg='#96BFFF')

# Store the API Key in the key variable
# generate the api at https://opencagedata.com/api
key = '533a945ad486402a80385ae38a3905a3'


def track_num():
    enter_num = entry.get()
    # take input the phone number along with the country code
    # number = input("Enter the PhoneNumber with the country code : ")

    # Parse the phone number string to convert it into phone number format
    phoneNumber = phonenumbers.parse(enter_num)

    # Using the geocoder module of phonenumbers to print the Location
    yourLocation = geocoder.description_for_number(phoneNumber, lang="en")
    country.config(text=yourLocation)

    # Using the carrier module of phonenumbers to print the service provider name
    yourServiceProvider = carrier.name_for_number(phoneNumber, "en")
    service.config(text=yourServiceProvider)

    # Use opencage to get the latitude and longitude of the location
    query = str(yourLocation)
    results = OpenCageGeocode(key).geocode(query)

    # Assign the latitude and longitude values to the lat and lng variables
    lat = results[0]['geometry']['lat']
    lng = results[0]['geometry']['lng']
    # print('Latitude: {}'.format(lat))
    # print('Longitude: {}'.format(lng))

    # Getting the map for the given latitude and longitude
    myMap = folium.Map(location=[lat, lng], zoom_start=9)

    # Adding a Marker on the map to show the location name
    folium.Marker(location=[lat, lng], popup=yourLocation).add_to(myMap)

    # save map to html file to open it and see the actual location in map format
    myMap.save('Location.html')


def open_map():
    webbrowser.open('Location.html')


# logo = PhotoImage(file='logo.png')
# Label(root, image=logo, bg='#96BFFF').place(x=135, y=40)

# search = PhotoImage(file='search.png')
# Label(root, image=search, bg='#96BFFF').place(x=14, y=244)

heading = Label(root, text='Track Number', font='arial 20 bold', fg='#39281E', bg='#96BFFF')
heading.place(x=160, y=50)
# heading.pack(pady=5)

entry = StringVar()
enter_num = Entry(root, textvariable=entry, justify="center", width=20, bd=0, font='arial 20 bold', fg='white', bg='#2C3541')
enter_num.place(x=100, y=140)
# enter_num.pack(pady=5)

# search_btn = PhotoImage(file='search_btn.png')
btn = Button(root, cursor='hand2', text='Search', command=track_num, width=10, bg='#EE8C62', bd=0, activebackground='#ED8051')
btn.place(x=140, y=200)
# btn.pack(pady=5)

country_label = Label(text='Country: ', bg='#96BFFF', fg='black', font='arial 14 bold')
country_label.place(x=100, y=250)
country = Label(root, bg='#96BFFF', fg='black', font='arial 14 bold')
country.place(x=180, y=250)
# country.pack(pady=5)

service_label = Label(text='Service Provider: ', bg='#96BFFF', fg='black', font='arial 14 bold')
service_label.place(x=100, y=300)
service = Label(root, bg='#96BFFF', fg='black', font='arial 14 bold')
service.place(x=260, y=300)
# service.pack(pady=5)

open_map_btn = Button(root, text='Open Map', cursor='hand2', command=open_map, width=10, bg='#EE8C82', bd=0, activebackground='#ED8051')
open_map_btn.place(x=280, y=200)
# open_map_btn.pack(pady=5)

root.mainloop()

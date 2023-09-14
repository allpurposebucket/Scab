from tkinter import *
from PIL import ImageTk, Image
import customtkinter
from functools import partial
from summoner import Summoner
from api import get_champion_splash_art

def Home():
    print("Home!!")

def Champions():
    print("Champions function")

def Items():
    print("Items function")

def Runes():
    print("Runes function")

def SummonerSpells():
    print("Summoner Spells function")

def Settings():
    print("Settings function")

def About():
    print("About function")

def Search():
    print("Search function")

def button_callback(function):
    function()

app = customtkinter.CTk()
app.title("Scab Summoner Stats")
app.geometry(f"{1100}x{580}")

sum_var = customtkinter.StringVar()
SearchBar = Frame(app, width=50, height=20)
SearchBar.pack(side=RIGHT)
entry = customtkinter.CTkEntry(SearchBar, textvariable=sum_var, bg_color='red', corner_radius=0)
entry.pack(side=LEFT)
submit = customtkinter.CTkButton(SearchBar, text="Submit", command=partial(button_callback, Search))
submit.pack(side=RIGHT)

NavBar = Frame(app, bg="black", width=200, height=480)
NavBar.pack(side=TOP)

button_data = [
    ("Home", Home),
    ("Champions", Champions),
    ("Items", Items),
    ("Runes", Runes),
    ("Summoner Spells", SummonerSpells),
    ("Settings", Settings),
    ("About", About)
]

button_list = []

for button_name, button_function in button_data:
    button = Button(NavBar, text=button_name, bg="black", fg="white", width=20, height=2, command=partial(button_callback, button_function))
    button_list.append(button)
    button.pack(side=LEFT, pady=5)

summoner = Summoner("allpurposebucket")
highest_mastery = list(summoner.masteries.keys())[0]
get_champion_splash_art(highest_mastery)
bg = ImageTk.PhotoImage(Image.open(f"assets/{highest_mastery}.jpg"))

SummonerInfo = Frame(app, width=900, height=480)
SummonerInfo.pack(side=TOP)

SummonerName = Label(SummonerInfo, text=summoner.summoner_name, image=bg, font=("Arial", 20))
SummonerName.pack(side=TOP)


app.mainloop()

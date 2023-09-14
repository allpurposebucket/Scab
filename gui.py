from tkinter import *
from PIL import ImageTk, Image
import customtkinter
from functools import partial
from summoner import Summoner
from match import Match
from api import get_champion_splash_art
import threading

class SummonerGUI:
    def __init__(self):
        self.app = customtkinter.CTk()
        self.app.title("Scab Summoner Stats")
        self.app.geometry(f"{1100}x{580}")

        self.sum_var = customtkinter.StringVar()
        self.SearchBar = Frame(self.app, width=50, height=20)
        self.SearchBar.pack(side=RIGHT)
        self.entry = customtkinter.CTkEntry(self.SearchBar, textvariable=self.sum_var, bg_color='red', corner_radius=0)
        self.entry.pack(side=LEFT)
        self.submit = customtkinter.CTkButton(self.SearchBar, text="Submit", command=self.search_summoner)
        self.submit.pack(side=RIGHT)

        self.NavBar = Frame(self.app, bg="black", width=200, height=480)
        self.NavBar.pack(side=TOP)

        self.button_data = [
            ("Home", self.Home),
            ("Champions", self.Champions),
            ("Items", self.Items),
            ("Runes", self.Runes),
            ("Summoner Spells", self.SummonerSpells),
            ("Settings", self.Settings),
            ("About", self.About)
        ]

        self.button_list = []

        for button_name, button_function in self.button_data:
            button = Button(self.NavBar, text=button_name, bg="black", fg="white", width=20, height=2, command=partial(self.button_callback, button_function))
            self.button_list.append(button)
            button.pack(side=LEFT, pady=5)

        self.SummonerInfo = Frame(self.app, width=900, height=480)
        self.SummonerInfo.pack(side=TOP)

        self.SummonerName = Label(self.SummonerInfo, text="", font=("Arial", 20))
        self.SummonerName.pack(side=TOP)

        self.GameList = Listbox(self.SummonerInfo, width=40, height=10)
        self.GameList.pack(side=TOP)

    def search_summoner(self):
        summoner_name = self.sum_var.get()
        t = threading.Thread(target=fill_with_summoner, args=(self, summoner_name))
        t.start()

    def Home(self):
        print("Home!!")

    def Champions(self):
        print("Champions function")

    def Items(self):
        print("Items function")

    def Runes(self):
        print("Runes function")

    def SummonerSpells(self):
        print("Summoner Spells function")

    def Settings(self):
        print("Settings function")

    def About(self):
        print("About function")

    def button_callback(self, function):
        function()

def fill_with_summoner(gui, summoner_name):
    try:
        summoner = Summoner(summoner_name)
        highest_mastery = list(summoner.masteries.keys())[0]
        mastery_image_path = f"assets/{highest_mastery}.jpg"

        # Open the image
        mastery_image = Image.open(mastery_image_path)
        # Resize the image if necessary
        mastery_image = mastery_image.resize((1215, 717), Image.LANCZOS)  # Adjust width and height as needed
        # Convert to ImageTk.PhotoImage
        bg = ImageTk.PhotoImage(mastery_image)

        gui.SummonerName.config(text=summoner.summoner_name, image=bg)
        gui.SummonerName.image = bg  # Keep a reference to the image

        gui.GameList.delete(0, END)

        match_ids = summoner.matches[:5]
        for match_id in match_ids:
            match = Match(match_id)
            for summoner in match.summoners:
                game_entry = f"Summoner Name: {summoner.summoner_name}"
                gui.GameList.insert(END, game_entry)

    except Exception as e:
        print(e)
        print("Summoner fill failed")


if __name__ == "__main__":
    summoner_gui = SummonerGUI()
    summoner_gui.app.mainloop()

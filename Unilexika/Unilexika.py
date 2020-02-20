from tkinter import *
from tkinter import Button, Label, Entry, Listbox, Frame, Tk, Text
import sys

class unilexika(): #-----------------------------------------------Lexika Klasse----------------------------------------------------------------------------------------------------------

    def __init__(self):
        self.dateinamenliste = []
        self.infos = ""
        self.eingabe = ""
        self.main = Tk()
        self.main.title("Unilexika")
        self.main.geometry("700x450")
        self.main.minsize(700,450)
        self.main.configure(bg = "#00e6e6")
        self.box = Listbox(self.main, relief = "flat", bg = "#e6ffff")
        self.box.place(relx = 0, rely = 0, relheight = 1, relwidth = 0.3)
        self.anzeige = Text(self.main, relief = "flat", font = 40, bg =  "#e6ffff")
        self.anzeige.place(relx = 0.32, rely = 0.3, relheight = 0.7 ,relwidth = 0.68)
        self.lesen = Button(self.main, text = "Lesen", command = self.datei_öffnen, font = 25, relief = "flat", bg = "#0ca692", fg = "white", activeforeground = "white",  activebackground = "#0ca692")
        self.lesen.place(relx = 0.35, rely = 0.05, relwidth = 0.2, relheight = 0.15)
        self.eintragen = Button(self.main, text = "Eintrag erstellen", command = self.erstellen, font = 25, relief = "flat", bg = "#0ca692", fg = "white", activeforeground = "white",  activebackground = "#0ca692")
        self.eintragen.place(relx = 0.60, rely = 0.05, relwidth = 0.2, relheight = 0.15)
        self.beenden = Button(self.main, text = "Beenden", command = lambda: self.main.destroy(), font = 25, relief = "flat", bg = "#0ca692", fg = "white", activeforeground = "white",  activebackground = "#0ca692")
        self.beenden.place(relx = 0.85, rely = 0.05, relwidth = 0.13, relheight = 0.15)
        self.pruefung()
        self.main.mainloop()

    def pruefung(self):
        if len(self.dateinamenliste) == 0:
            self.f = open("Systemspeicher/Dateinamen.txt", "r")
            self.datei = open("Systemspeicher/Dateinamen.txt", "r")
            self.liste = open("Systemspeicher/Listennamen.txt", "r")
            self.zeile = 1
            self.zeilen = len(self.f.readlines())
            while self.zeile <= self.zeilen:
                self.dateinamenliste.append(self.datei.readline().strip())
                self.box.insert(END, self.liste.readline())
                self.zeile += 1
            self.f.close()
            self.liste.close()
            self.datei.close()
        

    def datei_öffnen(self):
        self.datei = open("Speicher/" + self.dateinamenliste[self.box.index("active")], "r")
        self.infos = self.datei.readlines()
        self.datei.close()
        self.anzeige.delete(1.0,END)
        self.anzeige.insert(END,*self.infos)
        
    
    def erstellen(self):
        self.new = Toplevel()
        self.new.configure(bg = "#00e6e6")
        self.lbl = Label(self.new, text = "Listenname:", font = 25, bg = "#00e6e6")
        self.lbl.place(relx = 0.1, rely = 0, relheight = 0.3, relwidth = 0.8 )
        self.listeneintragung = Entry(self.new, font = 100, bg = "#e6ffff")
        self.listeneintragung.place(relx = 0.2,rely = 0.3, relheight = 0.3, relwidth = 0.6)
        self.button = Button(self.new, text = "Weiter",command = self.texteintrag, relief = "flat", bg = "#0ca692", fg = "white", activeforeground = "white",  activebackground = "#0ca692")
        self.button.place(relx = 0.2, rely = 0.65, relwidth = 0.6, relheight = 0.3)
       
    
    def texteintrag(self):
        self.info = Toplevel()
        self.info.configure(bg = "#00e6e6")
        self.info.geometry("1000x600")
        self.text = Text(self.info, bg = "#e6ffff")
        self.text.place(relx = 0, rely = 0, relheight = 1, relwidth = 0.4)
        self.lbl = Label(self.info, text = "Dateiname:", font = 50, bg = "#00e6e6")
        self.lbl.place(relx = 0.45, rely = 0, relheight = 0.3, relwidth = 0.5)
        self.eintragung = Entry(self.info, bg = "#e6ffff")
        self.eintragung.place(relx = 0.45,rely = 0.35, relheight = 0.3, relwidth = 0.5)
        self.bestätigung = Button(self.info, text = "Fertig", command = self.einlesen, relief = "flat", bg = "#0ca692", fg = "white", activeforeground = "white",  activebackground = "#0ca692")
        self.bestätigung.place(relx = 0.45, rely = 0.7, relwidth = 0.5, relheight = 0.25)
       

    def einlesen(self):
        self.dateinamenliste.append(self.eintragung.get() + ".txt")
        self.box.insert(END, self.listeneintragung.get())
        self.liste = open("Systemspeicher/Listennamen.txt", "a")
        self.liste.write(self.listeneintragung.get() + "\n")
        self.liste.close()
        self.eintrag = open("Speicher/" + self.eintragung.get() + ".txt", "a")
        self.eintrag.write(self.text.get("1.0",END))
        self.eintrag.close()
        self.documentname = open("Systemspeicher/Dateinamen.txt", "a")
        self.documentname.write(self.eintragung.get() + ".txt\n")
        self.documentname.close()
        self.new.destroy()
        self.info.destroy()
        
unilexika()
        

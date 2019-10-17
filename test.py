from tkinter import *
 
class Damier(object):
    "Création du damier et des pions"
    
    def __init__(self) :
        "Méthode constructeur"
        self.x = 50
    
    def damier(self):
        "Création du damier"
        self.main_window = Tk()
        self.main_window.title("Jeu de dames")
        self.main_window.resizable(False, False)
 
        self.cadre_principal = Frame(self.main_window, bg = 'black')
        self.cadre_principal.grid()
 
        self.can = Canvas(self.cadre_principal, width = self.x * 10, height = self.x * 10, bg = "white")
        self.can.grid(row = 0, column = 0, columnspan = 2)
        for i in range(0, 10, 2) :
            for i2 in range(0, 10, 2):
                self.can.create_rectangle(self.x * i2, self.x * i, self.x * (i2 + 1), self.x * (i + 1), width = 2, fill = "black")
                self.can.create_rectangle(self.x * (i2 + 1), self.x * (i + 1), self.x * (i2 + 2), self.x * (i + 2), width = 2, fill = "black")
 
        self.creer_pions = Button(self.cadre_principal, text = "Activer les pions", bg = 'white', fg = 'black', font = ('Times', '14', 'bold'), relief = 'ridge', bd = 3, command = self.pions)
        self.creer_pions.grid(row = 1, column = 0, padx = 5, pady = 5, sticky = 'e')
 
        self.quitter = Button(self.cadre_principal, text = "Quitter", bg = 'white', fg = 'black', font = ('Times', '14', 'bold'), relief = 'ridge', bd = 3, command = self.main_window.destroy)
        self.quitter.grid(row = 1, column = 1, padx = 5, pady = 5, sticky = 'w')
 
        self.main_window.mainloop()
                
    def pions(self):
        "Création des pions"
        self.ajuster_pion = 5 if self.x <= 50 else 10
        print(self.ajuster_pion)
        for i in range(0, 10, 2) :
            self.color = 'maroon' if i >= 6 else 'ivory'
            for i2 in range(0, 10, 2):
                if i <= 2 or i >= 6 :
                    self.can.create_oval((self.x * i2) + self.ajuster_pion, (self.x * i) + self.ajuster_pion, (self.x * (i2 + 1)) - self.ajuster_pion, (self.x * (i + 1)) - self.ajuster_pion, width = 2, fill = self.color)
                    self.can.create_oval((self.x * (i2 + 1)) + self.ajuster_pion, (self.x * (i + 1)) + self.ajuster_pion, (self.x * (i2 + 2)) - self.ajuster_pion, (self.x * (i + 2)) - self.ajuster_pion, width = 2, fill = self.color)
 
#======== Main Program =======================
 
damier = Damier()
damier.damier()

from tkinter import*
import  os
import time
from sys import platform as _platform
import subprocess
Windows = Tk()
print("Waring : Inizialisation du jeu mode développeur")
for i in range(0,11):
    print("Compte a rebours :"+" "+str(i)+"/10")
    time.sleep(1)
    os.system('cls')

print("LOADING SUCCES ")
class MenuBar(Frame):
    def __init__(self,boss=None):
        Frame.__init__(self,borderwidth = 2,relief = GROOVE)
        fileMenu = Menubutton(self,Text = 'Fichier')
        fileMenu.pack(side = LEFT,padx = 5)
        mel = Menu(fileMenu)
        mel.add_command(Label = 'Options',underline = 0,command = boss.options)
        mel.add_command(Label = 'Restart',underline = 0,command = boss.reset)
        mel.add_command(Label = 'Terminer',underline = 0,command = boss.quit)
        fileMenu.configure(menu =  mel)
        helpMenu = Menubutton(self,Text = 'Aide')
        helpMenu.pack(side = LEFT,padx = 5)
        mel = Menu(helpMenu)
        mel.add_command(label = 'Principe du jeu',underline = 0,command = boss.principe)
        mel.add_command(label = 'A propos ...',underline = 0,command = boss.aPropos)
        helpMenu.configure(menu = mel)

class Panneau(Frame):
    def __init__(self,boss = None):
        self.nlig,self.ncol = 4,4
        self.can = Canvas(self, bg = 'dark olive green',borderwidth = 0,highlightthickness = 1)
        self.can.bind("<Button-1>",self.clic)
        self.can.pack()
        self.initJeu()
    def initJeu(self):
        self.etat = []
        for i  in range(12):
            self.etat.append([0] * 12)
    def redim(self,Event):
        self.width,self.height = Event.width -4, Event.height-4
        self.traceGrille()
    
    def traceGrille(self):
       lmax= self.width/self.ncol
       hmax= self.height/self.nlig
       self.cote = min(lmax,hmax)
       larg, haut = self.cote*self.ncol, self.cote*self.nlig
       self.can.configure(width = larg, height = haut)
       self.can.delete(ALL)
       s = self.cote
       for l in range(self.nlig - 1):
             self.can.create_line(0,s,larg,s,fill="white")
             s+=self.cote
             for c in range(self.ncol -1):
                 self.can.create_line(s,0,s,haut,fill="white")
                 s+=self.cote
          
                
       for l in range(self.nlig):
         for c in range(self.ncol):
            x1= c * self.cote +5
            x2 = (c+1) * self.cote -5
            y1 = l * self.cote +5
            y2 = (l+1) * self.cote +5
            cou1 = ["white","black",] [self.etat[l][c]]
            self.can.create_oval(x1,y1,x2,y2,outline="grey", width=l,fill = cou1)

    def click(self,Event):
          for l in range(lig -1, lig+2):
              if l <0 or l >= self.nlig:
                  continue
              for c in range(col -1,col +2):
                  if c <0 or c >= self.ncol:
                      continue
                  if l == lig and c == col:
                      continue
                  self.etat[l][c] = not (self.etat[l][c])
          self.traceGrille()

class Ping(Frame):

    def __init__(self):
        Frame.__init__(self)
        self.master.geometry("400x300")
        self.master.title("Jeu de Ping")
        self.mbar = MenuBar(self)
        self.mbar.pack(side = TOP,expand = No,fill= X)
        self.jeu = Panneau(self)
        self.jeu.pack(expand = YES, fill = BOTH,padx = 8,pady = 8)
        self.pack()
    def options(self):
        opt = Toplevel(self)
        curL = Scale(opt,length = 200,Label = "Nombre de lignes : ",orient = HORIZONTAL,from_ = 1,to = 12, COMMAND = self.majLignes)
        curL.set(self.jeu.nlig)
        curL.pack()
        curH = Scale(opt,length = 200,Label = "Nombre de colonnes : ", orient = HORIZONTAL,from_ = 1,to = 12, COMMAND = self.majColonnes)
        curH.set(self.jeu.ncol)
        curH.pack()

    def majColonnes(self,n):
        self.jeu.ncol = int(n)
        self.jeu.traceGrille()
    def majLignes(self,n):
        self.jeu.nlig = int(n)
        self.jeu.traceGrille()
    def reset(self):
        self.jeu.initJeu()
        self.jeu.traceGrille()
    def principe(self):
        msg = Toplevel(self)
        Message(msg,bg = "navry",fg ="ivory",width = 400,font = "Helvetica 10 bold",Text = "Les pions de ce jeu possédent chacun une face blanche et")
    def aPropos(self):
        msg = Toplevel(self)
        Message(msg,width = 200,aspect = 100,justify = CENTER, Text = "Jeu de Ping\n\n")

if __name__ == '__main__':
        Ping().mainLoop()



        





         




              






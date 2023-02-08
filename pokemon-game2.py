from tkinter import *
from PIL import ImageTk,Image
import random

root=Tk()

root.title("Try and Except")
root.geometry("600x400")
root.configure(background="yellow")

Abra=ImageTk.PhotoImage(Image.open("abra.jpg"))
Bulbasour=ImageTk.PhotoImage(Image.open("bulbasour.jpg"))
img=ImageTk.PhotoImage(Image.open("button.jpg"))
Charmender=ImageTk.PhotoImage(Image.open("charmender.jpg"))
Iyvasour=ImageTk.PhotoImage(Image.open("iyvasour.jpg"))
Jigglypuff=ImageTk.PhotoImage(Image.open("jigglypuff.jpg"))
Kadabra=ImageTk.PhotoImage(Image.open("kadabra.jpg"))
Meowth=ImageTk.PhotoImage(Image.open("meowth.jpg"))
Nidoking=ImageTk.PhotoImage(Image.open("nidoking.jpg"))
Paras=ImageTk.PhotoImage(Image.open("paras.jpg"))
Persion=ImageTk.PhotoImage(Image.open("persion.jpg"))
Pikachu=ImageTk.PhotoImage(Image.open("pikachu.jpg"))
Ratata=ImageTk.PhotoImage(Image.open("ratata.jpg"))
Squirtle=ImageTk.PhotoImage(Image.open("squirtle.jpg"))

player1=Label(root, text="Player 1", bg="blue", fg="white")
player1.place(relx=0.1,rely=0.3,anchor=CENTER)

player_1_score_label=Label(root,bg="blue", fg="white")
player_1_score_label.place(relx=0.1,rely=0.4,anchor=CENTER)

player2=Label(root, text="Player 2", bg="blue", fg="white")
player2.place(relx=0.9,rely=0.3,anchor=CENTER)

player_2_score_label=Label(root,bg="blue", fg="white")
player_2_score_label.place(relx=0.9,rely=0.4,anchor=CENTER)

label=Label(root,bg="white",fg="black")
label.place(relx=0.5,rely=0.5,anchor=CENTER)

pokemon_list=[Abra, Bulbasour, Charmender, Iyvasour, Jigglypuff, Kadabra, Meowth, Nidoking, Paras, Persion, Pikachu, Ratata, Squirtle]
power_list=[30, 40, 50, 100, 70, 70, 60, 90, 40, 70, 40, 50]

player1_score=0
def generate_player_1_score():
    global player1_score
    random_no = random.randint(0,12)
    random_pokemon = pokemon_list[random_no]
    label["image"]= random_pokemon
    
    random_power = power_list[random_no]
    player1_score = player1_score + random_power
    player_1_score_label["text"] = str(player1_score)

player1_Button=Button(root,image=img,command=generate_player_1_score)
player1_Button.place(relx=0.1,rely=0.6,anchor=CENTER)



player2_score=0

def generate_player_2_score():
    global player2_score
    random_no2 = random.randint(0,12)
    random_pokemon2 = pokemon_list[random_no2]
    label["image"]= random_pokemon2
    
    random_power2 = power_list[random_no2]
    player2_score = player2_score + random_power2
    player_2_score_label["text"] = str(player2_score)

player2_Button=Button(root,image=img,command=generate_player_2_score)
player2_Button.place(relx=0.9,rely=0.6,anchor=CENTER)



root.mainloop();
from tkinter import *
import requests

def get_quote():
    response = requests.get(url="https://api.kanye.rest/")
    response.raise_for_status()
    quotes = response.json()
    canvas.itemconfig(quote_text,text=quotes["quote"])



window = Tk()
window.title("Kanyee says...")
window.config(padx=50,pady=50)

canvas = Canvas(width=481,height=519)
background_img = PhotoImage(file ="quote.png" )
canvas.create_image(240,264,image=background_img)
quote_text = canvas.create_text(240,264,text="",width=250,font=("Ariel",15,"italic")) 
canvas.grid(row=0,column=0)
kanyee_img = PhotoImage(file="kanye.png")
kanyee_button = Button(image=kanyee_img,highlightthickness=0,command=get_quote)
kanyee_button.grid(row=1,column=0)

window.mainloop()
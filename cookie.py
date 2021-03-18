from tkinter import *


cookie_count = 1
bonus = 1
switch = False


def add_cookie():
    global cookie_count
    global bonus
    cookie_count += bonus
    label_counter.config(text=cookie_count)


def buy():
    global bonus
    global cookie_count
    if cookie_count >= 20:
        bonus += 1
        cookie_count -= 20
        label_counter.config(text=cookie_count)
        label_bonus.config(text=bonus)
        return bonus, cookie_count


def update():
    global switch
    global cookie_count
    if switch:
        cookie_count += 1
        label_counter.config(text=cookie_count)
        frame.after(1000, update)


def auto():
    global cookie_count
    global switch
    if cookie_count >= 1000 and switch is False:
        cookie_count -= 1000
        switch = True
        update()



# créer la fenetre
window = Tk()
window.title("Cookie Clicker")
window.geometry("1040x480")
window.config(background='#5886e7')

# créer la frame principale
frame = Frame(window, bg='#5886e7')



# ajout du compteur
label_frame = Label(window, text="Cookie Clicker game", font=("Arial Bold", 40), bg="#5886e7", fg='white')
label_frame.pack(pady=20, padx=20)
label_counter = Label(frame, text=cookie_count, font=("Courier", 30), bg="#5886e7")
label_counter.grid(row=0, column=0, pady=20, padx=20)
label_title_clicker = Label(frame, text="Cliquer sur le cookie \n pour augmenter vos cookies", font=("Courier", 10), fg='white', bg="#5886e7")
label_title_clicker.grid(row=1, column=0, pady=20, padx=20)

label_bonus = Label(frame, text="Bonus", font=("Courier", 30), bg="#5886e7")
label_bonus.grid(row=0, column=1, pady=20, padx=20)

label_title_counter = Label(frame, text="Payer 20 cookies pour augmenter \n la récolte des cookies", font=("Courier", 10), fg='white', bg="#5886e7")
label_title_counter.grid(row=1, column=1, pady=20, padx=20)

label_button3 = Label(frame, text="Auto Click", font=("Courier", 30), bg="#5886e7")
label_button3.grid(row=0, column=2, pady=20, padx=20)
label_title_button3 = Label(frame, text="Payer 1000 cookies pour augmenter vos cookies \n de 1 chaque seconde", font=("Courier", 10), fg='white', bg="#5886e7")
label_title_button3.grid(row=1, column=2, pady=20, padx=20)

# creation d'image
width = 300
height = 300
image = PhotoImage(file="cookie.png").zoom(8).subsample(32)
image2 = PhotoImage(file="add.png").zoom(8).subsample(32)


# ajout du bouton/image
button = Button(frame, image=image, bg='#5886e7', bd=0, relief=SUNKEN, highlightthickness=0, command=add_cookie,  activebackground="#5886e7")
button.grid(row=2, column=0, pady=20, padx=20)

button2 = Button(frame,  image=image2, bg='#5886e7', bd=0, relief=SUNKEN, highlightthickness=0, command=buy, activebackground="#5886e7")
button2.grid(row=2, column=1, pady=20, padx=20)

button3 = Button(frame, image=image2, bg='#5886e7', bd=0, relief=SUNKEN, highlightthickness=0, command=auto, activebackground="#5886e7")
button3.grid(row=2, column=2, pady=20, padx=20)

# ajout de la frame au centre
frame.pack(expand=YES)



# affichage
window.mainloop()


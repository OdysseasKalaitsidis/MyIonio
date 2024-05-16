from tkinter import *
import webbrowser
import time
import json
from PIL import ImageTk, Image
from urllib.request import urlopen

def eclass():
    link = "https://sso.ionio.gr/login?service=https%3A%2F%2Fopencourses.ionio.gr%2Fmodules%2Fauth%2Fcas.php"
    webbrowser.open_new(link)

def update_message():
    current_time = time.localtime()
    hour = current_time.tm_hour
    minutes = current_time.tm_min
    #Define the opening Hours
    if (hour == 8 and minutes >= 30) or (hour > 8 and hour < 10):
        photo_path = r"C:\Users\Asus\OneDrive\Υπολογιστής\MyIonio\MORNING.png"
    elif (hour >= 13 and hour < 15) or (hour == 15 and minutes <= 30):
        photo_path = r"C:\Users\Asus\OneDrive\Υπολογιστής\MyIonio\AFTER.png"
    elif (hour == 18 and minutes >= 30) or (hour > 18 and hour < 21):
        photo_path = r"C:\Users\Asus\OneDrive\Υπολογιστής\MyIonio\NIGHT.png"
    else:
        photo_path = r"C:\Users\Asus\OneDrive\Υπολογιστής\MyIonio\CLOSED.png"

    # Load image and set it as the image of message_pic label
    photo = PhotoImage(file=photo_path)
    message_pic.config(image=photo)
    message_pic.image = photo #In order not to delete the image

    root.after(1000, update_message)  # Update message every second

def menu():
    new_window = Toplevel(root)
    new_window.title("Restaurant Menu")
    new_window.iconbitmap(r'C:\Users\Asus\OneDrive\Υπολογιστής\MyIonio\icona.ico')

    global message_label
    message_label = Label(new_window, text="", font=('Helvetica', 18))
    message_label.pack(pady=20)

    global message_pic
    message_pic = Label(new_window)
    message_pic.pack()

    global program_pic
    program_pic = PhotoImage(file=r"C:\Users\Asus\OneDrive\Υπολογιστής\MyIonio\LE1.png")
    p = Label(new_window, image=program_pic)
    p.pack()

    update_message()

def check():
    # Fetching user's IP information
    url = "http://ipinfo.io/json"
    response = urlopen(url)
    data = json.load(response)

    # Accessing individual pieces of user information
    ipaddress_user = data['ip']
    city_user = data['city']
    region_user = data['region']
    country_user = data['country']
    location_user = data['loc']

    # University Information to be compared
    ipaddress_uni = "195.130.124.0"
    location_uni = "39.587761, 19.824070"

    # Printing the separated data
    print("IP Address:", ipaddress_user)
    print("City:", city_user)
    print("Region:", region_user)
    print("Country:", country_user)
    print("Location:", location_user)

    # Checking conditions and displaying message box if conditions are met
    if location_user == location_uni and ipaddress_user == ipaddress_uni:
        # Create a Tkinter window
        window3 = Tk()
        window3.iconbitmap(r'C:\Users\Asus\OneDrive\Υπολογιστής\MyIonio\icona.ico')
        window3.title("Credits")
        XP = PhotoImage(file=r"C:\Users\Asus\OneDrive\Υπολογιστής\MyIonio\XP.png")
        X = Label(window3, image=XP)
        X.pack()
        # Run the Tkinter event loop
        window3.mainloop()
    else: 
        window3 = Tk()
        window3.iconbitmap(r'C:\Users\Asus\OneDrive\Υπολογιστής\MyIonio\icona.ico')
        window3.title("Not in Uni")
        G = Label(window3,text="GO TO UNI" )
        G.pack()
        window3.mainloop()

def corfu():
    window4 = Toplevel(root)
    window4.iconbitmap(r'C:\Users\Asus\OneDrive\Υπολογιστής\MyIonio\icona.ico')
    window4.title("Get to know Corfu")
    EN = PhotoImage(file=r"C:\Users\Asus\OneDrive\Υπολογιστής\MyIonio\EntertainmenT.png")
    STUD = PhotoImage(file=r"C:\Users\Asus\OneDrive\Υπολογιστής\MyIonio\STUDY.png")
    FOOD = PhotoImage(file=r"C:\Users\Asus\OneDrive\Υπολογιστής\MyIonio\FOOD.png")

    global ENTE
    global ST
    global FD
    ENTE = Label(window4, image=EN)
    ST = Label(window4, image=STUD)
    FD = Label(window4, image=FOOD)

    def show_entertainment_pics():
        # Create a new window for displaying entertainment pictures
        global window_entertainment
        window_entertainment = Toplevel(window4)
        window_entertainment.title("Entertainment in Corfu")
        window_entertainment.iconbitmap(r'C:\Users\Asus\OneDrive\Υπολογιστής\MyIonio\icona.ico')

        # Load and display entertainment pictures 
        pic_1 = PhotoImage(file=r"C:\Users\Asus\OneDrive\Υπολογιστής\MyIonio\54.png")
        label_pic_1 = Label(window_entertainment, image=pic_1)
        label_pic_1.pack(padx=10, pady=10)

        pic_2 = PhotoImage(file=r"C:\Users\Asus\OneDrive\Υπολογιστής\MyIonio\THEBAR.png")
        label_pic_2 = Label(window_entertainment, image=pic_2)
        label_pic_2.pack(padx=10, pady=10)
        #WITHOUT THE 3 LINES IT DOESNT WORK
        pic_3 = PhotoImage(file=r"C:\Users\Asus\OneDrive\Υπολογιστής\MyIonio\.png")
        label_pic_3 = Label(window_entertainment, image=pic_3)
        label_pic_3.pack(padx=10, pady=10)
    global en_button
    en_button = Button(window4, image=EN, borderwidth=0, command=show_entertainment_pics)
    en_button.grid(row=0, column=0, padx=20, pady=10)

    def show_study_pics():
        global window_study
        window_study = Toplevel(window4)
        window_study.title("Study Spots in Corfu")
        window_study.iconbitmap(r'C:\Users\Asus\OneDrive\Υπολογιστής\MyIonio\icona.ico')

        pic_1 = PhotoImage(file=r"C:\Users\Asus\OneDrive\Υπολογιστής\MyIonio\SILICON.png")
        label_pic_1 = Label(window_study, image=pic_1)
        label_pic_1.pack(padx=10, pady=10)
        #WITHOUT THE BELOW DOESNT WORK
        pic_2 = PhotoImage(file="study_pic_2.png")
        label_pic_2 = Label(window_study, image=pic_2)
        label_pic_2.pack(padx=10, pady=10)

        pic_3 = PhotoImage(file="study_pic_3.png")
        label_pic_3 = Label(window_study, image=pic_3)
        label_pic_3.pack(padx=10, pady=10)

    global stud_button
    stud_button = Button(window4, image=STUD, borderwidth=0, command=show_study_pics)
    stud_button.grid(row=0, column=1, padx=20, pady=10)

    def show_food_pics():
        global window_food
        window_food = Toplevel(window4)
        window_food.title("Food in Corfu")
        window_food.iconbitmap(r'C:\Users\Asus\OneDrive\Υπολογιστής\MyIonio\icona.ico')

        pic_1 = PhotoImage(file=r"C:\Users\Asus\OneDrive\Υπολογιστής\MyIonio\PININI.png")
        label_pic_1 = Label(window_food, image=pic_1)
        label_pic_1.pack(padx=10, pady=10)

        pic_2 = PhotoImage(file=r"C:\Users\Asus\OneDrive\Υπολογιστής\MyIonio\PITTA.png")
        label_pic_2 = Label(window_food, image=pic_2)
        label_pic_2.pack(padx=10, pady=10)

        pic_3 = PhotoImage(file="food_pic_3.png")
        label_pic_3 = Label(window_food, image=pic_3)
        label_pic_3.pack(padx=10, pady=10)
    global food_button
    food_button = Button(window4, image=FOOD, borderwidth=0, command=show_food_pics)
    food_button.grid(row=0, column=2, padx=20, pady=10)

    window4.mainloop()


def imageview():
    window11 = Toplevel(root)
    window11.iconbitmap(r'C:\Users\Asus\OneDrive\Υπολογιστής\MyIonio\icona.ico')
    window11.title("Academic Shedule")

    img_1 = PhotoImage(file=r"C:\Users\Asus\OneDrive\Υπολογιστής\MyIonio\B.png")
    img_2 = PhotoImage(file=r"C:\Users\Asus\OneDrive\Υπολογιστής\MyIonio\D .png")
    img_3 = PhotoImage(file=r"C:\Users\Asus\OneDrive\Υπολογιστής\MyIonio\ST .png")
    img_4 = PhotoImage(file=r"C:\Users\Asus\OneDrive\Υπολογιστής\MyIonio\H.png")

    image_list = [img_1, img_2, img_3, img_4]

    # Display the first image
    my_label = Label(window11, image=img_1)
    my_label.grid(row=0, column=0, columnspan=3)

    def forward(image_number):
        nonlocal my_label
        nonlocal button_forward
        nonlocal button_back

        # Change the displayed image
        my_label.grid_forget()
        my_label = Label(window11, image=image_list[image_number-1])

        # Update forward and back buttons
        button_forward.grid_forget()
        button_forward = Button(window11, text=">>", command=lambda: forward(image_number+1))
        button_back = Button(window11, text="<<", command=lambda: back(image_number-1))

        # Disable forward button if at the last image
        if image_number == len(image_list):
            button_forward.config(state="disabled")

        # Display the updated image and buttons
        my_label.grid(row=0, column=0, columnspan=3)
        button_forward.grid(row=1, column=2)
        button_back.grid(row=1, column=0)

    def back(image_number):
        nonlocal my_label
        nonlocal button_forward
        nonlocal button_back

        # Change the displayed image
        my_label.grid_forget()
        my_label = Label(window11, image=image_list[image_number - 1])

        # Update forward and back buttons
        button_forward.grid_forget()
        button_forward = Button(window11, text=">>", command=lambda: forward(image_number + 1))
        button_back = Button(window11, text="<<", command=lambda: back(image_number - 1))

        # Disable back button if at the first image
        if image_number == 1:
            button_back.config(state="disabled")

        # Display the updated image and buttons
        my_label.grid(row=0, column=0, columnspan=3)
        button_forward.grid(row=1, column=2)
        button_back.grid(row=1, column=0)

    # Initialize back and forward buttons
    button_back = Button(window11, text="<<", command=lambda: back(0), state="disabled")
    button_forward = Button(window11, text=">>", command=lambda: forward(2))

    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)

    window11.mainloop()

def maps():
    link = "https://maps.app.goo.gl/qQDJv5Ahrb5u1ufJ9"
    webbrowser.open_new(link)

def news(): 
    link = "https://ionio.gr/gr/news/all-news-f1-news-announcements-f2-di/"
    webbrowser.open_new(link)

def library():
    link= "https://library.ionio.gr/gr/our-library/opening-hours/"
    webbrowser.open_new(link)

#Initialize the first page
root = Tk()
root.title('MyIonio')
root.geometry("1920x1080")
root.iconbitmap(r'C:\Users\Asus\OneDrive\Υπολογιστής\MyIonio\icona.ico')

#Save the filepath in variables
title_im = PhotoImage(file=r"C:\Users\Asus\OneDrive\Υπολογιστής\MyIonio\MyIoniores1.png")
Schedule = PhotoImage(file=r"C:\Users\Asus\OneDrive\Υπολογιστής\MyIonio\SCHEDULE.png")
Lesxi = PhotoImage(file=r"C:\Users\Asus\OneDrive\Υπολογιστής\MyIonio\RESTAURANT.png")
Entertainment = PhotoImage(file=r"C:\Users\Asus\OneDrive\Υπολογιστής\MyIonio\PLACES.png")
Library = PhotoImage(file=r"C:\Users\Asus\OneDrive\Υπολογιστής\MyIonio\LIBRARY.png")
Checkin = PhotoImage(file=r"C:\Users\Asus\OneDrive\Υπολογιστής\MyIonio\CHECK IN .png")
News = PhotoImage(file=r"C:\Users\Asus\OneDrive\Υπολογιστής\MyIonio\NEWS.png")
Eclass= PhotoImage(file=r"C:\Users\Asus\OneDrive\Υπολογιστής\MyIonio\ECLASS.png")
Maps= PhotoImage(file=r"C:\Users\Asus\OneDrive\Υπολογιστής\MyIonio\MAPS1.png")
Erasmus = PhotoImage(file=r"C:\Users\Asus\Downloads\Erasmus.png")

#Create Labels
S = Label(image=Schedule)
L = Label(image=Lesxi)
E = Label(image=Entertainment)
Li= Label(image=Library)
C = Label(image=Checkin)
N = Label(image=News)
M = Label(image=Maps)
T = Label(image=title_im)
Er = Label(image=Erasmus)

#Create the button and place it on the page
schedule_but = Button(root, image=Schedule, borderwidth=0, command=imageview)
schedule_but.grid(row=2, column=0,padx=20, pady=10)

Lesxi_but = Button(root, image=Lesxi, borderwidth=0, command=menu)
Lesxi_but.grid(row=2, column=1,padx=10, pady=10)

Entertainment_but = Button(root, image=Entertainment, borderwidth=0, command=corfu)
Entertainment_but.grid(row=2, column=2, padx=10, pady=10)

Library_but = Button(root, image=Library, borderwidth=0, command=library)
Library_but.grid(row=2, column=3, padx=10, pady=10)

Checkin_but = Button(root, image=Checkin, borderwidth=0, command=check)
Checkin_but.grid(row=3, column=0, padx=20, pady=10)

News_but = Button(root, image=News, borderwidth=0, command=news)
News_but.grid(row=3, column=1, padx=10, pady=10)

Eclass_but = Button(root, image=Eclass, borderwidth=0, command=eclass) 
Eclass_but.grid(row=3, column=2, padx=10, pady=10)

Maps_but = Button(root, image=Maps, borderwidth=0, command=maps)
Maps_but.grid(row=3, column=3, padx=10, pady=10)

T.grid(row=0, column=0, columnspan=7)

#constant refresh of the page
root.mainloop()

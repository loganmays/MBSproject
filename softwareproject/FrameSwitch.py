import tkinter
import tkinter.messagebox
from tkinter import *
import tkinter.font as font 
from PIL import Image, ImageTk



filestream = open('userinfo.txt', 'w')
def RegAccount():#function of the button
    
    user_id = str(ent3.get())
    user_pass = str(ent4.get())
    print(user_id, file= filestream) 
    print(user_pass,file = filestream)
    msg = 'user id'
    msg2 = 'user pass'
    tkinter.messagebox.showinfo('User: ',msg)
    #pass_id = str(ent.get())
    # age=int(ent.get())
    # if(age<18):
    #     msg='Sorry, you are not eligible to vote'
    # else:
    #     msg='You are eligible to vote!'
    # tkinter.messagebox.showinfo('Eligibility',msg)

#function to change to the mainscreen after hit login
def change_to_Main():
    Login_frame.forget()
    Current_frame.forget()
    Upcoming_frame.forget()
    Checkout_frame.forget()
    Main_frame.pack(fill='both', expand=1)

#function to logout of Main page and go back to login page
def change_to_Login():
    Main_frame.forget()
    Register_frame.forget()
    Login_frame.pack(fill='both', expand=1)

#function to change frame to register frame
def change_to_Register():
    Login_frame.forget()
    Register_frame.pack(fill='both', expand=1)

#function to change frame to Current Movies
def change_to_Current():
    Login_frame.forget()
    Main_frame.forget()
    Current_frame.pack(fill='both', expand=1)

#function to change frame to upcoming Movies
def change_to_Upcoming():
    Login_frame.forget()
    Main_frame.forget()
    Upcoming_frame.pack(fill='both', expand=1)

#function to change frame to movie_description
def change_to_Description():
    Login_frame.forget()
    Main_frame.forget()
    Upcoming_frame.forget()
    Current_frame.forget()
    Description_frame.pack(fill='both', expand=1)

#function to change frame to Showtimes
def change_to_Showtime():
    Login_frame.forget()
    Main_frame.forget()
    Upcoming_frame.forget()
    Current_frame.forget()
    Description_frame.forget()
    Showtime_frame.pack(fill='both', expand=1)

#function to change frame to checkout
def change_to_Checkout():
    Login_frame.forget()
    Main_frame.forget()
    Upcoming_frame.forget()
    Current_frame.forget()
    Showtime_frame.forget()
    Checkout_frame.pack(fill='both', expand=1)


#setting up initial window
root = tkinter.Tk()
root.title("Movie Booking System")
root.geometry("450x600")

#making frames for each use case
Login_frame = tkinter.Frame(root)
Main_frame = tkinter.Frame(root)
Register_frame =tkinter.Frame(root)
Upcoming_frame = tkinter.Frame(root)
Current_frame = tkinter.Frame(root)
Showtime_frame = tkinter.Frame(root)
Checkout_frame = tkinter.Frame(root)
Description_frame = tkinter.Frame(root)

#font setup
font_large = font.Font(family='Georgia',size='20',weight='bold')
font_small = font.Font(family='Georgia',size='12')

#-------------------------Login Frame---------------------------------------------
#labels for login frame
lbl_heading_Login = tkinter.Label(Login_frame,text='Sign In',font=font_large)
lbl_enterusername_Login = tkinter.Label(Login_frame,text='Enter your username')
lbl_enterpassword_Login = tkinter.Label(Login_frame,text='Enter your Password')
ent = Entry(Login_frame)
ent2 = Entry(Login_frame)
#placing items on the login frame
lbl_enterpassword_Login.place(x=165,y=160)
lbl_heading_Login.pack(padx=150,pady=20)
lbl_enterusername_Login.place(x=165,y = 100)
ent.place(x=165,y=130)
ent2.place(x=165,y=190)
#making the buttons for the login frame
btn_change_to_Main = tkinter.Button(Login_frame,text='Login',font=font_small,command=change_to_Main,height=2,width=15)
btn_change_to_Register = tkinter.Button(Login_frame,text='Create Account',font=font_small,command=change_to_Register,height=2,width=15)
btn_change_to_Main.place(x=150,y=250)
btn_change_to_Register.place(x=150,y=500)

#-------------------------Register Frame---------------------------------------------
#labels for the Register page
lbl_heading_Register = tkinter.Label(Register_frame,text='Create Account',font=font_large)
lbl_enterusername_Register = tkinter.Label(Register_frame,text='Enter your username')
lbl_enterpassword_Register = tkinter.Label(Register_frame,text='Enter your Password')
ent3 = Entry(Register_frame)
ent4 = Entry(Register_frame)
#placing items on the Register Page
lbl_enterpassword_Register.place(x=165,y=160)
lbl_heading_Register.pack(pady=20)
lbl_enterusername_Register.place(x=165,y = 100)
ent3.place(x=165,y=130)
ent4.place(x=165,y=190)
#making buttons for the Register Frame
btn_change_to_Login = tkinter.Button(Register_frame,text='Sign In',font=font_small,command=change_to_Login,height=2,width=15)
btn_RegisterAccount=tkinter.Button(Register_frame,text="Register Account",command =RegAccount,height=2,width=15)
btn_change_to_Login.place(x=150,y=500)
btn_RegisterAccount.place(x=165,y=250)

#-------------------------Main Frame---------------------------------------------
#labels for the Main Page frame
lbl_heading_Main = tkinter.Label(Main_frame,text='Movie Booking System',font=font_large)
lbl_featuredmovies_main = tkinter.Label(Main_frame,text = 'Featured Movies',font = font_small)
#placing items into the main page
lbl_heading_Main.pack(pady=20)
lbl_featuredmovies_main.place(x=165,y=300)
#making buttons for the Main page frame
btn_change_to_Login = tkinter.Button(Main_frame,font=font_small,text='Logout',command=change_to_Login,height=2,width=40)
btn_change_to_Upcoming = tkinter.Button(Main_frame,font = font_small,text ="Browse Upcoming Movies",command=change_to_Upcoming)
btn_change_to_Current = tkinter.Button(Main_frame,font = font_small,text ="Browse Current Movies",command = change_to_Current)
btn_change_to_Login.place(x=40,y=530)
btn_change_to_Upcoming.place(x=130,y=100)
btn_change_to_Current.place(x=140,y=200)

#images for featured movies
image19 = Image.open('djangopic.jpg')
image20 = Image.open('sharktale.jpg')
image21 = Image.open('elfpic.jpg')

image13 = image19.resize((100,150), Image.ANTIALIAS)
image14 = image20.resize((100,150), Image.ANTIALIAS)
image15 = image21.resize((100,150), Image.ANTIALIAS)

img19= ImageTk.PhotoImage(image13)
img20= ImageTk.PhotoImage(image14)
img21= ImageTk.PhotoImage(image15)

#movie buttons
btn_FeaturedMovie_19 = tkinter.Button(Main_frame,image=img19,command= change_to_Description)
btn_FeaturedMovie_20 = tkinter.Button(Main_frame,image=img20)
btn_FeaturedMovie_21 = tkinter.Button(Main_frame,image=img21)

#placing movie buttons
btn_FeaturedMovie_19.place(x=40,y=330)
btn_FeaturedMovie_20.place(x=180,y=330)
btn_FeaturedMovie_21.place(x=320,y=330)

#-------------------------Current Movie Frame---------------------------------------------
#images for movies
image1 = Image.open('diehardpic.jpg')
image2 = Image.open('rushhourpic.jpg')
image3 = Image.open('elfpic.jpg')
image4 = Image.open('matrixpic.jpg')
image5 = Image.open('onepiecepic.jpg')
image6 = Image.open('fightclubpic.jpg')
image7 = Image.open('darkknightpic.jpg')
image8 = Image.open('djangopic.jpg')
image9 = Image.open('sharktale.jpg')

image1 = image1.resize((100,150), Image.ANTIALIAS)
image2 = image2.resize((100,150), Image.ANTIALIAS)
image3 = image3.resize((100,150), Image.ANTIALIAS)
image4 = image4.resize((100,150), Image.ANTIALIAS)
image5 = image5.resize((100,150), Image.ANTIALIAS)
image6 = image6.resize((100,150), Image.ANTIALIAS)
image7 = image7.resize((100,150), Image.ANTIALIAS)
image8 = image8.resize((100,150), Image.ANTIALIAS)
image9 = image9.resize((100,150), Image.ANTIALIAS)

img1= ImageTk.PhotoImage(image1)
img2= ImageTk.PhotoImage(image2)
img3= ImageTk.PhotoImage(image3)
img4= ImageTk.PhotoImage(image4)
img5= ImageTk.PhotoImage(image5)
img6= ImageTk.PhotoImage(image6)
img7= ImageTk.PhotoImage(image7)
img8= ImageTk.PhotoImage(image8)
img9= ImageTk.PhotoImage(image9)
#labels for the current movies frame
lbl_heading_current = tkinter.Label(Current_frame,text='Current Movies',font=font_large)
#placing labels into the current movies frame
lbl_heading_current.pack(pady=20)
#making buttons
btn_CurrentMovie_1 = tkinter.Button(Current_frame,image=img1)
btn_CurrentMovie_2 = tkinter.Button(Current_frame,image=img2)
btn_CurrentMovie_3 = tkinter.Button(Current_frame,image=img3)
btn_CurrentMovie_4 = tkinter.Button(Current_frame,image=img4)
btn_CurrentMovie_5 = tkinter.Button(Current_frame,image=img5)
btn_CurrentMovie_6 = tkinter.Button(Current_frame,image=img6)
btn_CurrentMovie_7 = tkinter.Button(Current_frame,image=img7)
btn_CurrentMovie_8 = tkinter.Button(Current_frame,image=img8,command= change_to_Description)
btn_CurrentMovie_9 = tkinter.Button(Current_frame,image=img9)
btn_change_to_Main = tkinter.Button(Current_frame,font = font_small,text ="Back",command = change_to_Main)

#placing buttons
btn_CurrentMovie_1.place(x=40,y=60)
btn_CurrentMovie_2.place(x=180,y=60)
btn_CurrentMovie_3.place(x=320,y=60)
btn_CurrentMovie_4.place(x=40,y=230)
btn_CurrentMovie_5.place(x=180,y=230)
btn_CurrentMovie_6.place(x=320,y=230)
btn_CurrentMovie_7.place(x=40,y=400)
btn_CurrentMovie_8.place(x=180,y=400)
btn_CurrentMovie_9.place(x=320,y=400)
btn_change_to_Main.place(x=10,y=10)


#-------------------------Upcoming Movie Frame---------------------------------------------
#images for movies
image10 = Image.open('Piratespic.jpg')
image11 = Image.open('lordofrings.jpg')
image12 = Image.open('inceptionpic.jpg')
image13 = Image.open('avengerspic.jpg')
image14 = Image.open('interstellarpic.jpg')
image15 = Image.open('privateryan.jpg')
image16 = Image.open('greenmile.jpg')
image17 = Image.open('starwars.jpg')
image18 = Image.open('johnwick.jpg')

image10 = image10.resize((100,150), Image.ANTIALIAS)
image11 = image11.resize((100,150), Image.ANTIALIAS)
image12 = image12.resize((100,150), Image.ANTIALIAS)
image13 = image13.resize((100,150), Image.ANTIALIAS)
image14 = image14.resize((100,150), Image.ANTIALIAS)
image15 = image15.resize((100,150), Image.ANTIALIAS)
image16 = image16.resize((100,150), Image.ANTIALIAS)
image17 = image17.resize((100,150), Image.ANTIALIAS)
image18 = image18.resize((100,150), Image.ANTIALIAS)

img10= ImageTk.PhotoImage(image10)
img11= ImageTk.PhotoImage(image11)
img12= ImageTk.PhotoImage(image12)
img13= ImageTk.PhotoImage(image13)
img14= ImageTk.PhotoImage(image14)
img15= ImageTk.PhotoImage(image15)
img16= ImageTk.PhotoImage(image16)
img17= ImageTk.PhotoImage(image17)
img18= ImageTk.PhotoImage(image18)

#labels for the upcoming movies frame
lbl_heading_upcoming = tkinter.Label(Upcoming_frame,text='Upcoming Movies',font=font_large)
#placing labels into the current movies frame
lbl_heading_upcoming.pack(pady=20)
#making buttons
btn_UpcomingMovie_10 = tkinter.Button(Upcoming_frame,image=img10)
btn_UpcomingMovie_11 = tkinter.Button(Upcoming_frame,image=img11)
btn_UpcomingMovie_12 = tkinter.Button(Upcoming_frame,image=img12)
btn_UpcomingMovie_13 = tkinter.Button(Upcoming_frame,image=img13)
btn_UpcomingMovie_14 = tkinter.Button(Upcoming_frame,image=img14)
btn_UpcomingMovie_15 = tkinter.Button(Upcoming_frame,image=img15)
btn_UpcomingMovie_16 = tkinter.Button(Upcoming_frame,image=img16)
btn_UpcomingMovie_17 = tkinter.Button(Upcoming_frame,image=img17)
btn_UpcomingMovie_18 = tkinter.Button(Upcoming_frame,image=img18)
btn_change_to_Main = tkinter.Button(Upcoming_frame,font = font_small,text ="Back",command = change_to_Main)

#placing buttons
btn_UpcomingMovie_10.place(x=40,y=60)
btn_UpcomingMovie_11.place(x=180,y=60)
btn_UpcomingMovie_12.place(x=320,y=60)
btn_UpcomingMovie_13.place(x=40,y=230)
btn_UpcomingMovie_14.place(x=180,y=230)
btn_UpcomingMovie_15.place(x=320,y=230)
btn_UpcomingMovie_16.place(x=40,y=400)
btn_UpcomingMovie_17.place(x=180,y=400)
btn_UpcomingMovie_18.place(x=320,y=400)
btn_change_to_Main.place(x=10,y=10)

#-------------------------Description Frame---------------------------------------------

#making buttons 
btn_change_to_showtime = tkinter.Button(Description_frame,font = font_small,text ="Book Now",command = change_to_Showtime)

#placing buttons
btn_change_to_showtime.place(x=185,y=500)

#-------------------------Showtime Frame---------------------------------------------


#making buttons 
btn_change_to_checkout = tkinter.Button(Showtime_frame,font = font_small,text ="Checkout",command = change_to_Checkout)

#placing buttons
btn_change_to_checkout.place(x=185,y=500)

#-------------------------Checkout Frame---------------------------------------------
#making buttons 
btn_change_to_confirm = tkinter.Button(Checkout_frame,font = font_small,text ="Confirm",command = change_to_Main)

#placing buttons
btn_change_to_confirm.place(x=185,y=500)



#running the program starting at the Login Frame
Login_frame.pack(fill='both', expand=1)

root.mainloop()




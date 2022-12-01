import tkinter
import tkinter.messagebox
from tkinter import *
import tkinter.font as font 
from PIL import Image, ImageTk
from itertools import cycle
from tkinter import ttk


heading_description = ''
movieruntime=''
movie_description = ''
movierating= ''
moviecost =''
moviefilename = ''
global image22
global img22
global image23
global img23
global djangosun1,djangosun2,djangosun3,djangomon1,djangomon2,djangomon3,djangotues1,djangotues2,djangotues3,djangowed1,djangowed2,djangowed3,djangothurs1,djangothurs2,djangothurs3,djangofri1,djangofri2,djangofri3,djangosat1,djangosat2,djangosat3
global diehardsun1,diehardsun2,diehardsun3
global rushhoursun1,rushhoursun2,rushhoursun3
global elfsun1,elfsun2,elfsun3
global matrixsun1,matrixsun2,matrixsun3
global onepiecesun1,onepiecesun2,onepiecesun3
global fightclubsun1,fightclubsun2,fightclubsun3
global batmansun1,batmansun2,batmansun3
global sharktalesun1,sharktalesun2,sharktalesun3
djangosun1 ='1:00 PM'
djangosun2 = '3:45 PM'
djangosun3 = '7:00PM'
diehardsun1 ='1:00 PM'
diehardsun2 = '3:45 PM'
diehardsun3 = '7:00PM'
rushhoursun1 ='1:00 PM'
rushhoursun2 = '3:45 PM'
rushhoursun3 = '7:00PM'
elfsun1 ='1:00 PM'
elfsun2 = '3:45 PM'
elfsun3 = '7:00PM'
matrixsun1 ='1:00 PM'
matrixsun2 = '3:45 PM'
matrixsun3 = '7:00PM'
onepiecesun1 ='1:00 PM'
onepiecesun2 = '3:45 PM'
onepiecesun3 = '7:00PM'
fightclubsun1 ='1:00 PM'
fightclubsun2 = '3:45 PM'
fightclubsun3 = '7:00PM'
batmansun1 ='1:00 PM'
batmansun2 = '3:45 PM'
batmansun3 = '7:00PM'
sharktalesun1 ='1:00 PM'
sharktalesun2 = '3:45 PM'
sharktalesun3 = '7:00PM'

diehard_price=15
Rushhour_price=15
elf_price=15
matrix_price=15
onepiece_price=15
fightclub_price=15
batman_price=15
django_price=15
sharktale_price =15



filestream = open('userinfo.txt', 'a')
#function to create an account and save it to a txt file
def RegAccount():
    user_id = str(ent3.get())
    user_pass = str(ent4.get())
    if user_id ==''or user_pass=='':
        tkinter.messagebox.showinfo('Account Creation Error','Please fill in all boxes')
    else:
        filestream.write(user_id + '\n')
        filestream.write(user_pass +'\n')
        filestream.close()
        msg = 'Account Successfully Created'
        tkinter.messagebox.showinfo('User: ',msg)
        change_to_Login()

#function to display message after hitting Checkout button
def CheckoutConfirmed():
    global smmer
    global moviefilename
    global ent5,ent6,ent7,ent8,ent9,ent10,ent11,ent12
    cardnumber = str(ent5.get())
    expdate=str(ent6.get())
    cvv=str(ent7.get())
    namecard=str(ent8.get())
    address=str(ent9.get())
    city=str(ent10.get())
    state=str(ent11.get())
    zipco=str(ent12.get())
    if cardnumber==''or expdate==''or cvv==''or namecard==''or address==''or city==''or state==''or zipco=='':
        tkinter.messagebox.showinfo('Checkout Failure','Please fill out all the boxes')
    else:
        with open ('TicketsSold.txt', 'a') as file:
            if moviefilename =='diehardpic.jpg':
                file.write('Die Hard\n' + (smmer)+'\n')
            if moviefilename =='djangopic.jpg':
                file.write('Django\n' + (smmer)+'\n')
            if moviefilename =='rushhourpic.jpg':
                file.write('Rush Hour\n' + (smmer)+'\n')
            if moviefilename =='elfpic.jpg':
                file.write('Elf\n' + (smmer)+'\n')
            if moviefilename =='matrixpic.jpg':
                file.write('Matrix\n' + (smmer)+'\n')
            if moviefilename =='onepiecepic.jpg':
                file.write('One Piece\n' + (smmer)+'\n')
            if moviefilename =='fightclubpic.jpg':
                file.write('Fight Club\n' + (smmer)+'\n')
            if moviefilename =='darkknightpic.jpg':
                file.write('Dark Knight\n' + (smmer)+'\n')
            if moviefilename =='sharktale.jpg':
                file.write('Shark Tale\n' + (smmer)+'\n')
        file.close()
        tkinter.messagebox.showinfo('Checkout','Checkout Successful')
        change_to_Main()

def paypalconfirm():
    with open ('TicketsSold.txt', 'a') as file:
            if moviefilename =='diehardpic.jpg':
                file.write('Die Hard\n' + (smmer)+'\n')
            if moviefilename =='djangopic.jpg':
                file.write('Django\n' + (smmer)+'\n')
            if moviefilename =='rushhourpic.jpg':
                file.write('Rush Hour\n' + (smmer)+'\n')
            if moviefilename =='elfpic.jpg':
                file.write('Elf\n' + (smmer)+'\n')
            if moviefilename =='matrixpic.jpg':
                file.write('Matrix\n' + (smmer)+'\n')
            if moviefilename =='onepiecepic.jpg':
                file.write('One Piece\n' + (smmer)+'\n')
            if moviefilename =='fightclubpic.jpg':
                file.write('Fight Club\n' + (smmer)+'\n')
            if moviefilename =='darkknightpic.jpg':
                file.write('Dark Knight\n' + (smmer)+'\n')
            if moviefilename =='sharktale.jpg':
                file.write('Shark Tale\n' + (smmer)+'\n')
    tkinter.messagebox.showinfo('Checkout','Checkout Successful')
    file.close()
    change_to_Main()



#function to display message of status report
def StatusReport():
    diehard_tickets=0
    django_tickets =0
    rushhour_tickets=0
    elf_tickets=0
    matrix_tickets=0
    onepiece_tickets=0
    fightclub_tickets=0
    darkknight_tickets=0
    django_tickets=0
    sharktale_tickets =0
    indexer2 =0
    file2 = open('TicketsSold.txt', 'r')
    Lines2 = file2.readlines()
    for line in Lines2:
        indexer2+=1
        line = line.strip('\n')
        if line == 'Django':
            django_tickets += int(Lines2[indexer2].strip('\n'))
        if line == 'Rush Hour':
            rushhour_tickets += int(Lines2[indexer2].strip('\n'))
        if line == 'Die Hard':
            diehard_tickets += int(Lines2[indexer2].strip('\n'))
        if line == 'Elf':
            elf_tickets += int(Lines2[indexer2].strip('\n'))
        if line == 'Matrix':
            matrix_tickets += int(Lines2[indexer2].strip('\n'))
        if line == 'One Piece':
            onepiece_tickets += int(Lines2[indexer2].strip('\n'))
        if line == 'Fight Club':
            fightclub_tickets += int(Lines2[indexer2].strip('\n'))
        if line == 'Dark Knight':
            darkknight_tickets += int(Lines2[indexer2].strip('\n'))
        if line == 'Shark Tale':
            sharktale_tickets += int(Lines2[indexer2].strip('\n'))
    msg4 = 'Die Hard= ' +str(diehard_tickets)+ '\nRush Hour=  '+ str(rushhour_tickets)+'\nElf = '+str(elf_tickets)+'\nThe matrix= '+str(matrix_tickets)+'\nOne Piece= '+str(onepiece_tickets)+'\nFight Club= '+str(fightclub_tickets)+'\nThe Dark Knight= '+str(darkknight_tickets)+'\nDjango= '+str(django_tickets)+'\nShark Tale= '+str(sharktale_tickets)

    tkinter.messagebox.showinfo('Number of Tickets Sold',msg4)


#function to validate user input
def login_valid():
    indexer =0
    usern = str(ent.get())
    userpass = str(ent2.get())
    file1 = open('userinfo.txt', 'r')
    Lines = file1.readlines()
    for line in Lines:
        indexer+=1
        line = line.strip('\n')
        if usern ==''or userpass=='':
            tkinter.messagebox.showinfo('Login Invalid','Username or Password is Incorrect')
            break
        else:
            if usern== line:
                if userpass==(Lines[indexer].strip('\n')):
                    change_to_Main()
                    break
                else:
                    tkinter.messagebox.showinfo('Login Invalid','Username or Password is Incorrect')
                    break
            elif usern == 'admin':
                if userpass == 'Password':
                    change_to_Admin()
                    break
                else:
                    tkinter.messagebox.showinfo('Login Invalid','Username or Password is Incorrect')
                    break
            elif usern != line and indexer == len(Lines):
                tkinter.messagebox.showinfo('Login Invalid','Username or Password is Incorrect')
    file1.close()

#function to sum up the tickets sold
def SumTicketsSold():
    global smmer
    global price
    global diehard_price,Rushhour_price,elf_price,matrix_price,onepiece_price,fightclub_price,batman_price,django_price,sharktale_price,spin_box1,spin_box2,spin_box3,spin_box4,spin_box5,spin_box6,spin_box7
    global TotalCost
    price =15
    aInt1 = spin_box1.get()
    bInt1 = spin_box2.get()
    cInt1 = spin_box3.get()
    dInt1 = spin_box4.get()
    eInt1 = spin_box5.get()
    fInt1 = spin_box6.get()
    gInt1 = spin_box7.get()
    aInt2=0
    bInt2=0
    cInt2=0
    dInt2=0
    eInt2=0
    fInt2=0
    gInt2=0
    if aInt1!='':
        aInt2 =int(aInt1)
    if bInt1!='':
        bInt2 =int(bInt1)
    if cInt1!='':
        cInt2 =int(cInt1)
    if dInt1!='':
        dInt2 =int(dInt1)
    if eInt1!='':
        eInt2 =int(eInt1)
    if fInt1!='':
        fInt2 =int(fInt1)
    if gInt1!='':
        gInt2 =int(gInt1)
    summy = aInt2 + bInt2 + cInt2 + dInt2 + eInt2 + fInt2 + gInt2
    if(moviefilename=='diehardpic.jpg'):
        TotalCost=summy * diehard_price
    if moviefilename =='djangopic.jpg':
        TotalCost=summy * django_price
    if moviefilename =='rushhourpic.jpg':
        TotalCost=summy * Rushhour_price
    if moviefilename =='elfpic.jpg':
        TotalCost=summy * elf_price
    if moviefilename =='matrixpic.jpg':
        TotalCost=summy * matrix_price
    if moviefilename =='onepiecepic.jpg':
        TotalCost=summy * onepiece_price
    if moviefilename =='fightclubpic.jpg':
        TotalCost=summy * fightclub_price
    if moviefilename =='darkknightpic.jpg':
        TotalCost=summy * batman_price
    if moviefilename =='sharktale.jpg':
        TotalCost=summy * sharktale_price
    smmer = str(summy)
    change_to_Checkout()

#function to change the editing page to have die hard info
def diehard_edit():
    global moviename
    global moviecost
    global movie_time1, movie_time2, movie_time3, movie_time4, movie_time5, movie_time6, movie_time7, movie_time8, movie_time9, movie_time10, movie_time11, movie_time12, movie_time13, movie_time14, movie_time15, movie_time16, movie_time17, movie_time18, movie_time19, movie_time20, movie_time21
    for widget in edit_shows_frame.winfo_children():
        widget.destroy()
    Login_frame.forget()
    Main_frame.forget()
    Upcoming_frame.forget()
    Current_frame.forget()
    ManageShows_frame.forget()
    edit_shows_frame.pack(fill='both', expand=1)
    moviename ='Die Hard'
    file3 = open('diehardcost.txt', 'r')
    Lines3 = file3.readlines()
    for line in Lines3:
        line = line.strip('\n')
        moviecost ='Cost= $'+str(line)

    file2 = open('diehardtime.txt', 'r')
    Lines2 = file2.readlines()
    movie_time1=Lines2[0].strip('\n')
    movie_time2=Lines2[1].strip('\n')
    movie_time3=Lines2[2].strip('\n')
    movie_time4=Lines2[3].strip('\n')
    movie_time5=Lines2[4].strip('\n')
    movie_time6=Lines2[5].strip('\n')
    movie_time7=Lines2[6].strip('\n')
    movie_time8=Lines2[7].strip('\n')
    movie_time9=Lines2[8].strip('\n')
    movie_time10=Lines2[9].strip('\n')
    movie_time11=Lines2[10].strip('\n')
    movie_time12=Lines2[11].strip('\n')
    movie_time13=Lines2[12].strip('\n')
    movie_time14=Lines2[13].strip('\n')
    movie_time15=Lines2[14].strip('\n')
    movie_time16=Lines2[15].strip('\n')
    movie_time17=Lines2[16].strip('\n')
    movie_time18=Lines2[17].strip('\n')
    movie_time19=Lines2[18].strip('\n')
    movie_time20=Lines2[19].strip('\n')
    movie_time21=Lines2[20].strip('\n')
    file3.close()
    file2.close()

    edit_show()

#function to change the editing page to have Rush hour info
def rushhour_edit():
    global moviename
    global moviecost
    global movie_time1, movie_time2, movie_time3, movie_time4, movie_time5, movie_time6, movie_time7, movie_time8, movie_time9, movie_time10, movie_time11, movie_time12, movie_time13, movie_time14, movie_time15, movie_time16, movie_time17, movie_time18, movie_time19, movie_time20, movie_time21
    for widget in edit_shows_frame.winfo_children():
        widget.destroy()
    Login_frame.forget()
    Main_frame.forget()
    Upcoming_frame.forget()
    Current_frame.forget()
    ManageShows_frame.forget()
    edit_shows_frame.pack(fill='both', expand=1)
    moviename ='Rush Hour'
    moviecost ='Cost= $'+str(Rushhour_price)
    file2 = open('rushhourtime.txt', 'r')
    Lines2 = file2.readlines()
    movie_time1=Lines2[0].strip('\n')
    movie_time2=Lines2[1].strip('\n')
    movie_time3=Lines2[2].strip('\n')
    movie_time4=Lines2[3].strip('\n')
    movie_time5=Lines2[4].strip('\n')
    movie_time6=Lines2[5].strip('\n')
    movie_time7=Lines2[6].strip('\n')
    movie_time8=Lines2[7].strip('\n')
    movie_time9=Lines2[8].strip('\n')
    movie_time10=Lines2[9].strip('\n')
    movie_time11=Lines2[10].strip('\n')
    movie_time12=Lines2[11].strip('\n')
    movie_time13=Lines2[12].strip('\n')
    movie_time14=Lines2[13].strip('\n')
    movie_time15=Lines2[14].strip('\n')
    movie_time16=Lines2[15].strip('\n')
    movie_time17=Lines2[16].strip('\n')
    movie_time18=Lines2[17].strip('\n')
    movie_time19=Lines2[18].strip('\n')
    movie_time20=Lines2[19].strip('\n')
    movie_time21=Lines2[20].strip('\n')


    edit_show()

#function to change the editing page to have Elf info
def elf_edit():
    global moviename
    global moviecost
    global movie_time1, movie_time2, movie_time3, movie_time4, movie_time5, movie_time6, movie_time7, movie_time8, movie_time9, movie_time10, movie_time11, movie_time12, movie_time13, movie_time14, movie_time15, movie_time16, movie_time17, movie_time18, movie_time19, movie_time20, movie_time21
    for widget in edit_shows_frame.winfo_children():
        widget.destroy()
    Login_frame.forget()
    Main_frame.forget()
    Upcoming_frame.forget()
    Current_frame.forget()
    ManageShows_frame.forget()
    edit_shows_frame.pack(fill='both', expand=1)
    moviename ='Elf'
    moviecost ='Cost= $'+str(elf_price)
    file2 = open('elftime.txt', 'r')
    Lines2 = file2.readlines()
    movie_time1=Lines2[0].strip('\n')
    movie_time2=Lines2[1].strip('\n')
    movie_time3=Lines2[2].strip('\n')
    movie_time4=Lines2[3].strip('\n')
    movie_time5=Lines2[4].strip('\n')
    movie_time6=Lines2[5].strip('\n')
    movie_time7=Lines2[6].strip('\n')
    movie_time8=Lines2[7].strip('\n')
    movie_time9=Lines2[8].strip('\n')
    movie_time10=Lines2[9].strip('\n')
    movie_time11=Lines2[10].strip('\n')
    movie_time12=Lines2[11].strip('\n')
    movie_time13=Lines2[12].strip('\n')
    movie_time14=Lines2[13].strip('\n')
    movie_time15=Lines2[14].strip('\n')
    movie_time16=Lines2[15].strip('\n')
    movie_time17=Lines2[16].strip('\n')
    movie_time18=Lines2[17].strip('\n')
    movie_time19=Lines2[18].strip('\n')
    movie_time20=Lines2[19].strip('\n')
    movie_time21=Lines2[20].strip('\n')

    edit_show()

#function to change the editing page to have Matrix info
def matrix_edit():
    global moviename
    global moviecost
    global movie_time1, movie_time2, movie_time3, movie_time4, movie_time5, movie_time6, movie_time7, movie_time8, movie_time9, movie_time10, movie_time11, movie_time12, movie_time13, movie_time14, movie_time15, movie_time16, movie_time17, movie_time18, movie_time19, movie_time20, movie_time21
    global timemovie1,timemovie2,timemovie3
    for widget in edit_shows_frame.winfo_children():
        widget.destroy()
    Login_frame.forget()
    Main_frame.forget()
    Upcoming_frame.forget()
    Current_frame.forget()
    ManageShows_frame.forget()
    edit_shows_frame.pack(fill='both', expand=1)
    moviename ='The Matrix'
    moviecost ='Cost= $'+str(matrix_price)
    file2 = open('matrixtime.txt', 'r')
    Lines2 = file2.readlines()
    movie_time1=Lines2[0].strip('\n')
    movie_time2=Lines2[1].strip('\n')
    movie_time3=Lines2[2].strip('\n')
    movie_time4=Lines2[3].strip('\n')
    movie_time5=Lines2[4].strip('\n')
    movie_time6=Lines2[5].strip('\n')
    movie_time7=Lines2[6].strip('\n')
    movie_time8=Lines2[7].strip('\n')
    movie_time9=Lines2[8].strip('\n')
    movie_time10=Lines2[9].strip('\n')
    movie_time11=Lines2[10].strip('\n')
    movie_time12=Lines2[11].strip('\n')
    movie_time13=Lines2[12].strip('\n')
    movie_time14=Lines2[13].strip('\n')
    movie_time15=Lines2[14].strip('\n')
    movie_time16=Lines2[15].strip('\n')
    movie_time17=Lines2[16].strip('\n')
    movie_time18=Lines2[17].strip('\n')
    movie_time19=Lines2[18].strip('\n')
    movie_time20=Lines2[19].strip('\n')
    movie_time21=Lines2[20].strip('\n')

    edit_show()

#function to change the editing page to have One Piece info
def onepiece_edit():
    global moviename
    global moviecost
    global movie_time1, movie_time2, movie_time3, movie_time4, movie_time5, movie_time6, movie_time7, movie_time8, movie_time9, movie_time10, movie_time11, movie_time12, movie_time13, movie_time14, movie_time15, movie_time16, movie_time17, movie_time18, movie_time19, movie_time20, movie_time21
    for widget in edit_shows_frame.winfo_children():
        widget.destroy()
    Login_frame.forget()
    Main_frame.forget()
    Upcoming_frame.forget()
    Current_frame.forget()
    ManageShows_frame.forget()
    edit_shows_frame.pack(fill='both', expand=1)
    moviename ='One Piece'
    moviecost ='Cost= $'+str(onepiece_price)
    file2 = open('onepiecetime.txt', 'r')
    Lines2 = file2.readlines()
    movie_time1=Lines2[0].strip('\n')
    movie_time2=Lines2[1].strip('\n')
    movie_time3=Lines2[2].strip('\n')
    movie_time4=Lines2[3].strip('\n')
    movie_time5=Lines2[4].strip('\n')
    movie_time6=Lines2[5].strip('\n')
    movie_time7=Lines2[6].strip('\n')
    movie_time8=Lines2[7].strip('\n')
    movie_time9=Lines2[8].strip('\n')
    movie_time10=Lines2[9].strip('\n')
    movie_time11=Lines2[10].strip('\n')
    movie_time12=Lines2[11].strip('\n')
    movie_time13=Lines2[12].strip('\n')
    movie_time14=Lines2[13].strip('\n')
    movie_time15=Lines2[14].strip('\n')
    movie_time16=Lines2[15].strip('\n')
    movie_time17=Lines2[16].strip('\n')
    movie_time18=Lines2[17].strip('\n')
    movie_time19=Lines2[18].strip('\n')
    movie_time20=Lines2[19].strip('\n')
    movie_time21=Lines2[20].strip('\n')

    edit_show()

#function to change the editing page to have Fight Club info
def fightclub_edit():
    global moviename
    global moviecost
    global movie_time1, movie_time2, movie_time3, movie_time4, movie_time5, movie_time6, movie_time7, movie_time8, movie_time9, movie_time10, movie_time11, movie_time12, movie_time13, movie_time14, movie_time15, movie_time16, movie_time17, movie_time18, movie_time19, movie_time20, movie_time21
    global timemovie1,timemovie2,timemovie3
    for widget in edit_shows_frame.winfo_children():
        widget.destroy()
    Login_frame.forget()
    Main_frame.forget()
    Upcoming_frame.forget()
    Current_frame.forget()
    ManageShows_frame.forget()
    edit_shows_frame.pack(fill='both', expand=1)
    moviename ='Fight Club'
    moviecost ='Cost= $'+str(fightclub_price)
    file2 = open('fightclubtime.txt', 'r')
    Lines2 = file2.readlines()
    movie_time1=Lines2[0].strip('\n')
    movie_time2=Lines2[1].strip('\n')
    movie_time3=Lines2[2].strip('\n')
    movie_time4=Lines2[3].strip('\n')
    movie_time5=Lines2[4].strip('\n')
    movie_time6=Lines2[5].strip('\n')
    movie_time7=Lines2[6].strip('\n')
    movie_time8=Lines2[7].strip('\n')
    movie_time9=Lines2[8].strip('\n')
    movie_time10=Lines2[9].strip('\n')
    movie_time11=Lines2[10].strip('\n')
    movie_time12=Lines2[11].strip('\n')
    movie_time13=Lines2[12].strip('\n')
    movie_time14=Lines2[13].strip('\n')
    movie_time15=Lines2[14].strip('\n')
    movie_time16=Lines2[15].strip('\n')
    movie_time17=Lines2[16].strip('\n')
    movie_time18=Lines2[17].strip('\n')
    movie_time19=Lines2[18].strip('\n')
    movie_time20=Lines2[19].strip('\n')
    movie_time21=Lines2[20].strip('\n')

    edit_show()

#function to change the editing page to have Batman info
def batman_edit():
    global moviename
    global moviecost
    global timemovie1,timemovie2,timemovie3
    global movie_time1, movie_time2, movie_time3, movie_time4, movie_time5, movie_time6, movie_time7, movie_time8, movie_time9, movie_time10, movie_time11, movie_time12, movie_time13, movie_time14, movie_time15, movie_time16, movie_time17, movie_time18, movie_time19, movie_time20, movie_time21
    for widget in edit_shows_frame.winfo_children():
        widget.destroy()
    Login_frame.forget()
    Main_frame.forget()
    Upcoming_frame.forget()
    Current_frame.forget()
    ManageShows_frame.forget()
    edit_shows_frame.pack(fill='both', expand=1)
    moviename ='The Dark Knight'
    moviecost ='Cost= $'+str(batman_price)
    file2 = open('batmantime.txt', 'r')
    Lines2 = file2.readlines()
    movie_time1=Lines2[0].strip('\n')
    movie_time2=Lines2[1].strip('\n')
    movie_time3=Lines2[2].strip('\n')
    movie_time4=Lines2[3].strip('\n')
    movie_time5=Lines2[4].strip('\n')
    movie_time6=Lines2[5].strip('\n')
    movie_time7=Lines2[6].strip('\n')
    movie_time8=Lines2[7].strip('\n')
    movie_time9=Lines2[8].strip('\n')
    movie_time10=Lines2[9].strip('\n')
    movie_time11=Lines2[10].strip('\n')
    movie_time12=Lines2[11].strip('\n')
    movie_time13=Lines2[12].strip('\n')
    movie_time14=Lines2[13].strip('\n')
    movie_time15=Lines2[14].strip('\n')
    movie_time16=Lines2[15].strip('\n')
    movie_time17=Lines2[16].strip('\n')
    movie_time18=Lines2[17].strip('\n')
    movie_time19=Lines2[18].strip('\n')
    movie_time20=Lines2[19].strip('\n')
    movie_time21=Lines2[20].strip('\n')

    edit_show()

#function to change the editing page to have Django info
def django_edit():
    global moviename
    global moviecost2
    global movie_time1, movie_time2, movie_time3, movie_time4, movie_time5, movie_time6, movie_time7, movie_time8, movie_time9, movie_time10, movie_time11, movie_time12, movie_time13, movie_time14, movie_time15, movie_time16, movie_time17, movie_time18, movie_time19, movie_time20, movie_time21
    for widget in edit_shows_frame.winfo_children():
        widget.destroy()
    Login_frame.forget()
    Main_frame.forget()
    Upcoming_frame.forget()
    Current_frame.forget()
    ManageShows_frame.forget()
    edit_shows_frame.pack(fill='both', expand=1)
    moviename ='Django Unchained'
    moviecost2 ='Cost= $'+str(django_price)
    file2 = open('djangotime.txt', 'r')
    Lines2 = file2.readlines()
    movie_time1=Lines2[0].strip('\n')
    movie_time2=Lines2[1].strip('\n')
    movie_time3=Lines2[2].strip('\n')
    movie_time4=Lines2[3].strip('\n')
    movie_time5=Lines2[4].strip('\n')
    movie_time6=Lines2[5].strip('\n')
    movie_time7=Lines2[6].strip('\n')
    movie_time8=Lines2[7].strip('\n')
    movie_time9=Lines2[8].strip('\n')
    movie_time10=Lines2[9].strip('\n')
    movie_time11=Lines2[10].strip('\n')
    movie_time12=Lines2[11].strip('\n')
    movie_time13=Lines2[12].strip('\n')
    movie_time14=Lines2[13].strip('\n')
    movie_time15=Lines2[14].strip('\n')
    movie_time16=Lines2[15].strip('\n')
    movie_time17=Lines2[16].strip('\n')
    movie_time18=Lines2[17].strip('\n')
    movie_time19=Lines2[18].strip('\n')
    movie_time20=Lines2[19].strip('\n')
    movie_time21=Lines2[20].strip('\n')
    
    edit_show()

#function to change the editing page to have Shark Tale info
def SharkTale_edit():
    global moviename
    global moviecost
    global movie_time1, movie_time2, movie_time3, movie_time4, movie_time5, movie_time6, movie_time7, movie_time8, movie_time9, movie_time10, movie_time11, movie_time12, movie_time13, movie_time14, movie_time15, movie_time16, movie_time17, movie_time18, movie_time19, movie_time20, movie_time21
    for widget in edit_shows_frame.winfo_children():
        widget.destroy()
    Login_frame.forget()
    Main_frame.forget()
    Upcoming_frame.forget()
    Current_frame.forget()
    ManageShows_frame.forget()
    edit_shows_frame.pack(fill='both', expand=1)
    moviename ='Shark Tale'
    moviecost ='Cost= $'+str(sharktale_price)
    file2 = open('sharktaletime.txt', 'r')
    Lines2 = file2.readlines()
    movie_time1=Lines2[0].strip('\n')
    movie_time2=Lines2[1].strip('\n')
    movie_time3=Lines2[2].strip('\n')
    movie_time4=Lines2[3].strip('\n')
    movie_time5=Lines2[4].strip('\n')
    movie_time6=Lines2[5].strip('\n')
    movie_time7=Lines2[6].strip('\n')
    movie_time8=Lines2[7].strip('\n')
    movie_time9=Lines2[8].strip('\n')
    movie_time10=Lines2[9].strip('\n')
    movie_time11=Lines2[10].strip('\n')
    movie_time12=Lines2[11].strip('\n')
    movie_time13=Lines2[12].strip('\n')
    movie_time14=Lines2[13].strip('\n')
    movie_time15=Lines2[14].strip('\n')
    movie_time16=Lines2[15].strip('\n')
    movie_time17=Lines2[16].strip('\n')
    movie_time18=Lines2[17].strip('\n')
    movie_time19=Lines2[18].strip('\n')
    movie_time20=Lines2[19].strip('\n')
    movie_time21=Lines2[20].strip('\n')

    edit_show()

#Function to apply the changes the admin made
def apply_edit():
    global movie_time1, movie_time2, movie_time3, movie_time4, movie_time5, movie_time6, movie_time7, movie_time8, movie_time9, movie_time10, movie_time11, movie_time12, movie_time13, movie_time14, movie_time15, movie_time16, movie_time17, movie_time18, movie_time19, movie_time20, movie_time21
    new_price = str(ent15.get())
    newtime1 = str(ent16.get())
    newtime2 =str(ent17.get())
    newtime3 =str(ent18.get())
    newtime4 =str(ent19.get())
    newtime5 =str(ent20.get())
    newtime6 =str(ent21.get())
    newtime7 =str(ent22.get())
    newtime8 =str(ent23.get())
    newtime9 = str(ent24.get())
    newtime10 =str(ent25.get())
    newtime11 =str(ent26.get())
    newtime12 =str(ent27.get())
    newtime13 =str(ent28.get())
    newtime14 =str(ent29.get())
    newtime15 =str(ent30.get())
    newtime16 =str(ent31.get())
    newtime17 = str(ent32.get())
    newtime18 =str(ent33.get())
    newtime19 =str(ent34.get())
    newtime20 =str(ent35.get())
    newtime21 =str(ent36.get())



    if moviename =='Die Hard':
        filestream3 =open('diehardtime.txt','r')
        data =filestream3.readlines()
        filestream3.close()
        if new_price!='':
            filestream2 = open('diehardcost.txt', 'w')
            filestream2.write(new_price)
            filestream2.close()
        if newtime1!='':
            data[0]=newtime1 +'\n'
            filestream4=open('diehardtime.txt','w')
            filestream4.writelines(data)
            filestream4.close()
        if newtime2!='':
            data[1]=newtime2 +'\n'
            filestream5=open('diehardtime.txt','w')
            filestream5.writelines(data)
            filestream5.close()
        if newtime3!='':
            data[2]=newtime3 +'\n'
            filestream6=open('diehardtime.txt','w')
            filestream6.writelines(data)
            filestream6.close() 
        if newtime4!='':
            data[3]=newtime4 +'\n'
            filestream7=open('diehardtime.txt','w')
            filestream7.writelines(data)
            filestream7.close() 
        if newtime5!='':
            data[4]=newtime5 +'\n'
            filestream8=open('diehardtime.txt','w')
            filestream8.writelines(data)
            filestream8.close()
        if newtime6!='':
            data[5]=newtime6 +'\n'
            filestream9=open('diehardtime.txt','w')
            filestream9.writelines(data)
            filestream9.close()
        if newtime7!='':
            data[6]=newtime7 +'\n'
            filestream10=open('diehardtime.txt','w')
            filestream10.writelines(data)
            filestream10.close() 
        if newtime8!='':
            data[7]=newtime8 +'\n'
            filestream11=open('diehardtime.txt','w')
            filestream11.writelines(data)
            filestream11.close() 
        if newtime9!='':
            data[8]=newtime9 +'\n'
            filestream12=open('diehardtime.txt','w')
            filestream12.writelines(data)
            filestream12.close()
        if newtime10!='':
            data[9]=newtime10 +'\n'
            filestream13=open('diehardtime.txt','w')
            filestream13.writelines(data)
            filestream13.close()
        if newtime11!='':
            data[10]=newtime11 +'\n'
            filestream14=open('diehardtime.txt','w')
            filestream14.writelines(data)
            filestream14.close() 
        if newtime12!='':
            data[11]=newtime12 +'\n'
            filestream15=open('diehardtime.txt','w')
            filestream15.writelines(data)
            filestream15.close() 
        if newtime13!='':
            data[12]=newtime13 +'\n'
            filestream16=open('diehardtime.txt','w')
            filestream16.writelines(data)
            filestream16.close()
        if newtime14!='':
            data[13]=newtime14 +'\n'
            filestream17=open('diehardtime.txt','w')
            filestream17.writelines(data)
            filestream17.close()
        if newtime15!='':
            data[14]=newtime15 +'\n'
            filestream18=open('diehardtime.txt','w')
            filestream18.writelines(data)
            filestream18.close() 
        if newtime16!='':
            data[15]=newtime16 +'\n'
            filestream19=open('diehardtime.txt','w')
            filestream19.writelines(data)
            filestream19.close() 
        if newtime17!='':
            data[16]=newtime17 +'\n'
            filestream20=open('diehardtime.txt','w')
            filestream20.writelines(data)
            filestream20.close() 
        if newtime18!='':
            data[17]=newtime18 +'\n'
            filestream20=open('diehardtime.txt','w')
            filestream20.writelines(data)
            filestream20.close()
        if newtime19!='':
            data[18]=newtime19 +'\n'
            filestream21=open('diehardtime.txt','w')
            filestream21.writelines(data)
            filestream21.close()
        if newtime20!='':
            data[19]=newtime20 +'\n'
            filestream22=open('diehardtime.txt','w')
            filestream22.writelines(data)
            filestream22.close() 
        if newtime21!='':
            data[20]=newtime21 +'\n'
            filestream23=open('diehardtime.txt','w')
            filestream23.writelines(data)
            filestream23.close() 

    if moviename =='Rush Hour':
        filestream3 =open('rushhourtime.txt','r')
        data =filestream3.readlines()
        filestream3.close()
        if new_price!='':
            filestream2 = open('rushhourcost.txt', 'w')
            filestream2.write(new_price)
            filestream2.close()
        if newtime1!='':
            data[0]=newtime1 +'\n'
            filestream4=open('rushhourtime.txt','w')
            filestream4.writelines(data)
            filestream4.close()
        if newtime2!='':
            data[1]=newtime2 +'\n'
            filestream5=open('rushhourtime.txt','w')
            filestream5.writelines(data)
            filestream5.close()
        if newtime3!='':
            data[2]=newtime3 +'\n'
            filestream6=open('rushhourtime.txt','w')
            filestream6.writelines(data)
            filestream6.close() 
        if newtime4!='':
            data[3]=newtime4 +'\n'
            filestream7=open('rushhourtime.txt','w')
            filestream7.writelines(data)
            filestream7.close() 
        if newtime5!='':
            data[4]=newtime5 +'\n'
            filestream8=open('rushhourtime.txt','w')
            filestream8.writelines(data)
            filestream8.close()
        if newtime6!='':
            data[5]=newtime6 +'\n'
            filestream9=open('rushhourtime.txt','w')
            filestream9.writelines(data)
            filestream9.close()
        if newtime7!='':
            data[6]=newtime7 +'\n'
            filestream10=open('rushhourtime.txt','w')
            filestream10.writelines(data)
            filestream10.close() 
        if newtime8!='':
            data[7]=newtime8 +'\n'
            filestream11=open('rushhourtime.txt','w')
            filestream11.writelines(data)
            filestream11.close() 
        if newtime9!='':
            data[8]=newtime9 +'\n'
            filestream12=open('rushhourtime.txt','w')
            filestream12.writelines(data)
            filestream12.close()
        if newtime10!='':
            data[9]=newtime10 +'\n'
            filestream13=open('rushhourtime.txt','w')
            filestream13.writelines(data)
            filestream13.close()
        if newtime11!='':
            data[10]=newtime11 +'\n'
            filestream14=open('rushhourtime.txt','w')
            filestream14.writelines(data)
            filestream14.close() 
        if newtime12!='':
            data[11]=newtime12 +'\n'
            filestream15=open('rushhourtime.txt','w')
            filestream15.writelines(data)
            filestream15.close() 
        if newtime13!='':
            data[12]=newtime13 +'\n'
            filestream16=open('rushhourtime.txt','w')
            filestream16.writelines(data)
            filestream16.close()
        if newtime14!='':
            data[13]=newtime14 +'\n'
            filestream17=open('rushhourtime.txt','w')
            filestream17.writelines(data)
            filestream17.close()
        if newtime15!='':
            data[14]=newtime15 +'\n'
            filestream18=open('rushhourtime.txt','w')
            filestream18.writelines(data)
            filestream18.close() 
        if newtime16!='':
            data[15]=newtime16 +'\n'
            filestream19=open('rushhourtime.txt','w')
            filestream19.writelines(data)
            filestream19.close() 
        if newtime17!='':
            data[16]=newtime17 +'\n'
            filestream20=open('rushhourtime.txt','w')
            filestream20.writelines(data)
            filestream20.close() 
        if newtime18!='':
            data[17]=newtime18 +'\n'
            filestream20=open('rushhourtime.txt','w')
            filestream20.writelines(data)
            filestream20.close()
        if newtime19!='':
            data[18]=newtime19 +'\n'
            filestream21=open('rushhourtime.txt','w')
            filestream21.writelines(data)
            filestream21.close()
        if newtime20!='':
            data[19]=newtime20 +'\n'
            filestream22=open('rushhourtime.txt','w')
            filestream22.writelines(data)
            filestream22.close() 
        if newtime21!='':
            data[20]=newtime21 +'\n'
            filestream23=open('rushhourtime.txt','w')
            filestream23.writelines(data)
            filestream23.close() 

    if moviename =='Elf':
        filestream3 =open('elftime.txt','r')
        data =filestream3.readlines()
        filestream3.close()
        if new_price!='':
            filestream2 = open('elfcost.txt', 'w')
            filestream2.write(new_price)
            filestream2.close()
        if newtime1!='':
            data[0]=newtime1 +'\n'
            filestream4=open('elftime.txt','w')
            filestream4.writelines(data)
            filestream4.close()
        if newtime2!='':
            data[1]=newtime2 +'\n'
            filestream5=open('elftime.txt','w')
            filestream5.writelines(data)
            filestream5.close()
        if newtime3!='':
            data[2]=newtime3 +'\n'
            filestream6=open('elftime.txt','w')
            filestream6.writelines(data)
            filestream6.close() 
        if newtime4!='':
            data[3]=newtime4 +'\n'
            filestream7=open('elftime.txt','w')
            filestream7.writelines(data)
            filestream7.close() 
        if newtime5!='':
            data[4]=newtime5 +'\n'
            filestream8=open('elftime.txt','w')
            filestream8.writelines(data)
            filestream8.close()
        if newtime6!='':
            data[5]=newtime6 +'\n'
            filestream9=open('elftime.txt','w')
            filestream9.writelines(data)
            filestream9.close()
        if newtime7!='':
            data[6]=newtime7 +'\n'
            filestream10=open('elftime.txt','w')
            filestream10.writelines(data)
            filestream10.close() 
        if newtime8!='':
            data[7]=newtime8 +'\n'
            filestream11=open('elftime.txt','w')
            filestream11.writelines(data)
            filestream11.close() 
        if newtime9!='':
            data[8]=newtime9 +'\n'
            filestream12=open('elftime.txt','w')
            filestream12.writelines(data)
            filestream12.close()
        if newtime10!='':
            data[9]=newtime10 +'\n'
            filestream13=open('elftime.txt','w')
            filestream13.writelines(data)
            filestream13.close()
        if newtime11!='':
            data[10]=newtime11 +'\n'
            filestream14=open('elftime.txt','w')
            filestream14.writelines(data)
            filestream14.close() 
        if newtime12!='':
            data[11]=newtime12 +'\n'
            filestream15=open('elftime.txt','w')
            filestream15.writelines(data)
            filestream15.close() 
        if newtime13!='':
            data[12]=newtime13 +'\n'
            filestream16=open('elftime.txt','w')
            filestream16.writelines(data)
            filestream16.close()
        if newtime14!='':
            data[13]=newtime14 +'\n'
            filestream17=open('elftime.txt','w')
            filestream17.writelines(data)
            filestream17.close()
        if newtime15!='':
            data[14]=newtime15 +'\n'
            filestream18=open('elftime.txt','w')
            filestream18.writelines(data)
            filestream18.close() 
        if newtime16!='':
            data[15]=newtime16 +'\n'
            filestream19=open('elftime.txt','w')
            filestream19.writelines(data)
            filestream19.close() 
        if newtime17!='':
            data[16]=newtime17 +'\n'
            filestream20=open('elftime.txt','w')
            filestream20.writelines(data)
            filestream20.close() 
        if newtime18!='':
            data[17]=newtime18 +'\n'
            filestream20=open('elftime.txt','w')
            filestream20.writelines(data)
            filestream20.close()
        if newtime19!='':
            data[18]=newtime19 +'\n'
            filestream21=open('elftime.txt','w')
            filestream21.writelines(data)
            filestream21.close()
        if newtime20!='':
            data[19]=newtime20 +'\n'
            filestream22=open('elftime.txt','w')
            filestream22.writelines(data)
            filestream22.close() 
        if newtime21!='':
            data[20]=newtime21 +'\n'
            filestream23=open('elftime.txt','w')
            filestream23.writelines(data)
            filestream23.close() 

    if moviename =='The Matrix':
        filestream3 =open('matrixtime.txt','r')
        data =filestream3.readlines()
        filestream3.close()
        if new_price!='':
            filestream2 = open('matrixcost.txt', 'w')
            filestream2.write(new_price)
            filestream2.close()
        if newtime1!='':
            data[0]=newtime1 +'\n'
            filestream4=open('matrixtime.txt','w')
            filestream4.writelines(data)
            filestream4.close()
        if newtime2!='':
            data[1]=newtime2 +'\n'
            filestream5=open('matrixtime.txt','w')
            filestream5.writelines(data)
            filestream5.close()
        if newtime3!='':
            data[2]=newtime3 +'\n'
            filestream6=open('matrixtime.txt','w')
            filestream6.writelines(data)
            filestream6.close() 
        if newtime4!='':
            data[3]=newtime4 +'\n'
            filestream7=open('matrixtime.txt','w')
            filestream7.writelines(data)
            filestream7.close() 
        if newtime5!='':
            data[4]=newtime5 +'\n'
            filestream8=open('matrixtime.txt','w')
            filestream8.writelines(data)
            filestream8.close()
        if newtime6!='':
            data[5]=newtime6 +'\n'
            filestream9=open('matrixtime.txt','w')
            filestream9.writelines(data)
            filestream9.close()
        if newtime7!='':
            data[6]=newtime7 +'\n'
            filestream10=open('matrixtime.txt','w')
            filestream10.writelines(data)
            filestream10.close() 
        if newtime8!='':
            data[7]=newtime8 +'\n'
            filestream11=open('matrixtime.txt','w')
            filestream11.writelines(data)
            filestream11.close() 
        if newtime9!='':
            data[8]=newtime9 +'\n'
            filestream12=open('matrixtime.txt','w')
            filestream12.writelines(data)
            filestream12.close()
        if newtime10!='':
            data[9]=newtime10 +'\n'
            filestream13=open('matrixtime.txt','w')
            filestream13.writelines(data)
            filestream13.close()
        if newtime11!='':
            data[10]=newtime11 +'\n'
            filestream14=open('matrixtime.txt','w')
            filestream14.writelines(data)
            filestream14.close() 
        if newtime12!='':
            data[11]=newtime12 +'\n'
            filestream15=open('matrixtime.txt','w')
            filestream15.writelines(data)
            filestream15.close() 
        if newtime13!='':
            data[12]=newtime13 +'\n'
            filestream16=open('matrixtime.txt','w')
            filestream16.writelines(data)
            filestream16.close()
        if newtime14!='':
            data[13]=newtime14 +'\n'
            filestream17=open('matrixtime.txt','w')
            filestream17.writelines(data)
            filestream17.close()
        if newtime15!='':
            data[14]=newtime15 +'\n'
            filestream18=open('matrixtime.txt','w')
            filestream18.writelines(data)
            filestream18.close() 
        if newtime16!='':
            data[15]=newtime16 +'\n'
            filestream19=open('matrixtime.txt','w')
            filestream19.writelines(data)
            filestream19.close() 
        if newtime17!='':
            data[16]=newtime17 +'\n'
            filestream20=open('matrixtime.txt','w')
            filestream20.writelines(data)
            filestream20.close() 
        if newtime18!='':
            data[17]=newtime18 +'\n'
            filestream20=open('matrixtime.txt','w')
            filestream20.writelines(data)
            filestream20.close()
        if newtime19!='':
            data[18]=newtime19 +'\n'
            filestream21=open('matrixtime.txt','w')
            filestream21.writelines(data)
            filestream21.close()
        if newtime20!='':
            data[19]=newtime20 +'\n'
            filestream22=open('matrixtime.txt','w')
            filestream22.writelines(data)
            filestream22.close() 
        if newtime21!='':
            data[20]=newtime21 +'\n'
            filestream23=open('matrixtime.txt','w')
            filestream23.writelines(data)
            filestream23.close() 

    if moviename =='One Piece':
        filestream3 =open('onepiecetime.txt','r')
        data =filestream3.readlines()
        filestream3.close()
        if new_price!='':
            filestream2 = open('onepiececost.txt', 'w')
            filestream2.write(new_price)
            filestream2.close()
        if newtime1!='':
            data[0]=newtime1 +'\n'
            filestream4=open('onepiecetime.txt','w')
            filestream4.writelines(data)
            filestream4.close()
        if newtime2!='':
            data[1]=newtime2 +'\n'
            filestream5=open('onepiecetime.txt','w')
            filestream5.writelines(data)
            filestream5.close()
        if newtime3!='':
            data[2]=newtime3 +'\n'
            filestream6=open('onepiecetime.txt','w')
            filestream6.writelines(data)
            filestream6.close() 
        if newtime4!='':
            data[3]=newtime4 +'\n'
            filestream7=open('onepiecetime.txt','w')
            filestream7.writelines(data)
            filestream7.close() 
        if newtime5!='':
            data[4]=newtime5 +'\n'
            filestream8=open('onepiecetime.txt','w')
            filestream8.writelines(data)
            filestream8.close()
        if newtime6!='':
            data[5]=newtime6 +'\n'
            filestream9=open('onepiecetime.txt','w')
            filestream9.writelines(data)
            filestream9.close()
        if newtime7!='':
            data[6]=newtime7 +'\n'
            filestream10=open('onepiecetime.txt','w')
            filestream10.writelines(data)
            filestream10.close() 
        if newtime8!='':
            data[7]=newtime8 +'\n'
            filestream11=open('onepiecetime.txt','w')
            filestream11.writelines(data)
            filestream11.close() 
        if newtime9!='':
            data[8]=newtime9 +'\n'
            filestream12=open('onepiecetime.txt','w')
            filestream12.writelines(data)
            filestream12.close()
        if newtime10!='':
            data[9]=newtime10 +'\n'
            filestream13=open('onepiecetime.txt','w')
            filestream13.writelines(data)
            filestream13.close()
        if newtime11!='':
            data[10]=newtime11 +'\n'
            filestream14=open('onepiecetime.txt','w')
            filestream14.writelines(data)
            filestream14.close() 
        if newtime12!='':
            data[11]=newtime12 +'\n'
            filestream15=open('onepiecetime.txt','w')
            filestream15.writelines(data)
            filestream15.close() 
        if newtime13!='':
            data[12]=newtime13 +'\n'
            filestream16=open('onepiecetime.txt','w')
            filestream16.writelines(data)
            filestream16.close()
        if newtime14!='':
            data[13]=newtime14 +'\n'
            filestream17=open('onepiecetime.txt','w')
            filestream17.writelines(data)
            filestream17.close()
        if newtime15!='':
            data[14]=newtime15 +'\n'
            filestream18=open('onepiecetime.txt','w')
            filestream18.writelines(data)
            filestream18.close() 
        if newtime16!='':
            data[15]=newtime16 +'\n'
            filestream19=open('onepiecetime.txt','w')
            filestream19.writelines(data)
            filestream19.close() 
        if newtime17!='':
            data[16]=newtime17 +'\n'
            filestream20=open('onepiecetime.txt','w')
            filestream20.writelines(data)
            filestream20.close() 
        if newtime18!='':
            data[17]=newtime18 +'\n'
            filestream20=open('onepiecetime.txt','w')
            filestream20.writelines(data)
            filestream20.close()
        if newtime19!='':
            data[18]=newtime19 +'\n'
            filestream21=open('onepiecetime.txt','w')
            filestream21.writelines(data)
            filestream21.close()
        if newtime20!='':
            data[19]=newtime20 +'\n'
            filestream22=open('onepiecetime.txt','w')
            filestream22.writelines(data)
            filestream22.close() 
        if newtime21!='':
            data[20]=newtime21 +'\n'
            filestream23=open('onepiecetime.txt','w')
            filestream23.writelines(data)
            filestream23.close() 

    if moviename =='Fight Club':
        filestream3 =open('fightclubtime.txt','r')
        data =filestream3.readlines()
        filestream3.close()
        if new_price!='':
            filestream2 = open('fightclubcost.txt', 'w')
            filestream2.write(new_price)
            filestream2.close()
        if newtime1!='':
            data[0]=newtime1 +'\n'
            filestream4=open('fightclubtime.txt','w')
            filestream4.writelines(data)
            filestream4.close()
        if newtime2!='':
            data[1]=newtime2 +'\n'
            filestream5=open('fightclubtime.txt','w')
            filestream5.writelines(data)
            filestream5.close()
        if newtime3!='':
            data[2]=newtime3 +'\n'
            filestream6=open('fightclubtime.txt','w')
            filestream6.writelines(data)
            filestream6.close() 
        if newtime4!='':
            data[3]=newtime4 +'\n'
            filestream7=open('fightclubtime.txt','w')
            filestream7.writelines(data)
            filestream7.close() 
        if newtime5!='':
            data[4]=newtime5 +'\n'
            filestream8=open('fightclubtime.txt','w')
            filestream8.writelines(data)
            filestream8.close()
        if newtime6!='':
            data[5]=newtime6 +'\n'
            filestream9=open('fightclubtime.txt','w')
            filestream9.writelines(data)
            filestream9.close()
        if newtime7!='':
            data[6]=newtime7 +'\n'
            filestream10=open('fightclubtime.txt','w')
            filestream10.writelines(data)
            filestream10.close() 
        if newtime8!='':
            data[7]=newtime8 +'\n'
            filestream11=open('fightclubtime.txt','w')
            filestream11.writelines(data)
            filestream11.close() 
        if newtime9!='':
            data[8]=newtime9 +'\n'
            filestream12=open('fightclubtime.txt','w')
            filestream12.writelines(data)
            filestream12.close()
        if newtime10!='':
            data[9]=newtime10 +'\n'
            filestream13=open('fightclubtime.txt','w')
            filestream13.writelines(data)
            filestream13.close()
        if newtime11!='':
            data[10]=newtime11 +'\n'
            filestream14=open('fightclubtime.txt','w')
            filestream14.writelines(data)
            filestream14.close() 
        if newtime12!='':
            data[11]=newtime12 +'\n'
            filestream15=open('fightclubtime.txt','w')
            filestream15.writelines(data)
            filestream15.close() 
        if newtime13!='':
            data[12]=newtime13 +'\n'
            filestream16=open('fightclubtime.txt','w')
            filestream16.writelines(data)
            filestream16.close()
        if newtime14!='':
            data[13]=newtime14 +'\n'
            filestream17=open('fightclubtime.txt','w')
            filestream17.writelines(data)
            filestream17.close()
        if newtime15!='':
            data[14]=newtime15 +'\n'
            filestream18=open('fightclubtime.txt','w')
            filestream18.writelines(data)
            filestream18.close() 
        if newtime16!='':
            data[15]=newtime16 +'\n'
            filestream19=open('fightclubtime.txt','w')
            filestream19.writelines(data)
            filestream19.close() 
        if newtime17!='':
            data[16]=newtime17 +'\n'
            filestream20=open('fightclubtime.txt','w')
            filestream20.writelines(data)
            filestream20.close() 
        if newtime18!='':
            data[17]=newtime18 +'\n'
            filestream20=open('fightclubtime.txt','w')
            filestream20.writelines(data)
            filestream20.close()
        if newtime19!='':
            data[18]=newtime19 +'\n'
            filestream21=open('fightclubtime.txt','w')
            filestream21.writelines(data)
            filestream21.close()
        if newtime20!='':
            data[19]=newtime20 +'\n'
            filestream22=open('fightclubtime.txt','w')
            filestream22.writelines(data)
            filestream22.close() 
        if newtime21!='':
            data[20]=newtime21 +'\n'
            filestream23=open('fightclubtime.txt','w')
            filestream23.writelines(data)
            filestream23.close() 

    if moviename =='The Dark Knight':
        filestream3 =open('batmantime.txt','r')
        data =filestream3.readlines()
        filestream3.close()
        if new_price!='':
            filestream2 = open('darkknightcost.txt', 'w')
            filestream2.write(new_price)
            filestream2.close()
        if newtime1!='':
            data[0]=newtime1 +'\n'
            filestream4=open('batmantime.txt','w')
            filestream4.writelines(data)
            filestream4.close()
        if newtime2!='':
            data[1]=newtime2 +'\n'
            filestream5=open('batmantime.txt','w')
            filestream5.writelines(data)
            filestream5.close()
        if newtime3!='':
            data[2]=newtime3 +'\n'
            filestream6=open('batmantime.txt','w')
            filestream6.writelines(data)
            filestream6.close() 
        if newtime4!='':
            data[3]=newtime4 +'\n'
            filestream7=open('batmantime.txt','w')
            filestream7.writelines(data)
            filestream7.close() 
        if newtime5!='':
            data[4]=newtime5 +'\n'
            filestream8=open('batmantime.txt','w')
            filestream8.writelines(data)
            filestream8.close()
        if newtime6!='':
            data[5]=newtime6 +'\n'
            filestream9=open('batmantime.txt','w')
            filestream9.writelines(data)
            filestream9.close()
        if newtime7!='':
            data[6]=newtime7 +'\n'
            filestream10=open('batmantime.txt','w')
            filestream10.writelines(data)
            filestream10.close() 
        if newtime8!='':
            data[7]=newtime8 +'\n'
            filestream11=open('batmantime.txt','w')
            filestream11.writelines(data)
            filestream11.close() 
        if newtime9!='':
            data[8]=newtime9 +'\n'
            filestream12=open('batmantime.txt','w')
            filestream12.writelines(data)
            filestream12.close()
        if newtime10!='':
            data[9]=newtime10 +'\n'
            filestream13=open('batmantime.txt','w')
            filestream13.writelines(data)
            filestream13.close()
        if newtime11!='':
            data[10]=newtime11 +'\n'
            filestream14=open('batmantime.txt','w')
            filestream14.writelines(data)
            filestream14.close() 
        if newtime12!='':
            data[11]=newtime12 +'\n'
            filestream15=open('batmantime.txt','w')
            filestream15.writelines(data)
            filestream15.close() 
        if newtime13!='':
            data[12]=newtime13 +'\n'
            filestream16=open('batmantime.txt','w')
            filestream16.writelines(data)
            filestream16.close()
        if newtime14!='':
            data[13]=newtime14 +'\n'
            filestream17=open('batmantime.txt','w')
            filestream17.writelines(data)
            filestream17.close()
        if newtime15!='':
            data[14]=newtime15 +'\n'
            filestream18=open('batmantime.txt','w')
            filestream18.writelines(data)
            filestream18.close() 
        if newtime16!='':
            data[15]=newtime16 +'\n'
            filestream19=open('batmantime.txt','w')
            filestream19.writelines(data)
            filestream19.close() 
        if newtime17!='':
            data[16]=newtime17 +'\n'
            filestream20=open('batmantime.txt','w')
            filestream20.writelines(data)
            filestream20.close() 
        if newtime18!='':
            data[17]=newtime18 +'\n'
            filestream20=open('batmantime.txt','w')
            filestream20.writelines(data)
            filestream20.close()
        if newtime19!='':
            data[18]=newtime19 +'\n'
            filestream21=open('batmantime.txt','w')
            filestream21.writelines(data)
            filestream21.close()
        if newtime20!='':
            data[19]=newtime20 +'\n'
            filestream22=open('batmantime.txt','w')
            filestream22.writelines(data)
            filestream22.close() 
        if newtime21!='':
            data[20]=newtime21 +'\n'
            filestream23=open('batmantime.txt','w')
            filestream23.writelines(data)
            filestream23.close() 

    if moviename =='Django Unchained':
        filestream3 =open('djangotime.txt','r')
        data =filestream3.readlines()
        filestream3.close()
        if new_price!='':
            filestream2 = open('djangocost.txt', 'w')
            filestream2.write(new_price)
            filestream2.close()
        if newtime1!='':
            data[0]=newtime1 +'\n'
            filestream4=open('djangotime.txt','w')
            filestream4.writelines(data)
            filestream4.close()
        if newtime2!='':
            data[1]=newtime2 +'\n'
            filestream5=open('djangotime.txt','w')
            filestream5.writelines(data)
            filestream5.close()
        if newtime3!='':
            data[2]=newtime3 +'\n'
            filestream6=open('djangotime.txt','w')
            filestream6.writelines(data)
            filestream6.close() 
        if newtime4!='':
            data[3]=newtime4 +'\n'
            filestream7=open('djangotime.txt','w')
            filestream7.writelines(data)
            filestream7.close() 
        if newtime5!='':
            data[4]=newtime5 +'\n'
            filestream8=open('djangotime.txt','w')
            filestream8.writelines(data)
            filestream8.close()
        if newtime6!='':
            data[5]=newtime6 +'\n'
            filestream9=open('djangotime.txt','w')
            filestream9.writelines(data)
            filestream9.close()
        if newtime7!='':
            data[6]=newtime7 +'\n'
            filestream10=open('djangotime.txt','w')
            filestream10.writelines(data)
            filestream10.close() 
        if newtime8!='':
            data[7]=newtime8 +'\n'
            filestream11=open('djangotime.txt','w')
            filestream11.writelines(data)
            filestream11.close() 
        if newtime9!='':
            data[8]=newtime9 +'\n'
            filestream12=open('djangotime.txt','w')
            filestream12.writelines(data)
            filestream12.close()
        if newtime10!='':
            data[9]=newtime10 +'\n'
            filestream13=open('djangotime.txt','w')
            filestream13.writelines(data)
            filestream13.close()
        if newtime11!='':
            data[10]=newtime11 +'\n'
            filestream14=open('djangotime.txt','w')
            filestream14.writelines(data)
            filestream14.close() 
        if newtime12!='':
            data[11]=newtime12 +'\n'
            filestream15=open('djangotime.txt','w')
            filestream15.writelines(data)
            filestream15.close() 
        if newtime13!='':
            data[12]=newtime13 +'\n'
            filestream16=open('djangotime.txt','w')
            filestream16.writelines(data)
            filestream16.close()
        if newtime14!='':
            data[13]=newtime14 +'\n'
            filestream17=open('djangotime.txt','w')
            filestream17.writelines(data)
            filestream17.close()
        if newtime15!='':
            data[14]=newtime15 +'\n'
            filestream18=open('djangotime.txt','w')
            filestream18.writelines(data)
            filestream18.close() 
        if newtime16!='':
            data[15]=newtime16 +'\n'
            filestream19=open('djangotime.txt','w')
            filestream19.writelines(data)
            filestream19.close() 
        if newtime17!='':
            data[16]=newtime17 +'\n'
            filestream20=open('djangotime.txt','w')
            filestream20.writelines(data)
            filestream20.close() 
        if newtime18!='':
            data[17]=newtime18 +'\n'
            filestream20=open('djangotime.txt','w')
            filestream20.writelines(data)
            filestream20.close()
        if newtime19!='':
            data[18]=newtime19 +'\n'
            filestream21=open('djangotime.txt','w')
            filestream21.writelines(data)
            filestream21.close()
        if newtime20!='':
            data[19]=newtime20 +'\n'
            filestream22=open('djangotime.txt','w')
            filestream22.writelines(data)
            filestream22.close() 
        if newtime21!='':
            data[20]=newtime21 +'\n'
            filestream23=open('djangotime.txt','w')
            filestream23.writelines(data)
            filestream23.close() 

    if moviename =='Shark Tale':
        filestream3 =open('sharktaletime.txt','r')
        data =filestream3.readlines()
        filestream3.close()
        if new_price!='':
            filestream2 = open('sharktalecost.txt', 'w')
            filestream2.write(new_price)
            filestream2.close()
        if newtime1!='':
            data[0]=newtime1 +'\n'
            filestream4=open('sharktaletime.txt','w')
            filestream4.writelines(data)
            filestream4.close()
        if newtime2!='':
            data[1]=newtime2 +'\n'
            filestream5=open('sharktaletime.txt','w')
            filestream5.writelines(data)
            filestream5.close()
        if newtime3!='':
            data[2]=newtime3 +'\n'
            filestream6=open('sharktaletime.txt','w')
            filestream6.writelines(data)
            filestream6.close() 
        if newtime4!='':
            data[3]=newtime4 +'\n'
            filestream7=open('sharktaletime.txt','w')
            filestream7.writelines(data)
            filestream7.close() 
        if newtime5!='':
            data[4]=newtime5 +'\n'
            filestream8=open('sharktaletime.txt','w')
            filestream8.writelines(data)
            filestream8.close()
        if newtime6!='':
            data[5]=newtime6 +'\n'
            filestream9=open('sharktaletime.txt','w')
            filestream9.writelines(data)
            filestream9.close()
        if newtime7!='':
            data[6]=newtime7 +'\n'
            filestream10=open('sharktaletime.txt','w')
            filestream10.writelines(data)
            filestream10.close() 
        if newtime8!='':
            data[7]=newtime8 +'\n'
            filestream11=open('sharktaletime.txt','w')
            filestream11.writelines(data)
            filestream11.close() 
        if newtime9!='':
            data[8]=newtime9 +'\n'
            filestream12=open('sharktaletime.txt','w')
            filestream12.writelines(data)
            filestream12.close()
        if newtime10!='':
            data[9]=newtime10 +'\n'
            filestream13=open('sharktaletime.txt','w')
            filestream13.writelines(data)
            filestream13.close()
        if newtime11!='':
            data[10]=newtime11 +'\n'
            filestream14=open('sharktaletime.txt','w')
            filestream14.writelines(data)
            filestream14.close() 
        if newtime12!='':
            data[11]=newtime12 +'\n'
            filestream15=open('sharktaletime.txt','w')
            filestream15.writelines(data)
            filestream15.close() 
        if newtime13!='':
            data[12]=newtime13 +'\n'
            filestream16=open('sharktaletime.txt','w')
            filestream16.writelines(data)
            filestream16.close()
        if newtime14!='':
            data[13]=newtime14 +'\n'
            filestream17=open('sharktaletime.txt','w')
            filestream17.writelines(data)
            filestream17.close()
        if newtime15!='':
            data[14]=newtime15 +'\n'
            filestream18=open('sharktaletime.txt','w')
            filestream18.writelines(data)
            filestream18.close() 
        if newtime16!='':
            data[15]=newtime16 +'\n'
            filestream19=open('sharktaletime.txt','w')
            filestream19.writelines(data)
            filestream19.close() 
        if newtime17!='':
            data[16]=newtime17 +'\n'
            filestream20=open('sharktaletime.txt','w')
            filestream20.writelines(data)
            filestream20.close() 
        if newtime18!='':
            data[17]=newtime18 +'\n'
            filestream20=open('sharktaletime.txt','w')
            filestream20.writelines(data)
            filestream20.close()
        if newtime19!='':
            data[18]=newtime19 +'\n'
            filestream21=open('sharktaletime.txt','w')
            filestream21.writelines(data)
            filestream21.close()
        if newtime20!='':
            data[19]=newtime20 +'\n'
            filestream22=open('sharktaletime.txt','w')
            filestream22.writelines(data)
            filestream22.close() 
        if newtime21!='':
            data[20]=newtime21 +'\n'
            filestream23=open('sharktaletime.txt','w')
            filestream23.writelines(data)
            filestream23.close() 

    change_to_Admin()

#function to change to the color of Showing time 1 when clicked
def change_Showing1_Color():
    global btn_Showing1
    global color1
    btn_Showing1.config(fg=next(color1))

#function to change to the color of Showing time 2 when clicked
def change_Showing2_Color():
    global color2
    global btn_Showing2
    btn_Showing2.config(fg=next(color2))

#function to change to the color of Showing time 3 when clicked
def change_Showing3_Color():
    global btn_Showing3
    global color3
    btn_Showing3.config(fg=next(color3))   

#function to change to the color of Showing time 4 when clicked
def change_Showing4_Color():
    global btn_Showing4
    global color4
    btn_Showing4.config(fg=next(color4))

#function to change to the color of Showing time 5 when clicked
def change_Showing5_Color():
    global btn_Showing5
    global color5
    btn_Showing5.config(fg=next(color5))

#function to change to the color of Showing time 6 when clicked
def change_Showing6_Color():
    global btn_Showing6
    global color6
    btn_Showing6.config(fg=next(color6))   

#function to change to the color of Showing time 7 when clicked
def change_Showing7_Color():
    global btn_Showing7
    global color7
    btn_Showing7.config(fg=next(color7))

#function to change to the color of Showing time 8 when clicked
def change_Showing8_Color():
    global btn_Showing8
    global color8
    btn_Showing8.config(fg=next(color8))

#function to change to the color of Showing time 9 when clicked
def change_Showing9_Color():
    global btn_Showing9
    global color9
    btn_Showing9.config(fg=next(color9))

#function to change to the color of Showing time 10 when clicked
def change_Showing10_Color():
    global btn_Showing10
    global color10
    btn_Showing10.config(fg=next(color10))

#function to change to the color of Showing time 11 when clicked
def change_Showing11_Color():
    global btn_Showing11
    global color11
    btn_Showing11.config(fg=next(color11))   

#function to change to the color of Showing time 12 when clicked
def change_Showing12_Color():
    global btn_Showing12
    global color12
    btn_Showing12.config(fg=next(color12))

#function to change to the color of Showing time 13 when clicked
def change_Showing13_Color():
    global btn_Showing13 
    global color13
    btn_Showing13.config(fg=next(color13))

#function to change to the color of Showing time 14 when clicked
def change_Showing14_Color():
    global btn_Showing14
    global color14
    btn_Showing14.config(fg=next(color14))   

#function to change to the color of Showing time 15 when clicked
def change_Showing15_Color():
    global btn_Showing15
    global color15
    btn_Showing15.config(fg=next(color15))

#function to change to the color of Showing time 16 when clicked
def change_Showing16_Color():
    global btn_Showing16
    global color16
    btn_Showing16.config(fg=next(color16))

#function to change to the color of Showing time 17 when clicked
def change_Showing17_Color():
    global btn_Showing17
    global color17
    btn_Showing17.config(fg=next(color17))

#function to change to the color of Showing time 18 when clicked
def change_Showing18_Color():
    global btn_Showing18
    global color18
    btn_Showing18.config(fg=next(color18))   

#function to change to the color of Showing time 19 when clicked
def change_Showing19_Color():
    global btn_Showing19
    global color19
    btn_Showing19.config(fg=next(color19))

#function to change to the color of Showing time 20 when clicked
def change_Showing20_Color():
    global btn_Showing20
    global color20
    btn_Showing20.config(fg=next(color20))

#function to change to the color of Showing time 21 when clicked
def change_Showing21_Color():
    global btn_Showing21
    global color21
    btn_Showing21.config(fg=next(color21))


#function to change to the mainscreen after hit login
def change_to_Main():
    Login_frame.forget()
    Current_frame.forget()
    Upcoming_frame.forget()
    Checkout_frame.forget()
    Description_Frame.forget()
    Checkout_frame.forget()
    Main_frame.pack(fill='both', expand=1)


#function to logout of Main page and go back to login page
def change_to_Login():
    Main_frame.forget()
    Register_frame.forget()
    Admin_frame.forget()
    Login_frame.pack(fill='both', expand=1)

#function to change frame to register frame
def change_to_Register():
    Login_frame.forget()
    Register_frame.pack(fill='both', expand=1)

#function to change frame to Current Movies
def change_to_Current():
    Login_frame.forget()
    Main_frame.forget()
    Description_Frame.forget()
    Current_frame.pack(fill='both', expand=1)

#function to change frame to upcoming Movies
def change_to_Upcoming():
    Login_frame.forget()
    Main_frame.forget()
    Description_Frame2.forget()
    Upcoming_frame.pack(fill='both', expand=1)

#function to change frame to movie_description
def change_to_Description():
    Login_frame.forget()
    Main_frame.forget()
    Upcoming_frame.forget()
    Current_frame.forget()
    Showtime_frame.forget()
    Description_Frame.pack(fill='both', expand=1)

#function to change frame to Showtimes
def change_to_Showtime():
    for widget in Showtime_frame.winfo_children():
        widget.destroy()
    global image23
    global img23
    global moviefilename
    global movie_time1,movie_time2,movie_time3
    global djangosun1,djangosun2,djangosun3,djangomon1,djangomon2,djangomon3,djangotues1,djangotues2,djangotues3,djangowed1,djangowed2,djangowed3,djangothurs1,djangothurs2,djangothurs3,djangofri1,djangofri2,djangofri3,djangosat1,djangosat2,djangosat3
    image23 = Image.open(moviefilename)
    image23 = image23.resize((200,250), Image.ANTIALIAS)
    img23 = ImageTk.PhotoImage(image23)
    if moviefilename=='djangopic.jpg':
        movie_time1 =djangosun1
        movie_time2 = djangosun2
        movie_time3 =djangosun3
    Login_frame.forget()
    Main_frame.forget()
    Upcoming_frame.forget()
    Current_frame.forget()
    Checkout_frame.forget()
    Description_Frame.forget()
    Showtime_frame.pack(fill='both', expand=1)
    showtimeframe()

#function to change frame to checkout
def change_to_Checkout():
    for widget in Checkout_frame.winfo_children():
        widget.destroy()
    Login_frame.forget()
    Main_frame.forget()
    Upcoming_frame.forget()
    Current_frame.forget()
    Showtime_frame.forget()
    Checkout_frame.pack(fill='both', expand=1)
    checkout()

#function to change frame to Admin
def change_to_Admin():
    Login_frame.forget()
    Current_frame.forget()
    Upcoming_frame.forget()
    Checkout_frame.forget()
    ManageShows_frame.forget()
    edit_shows_frame.forget()
    Admin_frame.pack(fill='both', expand=1)
    admin()

#function to change frame to manage shows
def change_to_ManageShows():
    global image25,image26,image27,image28,image29,image30,image31,image32,image33,img25,img26,img27,img28,img29,img30,img31,img32,img33
    for widget in ManageShows_frame.winfo_children():
        widget.destroy()
    #images for movies
    image25 = Image.open('diehardpic.jpg')
    image26 = Image.open('rushhourpic.jpg')
    image27 = Image.open('elfpic.jpg')
    image28= Image.open('matrixpic.jpg')
    image29 = Image.open('onepiecepic.jpg')
    image30 = Image.open('fightclubpic.jpg')
    image31 = Image.open('darkknightpic.jpg')
    image32 = Image.open('djangopic.jpg')
    image33 = Image.open('sharktale.jpg')

    image25 = image25.resize((100,150), Image.ANTIALIAS)
    image26 = image26.resize((100,150), Image.ANTIALIAS)
    image27 = image27.resize((100,150), Image.ANTIALIAS)
    image28 = image28.resize((100,150), Image.ANTIALIAS)
    image29 = image29.resize((100,150), Image.ANTIALIAS)
    image30 = image30.resize((100,150), Image.ANTIALIAS)
    image31 = image31.resize((100,150), Image.ANTIALIAS)
    image32 = image32.resize((100,150), Image.ANTIALIAS)
    image33 = image33.resize((100,150), Image.ANTIALIAS)

    img25= ImageTk.PhotoImage(image25)
    img26= ImageTk.PhotoImage(image26)
    img27= ImageTk.PhotoImage(image27)
    img28= ImageTk.PhotoImage(image28)
    img29= ImageTk.PhotoImage(image29)
    img30= ImageTk.PhotoImage(image30)
    img31= ImageTk.PhotoImage(image31)
    img32= ImageTk.PhotoImage(image32)
    img33= ImageTk.PhotoImage(image33)
    Login_frame.forget()
    Main_frame.forget()
    Upcoming_frame.forget()
    Current_frame.forget()
    Showtime_frame.forget()
    Admin_frame.forget()
    ManageShows_frame.forget()
    edit_shows_frame.forget()
    ManageShows_frame.pack(fill='both', expand=1)
    manage_shows()


#function to change frame to Admin
def change_to_edit_shows():
    Login_frame.forget()
    Current_frame.forget()
    Upcoming_frame.forget()
    Checkout_frame.forget()
    ManageShows_frame.forget()
    edit_shows_frame.pack(fill='both', expand=1)
    edit_show()



#function to fill description frame with diehard info
def diehard_description():
    for widget in Description_Frame.winfo_children():
        widget.destroy()
    global heading_description,movieruntime,movie_description,movierating,moviecost,moviefilename
    global image22
    global img22
    global movie_time1, movie_time2, movie_time3, movie_time4, movie_time5, movie_time6, movie_time7, movie_time8, movie_time9, movie_time10, movie_time11, movie_time12, movie_time13, movie_time14, movie_time15, movie_time16, movie_time17, movie_time18, movie_time19, movie_time20, movie_time21
    global diehardsun1,diehardsun2,diehardsun3
    Login_frame.forget()
    Main_frame.forget()
    Upcoming_frame.forget()
    Current_frame.forget()
    Description_Frame.pack(fill='both', expand=1)
    heading_description = 'Die Hard'
    movieruntime='Runtime: 2h 12m'
    movie_description = 'Description: A New York City police officer tries to save his estranged wife\n and several others taken hostage by terrorists during a Christmas party at the \nNakatomi Plaza in Los Angeles.'
    movierating= 'Rating: R'
    file3 = open('diehardcost.txt', 'r')
    Lines3 = file3.readlines()
    for line in Lines3:
        line = line.strip('\n')
        moviecost ='Cost= $'+str(line)
    moviefilename = 'diehardpic.jpg'

    file2 = open('diehardtime.txt', 'r')
    Lines2 = file2.readlines()
    movie_time1=Lines2[0].strip('\n')
    movie_time2=Lines2[1].strip('\n')
    movie_time3=Lines2[2].strip('\n')
    movie_time4=Lines2[3].strip('\n')
    movie_time5=Lines2[4].strip('\n')
    movie_time6=Lines2[5].strip('\n')
    movie_time7=Lines2[6].strip('\n')
    movie_time8=Lines2[7].strip('\n')
    movie_time9=Lines2[8].strip('\n')
    movie_time10=Lines2[9].strip('\n')
    movie_time11=Lines2[10].strip('\n')
    movie_time12=Lines2[11].strip('\n')
    movie_time13=Lines2[12].strip('\n')
    movie_time14=Lines2[13].strip('\n')
    movie_time15=Lines2[14].strip('\n')
    movie_time16=Lines2[15].strip('\n')
    movie_time17=Lines2[16].strip('\n')
    movie_time18=Lines2[17].strip('\n')
    movie_time19=Lines2[18].strip('\n')
    movie_time20=Lines2[19].strip('\n')
    movie_time21=Lines2[20].strip('\n')
    file2.close()
    file3.close()
    #images for frame
    image22= Image.open(moviefilename)

    image22 = image22.resize((200,250), Image.ANTIALIAS)

    img22= ImageTk.PhotoImage(image22)
    descriptionframe()
    image22.close()


#function to fill description frame with Rushhour info
def rushour_description():
    for widget in Description_Frame.winfo_children():
        widget.destroy()
    global rushhoursun1,rushhoursun2,rushhoursun3
    global heading_description,movieruntime,movie_description,movierating,moviecost,moviefilename
    global image22
    global img22
    global movie_time1, movie_time2, movie_time3, movie_time4, movie_time5, movie_time6, movie_time7, movie_time8, movie_time9, movie_time10, movie_time11, movie_time12, movie_time13, movie_time14, movie_time15, movie_time16, movie_time17, movie_time18, movie_time19, movie_time20, movie_time21
    Login_frame.forget()
    Main_frame.forget()
    Upcoming_frame.forget()
    Current_frame.forget()
    Description_Frame.pack(fill='both', expand=1)
    heading_description = 'Rush Hour'
    movieruntime='Runtime: 1h 38m'
    movie_description = 'Description: A loyal and dedicated Hong Kong Inspector teams up with a \nreckless and loudmouthed L.A.P.D. detective to rescue the Chinese Consuls\n kidnapped daughter, while trying to arrest a dangerous crime lord along the \nway.'
    movierating= 'Rating: PG-13'
    file3 = open('rushhourcost.txt', 'r')
    Lines3 = file3.readlines()
    for line in Lines3:
        line = line.strip('\n')
        moviecost ='Cost= $'+str(line)
    moviefilename = 'rushhourpic.jpg'
    file2 = open('rushhourtime.txt', 'r')
    Lines2 = file2.readlines()
    movie_time1=Lines2[0].strip('\n')
    movie_time2=Lines2[1].strip('\n')
    movie_time3=Lines2[2].strip('\n')
    movie_time4=Lines2[3].strip('\n')
    movie_time5=Lines2[4].strip('\n')
    movie_time6=Lines2[5].strip('\n')
    movie_time7=Lines2[6].strip('\n')
    movie_time8=Lines2[7].strip('\n')
    movie_time9=Lines2[8].strip('\n')
    movie_time10=Lines2[9].strip('\n')
    movie_time11=Lines2[10].strip('\n')
    movie_time12=Lines2[11].strip('\n')
    movie_time13=Lines2[12].strip('\n')
    movie_time14=Lines2[13].strip('\n')
    movie_time15=Lines2[14].strip('\n')
    movie_time16=Lines2[15].strip('\n')
    movie_time17=Lines2[16].strip('\n')
    movie_time18=Lines2[17].strip('\n')
    movie_time19=Lines2[18].strip('\n')
    movie_time20=Lines2[19].strip('\n')
    movie_time21=Lines2[20].strip('\n')
    #images for frame
    image22= Image.open(moviefilename)

    image22 = image22.resize((200,250), Image.ANTIALIAS)

    img22= ImageTk.PhotoImage(image22)
    descriptionframe()
    image22.close()


#function to fill description frame with elf info
def elf_description():
    for widget in Description_Frame.winfo_children():
        widget.destroy()
    global elfsun1,elfsun2,elfsun3
    global heading_description,movieruntime,movie_description,movierating,moviecost,moviefilename
    global image22
    global img22
    global movie_time1, movie_time2, movie_time3, movie_time4, movie_time5, movie_time6, movie_time7, movie_time8, movie_time9, movie_time10, movie_time11, movie_time12, movie_time13, movie_time14, movie_time15, movie_time16, movie_time17, movie_time18, movie_time19, movie_time20, movie_time21
    Login_frame.forget()
    Main_frame.forget()
    Upcoming_frame.forget()
    Current_frame.forget()
    Description_Frame.pack(fill='both', expand=1)
    heading_description = 'ELF'
    movieruntime='Runtime: 1h 37m'
    movie_description = 'Description: Raised as an oversized elf, Buddy travels from the North Pole to \nNew York City to meet his biological father, Walter Hobbs, who doesnt know he \nexists and is in desperate need of some Christmas spirit.'
    movierating= 'Rating: PG'
    file3 = open('elfcost.txt', 'r')
    Lines3 = file3.readlines()
    for line in Lines3:
        line = line.strip('\n')
        moviecost ='Cost= $'+str(line)
    moviefilename = 'elfpic.jpg'
    file2 = open('elftime.txt', 'r')
    Lines2 = file2.readlines()
    movie_time1=Lines2[0].strip('\n')
    movie_time2=Lines2[1].strip('\n')
    movie_time3=Lines2[2].strip('\n')
    movie_time4=Lines2[3].strip('\n')
    movie_time5=Lines2[4].strip('\n')
    movie_time6=Lines2[5].strip('\n')
    movie_time7=Lines2[6].strip('\n')
    movie_time8=Lines2[7].strip('\n')
    movie_time9=Lines2[8].strip('\n')
    movie_time10=Lines2[9].strip('\n')
    movie_time11=Lines2[10].strip('\n')
    movie_time12=Lines2[11].strip('\n')
    movie_time13=Lines2[12].strip('\n')
    movie_time14=Lines2[13].strip('\n')
    movie_time15=Lines2[14].strip('\n')
    movie_time16=Lines2[15].strip('\n')
    movie_time17=Lines2[16].strip('\n')
    movie_time18=Lines2[17].strip('\n')
    movie_time19=Lines2[18].strip('\n')
    movie_time20=Lines2[19].strip('\n')
    movie_time21=Lines2[20].strip('\n')
    #images for frame
    image22= Image.open(moviefilename)

    image22 = image22.resize((200,250), Image.ANTIALIAS)

    img22= ImageTk.PhotoImage(image22)
    descriptionframe()
    image22.close()


#function to fill description frame with matrix info
def matrix_description():
    for widget in Description_Frame.winfo_children():
        widget.destroy()
    global matrixsun1,matrixsun2,matrixsun3
    global heading_description,movieruntime,movie_description,movierating,moviecost,moviefilename
    global image22
    global img22
    global movie_time1, movie_time2, movie_time3, movie_time4, movie_time5, movie_time6, movie_time7, movie_time8, movie_time9, movie_time10, movie_time11, movie_time12, movie_time13, movie_time14, movie_time15, movie_time16, movie_time17, movie_time18, movie_time19, movie_time20, movie_time21
    Login_frame.forget()
    Main_frame.forget()
    Upcoming_frame.forget()
    Current_frame.forget()
    Description_Frame.pack(fill='both', expand=1)
    heading_description = 'The Matrix'
    movieruntime='Runtime: 2h 16m'
    movie_description = 'Description: When a beautiful stranger leads computer hacker Neo to a \nforbidding underworld, he discovers the shocking truth--the life he knows is \nthe elaborate deception of an evil cyber-intelligence.'
    movierating= 'Rating: R'
    file3 = open('matrixcost.txt', 'r')
    Lines3 = file3.readlines()
    for line in Lines3:
        line = line.strip('\n')
        moviecost ='Cost= $'+str(line)
    moviefilename = 'matrixpic.jpg'
    file2 = open('matrixtime.txt', 'r')
    Lines2 = file2.readlines()
    movie_time1=Lines2[0].strip('\n')
    movie_time2=Lines2[1].strip('\n')
    movie_time3=Lines2[2].strip('\n')
    movie_time4=Lines2[3].strip('\n')
    movie_time5=Lines2[4].strip('\n')
    movie_time6=Lines2[5].strip('\n')
    movie_time7=Lines2[6].strip('\n')
    movie_time8=Lines2[7].strip('\n')
    movie_time9=Lines2[8].strip('\n')
    movie_time10=Lines2[9].strip('\n')
    movie_time11=Lines2[10].strip('\n')
    movie_time12=Lines2[11].strip('\n')
    movie_time13=Lines2[12].strip('\n')
    movie_time14=Lines2[13].strip('\n')
    movie_time15=Lines2[14].strip('\n')
    movie_time16=Lines2[15].strip('\n')
    movie_time17=Lines2[16].strip('\n')
    movie_time18=Lines2[17].strip('\n')
    movie_time19=Lines2[18].strip('\n')
    movie_time20=Lines2[19].strip('\n')
    movie_time21=Lines2[20].strip('\n')
    #images for frame
    image22= Image.open(moviefilename)

    image22 = image22.resize((200,250), Image.ANTIALIAS)

    img22= ImageTk.PhotoImage(image22)
    descriptionframe()
    image22.close()


#function to fill description frame with one piece info
def onepiece_description():
    for widget in Description_Frame.winfo_children():
        widget.destroy()
    global heading_description,movieruntime,movie_description,movierating,moviecost,moviefilename
    global image22
    global img22
    global movie_time1, movie_time2, movie_time3, movie_time4, movie_time5, movie_time6, movie_time7, movie_time8, movie_time9, movie_time10, movie_time11, movie_time12, movie_time13, movie_time14, movie_time15, movie_time16, movie_time17, movie_time18, movie_time19, movie_time20, movie_time21
    global onepiecesun1,onepiecesun2,onepiecesun3
    Login_frame.forget()
    Main_frame.forget()
    Upcoming_frame.forget()
    Current_frame.forget()
    Description_Frame.pack(fill='both', expand=1)
    heading_description = 'One Piece Film: Red'
    movieruntime='Runtime: 1h 55m'
    movie_description = 'Description: For the first time ever, Uta - the most beloved singer in the \nworld - will reveal herself to the world at a live concert. The voice that the \nwhole world has been waiting for is about to resound.'
    movierating= 'Rating: PG-13'
    file3 = open('onepiececost.txt', 'r')
    Lines3 = file3.readlines()
    for line in Lines3:
        line = line.strip('\n')
        moviecost ='Cost= $'+str(line)
    moviefilename = 'onepiecepic.jpg'
    file2 = open('onepiecetime.txt', 'r')
    Lines2 = file2.readlines()
    movie_time1=Lines2[0].strip('\n')
    movie_time2=Lines2[1].strip('\n')
    movie_time3=Lines2[2].strip('\n')
    movie_time4=Lines2[3].strip('\n')
    movie_time5=Lines2[4].strip('\n')
    movie_time6=Lines2[5].strip('\n')
    movie_time7=Lines2[6].strip('\n')
    movie_time8=Lines2[7].strip('\n')
    movie_time9=Lines2[8].strip('\n')
    movie_time10=Lines2[9].strip('\n')
    movie_time11=Lines2[10].strip('\n')
    movie_time12=Lines2[11].strip('\n')
    movie_time13=Lines2[12].strip('\n')
    movie_time14=Lines2[13].strip('\n')
    movie_time15=Lines2[14].strip('\n')
    movie_time16=Lines2[15].strip('\n')
    movie_time17=Lines2[16].strip('\n')
    movie_time18=Lines2[17].strip('\n')
    movie_time19=Lines2[18].strip('\n')
    movie_time20=Lines2[19].strip('\n')
    movie_time21=Lines2[20].strip('\n')
    #images for frame
    image22= Image.open(moviefilename)

    image22 = image22.resize((200,250), Image.ANTIALIAS)

    img22= ImageTk.PhotoImage(image22)
    descriptionframe()
    image22.close()


#function to fill description frame with fight club info
def fightclub_description():
    for widget in Description_Frame.winfo_children():
        widget.destroy()
    global heading_description,movieruntime,movie_description,movierating,moviecost,moviefilename
    global image22
    global img22
    global movie_time1, movie_time2, movie_time3, movie_time4, movie_time5, movie_time6, movie_time7, movie_time8, movie_time9, movie_time10, movie_time11, movie_time12, movie_time13, movie_time14, movie_time15, movie_time16, movie_time17, movie_time18, movie_time19, movie_time20, movie_time21
    global fightclubsun1,fightclubsun2,fightclubsun3
    Login_frame.forget()
    Main_frame.forget()
    Upcoming_frame.forget()
    Current_frame.forget()
    Description_Frame.pack(fill='both', expand=1)
    heading_description = 'Fight Club'
    movieruntime='Runtime: 2h 19m'
    movie_description = 'Description: An insomniac office worker and a devil-may-care soap maker form \nan underground fight club that evolves into much more.'
    movierating= 'Rating: R'
    file3 = open('fightclubcost.txt', 'r')
    Lines3 = file3.readlines()
    for line in Lines3:
        line = line.strip('\n')
        moviecost ='Cost= $'+str(line)
    moviefilename = 'fightclubpic.jpg'
    file2 = open('fightclubtime.txt', 'r')
    Lines2 = file2.readlines()
    movie_time1=Lines2[0].strip('\n')
    movie_time2=Lines2[1].strip('\n')
    movie_time3=Lines2[2].strip('\n')
    movie_time4=Lines2[3].strip('\n')
    movie_time5=Lines2[4].strip('\n')
    movie_time6=Lines2[5].strip('\n')
    movie_time7=Lines2[6].strip('\n')
    movie_time8=Lines2[7].strip('\n')
    movie_time9=Lines2[8].strip('\n')
    movie_time10=Lines2[9].strip('\n')
    movie_time11=Lines2[10].strip('\n')
    movie_time12=Lines2[11].strip('\n')
    movie_time13=Lines2[12].strip('\n')
    movie_time14=Lines2[13].strip('\n')
    movie_time15=Lines2[14].strip('\n')
    movie_time16=Lines2[15].strip('\n')
    movie_time17=Lines2[16].strip('\n')
    movie_time18=Lines2[17].strip('\n')
    movie_time19=Lines2[18].strip('\n')
    movie_time20=Lines2[19].strip('\n')
    movie_time21=Lines2[20].strip('\n')
    #images for frame
    image22= Image.open(moviefilename)

    image22 = image22.resize((200,250), Image.ANTIALIAS)

    img22= ImageTk.PhotoImage(image22)
    descriptionframe()
    image22.close()


#function to fill description frame with dark knight info
def batman_description():
    for widget in Description_Frame.winfo_children():
        widget.destroy()
    global heading_description,movieruntime,movie_description,movierating,moviecost,moviefilename
    global image22
    global img22
    global movie_time1, movie_time2, movie_time3, movie_time4, movie_time5, movie_time6, movie_time7, movie_time8, movie_time9, movie_time10, movie_time11, movie_time12, movie_time13, movie_time14, movie_time15, movie_time16, movie_time17, movie_time18, movie_time19, movie_time20, movie_time21
    global batmansun1,batmansun2,batmansun3
    Login_frame.forget()
    Main_frame.forget()
    Upcoming_frame.forget()
    Current_frame.forget()
    Description_Frame.pack(fill='both', expand=1)
    heading_description = 'The Dark Knight'
    movieruntime='Runtime: 2h 32m'
    movie_description = 'Description: When the menace known as the Joker wreaks havoc and chaos on the \npeople of Gotham, Batman must accept one of the greatest psychological and \nphysical tests of his ability to fight injustice.'
    movierating= 'Rating: PG-13'
    file3 = open('darkknightcost.txt', 'r')
    Lines3 = file3.readlines()
    for line in Lines3:
        line = line.strip('\n')
        moviecost ='Cost= $'+str(line)
    moviefilename = 'darkknightpic.jpg'
    file2 = open('batmantime.txt', 'r')
    Lines2 = file2.readlines()
    movie_time1=Lines2[0].strip('\n')
    movie_time2=Lines2[1].strip('\n')
    movie_time3=Lines2[2].strip('\n')
    movie_time4=Lines2[3].strip('\n')
    movie_time5=Lines2[4].strip('\n')
    movie_time6=Lines2[5].strip('\n')
    movie_time7=Lines2[6].strip('\n')
    movie_time8=Lines2[7].strip('\n')
    movie_time9=Lines2[8].strip('\n')
    movie_time10=Lines2[9].strip('\n')
    movie_time11=Lines2[10].strip('\n')
    movie_time12=Lines2[11].strip('\n')
    movie_time13=Lines2[12].strip('\n')
    movie_time14=Lines2[13].strip('\n')
    movie_time15=Lines2[14].strip('\n')
    movie_time16=Lines2[15].strip('\n')
    movie_time17=Lines2[16].strip('\n')
    movie_time18=Lines2[17].strip('\n')
    movie_time19=Lines2[18].strip('\n')
    movie_time20=Lines2[19].strip('\n')
    movie_time21=Lines2[20].strip('\n')
    #images for frame
    image22= Image.open(moviefilename)

    image22 = image22.resize((200,250), Image.ANTIALIAS)

    img22= ImageTk.PhotoImage(image22)
    descriptionframe()
    image22.close()


#function to fill description frame with django info
def django_description():
    for widget in Description_Frame.winfo_children():
        widget.destroy()
    global heading_description,movieruntime,movie_description,movierating,moviecost,moviefilename
    global djangosun1,djangosun2,djangosun3,djangomon1,djangomon2,djangomon3,djangotues1,djangotues2,djangotues3,djangowed1,djangowed2,djangowed3,djangothurs1,djangothurs2,djangothurs3,djangofri1,djangofri2,djangofri3,djangosat1,djangosat2,djangosat3
    global movie_time1, movie_time2, movie_time3, movie_time4, movie_time5, movie_time6, movie_time7, movie_time8, movie_time9, movie_time10, movie_time11, movie_time12, movie_time13, movie_time14, movie_time15, movie_time16, movie_time17, movie_time18, movie_time19, movie_time20, movie_time21
    global image22
    global img22
    Login_frame.forget()
    Main_frame.forget()
    Upcoming_frame.forget()
    Current_frame.forget()
    Description_Frame.pack(fill='both', expand=1)
    heading_description = 'Django Unchained'
    movieruntime='Runtime: 2h 45m'
    movie_description = 'Description: With the help of a German bounty-hunter, a freed slave sets out to\n rescue his wife from a brutal plantation-owner in Mississippi.'
    movierating= 'Rating: R'
    file3 = open('djangocost.txt', 'r')
    Lines3 = file3.readlines()
    for line in Lines3:
        line = line.strip('\n')
        moviecost ='Cost= $'+str(line)
    moviefilename = 'djangopic.jpg'
    file2 = open('djangotime.txt', 'r')
    Lines2 = file2.readlines()
    movie_time1=Lines2[0].strip('\n')
    movie_time2=Lines2[1].strip('\n')
    movie_time3=Lines2[2].strip('\n')
    movie_time4=Lines2[3].strip('\n')
    movie_time5=Lines2[4].strip('\n')
    movie_time6=Lines2[5].strip('\n')
    movie_time7=Lines2[6].strip('\n')
    movie_time8=Lines2[7].strip('\n')
    movie_time9=Lines2[8].strip('\n')
    movie_time10=Lines2[9].strip('\n')
    movie_time11=Lines2[10].strip('\n')
    movie_time12=Lines2[11].strip('\n')
    movie_time13=Lines2[12].strip('\n')
    movie_time14=Lines2[13].strip('\n')
    movie_time15=Lines2[14].strip('\n')
    movie_time16=Lines2[15].strip('\n')
    movie_time17=Lines2[16].strip('\n')
    movie_time18=Lines2[17].strip('\n')
    movie_time19=Lines2[18].strip('\n')
    movie_time20=Lines2[19].strip('\n')
    movie_time21=Lines2[20].strip('\n')

    #images for frame
    image22= Image.open(moviefilename)

    image22 = image22.resize((200,250), Image.ANTIALIAS)

    img22= ImageTk.PhotoImage(image22)
    descriptionframe()
    image22.close()


#function to fill description frame with shark tale info
def sharktale_description():
    for widget in Description_Frame.winfo_children():
        widget.destroy()
    global heading_description,movieruntime,movie_description,movierating,moviecost,moviefilename
    global image22
    global img22
    global movie_time1, movie_time2, movie_time3, movie_time4, movie_time5, movie_time6, movie_time7, movie_time8, movie_time9, movie_time10, movie_time11, movie_time12, movie_time13, movie_time14, movie_time15, movie_time16, movie_time17, movie_time18, movie_time19, movie_time20, movie_time21
    global sharktalesun1,sharktalesun2,sharktalesun3
    Login_frame.forget()
    Main_frame.forget()
    Upcoming_frame.forget()
    Current_frame.forget()
    Description_Frame.pack(fill='both', expand=1)
    heading_description = 'Shark Tale'
    movieruntime='Runtime: 1h 30m'
    movie_description = 'Description: When a son of a gangster shark boss is accidentally killed while \non the hunt, his would-be prey and his vegetarian brother decide to use the \nincident to their own advantage.'
    movierating= 'Rating: PG'
    file3 = open('sharktalecost.txt', 'r')
    Lines3 = file3.readlines()
    for line in Lines3:
        line = line.strip('\n')
        moviecost ='Cost= $'+str(line)
    moviefilename = 'sharktale.jpg'
    file2 = open('sharktaletime.txt', 'r')
    Lines2 = file2.readlines()
    movie_time1=Lines2[0].strip('\n')
    movie_time2=Lines2[1].strip('\n')
    movie_time3=Lines2[2].strip('\n')
    movie_time4=Lines2[3].strip('\n')
    movie_time5=Lines2[4].strip('\n')
    movie_time6=Lines2[5].strip('\n')
    movie_time7=Lines2[6].strip('\n')
    movie_time8=Lines2[7].strip('\n')
    movie_time9=Lines2[8].strip('\n')
    movie_time10=Lines2[9].strip('\n')
    movie_time11=Lines2[10].strip('\n')
    movie_time12=Lines2[11].strip('\n')
    movie_time13=Lines2[12].strip('\n')
    movie_time14=Lines2[13].strip('\n')
    movie_time15=Lines2[14].strip('\n')
    movie_time16=Lines2[15].strip('\n')
    movie_time17=Lines2[16].strip('\n')
    movie_time18=Lines2[17].strip('\n')
    movie_time19=Lines2[18].strip('\n')
    movie_time20=Lines2[19].strip('\n')
    movie_time21=Lines2[20].strip('\n')
    #images for frame
    image22= Image.open(moviefilename)

    image22 = image22.resize((200,250), Image.ANTIALIAS)

    img22= ImageTk.PhotoImage(image22)
    descriptionframe()
    image22.close()



#function to fill description frame with pirates info
def pirates_description():
    for widget in Description_Frame2.winfo_children():
        widget.destroy()
    global heading_description,movieruntime,movie_description,movierating,moviecost,moviefilename
    global image24
    global img24
    Login_frame.forget()
    Main_frame.forget()
    Upcoming_frame.forget()
    Current_frame.forget()
    Description_Frame2.pack(fill='both', expand=1)
    heading_description = 'Pirates of the Carribean'
    movieruntime='Runtime: 2h 21m'
    movie_description = 'Description: Jack Sparrow and Barbossa embark on a quest to find the elusive \nfountain of youth, only to discover that Blackbeard and his daughter are after \nit too.'
    movierating= 'Rating: PG-13'
    moviecost ='cost = $15'
    moviefilename = 'Piratespic.jpg'
    #images for frame
    image24= Image.open(moviefilename)

    image24 = image24.resize((200,250), Image.ANTIALIAS)

    img24= ImageTk.PhotoImage(image24)
    descriptionframe2()
    image24.close()


#function to fill description frame with lord of the rings info
def lordofrings_description():
    for widget in Description_Frame2.winfo_children():
        widget.destroy()
    global heading_description,movieruntime,movie_description,movierating,moviecost,moviefilename
    global image24
    global img24
    Login_frame.forget()
    Main_frame.forget()
    Upcoming_frame.forget()
    Current_frame.forget()
    Description_Frame2.pack(fill='both', expand=1)
    heading_description = 'Lord of the Rings'
    movieruntime='Runtime: 2h 58m'
    movie_description = 'Description: A meek Hobbit from the Shire and eight companions set out on a\n journey to destroy the powerful One Ring and save Middle-earth from the Dark \nLord Sauron.'
    movierating= 'Rating: PG-13'
    moviecost ='cost = $15'
    moviefilename = 'lordofrings.jpg'
    #images for frame
    image24= Image.open(moviefilename)

    image24 = image24.resize((200,250), Image.ANTIALIAS)

    img24= ImageTk.PhotoImage(image24)
    descriptionframe2()
    image24.close()


#function to fill description frame with inception info
def inception_description():
    for widget in Description_Frame2.winfo_children():
        widget.destroy()
    global heading_description,movieruntime,movie_description,movierating,moviecost,moviefilename
    global image24
    global img24
    Login_frame.forget()
    Main_frame.forget()
    Upcoming_frame.forget()
    Current_frame.forget()
    Description_Frame2.pack(fill='both', expand=1)
    heading_description = 'Inception'
    movieruntime='Runtime: 2h 28m'
    movie_description = 'Description: A thief who steals corporate secrets through the use of \ndream-sharing technology is given the inverse task of planting an idea into the\n mind of a C.E.O., but his tragic past may doom the project and his team to \ndisaster..'
    movierating= 'Rating: PG-13'
    moviecost ='cost = $15'
    moviefilename = 'inceptionpic.jpg'
    #images for frame
    image24= Image.open(moviefilename)

    image24 = image24.resize((200,250), Image.ANTIALIAS)

    img24= ImageTk.PhotoImage(image24)
    descriptionframe2()
    image24.close()


#function to fill description frame with avengers info
def avengers_description():
    for widget in Description_Frame2.winfo_children():
        widget.destroy()
    global heading_description,movieruntime,movie_description,movierating,moviecost,moviefilename
    global image24
    global img24
    Login_frame.forget()
    Main_frame.forget()
    Upcoming_frame.forget()
    Current_frame.forget()
    Description_Frame2.pack(fill='both', expand=1)
    heading_description = 'Avengers: Endgame'
    movieruntime='Runtime: 2h 28m'
    movie_description = 'Description:After the devastating events of Avengers: Infinity War (2018), the\n universe is in ruins. With the help of remaining allies, the Avengers assemble \nonce more in order to reverse Thanos actions and restore balance to the \nuniverse.'
    movierating= 'Rating: PG-13'
    moviecost ='cost = $15'
    moviefilename = 'avengerspic.jpg'
    #images for frame
    image24= Image.open(moviefilename)

    image24 = image24.resize((200,250), Image.ANTIALIAS)

    img24= ImageTk.PhotoImage(image24)
    descriptionframe2()
    image24.close()


#function to fill description frame with interstellar info
def interstellar_description():
    for widget in Description_Frame2.winfo_children():
        widget.destroy()
    global heading_description,movieruntime,movie_description,movierating,moviecost,moviefilename
    global image24
    global img24
    Login_frame.forget()
    Main_frame.forget()
    Upcoming_frame.forget()
    Current_frame.forget()
    Description_Frame2.pack(fill='both', expand=1)
    heading_description = 'Interstellar'
    movieruntime='Runtime: 2h 28m'
    movie_description = 'Description: A team of explorers travel through a wormhole in space in an \nattempt to ensure humanity survival.'
    movierating= 'Rating: PG-13'
    moviecost ='cost = $15'
    moviefilename = 'interstellarpic.jpg'
    #images for frame
    image24= Image.open(moviefilename)

    image24 = image24.resize((200,250), Image.ANTIALIAS)

    img24= ImageTk.PhotoImage(image24)
    descriptionframe2()
    image24.close()


#function to fill description frame with saving private ryan info
def privateryan_description():
    for widget in Description_Frame2.winfo_children():
        widget.destroy()
    global heading_description,movieruntime,movie_description,movierating,moviecost,moviefilename
    global image24
    global img24
    Login_frame.forget()
    Main_frame.forget()
    Upcoming_frame.forget()
    Current_frame.forget()
    Description_Frame2.pack(fill='both', expand=1)
    heading_description = 'Saving private Ryan'
    movieruntime='Runtime: 2h 49m'
    movie_description = 'Description: Following the Normandy Landings, a group of U.S. soldiers go \nbehind enemy lines to retrieve a paratrooper whose brothers have been killed in \naction.'
    movierating= 'Rating: R'
    moviecost ='cost = $15'
    moviefilename = 'privateryan.jpg'
    #images for frame
    image24= Image.open(moviefilename)

    image24 = image24.resize((200,250), Image.ANTIALIAS)

    img24= ImageTk.PhotoImage(image24)
    descriptionframe2()
    image24.close()


#function to fill description frame with greenmile info
def greenmile_description():
    for widget in Description_Frame2.winfo_children():
        widget.destroy()
    global heading_description,movieruntime,movie_description,movierating,moviecost,moviefilename
    global image24
    global img24
    Login_frame.forget()
    Main_frame.forget()
    Upcoming_frame.forget()
    Current_frame.forget()
    Description_Frame2.pack(fill='both', expand=1)
    heading_description = 'The Green Mile'
    movieruntime='Runtime: 3h 9m'
    movie_description = 'Description: The lives of guards on Death Row are affected by one of their \ncharges: a black man accused of child murder and rape, yet who has a mysterious\n gift.'
    movierating= 'Rating: R'
    moviecost ='cost = $15'
    moviefilename = 'greenmile.jpg'
    #images for frame
    image24= Image.open(moviefilename)

    image24 = image24.resize((200,250), Image.ANTIALIAS)

    img24= ImageTk.PhotoImage(image24)
    descriptionframe2()
    image24.close()

#function to fill description frame with star wars info
def starwars_description():
    for widget in Description_Frame2.winfo_children():
        widget.destroy()
    global heading_description,movieruntime,movie_description,movierating,moviecost,moviefilename
    global image24
    global img24
    Login_frame.forget()
    Main_frame.forget()
    Upcoming_frame.forget()
    Current_frame.forget()
    Description_Frame2.pack(fill='both', expand=1)
    heading_description = 'Star Wars'
    movieruntime='Runtime: 2h 20m'
    movie_description = 'Description: Three years into the Clone Wars, the Jedi rescue Palpatine from \nCount Dooku. As Obi-Wan pursues a new threat, Anakin acts as a double agent \nbetween the Jedi Council and Palpatine and is lured into a sinister plan to \nrule the galaxy.'
    movierating= 'Rating: PG-13'
    moviecost ='cost = $15'
    moviefilename = 'starwars.jpg'
    #images for frame
    image24= Image.open(moviefilename)

    image24 = image24.resize((200,250), Image.ANTIALIAS)

    img24= ImageTk.PhotoImage(image24)
    descriptionframe2()
    image24.close()

#function to fill description frame with star wars info
def johnwick_description():
    for widget in Description_Frame2.winfo_children():
        widget.destroy()
    global heading_description,movieruntime,movie_description,movierating,moviecost,moviefilename
    global image24
    global img24
    Login_frame.forget()
    Main_frame.forget()
    Upcoming_frame.forget()
    Current_frame.forget()
    Description_Frame2.pack(fill='both', expand=1)
    heading_description = 'John Wick'
    movieruntime='Runtime: 1h 41m'
    movie_description = 'Description: An ex-hit-man comes out of retirement to track down the gangsters \nthat killed his dog and took his car.'
    movierating= 'Rating: R'
    moviecost ='cost = $15'
    moviefilename = 'johnwick.jpg'
    #images for frame
    image24= Image.open(moviefilename)

    image24 = image24.resize((200,250), Image.ANTIALIAS)

    img24= ImageTk.PhotoImage(image24)
    descriptionframe2()
    image24.close()




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
Description_Frame = tkinter.Frame(root)
Admin_frame = tkinter.Frame(root)
ManageShows_frame = tkinter.Frame(root)
Description_Frame2 = tkinter.Frame(root)
edit_shows_frame = tkinter.Frame(root)



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
btn_change_to_Main = tkinter.Button(Login_frame,text='Login',font=font_small,command=login_valid,height=2,width=15)
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
btn_change_to_Login = tkinter.Button(Register_frame,text='Back',font=font_small,command=change_to_Login,height=2,width=15)
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
btn_FeaturedMovie_19 = tkinter.Button(Main_frame,image=img19,command= django_description)
btn_FeaturedMovie_20 = tkinter.Button(Main_frame,image=img20,command= sharktale_description)
btn_FeaturedMovie_21 = tkinter.Button(Main_frame,image=img21,command=elf_description)

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
btn_CurrentMovie_1 = tkinter.Button(Current_frame,image=img1,command=diehard_description)
btn_CurrentMovie_2 = tkinter.Button(Current_frame,image=img2,command=rushour_description)
btn_CurrentMovie_3 = tkinter.Button(Current_frame,image=img3,command=elf_description)
btn_CurrentMovie_4 = tkinter.Button(Current_frame,image=img4,command=matrix_description)
btn_CurrentMovie_5 = tkinter.Button(Current_frame,image=img5,command= onepiece_description)
btn_CurrentMovie_6 = tkinter.Button(Current_frame,image=img6,command= fightclub_description)
btn_CurrentMovie_7 = tkinter.Button(Current_frame,image=img7,command = batman_description)
btn_CurrentMovie_8 = tkinter.Button(Current_frame,image=img8,command= django_description)
btn_CurrentMovie_9 = tkinter.Button(Current_frame,image=img9,command = sharktale_description)
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
btn_UpcomingMovie_10 = tkinter.Button(Upcoming_frame,image=img10,command=pirates_description)
btn_UpcomingMovie_11 = tkinter.Button(Upcoming_frame,image=img11,command= lordofrings_description)
btn_UpcomingMovie_12 = tkinter.Button(Upcoming_frame,image=img12,command= inception_description)
btn_UpcomingMovie_13 = tkinter.Button(Upcoming_frame,image=img13,command= avengers_description)
btn_UpcomingMovie_14 = tkinter.Button(Upcoming_frame,image=img14,command= interstellar_description)
btn_UpcomingMovie_15 = tkinter.Button(Upcoming_frame,image=img15,command= privateryan_description)
btn_UpcomingMovie_16 = tkinter.Button(Upcoming_frame,image=img16,command= greenmile_description)
btn_UpcomingMovie_17 = tkinter.Button(Upcoming_frame,image=img17,command= starwars_description)
btn_UpcomingMovie_18 = tkinter.Button(Upcoming_frame,image=img18,command= johnwick_description)
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


#-------------------------Description Frame for current movies---------------------------------------------
def descriptionframe():

    #lables for description
    lbl_heading_Description = tkinter.Label(Description_Frame,text=heading_description,font=font_large)
    lbl_description_Description = tkinter.Label(Description_Frame,text = movie_description)
    lbl_cost_Description = tkinter.Label(Description_Frame,text= moviecost)
    lbl_Runtime_Description = tkinter.Label(Description_Frame,text= movieruntime)
    lbl_Review_Description = tkinter.Label(Description_Frame,text= movierating)
    lbl_image_Description = tkinter.Label(Description_Frame,image=img22)
    btn_change_to_Current = tkinter.Button(Description_Frame,font = font_small,text ="Back",command = change_to_Current)
    #placing labels
    lbl_heading_Description.place(x=90,y=20)
    lbl_image_Description.place(x=120,y=80)
    lbl_description_Description.place(x=10,y=350)
    lbl_cost_Description.place(x=10,y=400)
    lbl_Runtime_Description.place(x=10,y=430)
    lbl_Review_Description.place(x=10,y=460)
    #making buttons 
    btn_change_to_showtime = tkinter.Button(Description_Frame,font = font_small,text ="Book Now",command = change_to_Showtime)

    #placing buttons
    btn_change_to_showtime.place(x=185,y=550)
    btn_change_to_Current.place(x=10,y=10)


#-------------------------Description Frame for upcoming movies---------------------------------------------
def descriptionframe2():
    #lables for description
    lbl_heading_Description2 = tkinter.Label(Description_Frame2,text=heading_description,font=font_large)
    lbl_description_Description2 = tkinter.Label(Description_Frame2,text = movie_description)
    lbl_cost_Description2 = tkinter.Label(Description_Frame2,text= moviecost)
    lbl_Runtime_Description2 = tkinter.Label(Description_Frame2,text= movieruntime)
    lbl_Review_Description2 = tkinter.Label(Description_Frame2,text= movierating)
    lbl_image_Description2 = tkinter.Label(Description_Frame2,image=img24)
    btn_change_to_Upcoming= tkinter.Button(Description_Frame2,font = font_small,text ="Back",command = change_to_Upcoming)
    #placing labels
    lbl_heading_Description2.place(x=90,y=20)
    lbl_image_Description2.place(x=120,y=80)
    lbl_description_Description2.place(x=10,y=350)
    lbl_cost_Description2.place(x=10,y=400)
    lbl_Runtime_Description2.place(x=10,y=430)
    lbl_Review_Description2.place(x=10,y=460)
    

    
    btn_change_to_Upcoming.place(x=10,y=10)




#-------------------------Showtime Frame---------------------------------------------
def showtimeframe():
    global btn_Showing1,btn_Showing2,btn_Showing3,btn_Showing4,btn_Showing5,btn_Showing6,btn_Showing7,btn_Showing8,btn_Showing9,btn_Showing10,btn_Showing11,btn_Showing12,btn_Showing13,btn_Showing14,btn_Showing15,btn_Showing16,btn_Showing17,btn_Showing18,btn_Showing19,btn_Showing20,btn_Showing21
    global color1,color2,color3,color4,color5,color6,color7,color8,color9,color10,color11,color12,color13,color14,color15,color16,color17,color18,color19,color20,color21
    global spin_box1,spin_box2,spin_box3,spin_box4,spin_box5,spin_box6,spin_box7
    global movie_time1, movie_time2, movie_time3


    # Location of the image
    lbl_image_Showtime  = tkinter.Label(Showtime_frame, image = img23)
    lbl_image_Showtime.place(x=240, y=150)

    # Selected movie title
    lbl_heading_Showtime = tkinter.Label(Showtime_frame,text='ShowTimes',font=font_large)
    lbl_heading_Showtime.pack(pady=10)

    # Sunday title and spinbox
    lbl_sunday_Showtime = tkinter.Label(Showtime_frame,text='Sunday',font=font_small)
    lbl_sunday_Showtime.place(x=20, y=60)
    btn_Showing1 = tkinter.Button(Showtime_frame,text =movie_time1,  command=change_Showing1_Color)
    btn_Showing1.place(x=10, y=95)
    btn_Showing2 = tkinter.Button(Showtime_frame,text =movie_time2,  command=change_Showing2_Color)
    btn_Showing2.place(x=90, y=95)
    btn_Showing3 = tkinter.Button(Showtime_frame,text =movie_time3,  command=change_Showing3_Color)
    btn_Showing3.place(x=170, y=95)
    color1 = cycle(['green', 'black', 'green', btn_Showing1['fg']])
    color2 = cycle(['green', 'black', 'green', btn_Showing2['fg']])
    color3 = cycle(['green', 'black', 'green', btn_Showing3['fg']])
    spin_box1 = ttk.Spinbox(Showtime_frame, from_ = 0, to = 10, width=10)
    spin_box1.place(x=110, y=62)

    # Monday title and spinbox
    lbl_monday_Showtime = tkinter.Label(Showtime_frame,text='Monday',font=font_small)
    lbl_monday_Showtime.place(x=20, y=135)
    btn_Showing4 = tkinter.Button(Showtime_frame,text =movie_time4,  command=change_Showing4_Color)
    btn_Showing4.place(x=10, y=170)
    btn_Showing5 = tkinter.Button(Showtime_frame,text =movie_time5,  command=change_Showing5_Color)
    btn_Showing5.place(x=90, y=170)
    btn_Showing6 = tkinter.Button(Showtime_frame,text =movie_time6,  command=change_Showing6_Color)
    btn_Showing6.place(x=170, y=170)
    color4 = cycle(['green', 'black', 'green', btn_Showing4['fg']])
    color5 = cycle(['green', 'black', 'green', btn_Showing5['fg']])
    color6 = cycle(['green', 'black', 'green', btn_Showing6['fg']])
    spin_box2 = ttk.Spinbox(Showtime_frame, from_ = 0, to = 10, width=10)
    spin_box2.place(x=110, y=137)

    # Tuesday title and spinbox
    lbl_tuesday_Showtime = tkinter.Label(Showtime_frame,text='Tuesday',font=font_small)
    lbl_tuesday_Showtime.place(x=20, y=210)
    btn_Showing7 = tkinter.Button(Showtime_frame,text =movie_time7,  command=change_Showing7_Color)
    btn_Showing7.place(x=10, y=245)
    btn_Showing8 = tkinter.Button(Showtime_frame,text =movie_time8,  command=change_Showing8_Color)
    btn_Showing8.place(x=90, y=245)
    btn_Showing9 = tkinter.Button(Showtime_frame,text =movie_time9,  command=change_Showing9_Color)
    btn_Showing9.place(x=170, y=245)
    color7 = cycle(['green', 'black', 'green', btn_Showing7['fg']])
    color8 = cycle(['green', 'black', 'green', btn_Showing8['fg']])
    color9 = cycle(['green', 'black', 'green', btn_Showing9['fg']])
    spin_box3 = ttk.Spinbox(Showtime_frame, from_ = 0, to = 10, width=10)
    spin_box3.place(x=110, y=212)

    # Wednesday title and spinbox
    lbl_wednesday_Showtime = tkinter.Label(Showtime_frame,text='Wednesday',font=font_small)
    lbl_wednesday_Showtime.place(x=20, y=285)
    btn_Showing10 = tkinter.Button(Showtime_frame,text =movie_time10,  command=change_Showing10_Color)
    btn_Showing10.place(x=10, y=320)
    btn_Showing11 = tkinter.Button(Showtime_frame,text =movie_time11,  command=change_Showing11_Color)
    btn_Showing11.place(x=90, y=320)
    btn_Showing12 = tkinter.Button(Showtime_frame,text =movie_time12,  command=change_Showing12_Color)
    btn_Showing12.place(x=170, y=320)
    color10 = cycle(['green', 'black', 'green', btn_Showing10['fg']])
    color11 = cycle(['green', 'black', 'green', btn_Showing11['fg']])
    color12 = cycle(['green', 'black', 'green', btn_Showing12['fg']])
    spin_box4 = ttk.Spinbox(Showtime_frame, from_ = 0, to = 10, width=10)
    spin_box4.place(x=110, y=287)

    # Thursday title and spinbox
    lbl_thursday_Showtime = tkinter.Label(Showtime_frame,text='Thursday',font=font_small)
    lbl_thursday_Showtime.place(x=20, y=360)
    btn_Showing13 = tkinter.Button(Showtime_frame,text =movie_time13,  command=change_Showing13_Color)
    btn_Showing13.place(x=10, y=395)
    btn_Showing14 = tkinter.Button(Showtime_frame,text =movie_time14,  command=change_Showing14_Color)
    btn_Showing14.place(x=90, y=395)
    btn_Showing15 = tkinter.Button(Showtime_frame,text =movie_time15,  command=change_Showing15_Color)
    btn_Showing15.place(x=170, y=395)
    color13 = cycle(['green', 'black', 'green', btn_Showing13['fg']])
    color14 = cycle(['green', 'black', 'green', btn_Showing14['fg']])
    color15 = cycle(['green', 'black', 'green', btn_Showing15['fg']])
    spin_box5 = ttk.Spinbox(Showtime_frame, from_ = 0, to = 10, width=10)
    spin_box5.place(x=110, y=362)

    # Friday title and spinbox
    lbl_friday_Showtime = tkinter.Label(Showtime_frame,text='Friday',font=font_small)
    lbl_friday_Showtime.place(x=20, y=435)
    btn_Showing16 = tkinter.Button(Showtime_frame,text =movie_time16,  command=change_Showing16_Color)
    btn_Showing16.place(x=10, y=470)
    btn_Showing17 = tkinter.Button(Showtime_frame,text =movie_time17,  command=change_Showing17_Color)
    btn_Showing17.place(x=90, y=470)
    btn_Showing18 = tkinter.Button(Showtime_frame,text =movie_time18,  command=change_Showing18_Color)
    btn_Showing18.place(x=170, y=470)
    color16 = cycle(['green', 'black', 'green', btn_Showing16['fg']])
    color17 = cycle(['green', 'black', 'green', btn_Showing17['fg']])
    color18 = cycle(['green', 'black', 'green', btn_Showing18['fg']])
    spin_box6 = ttk.Spinbox(Showtime_frame, from_ = 0, to = 10, width=10)
    spin_box6.place(x=110, y=437)

    # Saturday title and spinbox
    lbl_saturday_Showtime = tkinter.Label(Showtime_frame,text='Saturday',font=font_small)
    lbl_saturday_Showtime.place(x=20, y=510)
    btn_Showing19 = tkinter.Button(Showtime_frame,text =movie_time19,  command=change_Showing19_Color)
    btn_Showing19.place(x=10, y=545)
    btn_Showing20 = tkinter.Button(Showtime_frame,text =movie_time20,  command=change_Showing20_Color)
    btn_Showing20.place(x=90, y=545)
    btn_Showing21 = tkinter.Button(Showtime_frame,text =movie_time21,  command=change_Showing21_Color)
    btn_Showing21.place(x=170, y=545)
    color19 = cycle(['green', 'black', 'green', btn_Showing19['fg']])
    color20 = cycle(['green', 'black', 'green', btn_Showing20['fg']])
    color21 = cycle(['green', 'black', 'green', btn_Showing21['fg']])
    spin_box7 = ttk.Spinbox(Showtime_frame, from_ = 0, to = 10, width=10)
    spin_box7.place(x=110, y=512)

    #making buttons 
    btn_change_to_checkout = tkinter.Button(Showtime_frame,font = font_large,text ="Checkout",width=7,height=2,command = SumTicketsSold)
    btn_change_to_description = tkinter.Button(Showtime_frame,font = font_small,text ="Back",command = change_to_Description)
    btn_change_to_description.place(x=10,y=10)

    #placing buttons
    btn_change_to_checkout.place(x=275,y=480)
#-------------------------Checkout Frame---------------------------------------------
def checkout():
    global TotalCost
    global ent5,ent6,ent7,ent8,ent9,ent10,ent11,ent12
    #making buttons 
    btn_change_to_confirm = tkinter.Button(Checkout_frame,font = font_small,text ="Confirm",command = CheckoutConfirmed)

    lbl_username_Checkout = tkinter.Label(Checkout_frame,text='Checkout', font=font_large)
    lbl_creditcardnumber_Checkout = tkinter.Label(Checkout_frame,text='Credit Card Number:')
    lbl_expirationdate_Checkout = tkinter.Label(Checkout_frame,text='Expiration Date:')
    lbl_cvv_Checkout = tkinter.Label(Checkout_frame,text='CVV:')
    lbl_nameoncard_Checkout = tkinter.Label(Checkout_frame,text='Name on Card:')
    lbl_addressline_Checkout = tkinter.Label(Checkout_frame,text='Address:')
    lbl_city_Checkout = tkinter.Label(Checkout_frame,text='City:')
    lbl_state_Checkout = tkinter.Label(Checkout_frame,text='State:')
    lbl_zipcode_Checkout = tkinter.Label(Checkout_frame,text='ZIP code:')
    lbl_orLine_Checkout = tkinter.Label(Checkout_frame, text='---------------------------or---------------------------')
    btn_paypal_Checkout = tkinter.Button(Checkout_frame,font = font_small,text ="PayPal",command= paypalconfirm)
    lbl_PriceofTickets_Checkout = tkinter.Label(Checkout_frame,text='Your Total is: $',font = font_small)
    lbl_PriceofTickets2_Checkout = tkinter.Label(Checkout_frame,text=TotalCost,font=font_small)

    ent5 = Entry(Checkout_frame)
    ent6 = Entry(Checkout_frame)
    ent7 = Entry(Checkout_frame)
    ent8 = Entry(Checkout_frame)
    ent9 = Entry(Checkout_frame)
    ent10 = Entry(Checkout_frame)
    ent11 = Entry(Checkout_frame)
    ent12 = Entry(Checkout_frame)

    lbl_username_Checkout.pack(padx=150,pady=20)
    lbl_creditcardnumber_Checkout.place(x=70,y=120)
    lbl_expirationdate_Checkout.place(x=70,y=140)
    lbl_cvv_Checkout.place(x=70,y=160)
    lbl_nameoncard_Checkout.place(x=70,y=180)
    lbl_addressline_Checkout.place(x=70,y=200)
    lbl_city_Checkout.place(x=70,y=220)
    lbl_state_Checkout.place(x=70,y=240)
    lbl_zipcode_Checkout.place(x=70,y=260)
    lbl_orLine_Checkout.place(x=70,y=285)
    lbl_PriceofTickets_Checkout.place(x=70,y=400)
    lbl_PriceofTickets2_Checkout.place(x=181,y=400)
    btn_paypal_Checkout.place(x=180,y=310)
    btn_change_to_Showtime = tkinter.Button(Checkout_frame,font = font_small,text ="Back",command = change_to_Showtime)

    ent5.place(x=185,y=120)
    ent6.place(x=160,y=140)
    ent7.place(x=105,y=160)
    ent8.place(x=160,y=180)
    ent9.place(x=125,y=200)
    ent10.place(x=100,y=220)
    ent11.place(x=105,y=240)
    ent12.place(x=125,y=260)
    btn_change_to_Showtime.place(x=10,y=10)

    #placing buttons
    btn_change_to_confirm.place(x=180,y=500)


#-------------------------Admin Frame---------------------------------------------
def admin():
    lbl_adminview_Admin = tkinter.Label(Admin_frame,text='Administration Only', font=font_large)

    btn_kowalski_Admin = tkinter.Button(Admin_frame,font = font_small,text ="Status Report", command = StatusReport)
    btn_manageshow_Admin = tkinter.Button(Admin_frame,text='Manage Movies',font=font_small,command=change_to_ManageShows,height=2,width=15)
    btn_change_to_Login = tkinter.Button(Admin_frame,font=font_small,text='Logout',command=change_to_Login,height=2,width=40)


    lbl_adminview_Admin.place(x=85,y=20)
    btn_kowalski_Admin.place(x=175,y=100)
    btn_manageshow_Admin.place(x=157,y=150)
    btn_change_to_Login.place(x=40,y=530)



#-------------------------Manage Shows Frame---------------------------------------------
def manage_shows():
    #making and placing back button
    btn_change_to_admin = tkinter.Button(ManageShows_frame,font = font_small,text ="Back",command = change_to_Admin)
    btn_change_to_admin.place(x=10,y=10)

    #labels for the manage movies frame
    lbl_heading_manage = tkinter.Label(ManageShows_frame,text='Manage Movies',font=font_large)
    #placing labels into the manage movies frame
    lbl_heading_manage.pack(pady=20)
    #making buttons
    btn_manageMovie_1 = tkinter.Button(ManageShows_frame,image=img25,command=diehard_edit)
    btn_manageMovie_2 = tkinter.Button(ManageShows_frame,image=img26,command=rushhour_edit)
    btn_manageMovie_3 = tkinter.Button(ManageShows_frame,image=img27,command=elf_edit)
    btn_manageMovie_4 = tkinter.Button(ManageShows_frame,image=img28,command=matrix_edit)
    btn_manageMovie_5 = tkinter.Button(ManageShows_frame,image=img29,command=onepiece_edit)
    btn_manageMovie_6 = tkinter.Button(ManageShows_frame,image=img30,command=fightclub_edit)
    btn_manageMovie_7 = tkinter.Button(ManageShows_frame,image=img31,command=batman_edit)
    btn_manageMovie_8 = tkinter.Button(ManageShows_frame,image=img32,command=django_edit)
    btn_manageMovie_9 = tkinter.Button(ManageShows_frame,image=img33,command=SharkTale_edit)

    #placing buttons
    btn_manageMovie_1.place(x=40,y=60)
    btn_manageMovie_2.place(x=180,y=60)
    btn_manageMovie_3.place(x=320,y=60)
    btn_manageMovie_4.place(x=40,y=230)
    btn_manageMovie_5.place(x=180,y=230)
    btn_manageMovie_6.place(x=320,y=230)
    btn_manageMovie_7.place(x=40,y=400)
    btn_manageMovie_8.place(x=180,y=400)
    btn_manageMovie_9.place(x=320,y=400)

#-------------------------edit Shows Frame---------------------------------------------
def edit_show():
    global ent15,ent16,ent17,ent18,ent19,ent20,ent21,ent22,ent23,ent24,ent25,ent26,ent27,ent28,ent29,ent30,ent31,ent32,ent33,ent34,ent35,ent36
    global moviecost
    #making and placing back button
    btn_change_to_Manage_shows = tkinter.Button(edit_shows_frame,font = font_small,text ="Back",command = change_to_ManageShows)
    btn_change_to_Manage_shows.place(x=10,y=10)
    #labels for edit
    lbl_heading_edit = tkinter.Label(edit_shows_frame,text=moviename,font=font_large)
    lbl_cost_edit = tkinter.Label(edit_shows_frame,text= moviecost,font=font_small)
    lbl_cost2_edit = tkinter.Label(edit_shows_frame,text='To change the cost type in the box the new amount',font=font_small)
    lbl_time_edit = tkinter.Label(edit_shows_frame,text='Showtimes:')
    lbl_time_edit2 = tkinter.Label(edit_shows_frame,text='Type in the new time for any showtime or type N/A to remove the time')
    lbl_time_edit3 = tkinter.Label(edit_shows_frame,text='Sunday')
    lbl_time_edit4 = tkinter.Label(edit_shows_frame,text=movie_time1)
    lbl_time_edit5 = tkinter.Label(edit_shows_frame,text=movie_time2)
    lbl_time_edit6 = tkinter.Label(edit_shows_frame,text=movie_time3)
    lbl_time_edit7 = tkinter.Label(edit_shows_frame,text='Monday')
    lbl_time_edit8 = tkinter.Label(edit_shows_frame,text=movie_time4)
    lbl_time_edit9 = tkinter.Label(edit_shows_frame,text=movie_time5)
    lbl_time_edit10 = tkinter.Label(edit_shows_frame,text=movie_time6)
    lbl_time_edit11 = tkinter.Label(edit_shows_frame,text='Tuesday')
    lbl_time_edit12 = tkinter.Label(edit_shows_frame,text=movie_time7)
    lbl_time_edit13 = tkinter.Label(edit_shows_frame,text=movie_time8)
    lbl_time_edit14 = tkinter.Label(edit_shows_frame,text=movie_time9)
    lbl_time_edit15 = tkinter.Label(edit_shows_frame,text='Wednesday')
    lbl_time_edit16 = tkinter.Label(edit_shows_frame,text=movie_time10)
    lbl_time_edit17 = tkinter.Label(edit_shows_frame,text=movie_time11)
    lbl_time_edit18 = tkinter.Label(edit_shows_frame,text=movie_time12)
    lbl_time_edit19 = tkinter.Label(edit_shows_frame,text='Thursday')
    lbl_time_edit20 = tkinter.Label(edit_shows_frame,text=movie_time13)
    lbl_time_edit21 = tkinter.Label(edit_shows_frame,text=movie_time14)
    lbl_time_edit22 = tkinter.Label(edit_shows_frame,text=movie_time15)
    lbl_time_edit23 = tkinter.Label(edit_shows_frame,text='Friday')
    lbl_time_edit24 = tkinter.Label(edit_shows_frame,text=movie_time16)
    lbl_time_edit25 = tkinter.Label(edit_shows_frame,text=movie_time17)
    lbl_time_edit26 = tkinter.Label(edit_shows_frame,text=movie_time18)
    lbl_time_edit27 = tkinter.Label(edit_shows_frame,text='Saturday')
    lbl_time_edit28 = tkinter.Label(edit_shows_frame,text=movie_time19)
    lbl_time_edit29 = tkinter.Label(edit_shows_frame,text=movie_time20)
    lbl_time_edit30 = tkinter.Label(edit_shows_frame,text=movie_time21)
    
    #placing labels into the edit movies frame
    lbl_heading_edit.pack(pady=20)
    lbl_cost_edit.place(x=30,y=70)
    lbl_cost2_edit.place(x=30,y=100)
    lbl_time_edit.place(x=30,y=150)
    lbl_time_edit2.place(x=30,y=170)
    lbl_time_edit3.place(x=30,y=190)
    lbl_time_edit4.place(x=30,y=210)
    lbl_time_edit5.place(x=160,y=210)
    lbl_time_edit6.place(x=290,y=210)

    lbl_time_edit7.place(x=30,y=230)
    lbl_time_edit8.place(x=30,y=250)
    lbl_time_edit9.place(x=160,y=250)
    lbl_time_edit10.place(x=290,y=250)

    lbl_time_edit11.place(x=30,y=270)
    lbl_time_edit12.place(x=30,y=290)
    lbl_time_edit13.place(x=160,y=290)
    lbl_time_edit14.place(x=290,y=290)

    lbl_time_edit15.place(x=30,y=310)
    lbl_time_edit16.place(x=30,y=330)
    lbl_time_edit17.place(x=160,y=330)
    lbl_time_edit18.place(x=290,y=330)

    lbl_time_edit19.place(x=30,y=350)
    lbl_time_edit20.place(x=30,y=370)
    lbl_time_edit21.place(x=160,y=370)
    lbl_time_edit22.place(x=290,y=370)

    lbl_time_edit23.place(x=30,y=390)
    lbl_time_edit24.place(x=30,y=410)
    lbl_time_edit25.place(x=160,y=410)
    lbl_time_edit26.place(x=290,y=410)

    lbl_time_edit27.place(x=30,y=430)
    lbl_time_edit28.place(x=30,y=450)
    lbl_time_edit29.place(x=160,y=450)
    lbl_time_edit30.place(x=290,y=450)
    #making entry box
    ent15 = Entry(edit_shows_frame)
    ent15.place(x=30,y=130)
    ent16= Entry(edit_shows_frame,width=10)
    ent16.place(x=80,y=210)
    ent17 = Entry(edit_shows_frame,width=10)
    ent17.place(x=210,y=210)
    ent18 = Entry(edit_shows_frame,width=10)
    ent18.place(x=340,y=210)

    ent19= Entry(edit_shows_frame,width=10)
    ent19.place(x=80,y=250)
    ent20 = Entry(edit_shows_frame,width=10)
    ent20.place(x=210,y=250)
    ent21 = Entry(edit_shows_frame,width=10)
    ent21.place(x=340,y=250)

    ent22= Entry(edit_shows_frame,width=10)
    ent22.place(x=80,y=290)
    ent23 = Entry(edit_shows_frame,width=10)
    ent23.place(x=210,y=290)
    ent24 = Entry(edit_shows_frame,width=10)
    ent24.place(x=340,y=290)

    ent25= Entry(edit_shows_frame,width=10)
    ent25.place(x=80,y=330)
    ent26 = Entry(edit_shows_frame,width=10)
    ent26.place(x=210,y=330)
    ent27 = Entry(edit_shows_frame,width=10)
    ent27.place(x=340,y=330)

    ent28= Entry(edit_shows_frame,width=10)
    ent28.place(x=80,y=370)
    ent29 = Entry(edit_shows_frame,width=10)
    ent29.place(x=210,y=370)
    ent30 = Entry(edit_shows_frame,width=10)
    ent30.place(x=340,y=370)

    ent31= Entry(edit_shows_frame,width=10)
    ent31.place(x=80,y=410)
    ent32 = Entry(edit_shows_frame,width=10)
    ent32.place(x=210,y=410)
    ent33 = Entry(edit_shows_frame,width=10)
    ent33.place(x=340,y=410)

    ent34= Entry(edit_shows_frame,width=10)
    ent34.place(x=80,y=450)
    ent35 = Entry(edit_shows_frame,width=10)
    ent35.place(x=210,y=450)
    ent36 = Entry(edit_shows_frame,width=10)
    ent36.place(x=340,y=450)
    #making an apply button
    btn_apply_changes = tkinter.Button(edit_shows_frame,font=font_small,text='Apply',height=2,width=40,command=apply_edit)
    btn_apply_changes.place(x=40,y=530)





#running the program starting at the Login Frame
Login_frame.pack(fill='both', expand=1)

root.mainloop()




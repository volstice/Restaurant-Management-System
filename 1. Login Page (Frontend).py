
from tkinter import*
import tkinter.messagebox

b= Tk()
b.title('Restaurant Management System')
b.geometry('1350x750+0+0')
b.config(bg='grey') 

uname = StringVar()
paswd= StringVar()

#=========================================================Frames==================================================
mainframe=  Frame(b, bg = 'grey')
mainframe.grid()

b.txtno=Label(mainframe,text= '###:', font= ('Calibri', 12,  'bold'), padx= 2, pady= 2, bg= 'grey', foreground='grey')
b.txtno.grid(row=0, column=0)

b.txtno5=Label(mainframe,text= '###:', font= ('Calibri', 10,  'bold'), padx= 2, pady= 2, bg= 'grey', foreground='grey')
b.txtno5.grid(row=7, column=0)

b.txtno3=Label(mainframe,text= '###:', font= ('Calibri', 10,  'bold'), padx= 2, pady= 2, bg= 'grey', foreground='grey')
b.txtno3.grid(row=11, column=0)

titframe = Frame(mainframe, bd= 2, padx=120, pady= 8, bg= 'Ghost White', relief= RIDGE)
titframe.grid(row=1,column=0)
b.txtno=Label(mainframe,text= 'Username:', font= ('Calibri', 30,  'bold'), padx= 2, pady= 2, bg= 'grey', foreground='grey')
b.txtno.grid(row=4, column=0)

b.lbltit= Label (titframe, font= ('Century Schoolbook', 47,  'bold'), text= 'Restaurant Management System                  ', bg= 'Ghost white')
b.lbltit.grid(row=0, column=0)

dataframe = Frame(mainframe, bd= 1, width= 1300, height= 200, padx= 455,pady= 20, bg= 'ghost white', relief= RIDGE)
dataframe.grid(row=6, column=0)

staffframe = Frame(mainframe, bd= 1, width= 1300, height= 200, padx= 455,pady= 20, bg= 'ghost white', relief= RIDGE)
staffframe.grid(row=10, column=0)

exframe=Frame(mainframe, bd= 1, width= 1300, height= 200, padx= 718,pady= 20, bg= 'ghost white', relief= RIDGE)
exframe.grid(row=12, column=0)

#===========================================================Exit Button=========================================================================
def qexit():
        qexit=tkinter.messagebox.askyesno('Exit Restaurant System', 'Confirm to exit')
        if qexit>0:
            b.destroy()
            return
        
b.exbtn = Button (exframe, text= 'Exit',  font=('arial', 20, 'bold'), width= 11, height= 1, bd=4, command= qexit)
b.exbtn.grid(row=4, column=1)

#===========================================================Login Page==========================================================================

def adminpage():
    import tkinter.messagebox
    a= Toplevel()
    a.title('Admin Menu Editor')
    a.geometry('1350x750+0+0')
    a.config(bg='grey') 

    itmname = StringVar()
    itmcst= StringVar()
    sgst = StringVar()
    cgst= StringVar()
    itmid = StringVar()
    #=========================================================Frames==================================================
    mainframe=  Frame(a, bg = 'grey')
    mainframe.grid()

    titframe = Frame(mainframe, bd= 10, padx= 54, pady= 8, bg= 'Ghost White', relief= RIDGE)
    titframe.grid(row=1,column=0)

    a.txtno=Label(mainframe,text= '###:', font= ('Calibri', 1,  'bold'), padx= 2, pady= 2, bg= 'grey', foreground='grey')
    a.txtno.grid(row=0, column=0)

    a.txtno3=Label(mainframe,text= '###:', font= ('Calibri', 18,  'bold'), padx= 2, pady= 2, bg= 'grey', foreground='grey')
    a.txtno3.grid(row=2, column=0)

    a.txtno2=Label(mainframe,text= '###:', font= ('Calibri', 18,  'bold'), padx= 2, pady= 2, bg= 'grey', foreground='grey')
    a.txtno2.grid(row=4, column=0)

    a.lbltit= Label (titframe, font= ('Century Schoolbook', 47,  'bold'), text= 'Admin Menu Editor', bg= 'Ghost white')
    a.lbltit.grid()

    buttonframe = Frame(mainframe, bd= 10, width= 1350, height= 70,padx= 22, pady= 10, bg= 'Ghost White', relief= RIDGE)
    buttonframe.grid(row=6,column=0)

    dataframe = Frame(mainframe, bd= 10, width= 1300, height= 400, padx= 20,pady= 20, bg= 'Grey', relief= RIDGE)
    dataframe.grid(row=3,column=0)

    dataframeleft = LabelFrame(dataframe, bd= 7, width= 1000, height= 600, padx= 20, bg= 'Ghost White', relief= RIDGE,
                               font= ('Century Schoolbook', 20,  'bold'), text = 'Menu Information\n')
    dataframeleft.pack(side=LEFT)

    dataframeright = LabelFrame(dataframe, bd= 7, width= 450, height= 300, padx= 31, pady=3, bg= 'Ghost White', relief= RIDGE,
                                 font= ('Century Schoolbook', 20,  'bold'), text= 'Menu Details' )
    dataframeright.pack(side=RIGHT)
    #========================================================Function=============================================
    def Clear():
            a.txtid.delete(0,'end')
            a.txtname.delete(0,END)
            a.txtcost.delete(0,END)
            a.txtsgst.delete(0,END)
            a.txtcgst.delete(0,END)
            viewlist.delete('0',END)

            a.txtname.configure(state= DISABLED)
            a.txtcost.configure(state= DISABLED)
            a.txtsgst.configure(state= DISABLED)
            a.txtcgst.configure(state= DISABLED)

            v1.set('0')
            v2.set('0')
            v3.set('0')

            a.txtid.focus()
    def view():
            viewlist.delete('0',END)
            import mysql.connector as c
            chk=0
            con=c.connect(host="localhost",user="root",passwd="sandy",database="billservice")
            cursor=con.cursor()  
            cursor.execute( "select * from data")
            row=cursor.fetchall()
        
            a=row[0][0]
            b=row[1][0]
            xx=row[2][0]
            d=row[3][0]
            e=row[4][0]
            f=row[5][0]
            g=row[6][0]
            h=row[7][0]
            i=row[8][0]
            j=row[9][0]
            k=row[10][0]
            l=row[11][0]
            m=row[12][0]
            n=row[13][0]
            o=row[14][0]
            p=row[15][0]
            F=str(row[0][1])
            q=str(row[1][1])
            r=str(row[2][1])
            s=str(row[3][1])
            t=str(row[4][1])
            u=str(row[5][1])
            v=str(row[6][1])
            w=str(row[7][1])
            x=str(row[8][1])
            y=str(row[9][1])
            z=str(row[10][1])
            A=str(row[11][1])
            B=str(row[12][1])
            C=str(row[13][1])
            D=str(row[14][1])
            E=str(row[15][1])
            G=str(row[0][2])
            H=str(row[1][2])
            I=str(row[2][2])
            J=str(row[3][2])
            K=str(row[4][2])
            L=str(row[5][2])
            M=str(row[6][2])
            N=str(row[7][2])
            O=str(row[8][2])
            P=str(row[9][2])
            R=str(row[10][2])
            S=str(row[12][2])
            T=str(row[12][2])
            U=str(row[13][2])
            V=str(row[14][2])
            W=str(row[15][2])

            import mysql.connector as c
            chk=0
            con=c.connect(host="localhost",user="root",passwd="sandy",database="billservice")
            cursor=con.cursor()  
            cursor.execute( "select * from gst")
            row=cursor.fetchall()
            oo=str(row[0][0])

            viewlist.insert (END,'    ' + 'Id    '+' ' +'Items                          \t\t\t\t' + 'Cost \n'+'       '+'GST')
            viewlist.insert (END,'    ' + '\n')
            viewlist.insert (END, '    ' +G+'       '+a +':                             '  + F +'       '+oo+'\n')
            viewlist.insert (END,'    ' + H+'       '+b   +':                              '  + q +'       '+oo+'\n')
            viewlist.insert (END, '    ' +I+'       '+xx  +':                        '   + r +'       '+oo+ '\n')
            viewlist.insert (END, '    ' +J+'       '+d +':                           '    + s +'        '+oo+'\n')
            viewlist.insert (END, '    ' +K+'       '+e +':                       '   + t +'        '+oo+'\n')
            viewlist.insert (END, '    ' +L+'       '+f   +':                  '  + u +'        '+oo+'\n')
            viewlist.insert (END, '    ' +M+'       '+g+':                      '     + v +'        '+oo+'\n')
            viewlist.insert (END, '    ' +N+'       '+h   +':                    '  + w +'       '+oo+'\n')
            viewlist.insert (END, '    ' +O+'       '+i +':      '   + x +'       '+oo+'\n')
            viewlist.insert (END, '    ' +P+'     '+j  +':             '   +y +'       '+oo+'\n')
            viewlist.insert (END, '    ' +R+'     '+k +':            '    +z +'       '+oo+'\n')
            viewlist.insert (END, '    ' +S+'     '+l  +':              '   + A +'       '+oo+'\n')
            viewlist.insert (END, '    ' +T+'     '+m  +'             '   + B +'       '+oo+'\n')
            viewlist.insert (END, '    ' +U+'     '+n  +':                       '   + C +'       '+oo+'\n')
            viewlist.insert (END, '    ' +V+'     '+o  +':                '   + D +'         '+oo+'\n')
            viewlist.insert (END, '    ' +W+'     '+p +':                 '    + E +'         '+oo+'\n')

    def update1():
            import mysql.connector as c
            con=c.connect(host="localhost",user="root",passwd="sandy",database="billservice")
            cursor=con.cursor()  
            cursor.execute("update data set Item='{}' where Id={}".format(a.txtname.get(),a.txtid.get()))
            con.commit()
    def update2():
            import mysql.connector as c
            con=c.connect(host="localhost",user="root",passwd="sandy",database="billservice")
            cursor=con.cursor()  
            cursor.execute("update data set Cost='{}' where Id='{}'".format(a.txtcost.get(),a.txtid.get()))
            con.commit()
    def update5():
            import mysql.connector as c
            con=c.connect(host="localhost",user="root",passwd="sandy",database="billservice")
            cursor=con.cursor()       
            cursor.execute( "update gst set tax={} ".format(a.txtsgst.get()))
            con.commit()
            
    def update3():
           if a.txtname.get()!='':
                   update1()
           if a.txtcost.get()!='':
                   update2()
           if a.txtsgst.get()!='':
                   update5()
           
    def update4():
            if a.txtid.get()=='':
                    q=tkinter.messagebox.askyesno('Enter Id number', 'PLEASE ENTER ID NUMBER')
                    if q>0:
                        a.txtid.focus()
                        return
                    else:
                            cexit=tkinter.messagebox.askyesno('Exit Admin Etitor', 'CONFIRM IF YOU WANT TO EXIT')
                            if cexit>0:
                                    a.destroy()
                                    return
                            else:
                                    a.txtid.focus()
    def update():
            update4()
            update3()
            
            Clear()
            view()
            
    def sale():
            import tkinter.messagebox
            s=Toplevel()
            s.title('Sales Viewer')
            s.geometry('419x300+100+200')
            s.config(bg='grey') 


            
            
    #===============================================================Checkbutton Var================================================
    v1=IntVar()
    v2=IntVar()
    v3=IntVar()
     #=========================================================CheckButton Functions==================================================
    def itmnm():
        if (v1.get() == 1):
            a.txtname.configure(state = NORMAL)
            a.txtname.focus()
            a.txtname.delete('0',END)
            itmname.set('')
        elif (v1.get() == 0):
            a.txtname.configure(state=DISABLED)
            itmname.set('')

    def itmct():
        if (v2.get() == 1):
            a.txtcost.configure(state = NORMAL)
            a.txtcost.focus()
            a.txtcost.delete('0',END)
            itmcst.set('')
        elif (v2.get() == 0):
            a.txtcost.configure(state=DISABLED)
            itmcst.set('')

    def itmgst():
        if (v3.get() == 1):
            if a.txtid.get()=='':
                    itmid.set('%')
            a.txtcgst.configure(state = NORMAL)
            a.txtsgst.configure(state = NORMAL)
            a.txtsgst.focus()
            a.txtcgst.delete('0',END)
            a.txtsgst.delete('0',END)
            sgst.set('')
        elif (v3.get() == 0):
            if a.txtid.get()=='%':
                    itmid.set('')
            a.txtcgst.configure(state=DISABLED)
            a.txtsgst.configure(state=DISABLED)
            sgst.set('')

    #=========================================================Label and Entry Widget==================================================
    a.lblid= Label(dataframeleft, font= ('Century Schoolbook', 20,  'bold'), text= 'ID No:             ', padx= 2, pady= 2, bg= 'Ghost white', bd= 5, relief= RIDGE)
    a.lblid.grid(row=0, column= 0, sticky=W)
    a.txtid= Entry (dataframeleft, font= ('Calibri', 20,  'bold'), textvariable= itmid,width= 39, bd= 5, relief= RIDGE)
    a.txtid.grid(row=0, column= 1)

    a.lblname= Checkbutton (dataframeleft, variable=v1, font= ('Century Schoolbook', 20,  'bold'), text= 'Item Name:', padx= 2, pady= 2, bg= 'Ghost white', bd= 5, relief= RIDGE, command= itmnm)
    a.lblname.grid(row=1, column= 0, sticky=W)
    a.txtname= Entry (dataframeleft, font= ('Calibri', 20,  'bold'), textvariable= itmname,width= 39, bd= 5, relief= RIDGE, state=DISABLED)
    a.txtname.grid(row=1, column= 1)

    a.lblcost= Checkbutton (dataframeleft, variable=v2, font= ('Century Schoolbook', 20,  'bold'), text= 'Item Cost:  ', padx= 2, pady= 2, bg= 'Ghost white', bd= 5, relief= RIDGE, command=itmct)
    a.lblcost.grid(row=2, column= 0, sticky=W)
    a.txtcost= Entry (dataframeleft, font= ('Calibri', 20,  'bold'), textvariable= itmcst,width= 39, bd= 5, relief= RIDGE, state=DISABLED)
    a.txtcost.grid(row=2, column= 1)

    a.lblsgst= Checkbutton (dataframeleft, variable=v3, font= ('Century Schoolbook', 20,  'bold'), text= 'Item SGST:', padx= 2, pady= 2, bg= 'Ghost white', bd= 5, relief= RIDGE, command=itmgst)
    a.lblsgst.grid(row=3, column= 0, sticky=W)
    a.txtsgst= Entry (dataframeleft, font= ('Calibri', 20,  'bold'), textvariable= sgst,width= 39, bd= 5, relief= RIDGE, state=DISABLED)
    a.txtsgst.grid(row=3, column= 1)

    a.lblcgst= Checkbutton (dataframeleft, variable=v3, font= ('Century Schoolbook', 20,  'bold'), text= 'Item CGST:', padx= 2, pady= 2, bg= 'Ghost white', bd= 5, relief= RIDGE, command=itmgst)
    a.lblcgst.grid(row=4, column= 0, sticky=W)
    a.txtcgst= Entry (dataframeleft, font= ('Calibri', 20,  'bold'), textvariable= sgst,width= 39, bd= 5, relief= RIDGE, state=DISABLED)
    a.txtcgst.grid(row=4, column= 1)

    a.txtid.focus()
    #=========================================================ListBox and ScrollbarWidget==================================================

    scrollbar= Scrollbar(dataframeright)
    scrollbar.grid(row=0, column=1, sticky= NS)

    viewlist = Listbox(dataframeright, width= 41, height= 16, font=('century schoolbook', 12, 'bold'), yscrollcommand= scrollbar.set)
    viewlist.grid(row=0, column=0, padx=8)
    scrollbar.config(command= viewlist.yview)
    #=========================================================Exit========================================================
    def mexit():
        qexit=tkinter.messagebox.askyesno('Logout Restaurant System', 'Confirm to Logout')
        if qexit>0:
            a.destroy()
            return
        else:
            a.txtname.focus()
    #=========================================================Menu Button func==================================================
    def Menu():
            menu=tkinter.messagebox.askyesno('Logout Restaurant System', 'Confirm to Logout')
            if menu>0:
                a.destroy()
                window()
                return
            else:
                a.txtname.focus()
    #=========================================================Button Widget==================================================
    
   
    a.btndisplaydata = Button (buttonframe, text= 'Display', font=('arial', 20, 'bold'), width= 11, height= 1, bd=4,comman=view)
    a.btndisplaydata.grid(row=0, column=1)

    a.btncleardata = Button (buttonframe, text= 'Clear', font=('arial', 20, 'bold'), width= 12, height= 1, bd=4, command=Clear)
    a.btncleardata.grid(row=0, column=2)


    a.btnupdatedata = Button (buttonframe, text= 'Update', font=('arial', 20, 'bold'), width= 12, height= 1, bd=4,command=update )
    a.btnupdatedata.grid(row=0, column=5)

    a.btnexit = Button (buttonframe, text= 'Logout', font=('arial', 20, 'bold'),width= 12, height= 1, bd=4, command= mexit)
    a.btnexit.grid(row=0, column=6)

    a.btnmenu = Button (buttonframe, text= 'Menu', font=('arial', 20, 'bold'),width= 12, height= 1, bd=4, command= Menu)
    a.btnmenu.grid(row=0, column=8)

    a.btnsale=Button (buttonframe, text= 'Sales', font=('arial', 20, 'bold'),width= 12, height= 1, bd=4, command=sale)
    a.btnsale.grid(row=0, column=7)
    a.mainloop()

#============================================================Login Credentials===================================================================
def credentials():
    import mysql.connector as c
    chk=0
    con=c.connect(host="localhost",user="root",passwd="sandy",database="billservice")

    d=uname.get()
    c=paswd.get()

    cursor=con.cursor()  
    cursor.execute( "select * from users")
    row=cursor.fetchall()
    for i in row:
        if i[0]==d and i[1]==c:
            chk=1
            break
    if chk==1:
        uname.set('')
        paswd.set('')
        b.txtuname.focus()
        adminpage()
        

    else:
        q=tkinter.messagebox.askyesno('Login Error','Please check the Login details')
        uname.set('')
        paswd.set('')
           
        if  q>0:
            b.txtuname.focus()
        else:
            p=tkinter.messagebox.askyesno('Exit','Do you want to Quit?')
            if p>0:
                b.destroy()
                return
            else:
                b.txtuname.focus()
    con.close
#=========================================================Label and Entry and Button Widget (Admin)==================================================
b.lbltit= Label (dataframe, font= ('Century Schoolbook', 25,  'bold'), text= 'Admin Login:', padx= 2, pady= 2, bg= 'Ghost white')
b.lbltit.grid(row=0, column= 0, sticky=W)

b.lbluname= Label (dataframe, font= ('Century Schoolbook', 20,  'bold'), text= '    Username:', padx= 2, pady= 2, bg= 'Ghost white')
b.lbluname.grid(row=2, column= 0, sticky=W)
b.txtuname= Entry (dataframe, font= ('Calibri', 20,  'bold'), textvariable= uname,width= 20)
b.txtuname.grid(row=2, column= 2)

b.lblpaswd= Label (dataframe, font= ('Century Schoolbook', 20,  'bold'), text= '    Password:', padx= 2, pady= 2, bg= 'Ghost white')
b.lblpaswd.grid(row=3, column= 0, sticky=W)
b.txtpaswd= Entry (dataframe, font= ('Calibri', 20,  'bold'), textvariable= paswd,width= 20, show='*')
b.txtpaswd.grid(row=3, column= 2)

b.btnlogin = Button (dataframe, text= 'Login',  font=('arial', 20, 'bold'), width= 11, height= 1, bd=4, command=credentials )
b.btnlogin.grid(row=4, column=1)

#=========================================================Toplevel(Billing)======================================================
def window():
    import random
    import time
    import datetime
    import tkinter.messagebox
    root=Toplevel()
    root.geometry ('1350x750+0+0')
    root.title('Restaurent Billing System')
    root.configure (background= 'Cadet Blue')
    #======================================Frames==================================
    #----------------------------------------------------------------Tops-----------------------------------------------------------------------
    Tops = Frame(root, bg='Green', bd=20, pady=5, relief= RIDGE)
    Tops.pack(side=TOP)
    lbltitle = Label(Tops, font= ('Century Schoolbook', 60, 'bold'), text= 'Restaurant Billing System', bd=21, bg='Light Green',
                     fg='brown', justify= CENTER)
    lbltitle.grid(row=0, column=0)
    RecieptCal = Frame(root, bg='Green', bd=10, relief= RIDGE)
    RecieptCal.pack(side=RIGHT)
    Buttons_F= Frame(RecieptCal, bg='Green', bd=7, relief= RIDGE)
    Buttons_F.pack(side=BOTTOM)
    Cal_F= Frame(RecieptCal, bg='Green', bd=7, relief= RIDGE)
    Cal_F.pack(side=TOP)
    Reciept_F = Frame(RecieptCal, bg='Green', bd=7, relief= RIDGE)
    Reciept_F.pack(side=BOTTOM)

    #----------------------------------------------------------------Menu Frame-------------------------------------------------------------------

    MenuFrame = Frame(root, bg='green', bd=10, relief= RIDGE)
    MenuFrame.pack(side=LEFT)
    Drinks_F = Frame(MenuFrame, bg='Powder Blue', bd=10)
    Drinks_F.pack(side=TOP)
    Cost_F = Frame(MenuFrame, bg='Powder Blue', bd=10, relief= RIDGE)
    Cost_F.pack(side=BOTTOM)

    Drinks_F = Frame(MenuFrame, bg='Powder Blue', bd=10, relief= RIDGE)
    Drinks_F.pack(side=LEFT)
    Cake_F = Frame(MenuFrame, bg='Powder Blue', bd=10, relief= RIDGE)
    Cake_F.pack(side=LEFT)
    #=======================================Menu=======================================
    #----------------------------------------------------------------------------------Variables-----------------------------------------------------------------
    var1= IntVar()
    var2= IntVar()
    var3= IntVar()
    var4= IntVar()
    var5= IntVar()
    var6= IntVar()
    var7= IntVar()
    var8= IntVar()
    var9= IntVar()
    var10= IntVar()
    var11= IntVar()
    var12= IntVar()
    var13= IntVar()
    var14= IntVar()
    var15= IntVar()
    var16= IntVar()

    dateoforder= StringVar()
    receipt_ref= StringVar()
    paidtax= StringVar()
    subtotal= StringVar()
    totalcost= StringVar()
    costofdrinks= StringVar()
    costofmeals= StringVar()
    servicecharges= StringVar()

    text_input= StringVar()
    paid=StringVar()
    change=StringVar()
    global operator
    operator=''
    e_latta= StringVar()
    e_coke= StringVar()
    e_iced_tea= StringVar()
    e_mojito= StringVar()
    e_espresso= StringVar()
    e_cappucino= StringVar()
    e_iced_latta= StringVar()
    e_lemonade= StringVar()

    e_chicken_sandwich= StringVar()
    e_chicken_wings= StringVar()
    e_smoky_bucket= StringVar()
    e_cheese_burger= StringVar()
    e_chicken_burger= StringVar()
    e_periperi= StringVar()
    e_veg_periperi= StringVar()
    e_fries= StringVar()

    e_latta.set('0')
    e_coke.set('0')
    e_iced_tea.set('0')
    e_mojito.set('0')
    e_espresso.set('0')
    e_cappucino.set('0')
    e_iced_latta.set('0')
    e_lemonade.set('0')

    e_chicken_sandwich.set('0')
    e_chicken_wings.set('0')
    e_smoky_bucket.set('0')
    e_cheese_burger.set('0')
    e_chicken_burger.set('0')
    e_periperi.set('0')
    e_veg_periperi.set('0')
    e_fries.set('0')

    dateoforder.set(time.strftime('%d/%m/%y'))

    def costofitem():
        
        item1=float( e_latta.get())
        item2=float(e_coke.get())
        item3=float(e_iced_tea.get())
        item4=float(e_mojito.get())
        item5=float(e_espresso.get())
        item6=float(e_cappucino.get())
        item7=float(e_iced_latta.get())
        item8=float(e_lemonade.get())
        
        item9=float(e_chicken_sandwich.get())
        item10=float(e_chicken_wings.get())
        item11=float(e_smoky_bucket.get())
        item12=float(e_cheese_burger.get())
        item13=float(e_chicken_burger.get())
        item14=float(e_periperi.get())
        item15=float(e_veg_periperi.get())
        item16=float(e_fries.get())
              
        import mysql.connector as c
        con=c.connect(host="localhost",user="root",passwd="sandy",database="billservice")
        cursor=con.cursor()       
        cursor.execute( "select * from data")
        row=cursor.fetchall()
        a=row[0][0]
        b=row[1][0]
        c=row[2][0]
        d=row[3][0]
        e=row[4][0]
        f=row[5][0]
        g=row[6][0]
        h=row[7][0]
        i=row[8][0]
        j=row[9][0]
        k=row[10][0]
        l=row[11][0]
        m=row[12][0]
        n=row[13][0]
        o=row[14][0]
        p=row[15][0]
        F=row[0][1]
        q=row[1][1]
        r=row[2][1]
        s=row[3][1]
        t=row[4][1]
        u=row[5][1]
        v=row[6][1]
        w=row[7][1]
        x=row[8][1]
        y=row[9][1]
        z=row[10][1]
        A=row[11][1]
        B=row[12][1]
        C=row[13][1]
        D=row[14][1]
        E=row[15][1]

   
        priceofdrinks=(item1*F)+(item2*q)+(item3* r)+(item4 *s)+(item5 *t)+(item6 *u)+(item7 *v)+(item8 *w)
        
        priceofmeals=(item9 * x)+(item10 * y)+(item11 * z)+(item12 * A)+(item13 * B)+(item14 * C)+(item15 * D)+(item16 * E)
                
        drinksprice = 'Rs', str('%.2f'%(priceofdrinks))
        mealsprice = 'Rs', str('%.2f'%(priceofmeals))
        costofdrinks.set(drinksprice)
        costofmeals.set(mealsprice)
        
        
        if (txtlatta.configure(state= DISABLED)or txtcoke.configure(state= DISABLED) or txticed_tea.configure(state= DISABLED) or txtmojito.configure(state= DISABLED) or txtespresso.configure(state= DISABLED) or txtcappucino.configure(state= DISABLED) or 
            txticed_latta.configure(state= DISABLED) or txtlemonade.configure(state= DISABLED) or txtsandwich.configure(state= DISABLED) or txtwings.configure(state= DISABLED) or txtsmoky.configure(state= DISABLED) or txtcheeseb.configure(state= DISABLED) or
            txtchickenb.configure(state= DISABLED) or txtperi.configure(state= DISABLED) or txtvegperi.configure(state= DISABLED) or txtfries.configure(state= DISABLED)):
                sc=str('%.2f'%(0))
                SC='Rs', str('%.2f'%(0))
                servicecharges.set(SC)
                h=str(SC[1])
                H=str(sc[1])
                sbt=str('%.2f'%(priceofdrinks + priceofmeals + float(H)))
                subtotalofitems = 'Rs', str('%.2f'%(priceofdrinks + priceofmeals + float(h)))
                subtotal.set(subtotalofitems)

                import mysql.connector as c
                con=c.connect(host="localhost",user="root",passwd="sandy",database="billservice")
                cursor=con.cursor()       
                cursor.execute( "select * from gst")
                row=cursor.fetchall()
                a=row[0][0]
                Tax=str('%.2f'%((priceofdrinks + priceofmeals + float(H))*a))
                tax = 'Rs', str('%.2f'%((priceofdrinks + priceofmeals + float(h))*a))
                paidtax.set(tax)
                tt = ((priceofdrinks + priceofmeals + float(h))*a)
                TT = ((priceofdrinks + priceofmeals + float(H))*a)
                tc= 'Rs', str('%.2f'%(priceofdrinks + priceofmeals +float(h)+tt))
                TC=str('%.2f'%(priceofdrinks + priceofmeals +float(h)+TT))
                totalcost.set(tc)
                txttotal.delete('0',END)
                txttotal.insert(END,TC)

        else:
                
                sc=str('%.2f'%(10))
                SC = 'Rs', str('%.2f'%(10))
                servicecharges.set(SC)
                h=str(SC[1])
                H=str(sc[1])
                subtotalofitems = 'Rs', str('%.2f'%(priceofdrinks + priceofmeals + float(h)))
                sbt=str('%.2f'%(priceofdrinks + priceofmeals + float(H)))
                subtotal.set(subtotalofitems)

                import mysql.connector as c
                con=c.connect(host="localhost",user="root",passwd="sandy",database="billservice")
                cursor=con.cursor()       
                cursor.execute( "select * from gst")
                row=cursor.fetchall()
                a=row[0][0]
                Tax=str('%.2f'%((priceofdrinks + priceofmeals + float(H))*a))
                tax = 'Rs', str('%.2f'%((priceofdrinks + priceofmeals + float(h))*a))
                paidtax.set(tax)
                tt = ((priceofdrinks + priceofmeals + float(h))*a)
                TT = ((priceofdrinks + priceofmeals + float(H))*a)
                tc= 'Rs', str('%.2f'%(priceofdrinks + priceofmeals +float(h)+tt))
                TC=str('%.2f'%(priceofdrinks + priceofmeals +float(h)+TT))
                totalcost.set(tc)
                txttotal.delete('0',END)


                txttotal.insert(END,TC)
                

    def Receipt():
        import mysql.connector as c
        con=c.connect(host="localhost",user="root",passwd="sandy",database="billservice")
        cursor=con.cursor()       
        cursor.execute( "select * from data")
        row=cursor.fetchall()
        F=str(row[0][1])
        q=str(row[1][1])
        r=str(row[2][1])
        s=str(row[3][1])
        t=str(row[4][1])
        u=str(row[5][1])
        v=str(row[6][1])
        w=str(row[7][1])
        xx=str(row[8][1])
        y=str(row[9][1])
        z=str(row[10][1])
        A=str(row[11][1])
        B=str(row[12][1])
        C=str(row[13][1])
        D=str(row[14][1])
        E=str(row[15][1])
        
        txtReceipt.delete('1.0', END)
        x= random.randint(10980,125560)
        randomref=str(x)
        receipt_ref.set('BILL NO:' + randomref)
        
        txtReceipt.insert (END, 'Receipt Ref:\t\t'+ receipt_ref.get()+'\t' +dateoforder.get()+'\n')
        txtReceipt.insert (END, 'Items\t\t' + 'Cost of Items\t'+'\tNo of Items'+'\n')
        if var1.get()==1:
                txtReceipt.insert (END, 'Latta:\t\t\t' + F +'\t\t' + e_latta.get()+'\n')
        if var2.get()==1:
                txtReceipt.insert (END, 'Coke:\t\t\t' + q +'\t\t'+ e_coke.get() +'\n')
        if   var3.get()==1:
                txtReceipt.insert (END, 'Iced Tea:\t\t\t' + r +'\t\t'+ e_iced_tea.get() +'\n')
        if  var4.get()==1:
                txtReceipt.insert (END, 'Mojito:\t\t\t' + s +'\t\t'+e_mojito.get() +'\n')
        if  var5.get()==1:
                txtReceipt.insert (END, 'Espresso:\t\t\t' + t +'\t\t' + e_espresso.get() +'\n')
        if  var6.get()==1:
                txtReceipt.insert (END, 'Cappucino:\t\t\t' + u +'\t\t'+ e_cappucino.get() +'\n')
        if var7.get()==1:
                txtReceipt.insert (END, 'Iced Latta:\t\t\t' + v +'\t\t'+ e_iced_latta.get() +'\n')
        if var8.get()==1:
                txtReceipt.insert (END, 'Lemonade:\t\t\t' + w +'\t\t' + e_lemonade.get() +'\n')
        if var9.get()==1:
                txtReceipt.insert (END, 'Chicken Sandwich:\t\t\t' + xx +'\t\t'+ e_chicken_sandwich.get() +'\n')
        if var10.get()==1:
                txtReceipt.insert (END, 'Chicken Wings:\t\t\t' +y +'\t\t'+ e_chicken_wings.get() +'\n')
        if var11.get()==1:
                txtReceipt.insert (END, 'Smoky Bucket:\t\t\t' +z +'\t\t' +e_smoky_bucket.get() +'\n')
        if var12.get()==1:
                txtReceipt.insert (END, 'Cheese Burger:\t\t\t' + A +'\t\t'+ e_cheese_burger.get() +'\n')
        if var13.get()==1:
                txtReceipt.insert (END, 'Chicken Burger:\t\t\t' + B +'\t\t' + e_chicken_burger.get() +'\n')
        if var14.get()==1:
                txtReceipt.insert (END, 'Peri Peri:\t\t\t' + C +'\t\t' + e_periperi.get() +'\n')
        if var15.get()==1:
                txtReceipt.insert (END, 'Veg Peri Peri:\t\t\t' + D +'\t\t' + e_veg_periperi.get() +'\n')
        if var16.get()==1:
                txtReceipt.insert (END, 'French Fries:\t\t\t' + E +'\t\t'+ e_fries.get() +'\n')
        txtReceipt.insert (END, '\t\tHave a Great Meal' +'\n')
        txtReceipt.insert (END, '\t\tThank You for Visiting Us' +'\n')
        
      
        

            
    def chklatta():
        if (var1.get() == 1):
            txtlatta.configure(state = NORMAL)
            txtlatta.focus()
            txtlatta.delete('0',END)
            e_latta.set('')
        elif (var1.get() == 0):
            txtlatta.configure(state=DISABLED)
            e_latta.set('0')

    def chkcoke():
        if (var2.get() == 1):
            txtcoke.configure(state = NORMAL)
            txtcoke.focus()
            txtcoke.delete('0',END)
            e_coke.set('')
        elif (var2.get() == 0):
            txtcoke.configure(state=DISABLED)
            e_coke.set('0')

    def chkicetea():
        if (var3.get() == 1):
            txticed_tea.configure(state = NORMAL)
            txticed_tea.focus()
            txticed_tea.delete('0',END)
            e_iced_tea.set('')
        elif (var3.get() == 0):
            txticed_tea.configure(state=DISABLED)
            e_iced_tea.set('0')

    def chkmojito():
        if (var4.get() == 1):
            txtmojito.configure(state = NORMAL)
            txtmojito.focus()
            txtmojito.delete('0',END)
            e_mojito.set('')
        elif (var4.get() == 0):
            txtmojito.configure(state=DISABLED)
            e_mojito.set('0')

    def chkespresso():
        if (var5.get() == 1):
            txtespresso.configure(state = NORMAL)
            txtespresso.focus()
            txtespresso.delete('0',END)
            e_espresso.set('')
        elif (var5.get() == 0):
            txtespresso.configure(state=DISABLED)
            e_espresso.set('0')

    def chkcappucino():
        if (var6.get() == 1):
            txtcappucino.configure(state = NORMAL)
            txtcappucino.focus()
            txtcappucino.delete('0',END)
            e_cappucino.set('')
        elif (var6.get() == 0):
            txtcappucino.configure(state=DISABLED)
            e_cappucino.set('0')

    def chkicedlatta():
        if (var7.get() == 1):
            txticed_latta.configure(state = NORMAL)
            txticed_latta.focus()
            txticed_latta.delete('0',END)
            e_iced_latta.set('')
        elif (var8.get() == 0):
            txticed_latta.configure(state=DISABLED)
            e_iced_latta.set('0')

    def chklemonade():
        if (var8.get() == 1):
            txtlemonade.configure(state = NORMAL)
            txtlemonade.focus()
            txtlemonade.delete('0',END)
            e_lemonade.set('')
        elif (var8.get() == 0):
            txtlemonade.configure(state=DISABLED)
            e_lemonade.set('0')

    def chksand():
        if (var9.get() == 1):
            txtsandwich.configure(state = NORMAL)
            txtsandwich.focus()
            txtsandwich.delete('0',END)
            e_chicken_sandwich.set('')
        elif (var9.get() == 0):
            txtsandwich.configure(state=DISABLED)
            e_chicken_sandwich.set('0')

    def chkwings():
        if (var10.get() == 1):
            txtwings.configure(state = NORMAL)
            txtwings.focus()
            txtwings.delete('0',END)
            e_chicken_wings.set('')
        elif (var10.get() == 0):
            txtwings.configure(state=DISABLED)
            e_chicken_wings.set('0')

    def chksmoky():
        if (var11.get() == 1):
            txtsmoky.configure(state = NORMAL)
            txtsmoky.focus()
            txtsmoky.delete('0',END)
            e_smoky_bucket.set('')
        elif (var11.get() == 0):
            txtsmoky.configure(state=DISABLED)
            e_smoky_bucket.set('0')

    def chkcheeseb():
        if (var12.get() == 1):
            txtcheeseb.configure(state = NORMAL)
            txtcheeseb.focus()
            txtcheeseb.delete('0',END)
            e_cheese_burger.set('')
        elif (var12.get() == 0):
            txtcheeseb.configure(state=DISABLED)
            e_cheese_burger.set('0')

    def chkchickenb():
        if (var13.get() == 1):
            txtchickenb.configure(state = NORMAL)
            txtchickenb.focus()
            txtchickenb.delete('0',END)
            e_chicken_burger.set('')
        elif (var13.get() == 0):
            txtchickenb.configure(state=DISABLED)
            e_chicken_burger.set('0')

    def chkperi():
        if (var14.get() == 1):
            txtperi.configure(state = NORMAL)
            txtperi.focus()
            txtperi.delete('0',END)
            e_periperi.set('')
        elif (var14.get() == 0):
            txtperi.configure(state=DISABLED)
            e_periperi.set('0')

    def chkvegperi():
        if (var15.get() == 1):
            txtvegperi.configure(state = NORMAL)
            txtvegperi.focus()
            txtvegperi.delete('0',END)
            e_veg_periperi.set('')
        elif (var15.get() == 0):
            txtvegperi.configure(state=DISABLED)
            e_veg_periperi.set('0')

    def chkfries():
        if (var16.get() == 1):
            txtfries.configure(state = NORMAL)
            txtfries.focus()
            txtfries.delete('0',END)
            e_fries.set('')
        elif (var1.get() == 0):
            txtfries.configure(state=DISABLED)
            e_fries.set('0')

    #========================================================Drinks=================================================
    def item():
         import mysql.connector as c
         con=c.connect(host="localhost",user="root",passwd="sandy",database="billservice")
         cursor=con.cursor()       
         cursor.execute( "select * from data")
         row=cursor.fetchall()
         a=row[0][0]
         b=row[1][0]
         c=row[2][0]
         d=row[3][0]
         e=row[4][0]
         f=row[5][0]
         g=row[6][0]
         h=row[7][0]
         i=row[8][0]
         j=row[9][0]
         k=row[10][0]
         l=row[11][0]
         m=row[12][0]
         n=row[13][0]
         o=row[14][0]
         p=row[15][0]

         Latta= Checkbutton(Drinks_F, text=a     , variable=var1, onvalue=1, offvalue=0, font=('Century Schoolbook', 18, 'bold'),
                           bg='Powder Blue', command=chklatta).grid(row=0, sticky=W)
         Coke= Checkbutton(Drinks_F, text=b, variable=var2, onvalue=1, offvalue=0, font=('Century Schoolbook', 18, 'bold'),
                           bg='Powder Blue', command=chkcoke).grid(row=1, sticky=W)
         Iced_Tea= Checkbutton(Drinks_F, text=c, variable=var3, onvalue=1, offvalue=0, font=('Century Schoolbook', 18, 'bold'),
                           bg='Powder Blue', command=chkicetea).grid(row=2, sticky=W)
         Mojito= Checkbutton(Drinks_F, text=d, variable=var4, onvalue=1, offvalue=0, font=('Century Schoolbook', 18, 'bold'),
                           bg='Powder Blue', command=chkmojito).grid(row=3, sticky=W)
         Espresso= Checkbutton(Drinks_F, text=e, variable=var5, onvalue=1, offvalue=0, font=('Century Schoolbook', 18, 'bold'),
                           bg='Powder Blue', command=chkespresso).grid(row=4, sticky=W)
         Cappucino= Checkbutton(Drinks_F, text=f, variable=var6, onvalue=1, offvalue=0, font=('Century Schoolbook', 18, 'bold'),
                           bg='Powder Blue', command=chkcappucino).grid(row=5, sticky=W)
         Iced_Latta= Checkbutton(Drinks_F, text=g, variable=var7, onvalue=1, offvalue=0, font=('Century Schoolbook', 18, 'bold'),
                           bg='Powder Blue', command=chkicedlatta).grid(row=6, sticky=W)
         Lemonade= Checkbutton(Drinks_F, text=h+'                       ', variable=var8, onvalue=1, offvalue=0, font=('Century Schoolbook', 18, 'bold'),
                           bg='Powder Blue', command=chklemonade).grid(row=7, sticky=W)
         Chicken_Sandwich= Checkbutton(Cake_F, text=i+'     ', variable=var9, onvalue=1, offvalue=0, font=('Century Schoolbook', 18, 'bold'),
                           bg='Powder Blue', command=chksand).grid(row=0, sticky=W)
         Chicken_Wings= Checkbutton(Cake_F, text=j, variable=var10, onvalue=1, offvalue=0, font=('Century Schoolbook', 18, 'bold'),
                           bg='Powder Blue', command=chkwings).grid(row=1, sticky=W)
         Smoky_Bucket= Checkbutton(Cake_F, text=k, variable=var11, onvalue=1, offvalue=0, font=('Century Schoolbook', 18, 'bold'),
                           bg='Powder Blue', command=chksmoky).grid(row=2, sticky=W)
         Cheese_Burger= Checkbutton(Cake_F, text=l, variable=var12, onvalue=1, offvalue=0, font=('Century Schoolbook', 18, 'bold'),
                           bg='Powder Blue', command=chkcheeseb).grid(row=3, sticky=W)
         Chicken_Burger= Checkbutton(Cake_F, text=m, variable=var13, onvalue=1, offvalue=0, font=('Century Schoolbook', 18, 'bold'),
                           bg='Powder Blue', command=chkchickenb).grid(row=4, sticky=W)
         Peri_Peri= Checkbutton(Cake_F, text=n, variable=var14, onvalue=1, offvalue=0, font=('Century Schoolbook', 18, 'bold'),
                           bg='Powder Blue', command=chkperi).grid(row=5, sticky=W)
         Veg_Peri_Peri= Checkbutton(Cake_F, text=o, variable=var15, onvalue=1, offvalue=0, font=('Century Schoolbook', 18, 'bold'),
                           bg='Powder Blue', command=chkvegperi).grid(row=6, sticky=W)
         Fries= Checkbutton(Cake_F, text=p, variable=var16, onvalue=1, offvalue=0, font=('Century Schoolbook', 18, 'bold'),
                           bg='Powder Blue', command=chkfries).grid(row=7, sticky=W)
    item()
    #============================================================Text Box (Item)==================================================
    txtlatta = Entry(Drinks_F, font=('Century Schoolbook', 16, 'bold'), bd=8, width=6, justify='left', state=DISABLED, textvariable=e_latta)
    txtlatta.grid(row=0, column=1)
    txtcoke = Entry(Drinks_F, font=('Century Schoolbook', 16, 'bold'), bd=8, width=6, justify='left', state=DISABLED, textvariable=e_coke)
    txtcoke.grid(row=1, column=1)
    txticed_tea = Entry(Drinks_F, font=('Century Schoolbook', 16, 'bold'), bd=8, width=6, justify='left', state=DISABLED, textvariable=e_iced_tea)
    txticed_tea.grid(row=2, column=1)
    txtmojito = Entry(Drinks_F, font=('Century Schoolbook', 16, 'bold'), bd=8, width=6, justify='left', state=DISABLED, textvariable=e_mojito)
    txtmojito.grid(row=3, column=1)
    txtespresso = Entry(Drinks_F, font=('Century Schoolbook', 16, 'bold'), bd=8, width=6, justify='left', state=DISABLED, textvariable=e_espresso)
    txtespresso.grid(row=4, column=1)
    txtcappucino = Entry(Drinks_F, font=('Century Schoolbook', 16, 'bold'), bd=8, width=6, justify='left', state=DISABLED, textvariable=e_cappucino)
    txtcappucino.grid(row=5, column=1)
    txticed_latta = Entry(Drinks_F, font=('Century Schoolbook', 16, 'bold'), bd=8, width=6, justify='left', state=DISABLED, textvariable=e_iced_latta)
    txticed_latta.grid(row=6, column=1)
    txtlemonade = Entry(Drinks_F, font=('Century Schoolbook', 16, 'bold'), bd=8, width=6, justify='left', state=DISABLED, textvariable=e_lemonade)
    txtlemonade.grid(row=7, column=1)
    txtsandwich = Entry(Cake_F, font=('Century Schoolbook', 16, 'bold'), bd=8, width=6, justify='left', state=DISABLED, textvariable=e_chicken_sandwich)
    txtsandwich.grid(row=0, column=1)
    txtwings = Entry(Cake_F, font=('Century Schoolbook', 16, 'bold'), bd=8, width=6, justify='left', state=DISABLED, textvariable=e_chicken_wings)
    txtwings.grid(row=1, column=1)
    txtsmoky = Entry(Cake_F, font=('Century Schoolbook', 16, 'bold'), bd=8, width=6, justify='left', state=DISABLED, textvariable=e_smoky_bucket)
    txtsmoky.grid(row=2, column=1)
    txtcheeseb = Entry(Cake_F, font=('Century Schoolbook', 16, 'bold'), bd=8, width=6, justify='left', state=DISABLED, textvariable=e_cheese_burger)
    txtcheeseb.grid(row=3, column=1)
    txtchickenb = Entry(Cake_F, font=('Century Schoolbook', 16, 'bold'), bd=8, width=6, justify='left', state=DISABLED, textvariable=e_chicken_burger)
    txtchickenb.grid(row=4, column=1)
    txtperi = Entry(Cake_F, font=('Century Schoolbook', 16, 'bold'), bd=8, width=6, justify='left', state=DISABLED, textvariable=e_periperi)
    txtperi.grid(row=5, column=1)
    txtvegperi = Entry(Cake_F, font=('Century Schoolbook', 16, 'bold'), bd=8, width=6, justify='left', state=DISABLED, textvariable=e_veg_periperi)
    txtvegperi.grid(row=6, column=1)
    txtfries = Entry(Cake_F, font=('Century Schoolbook', 16, 'bold'), bd=8, width=6, justify='left', state=DISABLED, textvariable=e_fries)
    txtfries.grid(row=7, column=1)
    #----------------------------------------------------------------------------------------------------------Total costs----------------------------------------------------------------------------------------------
    lblCostOfDrinks = Label(Cost_F, font= ('Century Schoolbook', 14, 'bold'), text= '          Cost Of Drinks           ', bg='Powder blue',
                     fg='black')
    lblCostOfDrinks.grid(row=0, column=0, sticky=W)
    txtCostOfDrinks= Entry (Cost_F, insertwidth=2,  bg= 'white', bd=7, font=('Century schoolbook', 12,'bold'), justify=RIGHT, textvariable=costofdrinks)
    txtCostOfDrinks.grid(row=0, column=1)

    lblCostOfCakes = Label(Cost_F, font= ('Century Schoolbook', 14, 'bold'), text= '          Cost Of Meals', bg='Powder blue',
                     fg='black')
    lblCostOfCakes.grid(row=1, column=0, sticky=W)
    txtCostOfCakes= Entry (Cost_F, insertwidth=2,  bg= 'white', bd=7, font=('Century schoolbook', 12,'bold'), justify=RIGHT, textvariable=costofmeals)
    txtCostOfCakes.grid(row=1, column=1)

    lblServiceCharges = Label(Cost_F, font= ('Century Schoolbook', 14, 'bold'), text= '          Service Charges', bg='Powder blue',
                     fg='black')
    lblServiceCharges.grid(row=2, column=0, sticky=W)
    txtServiceCharges= Entry (Cost_F, insertwidth=2,  bg= 'white', bd=7, font=('Century schoolbook', 12,'bold'), justify=RIGHT, textvariable=servicecharges)
    txtServiceCharges.grid(row=2, column=1)
    #-------------------------------------------------------------------------------------------------------------------Payment Information--------------------------------------------------------------------------------------

    lblPaidTax = Label(Cost_F, font= ('Century Schoolbook', 14, 'bold'), text= '          Paid GST    \t', bg='Powder blue',
                     fg='black')
    lblPaidTax.grid(row=0, column=2, sticky=W)
    txtPaidTax= Entry (Cost_F, insertwidth=2,  bg= 'white', bd=7, font=('Century schoolbook', 12,'bold'), justify=RIGHT, textvariable=paidtax)
    txtPaidTax.grid(row=0, column=3)

    lblSubTotal = Label(Cost_F, font= ('Century Schoolbook', 14, 'bold'), text= '          Sub Total    \t', bg='Powder blue',
                     fg='black')
    lblSubTotal.grid(row=1, column=2, sticky=W)
    txtSubTotal= Entry (Cost_F, insertwidth=2,  bg= 'white', bd=7, font=('Century schoolbook', 12,'bold'), justify=RIGHT, textvariable=subtotal)
    txtSubTotal.grid(row=1, column=3)

    lblTotalCost = Label(Cost_F, font= ('Century Schoolbook', 14, 'bold'), text= '          Total Cost    ', bg='Powder blue',
                     fg='black')
    lblTotalCost.grid(row=2, column=2, sticky=W)
    txtTotalCost= Entry (Cost_F, insertwidth=2,  bg= 'white', bd=7, font=('Century schoolbook', 12,'bold'), justify=RIGHT, textvariable=totalcost)
    txtTotalCost.grid(row=2, column=3)

    #====================================================================Reciept===================================================
    txtReceipt= Text (Reciept_F, width=46, height=12, bg= 'white', bd=4, font=('Century schoolbook', 12,'bold'))
    txtReceipt.grid(row=0, column=0)

    #----------------------------------------------------------------Scroll Bar-------------------------------------------------------------------
    scrollbar= Scrollbar(Reciept_F, command= txtReceipt.yview)
    txtReceipt.configure(yscrollcommand = scrollbar.set)
    txtReceipt.pack(side=LEFT)
    scrollbar.pack(side=RIGHT, fill = Y)

    #-------------------------------------------------------------------------------------Buttons ----------------------------------------------------------------------------------------------------------------------------------
    def cexit():
            cexit=tkinter.messagebox.askyesno('Exit Restaurant System', 'CONFIRM IF YOU WANT TO EXIT')
            if cexit>0:
                root.destroy()
                return
            else:
                txtDisplay.focus()
    def reset():
        paidtax.set('')
        subtotal.set('')
        totalcost.set('')
        costofdrinks.set('')
        costofmeals.set('')
        servicecharges.set('')
        txtReceipt.delete('1.0',END)

        e_latta.set('0')
        e_coke.set('0')
        e_iced_tea.set('0')
        e_mojito.set('0')
        e_espresso.set('0')
        e_cappucino.set('0')
        e_iced_latta.set('0')
        e_lemonade.set('0')

        e_chicken_sandwich.set('0')
        e_chicken_wings.set('0')
        e_smoky_bucket.set('0')
        e_cheese_burger.set('0')
        e_chicken_burger.set('0')
        e_periperi.set('0')
        e_veg_periperi.set('0')
        e_fries.set('0')


        var1.set('0')
        var2.set('0')
        var3.set('0')
        var4.set('0')
        var5.set('0')
        var6.set('0')
        var7.set('0')
        var8.set('0')
        var9.set('0')
        var10.set('0')
        var11.set('0')
        var12.set('0')
        var13.set('0')
        var14.set('0')
        var15.set('0')
        var16.set('0')

        txtlatta.configure(state= DISABLED)
        txtcoke.configure(state= DISABLED)
        txticed_tea.configure(state= DISABLED)
        txtmojito.configure(state= DISABLED)
        txtespresso.configure(state= DISABLED)
        txtcappucino.configure(state= DISABLED)
        txticed_latta.configure(state= DISABLED)
        txtlemonade.configure(state= DISABLED)

        txtsandwich.configure(state= DISABLED)
        txtwings.configure(state= DISABLED)
        txtsmoky.configure(state= DISABLED)
        txtcheeseb.configure(state= DISABLED)
        txtchickenb.configure(state= DISABLED)
        txtperi.configure(state= DISABLED)
        txtvegperi.configure(state= DISABLED)
        txtfries.configure(state= DISABLED)


        

    btnTotal= Button (Buttons_F, padx=16, pady=1, bd=7, fg='black', font=('Century Schoolbook', 16, 'bold'), width=4, text= 'Total'
                      ,bg='powder blue', command=costofitem).grid(row=0, column=0)
    btnReceipt= Button (Buttons_F, padx=16, pady=1, bd=7, fg='black', font=('Century Schoolbook', 16, 'bold'), width=4, text= 'Receipt'
                      ,bg='powder blue', command= Receipt).grid(row=0, column=1)
    btnReset= Button (Buttons_F, padx=16, pady=1, bd=7, fg='black', font=('Century Schoolbook', 16, 'bold'), width=4, text= 'Reset'
                      ,bg='powder blue', command=reset).grid(row=0, column=2)
    btnExit= Button (Buttons_F, padx=16, pady=1, bd=7, fg='black', font=('Century Schoolbook', 16, 'bold'), width=4, text= 'Exit'
                      ,bg='powder blue', command=cexit).grid(row=0, column=3)
    #=====================================================================================Calculator==============================================
    #------------------------------------------------------------------------------------------------------------------------------------------------Calculator function----------------------------------------------------------------------------------

#----------------------------------------------------------------------------------------------------------------Functions-----------------------------------------------------------------------------------------------------

            


    def change():
            a=float(txttotal.get())
            b=float(txtpaid.get())
            if a>b:
                    w=Toplevel()
                    w.geometry ('290x200+530+250')
                    w.title('Restaurent Billing System')
                    w.configure(bg='White')
                    f=Frame(w, bg='white')
                    def yes():
                            txtpaid.delete('0',END)
                            txtpaid.focus()
                            w.destroy()

                    f.grid(row=4)
                    txtno=Label(w,text= '###:', font= ('Calibri', 12,  'bold'), padx= 2, pady= 2, bg= 'white', foreground='white')
                    txtno.grid(row=0, column=0)
                    txtno=Label(w,text= '###:', font= ('Calibri', 12,  'bold'), padx= 2, pady= 2, bg= 'white', foreground='white')
                    txtno.grid(row=2, column=0)
                    txtno=Label(w,text= '###:', font= ('Calibri', 12,  'bold'), padx= 2, pady= 2, bg= 'white', foreground='white')
                    txtno.grid(row=3, column=0)
                    txtno=Label(f,text= '####:', font= ('Calibri', 25,  'bold'), padx= 2, pady= 2, bg= 'white', foreground='white')
                    txtno.grid(row=1, column=2)
                    txt=Label(w,text= '  Please Enter a Bigger Amount:', font= ('Century Schoolbook', 12,  'bold'), bg= 'white',padx= 2, pady= 2)
                    txt.grid(row=1, column=0)
                    btm=Button (f, bd=1, fg='black', font=('Century Schoolbook', 12, 'bold'), width=5, text= 'Yes'
                      ,bg='powder blue', padx=2, pady=2, command=yes)
                    btm.grid(row=0, column=0)
                    btm1=Button (f, bd=1, fg='black', font=('Century Schoolbook', 12, 'bold'), width=5, text= 'No' ,bg='powder blue', padx=2, pady=2, state=DISABLED)                    
                    btm1.grid(row=0, column=3)

                    
                    
            else:
                    c=b-a
                    d='%.2f'%(c)
                    txtchange.insert(END,d)         

    txttotal= Entry(Cal_F, width=20, bg= 'white', bd=4, font=('Century schoolbook', 12,'bold'), justify=RIGHT)
    txttotal.grid(row=0, column=1)
    lbltotal=Label(Cal_F, width=13, bg= 'white', bd=4, font=('Century schoolbook', 16,'bold'), justify=RIGHT, text='Total', relief=RIDGE)
    lbltotal.grid(row=0,column=0)
    lbltotal=Label(Cal_F, width=13, bg= 'green', bd=4, font=('Century schoolbook', 8,'bold'), foreground='green', justify=RIGHT, text='Total')
    lbltotal.grid(row=1,column=0)
    txtpaid= Entry (Cal_F, width=20, bg= 'white', bd=4, font=('Century schoolbook', 16,'bold'), justify=RIGHT, textvariable= paid)
    txtpaid.grid(row=2, column=1, columnspan=4, pady=1)

    lblpaid=Label(Cal_F, width=13, bg= 'white', bd=4, font=('Century schoolbook', 16,'bold'), justify=RIGHT, text='Amount Paid', relief=RIDGE)
    lblpaid.grid(row=2,column=0)
    lbltotal=Label(Cal_F, width=13, bg= 'green', bd=4, font=('Century schoolbook', 8,'bold'), foreground='green', justify=RIGHT, text='Total')
    lbltotal.grid(row=3,column=0)
    txtchange= Entry(Cal_F, width=20, bg= 'white', bd=4, font=('Century schoolbook', 16,'bold'), justify=RIGHT)
    txtchange.grid(row=4, column=1, columnspan=4, pady=1)
    btnchange=Button (Cal_F, bd=4, fg='black', font=('Century Schoolbook', 15, 'bold'), width=13, text= 'Change'
                      ,bg='powder blue', command=change).grid(row=4, column=0)
    

    


#=========================================================Button Widget (Staff)==================================================

b.lbltit= Label (staffframe, font= ('Century Schoolbook', 25,  'bold'), text= 'Staff Login:                                               ', padx= 50, pady= 2, bg= 'Ghost white')
b.lbltit.grid(row=1, column= 1, sticky=W)

b.btnlogin = Button (staffframe, text= 'Login',  font=('arial', 20, 'bold'), width= 11, height= 1, bd=4, command=window)
b.btnlogin.grid(row=3, column=1)


b.txtuname.focus()


b.mainloop()

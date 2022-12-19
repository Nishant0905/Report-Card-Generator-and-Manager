import os
from mysql import connector
from tkinter import *
from tkinter import ttk
from csv import *
from statistics import *


def ent():
    # BasicEntry
    global n1, c1, s1, r1,table_name
    n1 = name_entry.get()
    table_name = n1
    c1 = class_entry.get()
    s1 = section_entry.get()
    r1 = roll_entry.get()

def ent7():
    # For Password(SQL)
    global password, table_name
    password = pw_entry.get()
    

def pw_window():
    # Password Window

    def shbtn():
        if (cbvar.get()) == 1:
            pw_entry.config(show="")
        else:
            pw_entry.config(show="•")

    pws = Toplevel()
    pws.title('Enter password for SQL')
    pwb = Button(pws, text='MY SQL PASSWORD', bg='black', font=('Calibri', 24), state='disabled')
    pws.geometry("512x456")
    pwb.place(x=10, y=220)

    global pw_entry
    pw_s = StringVar()
    pw_entry = Entry(pws, textvariable=pw_s, show='•')
    pw_entry.place(x=310, y=220)
    

    global shp_btn
    cbvar = IntVar(value=0)
    cb_style = ttk.Style()
    cb_style.configure("R.TCheckbutton")

    shp_btn = ttk.Checkbutton(pws, text="Show Password", variable=cbvar, onvalue=1, offvalue=0, command=shbtn,
                              style="R.TCheckbutton")
    shp_btn.place(x=250, y=370)
    
    submit = Button(pws, text='SUBMIT', bg='Blue', font=("Calibri", 16), command=lambda: [ent7(), pws.destroy(),
                                                                                          sql_database(),
                                                                                          sql_report()])
    submit.place(x=250, y=420)
    pws.mainloop()


def sql_database():
    # Create database
    mydb = connector.connect(host="127.0.0.1", port=3306, user='root', passwd=password, auth_plugin='mysql_native_password')
    mycursor = mydb.cursor()
    mycursor.execute('create database if not exists {};'.format(c1))



def csv_read():
    # Reading from CSV
    global ac, bc, cc, dc, ec, fc, gc, hc
    with open(n1 + ".csv") as f1:
        creader = reader(f1)
        ac, bc, cc, dc, ec, fc, gc, hc = creader


def text_write():
    # ReportCard
    with open(n1 + ".txt", 'w') as f2:
        f2.write('\t\t\t\t\t\tREPORT CARD' + '\n')
        f2.write("\n")
        f2.write("\n")
        f2.write("Name: " + n1 + "\n")
        f2.write("Class: " + str(c1) + "\n")
        f2.write("Section: " + s1 + "\n")
        f2.write("Rollno: " + r1 + "\n")
        f2.write("\n")
        for i in range(1, 6):
            f2.write(ac[i] + '\n')
            f2.write("\n")
            f2.write(sub1 + ':' + bc[i] + '\n')
            f2.write("\n")
            f2.write(sub2 + ':' + cc[i] + '\n')
            f2.write("\n")
            f2.write(sub3 + ':' + dc[i] + '\n')
            f2.write("\n")
            f2.write(sub4 + ':' + ec[i] + '\n')
            f2.write("\n")
            f2.write(sub5 + ':' + fc[i] + '\n')
            f2.write("\n")
            f2.write('Average' + ':' + gc[i] + '\n')
            f2.write("\n")
            f2.write("Percentage" + ':' + hc[i] + '\n')
            f2.write("\n")
        f2.write('\n')
        f2.write('Overall Grade:' + grade + '\n')


def csv_write():
    dict = [{"Subject": sub1, "UT-1": s11m, "UT-2": s21m, "TERM-1": s31m, "UT-3": s41m, "TERM-2": s51m},
            {"Subject": sub2, "UT-1": s12m, "UT-2": s22m, "TERM-1": s32m, "UT-3": s42m, "TERM-2": s52m},
            {"Subject": sub3, "UT-1": s13m, "UT-2": s23m, "TERM-1": s33m, "UT-3": s43m, "TERM-2": s53m},
            {"Subject": sub4, "UT-1": s14m, "UT-2": s24m, "TERM-1": s34m, "UT-3": s44m, "TERM-2": s54m},
            {"Subject": sub5, "UT-1": s15m, "UT-2": s25m, "TERM-1": s35m, "UT-3": s45m, "TERM-2": s55m}]

    a = mean([int(s11m), int(s12m), int(s13m), int(s14m), int(s15m)])
    b = mean([int(s21m), int(s22m), int(s23m), int(s24m), int(s25m)])
    c = mean([int(s31m), int(s32m), int(s33m), int(s34m), int(s35m)])
    d = mean([int(s41m), int(s42m), int(s43m), int(s44m), int(s45m)])
    e = mean([int(s51m), int(s52m), int(s53m), int(s54m), int(s55m)])

    fields = ["Subject", 'UT-1', 'UT-2', 'TERM-1', 'UT-3', 'TERM-2']

    with open(n1 + '.csv', 'w') as f:
        write = DictWriter(f, fieldnames=fields)
        write.writeheader()
        write.writerows(dict)
        write.writerow({"Subject": "Average", "UT-1": a, "UT-2": b, "TERM-1": c, "UT-3": d, "TERM-2": e})
        a1 = (a / int(max_ut)) * 100
        b1 = (b / int(max_ut)) * 100
        c1 = (c / int(max_term)) * 100
        d1 = (d / int(max_ut)) * 100
        e1 = (e / int(max_term)) * 100
        write.writerow({"Subject": "Percentage","UT-1": a1, "UT-2": b1, "TERM-1": c1, "UT-3": d1, "TERM-2": e1})
    # Percentage
    percent_a = mean([a1, b1, c1, d1, e1])
    global grade
    if percent_a >= 90:
        grade = 'A'
    elif percent_a < 90 and percent_a >= 80:
        grade = 'B'
    elif percent_a < 80 and percent_a >= 70:
        grade = 'C'
    elif percent_a < 70 and percent_a >= 60:
        grade = 'D'
    elif percent_a < 60 and percent_a >= 50:
        grade = 'E'
    else:
        grade = 'FAIL'





def ent1():
    global sub1, sub2, sub3, sub4, sub5, max_ut, max_term
    sn = clicked.get()
    max_ut = m_ut.get()
    max_term = m_term.get()
    sub1, sub2, sub3, sub4, sub5 = sn.split(',')
    


def sql_report():
    # Writing into SQL
    mydb = connector.connect(host='localhost', user='root', passwd=password, database=c1)
    mycursor = mydb.cursor()
    mycursor.execute("create table if not exists {} (SUBJECT varchar(50),UT1 float,UT2 float,TERM1 float,UT3 float,"
                     "TERM2 float) ;".format(table_name))
    if ch == 4 or ch == 1 :
        mycursor.execute("truncate table {}".format(table_name))
    else:
        pass    
    mycursor.execute("insert into {} values('{}','{}','{}','{}','{}','{}'), ('{}','{}','{}','{}','{}','{}'),('{}','{}','{}','{}','{}','{}'),('{}','{}','{}','{}','{}','{}'),('{}','{}','{}','{}','{}','{}');".format(table_name, sub1, s11m, s21m, s31m, s41m, s51m, sub2, s12m, s22m, s32m, s42m, s52m,
                                     sub3, s13m, s23m, s33m, s43m, s53m, sub4, s14m, s24m, s34m, s44m, s54m, sub5, s15m,
                                     s25m, s35m, s45m, s55m))

    mydb.commit()
    mydb.close()


def ent6():
    # Entry for term 2
    global s51m, s52m, s53m, s54m, s55m

    s51m = s51_entry.get()
    s52m = s52_entry.get()
    s53m = s53_entry.get()
    s54m = s54_entry.get()
    s55m = s55_entry.get()




def term2():
    # Term-2 Window
    t2 = Toplevel()


    t2.title('#TERM2')
    t2.geometry("512x620")

    t2b = Button(t2, text='TERM2 MARKS', bg='Black', font=('Calibri', 22), state='disabled')
    t2b.place(x=180, y=15)

    s51 = Button(t2, text=sub1, bg='Black', font=('Calibri', 15), state='disabled')
    s51.place(x=10, y=120)

    s52 = Button(t2, text=sub2, bg='Black', font=('Calibri', 15), state='disabled')
    s52.place(x=10, y=220)

    s53 = Button(t2, text=sub3, bg='Black', font=('Calibri', 15), state='disabled')
    s53.place(x=10, y=320)

    s54 = Button(t2, text=sub4, bg='Black', font=('Calibri', 15), state='disabled')
    s54.place(x=10, y=420)

    s55 = Button(t2, text=sub5, bg='Black', font=('Calibri', 15), state='disabled')
    s55.place(x=10, y=520)

    proceed6 = Button(t2, text="PROCEED>>>", bg='BLUE', font=('Calibri', 16), command=lambda: [ent6(), t2.destroy(),
                                                                                               csv_write(), csv_read(),
                                                                                               text_write(),
                                                                                               pw_window()])
    proceed6.place(x=400, y=345)

    global s51_entry, s52_entry, s53_entry, s54_entry, s55_entry
    global s51v, s52v, s53v, s54v, s55v
    
    try:
        f = open(n1+".csv")
        creader = reader(f)
        ac, bc, cc, dc, ec, fc, gc, hc = creader
        s51v = IntVar(value= bc[5])
        s52v = IntVar(value= cc[5])
        s53v = IntVar(value= dc[5])
        s54v = IntVar(value= ec[5])
        s55v = IntVar(value= fc[5])
    except FileNotFoundError:
        s51v = IntVar()
        s52v = IntVar()
        s53v = IntVar()
        s54v = IntVar()
        s55v = IntVar()

    
    s51_entry = Entry(t2, textvariable=s51v)
    s52_entry = Entry(t2, textvariable=s52v)
    s53_entry = Entry(t2, textvariable=s53v)
    s54_entry = Entry(t2, textvariable=s54v)
    s55_entry = Entry(t2, textvariable=s55v)

    s51_entry.place(x=210, y=120)
    s52_entry.place(x=210, y=220)
    s53_entry.place(x=210, y=320)
    s54_entry.place(x=210, y=420)
    s55_entry.place(x=210, y=520)

    t2.mainloop()


def ent5():
    # Entry for Ut-3
    global s41m, s42m, s43m, s44m, s45m
    s41m = s41_entry.get()
    s42m = s42_entry.get()
    s43m = s43_entry.get()
    s44m = s44_entry.get()
    s45m = s45_entry.get()


def ut3():
    # UT-3 Window
    u3 = Toplevel()


    u3.title('#UT3')
    u3.geometry("512x620")


    u3b = Button(u3, text="UT3 MARKS", bg='Black', font=('Calibri', 22), state='disabled')
    u3b.place(x=180, y=15)

    s41 = Button(u3, text=sub1, bg='Black', font=('Calibri', 15), state='disabled')
    s41.place(x=10, y=120)

    s42 = Button(u3, text=sub2, bg='Black', font=('Calibri', 15), state='disabled')
    s42.place(x=10, y=220)

    s43 = Button(u3, text=sub3, bg='Black', font=('Calibri', 15), state='disabled')
    s43.place(x=10, y=320)

    s44 = Button(u3, text=sub4, bg='Black', font=('Calibri', 15), state='disabled')
    s44.place(x=10, y=420)

    s45 = Button(u3, text=sub5, bg='Black', font=('Calibri', 15), state='disabled')
    s45.place(x=10, y=520)

    proceed5 = Button(u3, text="PROCEED>>>", bg='BLUE', font=('Calibri', 16), command=lambda: [ent5(), u3.destroy(),
                                                                                               term2()])
    proceed5.place(x=400, y=345)

    global s41_entry, s42_entry, s43_entry, s44_entry, s45_entry
    global s41v, s42v, s43v, s44v, s45v
    

    try:
        f = open(n1+".csv")
        creader = reader(f)
        ac, bc, cc, dc, ec, fc, gc, hc = creader
        s41v = IntVar(value= bc[4])
        s42v = IntVar(value= cc[4])
        s43v = IntVar(value= dc[4])
        s44v = IntVar(value= ec[4])
        s45v = IntVar(value= fc[4])
    except FileNotFoundError:
        s41v = IntVar()
        s42v = IntVar()
        s43v = IntVar()
        s44v = IntVar()
        s45v = IntVar() 

    s41_entry = Entry(u3, textvariable=s41v)
    s42_entry = Entry(u3, textvariable=s42v)
    s43_entry = Entry(u3, textvariable=s43v)
    s44_entry = Entry(u3, textvariable=s44v)
    s45_entry = Entry(u3, textvariable=s45v)

    s41_entry.place(x=210, y=120)
    s42_entry.place(x=210, y=220)
    s43_entry.place(x=210, y=320)
    s44_entry.place(x=210, y=420)
    s45_entry.place(x=210, y=520)

    u3.mainloop()


def ent4():
    # Entry for Term-1
    global s31m, s32m, s33m, s34m, s35m
    s31m = s31_entry.get()
    s32m = s32_entry.get()
    s33m = s33_entry.get()
    s34m = s34_entry.get()
    s35m = s35_entry.get()



def term1():
    # TERM-1 Window
    t1 = Toplevel()

    t1.title('#TERM1')
    t1.geometry("512x620")

    t1b = Button(t1, text="TERM1 MARKS", bg='Black', font=('Calibri', 22), state='disabled')
    t1b.place(x=180, y=15)

    s31 = Button(t1, text=sub1, bg='Black', font=('Calibri', 15), state='disabled')
    s31.place(x=10, y=120)

    s32 = Button(t1, text=sub2, bg='Black', font=('Calibri', 15), state='disabled')
    s32.place(x=10, y=220)

    s33 = Button(t1, text=sub3, bg='Black', font=('Calibri', 15), state='disabled')
    s33.place(x=10, y=320)

    s34 = Button(t1, text=sub4, bg='Black', font=('Calibri', 15), state='disabled')
    s34 = Button(t1, text=sub4, bg='Black', font=('Calibri', 15), state='disabled')
    s34.place(x=10, y=420)

    s35 = Button(t1, text=sub5, bg='Black', font=('Calibri', 15), state='disabled')
    s35.place(x=10, y=520)

    proceed4 = Button(t1, text="PROCEED>>>", bg='BLUE', font=('Calibri', 16), command=lambda: [ent4(), t1.destroy(),
                                                                                               ut3()])
    proceed4.place(x=400, y=345)

    global s31_entry, s32_entry, s33_entry, s34_entry, s35_entry
    global s31v, s32v, s33v, s34v, s35v

    try:
        f = open(n1+".csv")
        creader = reader(f)
        ac, bc, cc, dc, ec, fc, gc, hc = creader
        s31v = IntVar(value= bc[3])
        s32v = IntVar(value= cc[3])
        s33v = IntVar(value= dc[3])
        s34v = IntVar(value= ec[3])
        s35v = IntVar(value= fc[3])
    except FileNotFoundError:
        s31v = IntVar()
        s32v = IntVar()
        s33v = IntVar()
        s34v = IntVar()
        s35v = IntVar()
    s31_entry = Entry(t1, textvariable=s31v)
    s32_entry = Entry(t1, textvariable=s32v)
    s33_entry = Entry(t1, textvariable=s33v)
    s34_entry = Entry(t1, textvariable=s34v)
    s35_entry = Entry(t1, textvariable=s35v)

    s31_entry.place(x=210, y=120)
    s32_entry.place(x=210, y=220)
    s33_entry.place(x=210, y=320)
    s34_entry.place(x=210, y=420)
    s35_entry.place(x=210, y=520)

    t1.mainloop()


def ent3():
    # Entry for UT-2
    global s21m, s22m, s23m, s24m, s25m
    s21m = s21_entry.get()
    s22m = s22_entry.get()
    s23m = s23_entry.get()
    s24m = s24_entry.get()
    s25m = s25_entry.get()



def ut2():
    # UT-2 Window
    u2 = Toplevel()


    u2.title('#UT2 ')
    u2.geometry("512x620")

    u2b = Button(u2, text="UT2 MARKS", bg='Black', font=('Calibri', 22), state='disabled')
    u2b.place(x=180, y=15)

    s21 = Button(u2, text=sub1, bg='Black', font=('Calibri', 15), state='disabled')
    s21.place(x=10, y=120)

    s22 = Button(u2, text=sub2, bg='Black', font=('Calibri', 15), state='disabled')
    s22.place(x=10, y=220)

    s23 = Button(u2, text=sub3, bg='Black', font=('Calibri', 15), state='disabled')
    s23.place(x=10, y=320)

    s24 = Button(u2, text=sub4, bg='Black', font=('Calibri', 15), state='disabled')
    s24.place(x=10, y=420)

    s25 = Button(u2, text=sub5, bg='Black', font=('Calibri', 15), state='disabled')
    s25.place(x=10, y=520)

    proceed3 = Button(u2, text="PROCEED>>>", bg='BLUE', font=('Calibri', 16), command=lambda: [ent3(), u2.destroy(),
                                                                                               term1()])
    proceed3.place(x=400, y=345)

    global s21_entry, s22_entry, s23_entry, s24_entry, s25_entry
    global s21v, s22v, s23v, s24v, s25v


    try:
        f = open(n1+".csv")
        creader = reader(f)
        ac, bc, cc, dc, ec, fc, gc, hc = creader
        s21v = IntVar(value= bc[2])
        s22v = IntVar(value= cc[2])
        s23v = IntVar(value= dc[2])
        s24v = IntVar(value= ec[2])
        s25v = IntVar(value= fc[2])
    except FileNotFoundError:
        s21v = IntVar()
        s22v = IntVar()
        s23v = IntVar()
        s24v = IntVar()
        s25v = IntVar()  
    s21_entry = Entry(u2, textvariable=s21v)
    s22_entry = Entry(u2, textvariable=s22v)
    s23_entry = Entry(u2, textvariable=s23v)
    s24_entry = Entry(u2, textvariable=s24v)
    s25_entry = Entry(u2, textvariable=s25v)

    s21_entry.place(x=210, y=120)
    s22_entry.place(x=210, y=220)
    s23_entry.place(x=210, y=320)
    s24_entry.place(x=210, y=420)
    s25_entry.place(x=210, y=520)

    u2.mainloop()


def ent2():
    # Entry for UT-1
    global s11m, s12m, s13m, s14m, s15m
    s11m = s11_entry.get()
    s12m = s12_entry.get()
    s13m = s13_entry.get()
    s14m = s14_entry.get()
    s15m = s15_entry.get()



def ut1():
    # UT-1 Window
    u1 = Toplevel()


    u1.title('#UT1 ')
    u1.geometry("512x620")
    
    u1b = Button(u1, text="UT1 MARKS", bg='Black', font=('Calibri', 22), state='disabled')
    u1b.place(x=180, y=15)

    s11 = Button(u1, text=sub1, bg='Black', font=('Calibri', 15), state='disabled')
    s11.place(x=10, y=120)

    s12 = Button(u1, text=sub2, bg='Black', font=('Calibri', 15), state='disabled')
    s12.place(x=10, y=220)

    s13 = Button(u1, text=sub3, bg='Black', font=('Calibri', 15), state='disabled')
    s13.place(x=10, y=320)

    s14 = Button(u1, text=sub4, bg='Black', font=('Calibri', 15), state='disabled')
    s14.place(x=10, y=420)

    s15 = Button(u1, text=sub5, bg='Black', font=('Calibri', 15), state='disabled')
    s15.place(x=10, y=520)

    proceed2 = Button(u1, text="PROCEED>>>", bg='BLUE', font=('Calibri', 16), command=lambda: [ent2(), u1.destroy(),
                                                                                               ut2()])
    proceed2.place(x=400, y=345)

    global s11_entry, s12_entry, s13_entry, s14_entry, s15_entry
    global s11v, s12v, s13v, s14v, s15v
    
    try:
        f = open(n1+".csv")
        creader = reader(f)
        ac, bc, cc, dc, ec, fc, gc, hc = creader
        s11v = IntVar(value= bc[1])
        s12v = IntVar(value= cc[1])
        s13v = IntVar(value= dc[1])
        s14v = IntVar(value= ec[1])
        s15v = IntVar(value= fc[1])

    except FileNotFoundError:
        s11v = IntVar()
        s12v = IntVar()
        s13v = IntVar()
        s14v = IntVar()
        s15v = IntVar()

    s11_entry = Entry(u1, textvariable=s11v)
    s12_entry = Entry(u1, textvariable=s12v)
    s13_entry = Entry(u1, textvariable=s13v)
    s14_entry = Entry(u1, textvariable=s14v)
    s15_entry = Entry(u1, textvariable=s15v)

    s11_entry.place(x=210, y=120)
    s12_entry.place(x=210, y=220)
    s13_entry.place(x=210, y=320)
    s14_entry.place(x=210, y=420)
    s15_entry.place(x=210, y=520)

    u1.mainloop()


def sub():
            # Subject Details
            s = Toplevel()
            s.geometry("755x356")

            s.title('#SUBJECT DETAILS ')
            sd = Button(s, text="SUBJECT DETAILS", bg='Black', font=('Calibri', 22), state='disabled')
            sd.place(x=180, y=10)

            ns = Button(s, text="ENTER NAMES OF 5 SUBJECTS", bg='Black', font=('Calibri', 15), state='disabled')
            ns.place(x=10, y=60)

            proceed1 = Button(s, text="PROCEED>>>", bg='BLUE', font=('Calibri', 16), command=lambda: [ent1(), s.destroy(),
                                                                                                      ut1()])
            proceed1.place(x=200, y=240)


            global m_ut, m_term, clicked

            clicked = StringVar()
            options = ["ENGLISH,CHEMISTRY,PHYSICS,MATHS,COMPUTER",
                       "ENGLISH,CHEMISTRY,PHYSICS,MATHS,BIOLOGY",
                       "ACCOUNTANCY,BUSINESS_STUDIES,ECONOMICS,ENGLISH,COMPUTER",
                       "ACCOUNTANCY,BUSINESS_STUDIES,ECONOMICS,ENGLISH,MATHS",
                       "HISTORY,POLITICAL_SCIENCE,GEOGRAPHY,FINE_ARTS,SOCIOLOGY",
                       "ENGLISH,HINDI,SCIENCE,SOCIAL,MATHS",
                       "ENGLISH,KANNADA,SCIENCE,SOCIAL,MATHS",
                       "ENGLISH,SANSKRIT,SCIENCE,SOCIAL,MATHS",
                       "ENGLISH,FRENCH,SCIENCE,SOCIAL,MATHS",
                       "ENGLISH,LANGUAGE,EVS,GK,MATHS",
                       "GK,GMAT,APTITUDE,MATHS,ENGLISH"]

            subj_drop = OptionMenu(s, clicked, *options)
            subj_drop.place(x=250, y=60)

            mu = Button(s, text="MAX MARKS OF UT", bg='Black', font=('Calibri', 15), state='disabled')
            mu.place(x=10, y=120)

            mt = Button(s, text="MAX MARKS OF TERM", bg='Black', font=('Calibri', 15), state='disabled')
            mt.place(x=10, y=180)

            mut = IntVar()
            mte = IntVar()

            m_ut = Entry(s, textvariable=mut)
            m_ut.place(x=250, y=120)

            m_term = Entry(s, textvariable=mte)
            m_term.place(x=250, y=180)

            s.mainloop()


# __main__



def mainw():
    r = Toplevel()

    r.title("#Enter DETAILS")
    r.geometry("512x456")
    name = Button(r, text="NAME", bg='Black', font=('Calibri', 16), state='disabled',)
    name.place(x=100, y=120)

    f = Button(r, text="ENTER DETAILS", bg='Black', font=('Calibri', 16), state='disabled')
    f.place(x=180, y=15)

    class_1 = Button(r, text="CLASS", bg='Black', font=('Calibri', 16), state='disabled')
    class_1.place(x=100, y=170)

    sec = Button(r, text="SECTION", bg='Black', font=('Calibri', 16), state='disabled')
    sec.place(x=100, y=220)

    rollno = Button(r, text="ROLL_NO", bg='Black', font=('Calibri', 16), state='disabled')
    rollno.place(x=100, y=270)

    proceed = Button(r, text="PROCEED", bg='BLUE', font=('Calibri', 16), command=lambda: [ent(), r.destroy(), sub()])
    proceed.place(x=200, y=370)

    global name_entry, class_entry, section_entry, roll_entry

    na = StringVar()
    cl = StringVar()
    se = StringVar()
    rn = IntVar()

    name_entry = Entry(r, textvariable=na)
    name_entry.place(x=215, y=120)

    class_entry = StringVar()
    options = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X", "XI", "XII"]

    subj_drop = OptionMenu(r, class_entry, *options)
    subj_drop.place(x=260, y=170)

    section_entry = Entry(r, textvariable=se)
    section_entry.place(x=215, y=220)

    roll_entry = Entry(r, textvariable=rn)
    roll_entry.place(x=215, y=270)

    r.mainloop()

# Designing window for registration

def register():
    global register_screen
    register_screen = Toplevel(main_screen)
    register_screen.title("REGISTER")
    register_screen.geometry("300x250")

    global username
    global password
    global username_entry
    global password_entry
    username = StringVar()
    password = StringVar()

    Label(register_screen, text="Please enter details below", bg="blue").pack()
    Label(register_screen, text="").pack()
    username_lable = Label(register_screen, text="Username * ")
    username_lable.pack()
    username_entry = Entry(register_screen, textvariable=username)
    username_entry.pack()
    password_lable = Label(register_screen, text="Password * ")
    password_lable.pack()
    password_entry = Entry(register_screen, textvariable=password, show='*')
    password_entry.pack()
    Label(register_screen, text="").pack()
    Button(register_screen, text="Register", width=10, height=1, bg="blue", command=register_user).pack()


# Designing window for login

def login():
    global login_screen
    login_screen = Toplevel(main_screen)
    login_screen.title("Login")
    login_screen.geometry("300x250")
    Label(login_screen, text="Please enter details below to login").pack()
    Label(login_screen, text="").pack()

    global username_verify
    global password_verify

    username_verify = StringVar()
    password_verify = StringVar()

    global username_login_entry
    global password_login_entry

    Label(login_screen, text="Username * ").pack()
    username_login_entry = Entry(login_screen, textvariable=username_verify)
    username_login_entry.pack()
    Label(login_screen, text="").pack()
    Label(login_screen, text="Password * ").pack()
    password_login_entry = Entry(login_screen, textvariable=password_verify, show='*')
    password_login_entry.pack()
    Label(login_screen, text="").pack()
    Button(login_screen, text="Login", width=10, height=1, command=login_verify).pack()


# Implementing event on register button

def register_user():
    username_info = username.get()
    password_info = password.get()

    file = open(username_info, "w")
    file.write(username_info + "\n")
    file.write(password_info)
    file.close()

    username_entry.delete(0, END)
    password_entry.delete(0, END)

    Label(register_screen, text="Registration Success", fg="green", font=("calibri", 11)).pack()


# Implementing event on login button

def login_verify():
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_login_entry.delete(0, END)
    password_login_entry.delete(0, END)

    list_of_files = os.listdir()
    if username1 in list_of_files:
        file1 = open(username1, "r")
        verify = file1.read().splitlines()
        if password1 in verify:
            login_sucess()

        else:
            password_not_recognised()

    else:
        user_not_found()


 # Deleting popups

def delete_login_success():
    login_success_screen.destroy()


def delete_password_not_recognised():
    password_not_recog_screen.destroy()


def delete_user_not_found_screen():
    user_not_found_screen.destroy()
       


# Designing popup for login success

def login_sucess():
    global login_success_screen
    login_success_screen = Toplevel(login_screen)
    login_success_screen.title("Success😄😄😄")
    login_success_screen.geometry("150x100")
    Label(login_success_screen, text="Login Success").pack()
    Button(login_success_screen, text="OK", command=lambda: [delete_login_success, mainw()]).pack()


# Designing popup for login invalid password

def password_not_recognised():
    global password_not_recog_screen
    password_not_recog_screen = Toplevel(login_screen)
    password_not_recog_screen.title("Success")
    password_not_recog_screen.geometry("150x100")
    Label(password_not_recog_screen, text="Invalid Password ").pack()
    Button(password_not_recog_screen, text="OK", command=delete_password_not_recognised).pack()


# Designing popup for user not found

def user_not_found():
    global user_not_found_screen
    user_not_found_screen = Toplevel(login_screen)
    user_not_found_screen.title("Success")
    user_not_found_screen.geometry("150x100")
    Label(user_not_found_screen, text="User Not Found").pack()
    Button(user_not_found_screen, text="OK", command=delete_user_not_found_screen).pack()


# Deleting popups

def delete_login_success():
    login_success_screen.destroy()


def delete_password_not_recognised():
    password_not_recog_screen.destroy()


def delete_user_not_found_screen():
    user_not_found_screen.destroy()


# Designing Main(first) window

def m():
    global main_screen
    main_screen = Tk()
    main_screen.geometry("300x250")
    main_screen.title("Account Login")
    Label(text="Select Your Choice", bg="blue", width="300", height="2", font=("Calibri", 13)).pack()
    Label(text="").pack()
    Button(text="Login", height="2", width="30", command=login).pack()
    Label(text="").pack()
    Button(text="Register", height="2", width="30", command=register).pack()

    main_screen.mainloop()

def search_user():
    v = input("Enter the name of the student you want to search: ")
    try:
        with open(v + ".txt") as f1:
            sear = f1.readlines()
            for i in sear:
               print(i)
               

    except FileNotFoundError:
        print("No such student!")

def calc_max():
    password = input("Enter Mysql Password: ")
   

    mydb = connector.connect(host='localhost', user='root', passwd=password, database=cl_ask)
    mycursor = mydb.cursor()
    mycursor.execute("use {};".format(cl_ask))
    mycursor.execute("show tables;")
    tab = mycursor.fetchall()


    count1 = count2 = count3 = count4 = count5 = 0
    for i in tab:
        for j in i:

            mycursor.execute("select avg(ut1),avg(ut2),avg(term1),avg(ut3),avg(term2) from {};".format(j.strip("'")))
            av1, av2, av3, av4, av5 = mycursor.fetchone()

            count1 += av1
            count2 += av2
            count3 += av3
            count4 += av4
            count5 += av5

 
    print("Overall average in '{}': ".format("ut1"), count1/len(tab))    
    print("Overall average in '{}': ".format("ut2"), count2/len(tab))
    print("Overall average in '{}': ".format("term1"), count3/len(tab))
    print("Overall average in '{}': ".format("ut3"), count4/len(tab))
    print("Overall average in '{}': ".format("term2"), count5/len(tab))

def del_report():
    password = input("Enter Mysql Password: ")
    table_name = input("Enter the Name of the student you want to delete: ")
    mydb = connector.connect(host='localhost', user='root', passwd=password, database=cls_ask)
    mycursor = mydb.cursor()
    mycursor.execute("use {};".format(cls_ask))
    mycursor.execute("drop table {};".format(table_name))
    mydb.commit()
    mydb.close()
    print("Student Record Deleted!!!👍👍")

while True:
    print("""MENU:
    1. Report Card Generation
    2. Search Student Details
    3. Calculate average marks from a class
    4. Update Report Card
    5. Delete Student Record
    6. Exit""")

    ch = int(input("Enter Your Choice: "))
    if ch == 1:
        m()
    elif ch == 2:
        search_user()
    
   

    elif ch == 3:
        cl_ask = input("Enter the class in roman numerals: ")
        calc_max()

    elif ch == 4:
        m()    

    elif ch == 5:
        cls_ask = input("Enter the class in roman numerals: ")
        del_report()
    elif ch == 6:

        print("Thank you for using our application😀😀!!!")        

        break    

    else:
        print("Invalid Choice🤨🤨")

        continue
# Program has been executed with all the necessary features

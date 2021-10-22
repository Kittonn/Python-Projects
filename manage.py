from tkinter import *
from tkinter import ttk,messagebox
import mysql.connector as mysql

main = Tk()
main.title('Grade Management')
main.geometry('1025x800')
main.resizable(False, False)

global total_score
global total_grade
global total_unit
global thai_txt; global math_txt; global sci_txt; global soc_txt; global eng_txt; 
global phy_txt; global bio_txt; global chem_txt; global chinese_txt; global art_txt;
global u_thai_txt; global u_math_txt; global u_sci_txt; global u_soc_txt; global u_eng_txt
global u_phy_txt; global u_bio_txt; global u_chem_txt; global u_art_txt; global u_chinese_txt

total_score = IntVar()
total_grade = DoubleVar()
total_unit = IntVar()


def about():
    about_tp = Toplevel(main)
    about_tp.title('About')
    about_tp.geometry('400x400')

    Label(about_tp, text = "Kittipod \"Ton\" Lambangchang").place(x = 120, y = 20)

def insert():
    title = title_cbb.get()
    name = name_ent.get()
    surname = surname_ent.get()
    number = number_ent.get()
    section = class_cbb.get()
    total_name = title+ ' ' + name + ' ' + surname

    thai_sc = thai_ent.get()
    math_sc = math_ent.get()
    sci_sc = sci_ent.get()
    soc_sc = soc_ent.get()
    eng_sc = eng_ent.get()
    phy_sc = phy_ent.get()
    bio_sc = bio_ent.get()
    chem_sc = chem_ent.get()
    art_sc = art_ent.get()
    chinese_sc = chinese_ent.get()

    thai_unit = u_math_ent.get()
    math_unit = u_math_ent.get()
    sci_unit = u_sci_ent.get()
    soc_unit = u_soc_ent.get()
    eng_unit = u_eng_ent.get()
    phy_unit = u_phy_ent.get()
    bio_unit = u_bio_ent.get()
    chem_unit = u_chem_ent.get()
    art_unit = u_art_ent.get()
    chinese_unit = u_chinese_ent.get()

    if (int(thai_sc) >= 80 and int(thai_sc) <= 100):
        thai_gd = '4.00'
    elif (int(thai_sc) >= 75 and int(thai_sc) < 80):
        thai_gd = '3.50'
    elif (int(thai_sc) >= 70 and int(thai_sc) < 75):
        thai_gd = '3.00'
    elif (int(thai_sc) >= 65 and int(thai_sc) < 70):
        thai_gd = '2.50'
    elif (int(thai_sc) >= 60 and int(thai_sc) < 65):
        thai_gd = '2.00'
    elif (int(thai_sc) >= 55 and int(thai_sc) < 60):
        thai_gd = '1.50'
    elif (int(thai_sc) >= 50 and int(thai_sc) < 55):
        thai_gd = '1.00'
    else:
        thai_gd = '0.00'

    if (int(math_sc) >= 80 and int(math_sc) <= 100):
        math_gd = '4.00'
    elif (int(math_sc) >= 75 and int(math_sc) < 80):
        math_gd = '3.50'
    elif (int(math_sc) >= 70 and int(math_sc) < 75):
        math_gd = '3.00'
    elif (int(math_sc) >= 65 and int(math_sc) < 70):
        math_gd = '2.50'
    elif (int(math_sc) >= 60 and int(math_sc) < 65):
        math_gd = '2.00'
    elif (int(math_sc) >= 55 and int(math_sc) < 60):
        math_gd = '1.50'
    elif (int(math_sc) >= 50 and int(math_sc) < 55):
        math_gd = '1.00'
    else:
        math_gd = '0.00'

    if (int(sci_sc) >= 80 and int(sci_sc) <= 100):
        sci_gd = '4.00'
    elif (int(sci_sc) >= 75 and int(sci_sc) < 80):
        sci_gd = '3.50'
    elif (int(sci_sc) >= 70 and int(sci_sc) < 75):
        sci_gd = '3.00'
    elif (int(sci_sc) >= 65 and int(sci_sc) < 70):
        sci_gd = '2.50'
    elif (int(sci_sc) >= 60 and int(sci_sc) < 65):
        sci_gd = '2.00'
    elif (int(sci_sc) >= 55 and int(sci_sc) < 60):
        sci_gd = '1.50'
    elif (int(sci_sc) >= 50 and int(sci_sc) < 55):
        sci_gd = '1.00'
    else:
        sci_gd = '0.00'

    if (int(soc_sc) >= 80 and int(soc_sc) <= 100):
        soc_gd = '4.00'
    elif (int(soc_sc) >= 75 and int(soc_sc) < 80):
        soc_gd = '3.50'
    elif (int(soc_sc) >= 70 and int(soc_sc) < 75):
        soc_gd = '3.00'
    elif (int(soc_sc) >= 65 and int(soc_sc) < 70):
        soc_gd = '2.50'
    elif (int(soc_sc) >= 60 and int(soc_sc) < 65):
        soc_gd = '2.00'
    elif (int(soc_sc) >= 55 and int(soc_sc) < 60):
        soc_gd = '1.50'
    elif (int(soc_sc) >= 50 and int(soc_sc) < 55):
        soc_gd = '1.00'
    else:
        soc_gd = '0.00'

    if (int(eng_sc) >= 80 and int(eng_sc) <= 100):
        eng_gd = '4.00'
    elif (int(eng_sc) >= 75 and int(eng_sc) < 80):
        eng_gd = '3.50'
    elif (int(eng_sc) >= 70 and int(eng_sc) < 75):
        eng_gd = '3.00'
    elif (int(eng_sc) >= 65 and int(eng_sc) < 70):
        eng_gd = '2.50'
    elif (int(eng_sc) >= 60 and int(eng_sc) < 65):
        eng_gd = '2.00'
    elif (int(eng_sc) >= 55 and int(eng_sc) < 60):
        eng_gd = '1.50'
    elif (int(eng_sc) >= 50 and int(eng_sc) < 55):
        eng_gd = '1.00'
    else:
        eng_gd = '0.00'
    
    if (int(phy_sc) >= 80 and int(phy_sc) <= 100):
        phy_gd = '4.00'
    elif (int(phy_sc) >= 75 and int(phy_sc) < 80):
        phy_gd = '3.50'
    elif (int(phy_sc) >= 70 and int(phy_sc) < 75):
        phy_gd = '3.00'
    elif (int(phy_sc) >= 65 and int(phy_sc) < 70):
        phy_gd = '2.50'
    elif (int(phy_sc) >= 60 and int(phy_sc) < 65):
        phy_gd = '2.00'
    elif (int(phy_sc) >= 55 and int(phy_sc) < 60):
        phy_gd = '1.50'
    elif (int(phy_sc) >= 50 and int(phy_sc) < 55):
        phy_gd = '1.00'
    else:
        phy_gd = '0.00'

    if (int(bio_sc) >= 80 and int(bio_sc) <= 100):
        bio_gd = '4.00'
    elif (int(bio_sc) >= 75 and int(bio_sc) < 80):
        bio_gd = '3.50'
    elif (int(bio_sc) >= 70 and int(bio_sc) < 75):
        bio_gd = '3.00'
    elif (int(bio_sc) >= 65 and int(bio_sc) < 70):
        bio_gd = '2.50'
    elif (int(bio_sc) >= 60 and int(bio_sc) < 65):
        bio_gd = '2.00'
    elif (int(bio_sc) >= 55 and int(bio_sc) < 60):
        bio_gd = '1.50'
    elif (int(bio_sc) >= 50 and int(bio_sc) < 55):
        bio_gd = '1.00'
    else:
        bio_gd = '0.00'

    if (int(chem_sc) >= 80 and int(chem_sc) <= 100):
        chem_gd = '4.00'
    elif (int(chem_sc) >= 75 and int(chem_sc) < 80):
        chem_gd = '3.50'
    elif (int(chem_sc) >= 70 and int(chem_sc) < 75):
        chem_gd = '3.00'
    elif (int(chem_sc) >= 65 and int(chem_sc) < 70):
        chem_gd = '2.50'
    elif (int(chem_sc) >= 60 and int(chem_sc) < 65):
        chem_gd = '2.00'
    elif (int(chem_sc) >= 55 and int(chem_sc) < 60):
        chem_gd = '1.50'
    elif (int(chem_sc) >= 50 and int(chem_sc) < 55):
        chem_gd = '1.00'
    else:
        chem_gd = '0.00'
    
    if (int(art_sc) >= 80 and int(art_sc) <= 100):
        art_gd = '4.00'
    elif (int(art_sc) >= 75 and int(art_sc) < 80):
        art_gd = '3.50'
    elif (int(art_sc) >= 70 and int(art_sc) < 75):
        art_gd = '3.00'
    elif (int(art_sc) >= 65 and int(art_sc) < 70):
        art_gd = '2.50'
    elif (int(art_sc) >= 60 and int(art_sc) < 65):
        art_gd = '2.00'
    elif (int(art_sc) >= 55 and int(art_sc) < 60):
        art_gd = '1.50'
    elif (int(art_sc) >= 50 and int(art_sc) < 55):
        art_gd = '1.00'
    else:
        art_gd = '0.00'
    
    if (int(chinese_sc) >= 80 and int(chinese_sc) <= 100):
        chinese_gd = '4.00'
    elif (int(chinese_sc) >= 75 and int(chinese_sc) < 80):
        chinese_gd = '3.50'
    elif (int(chinese_sc) >= 70 and int(chinese_sc) < 75):
        chinese_gd = '3.00'
    elif (int(chinese_sc) >= 65 and int(chinese_sc) < 70):
        chinese_gd = '2.50'
    elif (int(chinese_sc) >= 60 and int(chinese_sc) < 65):
        chinese_gd = '2.00'
    elif (int(chinese_sc) >= 55 and int(chinese_sc) < 60):
        chinese_gd = '1.50'
    elif (int(chinese_sc) >= 50 and int(chinese_sc) < 55):
        chinese_gd = '1.00'
    else:
        chinese_gd = '0.00'

    total_sc = int(thai_sc) + int(math_sc) + int(sci_sc) + int(soc_sc) + int(eng_sc) + int(phy_sc) + int(bio_sc) + int(chem_sc) + int(art_sc) + int(chinese_sc)
    
    total_un = int(thai_unit) + int(math_unit) + int(sci_unit) + int(soc_unit) + int(eng_unit) + int(phy_unit) + int(bio_unit) + int(chem_unit) + int(art_unit) + int(chinese_unit)

    tot_sc_un = (float(math_gd) * int(math_unit)) + (float(thai_gd) * int(thai_unit)) + (float(sci_gd) * int(sci_unit)) + (float(soc_gd) * int(soc_unit)) + (float(eng_gd) * int(eng_unit)) + (float(phy_gd) * int(phy_unit)) + (float(bio_gd) * int(bio_unit)) + (float(chem_gd) * int(chem_unit)) + (float(art_gd) * int(art_unit)) + (float(chinese_gd) * int(chinese_unit))

    tot_grade = '{:.2f}'.format(tot_sc_un / total_un)

    if ((title_cbb.get() == '') or (name_ent.get() == '') or (surname_ent.get() == '') or (class_cbb.get() == '') or (number_ent.get() == '') or 
        (thai_ent.get() == '') or (math_ent.get() == '') or (sci_ent.get() == '') or (soc_ent.get() == '') or (eng_ent.get() == '') or 
        (phy_ent.get() == '') or (bio_ent.get() == '') or (chem_ent.get() == '') or (art_ent.get() == '') or (chinese_ent.get() == '') or 
        (u_thai_ent.get() == '') or (u_math_ent.get() == '') or (u_sci_ent.get() == '') or (u_soc_ent.get() == '') or (u_eng_ent.get() == '') or 
        (u_phy_ent.get() == '') or (u_bio_ent.get() == '') or (u_chem_ent.get() == '') or (u_art_ent.get() == '') or (u_chinese_ent.get() == '')):
        messagebox.showinfo('Insert Status', 'All field are empty.')
        clear()

    else:
        if (class_cbb.get() == 'M.6/1'):
            con = mysql.connect(host = "localhost", user = "root",password = "12345678", database="grade_project")
            cursor = con.cursor()
            cursor.execute("insert into score_table values ('"+ title +"', '"+ name +"', '"+ surname +"', '"+ section +"', '"+ number +"', '"+ total_name +"', '"+ tot_grade +"', '"+ str(total_sc) +"', '"+ thai_sc +"', '"+ math_sc +"', '"+ sci_sc +"', '"+ soc_sc +"', '"+ eng_sc +"', '"+ phy_sc +"', '"+ chem_sc +"', '"+ bio_sc +"', '"+ art_sc +"', '"+ chinese_sc +"')")
            cursor.execute('commit')
            clear()
            messagebox.showinfo('Insert Status', 'Inserted Successfully')
            con.close()
        
        elif (class_cbb.get() == 'M.6/2'):
            con = mysql.connect(host = "localhost", user = "root",password = "12345678", database="grade_project")
            cursor = con.cursor()
            cursor.execute("insert into score_table_62 values ('"+ title +"', '"+ name +"', '"+ surname +"', '"+ section +"', '"+ number +"', '"+ total_name +"', '"+ tot_grade +"', '"+ str(total_sc) +"', '"+ thai_sc +"', '"+ math_sc +"', '"+ sci_sc +"', '"+ soc_sc +"', '"+ eng_sc +"', '"+ phy_sc +"', '"+ chem_sc +"', '"+ bio_sc +"', '"+ art_sc +"', '"+ chinese_sc +"')")
            cursor.execute('commit')
            clear()
            messagebox.showinfo('Insert Status', 'Inserted Successfully')
            con.close()
        
        elif (class_cbb.get() == 'M.6/3'):
            con = mysql.connect(host = "localhost", user = "root",password = "12345678", database="grade_project")
            cursor = con.cursor()
            cursor.execute("insert into score_table_63 values ('"+ title +"', '"+ name +"', '"+ surname +"', '"+ section +"', '"+ number +"', '"+ total_name +"', '"+ tot_grade +"', '"+ str(total_sc) +"', '"+ thai_sc +"', '"+ math_sc +"', '"+ sci_sc +"', '"+ soc_sc +"', '"+ eng_sc +"', '"+ phy_sc +"', '"+ chem_sc +"', '"+ bio_sc +"', '"+ art_sc +"', '"+ chinese_sc +"')")
            cursor.execute('commit')
            clear()
            messagebox.showinfo('Insert Status', 'Inserted Successfully')
            con.close()

        else:
            con = mysql.connect(host = "localhost", user = "root",password = "12345678", database="grade_project")
            cursor = con.cursor()
            cursor.execute("insert into score_table_64 values ('"+ title +"', '"+ name +"', '"+ surname +"', '"+ section +"', '"+ number +"', '"+ total_name +"', '"+ tot_grade +"', '"+ str(total_sc) +"', '"+ thai_sc +"', '"+ math_sc +"', '"+ sci_sc +"', '"+ soc_sc +"', '"+ eng_sc +"', '"+ phy_sc +"', '"+ chem_sc +"', '"+ bio_sc +"', '"+ art_sc +"', '"+ chinese_sc +"')")
            cursor.execute('commit')
            clear()
            messagebox.showinfo('Insert Status', 'Inserted Successfully')
            con.close()

def clear():
    title_cbb.set('')
    name_ent.delete(0,'end')
    surname_ent.delete(0,'end')
    number_ent.delete(0,'end')
    class_cbb.set('')

    thai_ent.delete(0,'end')
    math_ent.delete(0,'end')
    sci_ent.delete(0,'end')
    soc_ent.delete(0,'end')
    eng_ent.delete(0,'end')
    phy_ent.delete(0,'end')
    bio_ent.delete(0,'end')
    chem_ent.delete(0,'end')
    art_ent.delete(0,'end')
    chinese_ent.delete(0,'end')

    '''u_thai_ent.delete(0,'end')
    u_math_ent.delete(0,'end')
    u_sci_ent.delete(0,'end')
    u_soc_ent.delete(0,'end')
    u_eng_ent.delete(0,'end')
    u_phy_ent.delete(0,'end')
    u_chem_ent.delete(0,'end')
    u_bio_ent.delete(0,'end')
    u_art_ent.delete(0,'end')
    u_chinese_ent.delete(0,'end')'''

def delete():
    if(number_ent.get() == '' or class_cbb.get() == ''):
        messagebox.showinfo('Delete Status', 'Number is compolsara for delete')
        clear()

    else:
        if (class_cbb == 'M.6/1'):
            con = mysql.connect(host = "localhost", user = "root",password = "12345678", database="grade_project")
            cursor = con.cursor()
            cursor.execute("delete from score_table where number = '"+ number_ent.get() +"'")
            cursor.execute('commit')
            clear()
            messagebox.showinfo('Delete Status', 'Delete Successfully')
            con.close()
        elif (class_cbb.get() == 'M.6/2'):
            con = mysql.connect(host = "localhost", user = "root",password = "12345678", database="grade_project")
            cursor = con.cursor()
            cursor.execute("delete from score_table_62 where number = '"+ number_ent.get() +"'")
            cursor.execute('commit')
            clear()
            messagebox.showinfo('Delete Status', 'Delete Successfully')
            con.close()

        elif (class_cbb.get() == 'M.6/3'):
            con = mysql.connect(host = "localhost", user = "root",password = "12345678", database="grade_project")
            cursor = con.cursor()
            cursor.execute("delete from score_table_63 where number = '"+ number_ent.get() +"'")
            cursor.execute('commit')
            clear()
            messagebox.showinfo('Delete Status', 'Delete Successfully')
            con.close()

        else:
            con = mysql.connect(host = "localhost", user = "root",password = "12345678", database="grade_project")
            cursor = con.cursor()
            cursor.execute("delete from score_table_64 where number = '"+ number_ent.get() +"'")
            cursor.execute('commit')
            clear()
            messagebox.showinfo('Delete Status', 'Delete Successfully')
            con.close()

def update():
    title = title_cbb.get()
    name = name_ent.get()
    surname = surname_ent.get()
    number = number_ent.get()
    section = class_cbb.get()
    total_name = title+ ' ' + name + ' ' + surname

    thai_sc = thai_ent.get()
    math_sc = math_ent.get()
    sci_sc = sci_ent.get()
    soc_sc = soc_ent.get()
    eng_sc = eng_ent.get()
    phy_sc = phy_ent.get()
    bio_sc = bio_ent.get()
    chem_sc = chem_ent.get()
    art_sc = art_ent.get()
    chinese_sc = chinese_ent.get()

    thai_unit = u_math_ent.get()
    math_unit = u_math_ent.get()
    sci_unit = u_sci_ent.get()
    soc_unit = u_soc_ent.get()
    eng_unit = u_eng_ent.get()
    phy_unit = u_phy_ent.get()
    bio_unit = u_bio_ent.get()
    chem_unit = u_chem_ent.get()
    art_unit = u_art_ent.get()
    chinese_unit = u_chinese_ent.get()

    if (int(thai_sc) >= 80 and int(thai_sc) <= 100):
        thai_gd = '4.00'
    elif (int(thai_sc) >= 75 and int(thai_sc) < 80):
        thai_gd = '3.50'
    elif (int(thai_sc) >= 70 and int(thai_sc) < 75):
        thai_gd = '3.00'
    elif (int(thai_sc) >= 65 and int(thai_sc) < 70):
        thai_gd = '2.50'
    elif (int(thai_sc) >= 60 and int(thai_sc) < 65):
        thai_gd = '2.00'
    elif (int(thai_sc) >= 55 and int(thai_sc) < 60):
        thai_gd = '1.50'
    elif (int(thai_sc) >= 50 and int(thai_sc) < 55):
        thai_gd = '1.00'
    else:
        thai_gd = '0.00'

    if (int(math_sc) >= 80 and int(math_sc) <= 100):
        math_gd = '4.00'
    elif (int(math_sc) >= 75 and int(math_sc) < 80):
        math_gd = '3.50'
    elif (int(math_sc) >= 70 and int(math_sc) < 75):
        math_gd = '3.00'
    elif (int(math_sc) >= 65 and int(math_sc) < 70):
        math_gd = '2.50'
    elif (int(math_sc) >= 60 and int(math_sc) < 65):
        math_gd = '2.00'
    elif (int(math_sc) >= 55 and int(math_sc) < 60):
        math_gd = '1.50'
    elif (int(math_sc) >= 50 and int(math_sc) < 55):
        math_gd = '1.00'
    else:
        math_gd = '0.00'

    if (int(sci_sc) >= 80 and int(sci_sc) <= 100):
        sci_gd = '4.00'
    elif (int(sci_sc) >= 75 and int(sci_sc) < 80):
        sci_gd = '3.50'
    elif (int(sci_sc) >= 70 and int(sci_sc) < 75):
        sci_gd = '3.00'
    elif (int(sci_sc) >= 65 and int(sci_sc) < 70):
        sci_gd = '2.50'
    elif (int(sci_sc) >= 60 and int(sci_sc) < 65):
        sci_gd = '2.00'
    elif (int(sci_sc) >= 55 and int(sci_sc) < 60):
        sci_gd = '1.50'
    elif (int(sci_sc) >= 50 and int(sci_sc) < 55):
        sci_gd = '1.00'
    else:
        sci_gd = '0.00'

    if (int(soc_sc) >= 80 and int(soc_sc) <= 100):
        soc_gd = '4.00'
    elif (int(soc_sc) >= 75 and int(soc_sc) < 80):
        soc_gd = '3.50'
    elif (int(soc_sc) >= 70 and int(soc_sc) < 75):
        soc_gd = '3.00'
    elif (int(soc_sc) >= 65 and int(soc_sc) < 70):
        soc_gd = '2.50'
    elif (int(soc_sc) >= 60 and int(soc_sc) < 65):
        soc_gd = '2.00'
    elif (int(soc_sc) >= 55 and int(soc_sc) < 60):
        soc_gd = '1.50'
    elif (int(soc_sc) >= 50 and int(soc_sc) < 55):
        soc_gd = '1.00'
    else:
        soc_gd = '0.00'

    if (int(eng_sc) >= 80 and int(eng_sc) <= 100):
        eng_gd = '4.00'
    elif (int(eng_sc) >= 75 and int(eng_sc) < 80):
        eng_gd = '3.50'
    elif (int(eng_sc) >= 70 and int(eng_sc) < 75):
        eng_gd = '3.00'
    elif (int(eng_sc) >= 65 and int(eng_sc) < 70):
        eng_gd = '2.50'
    elif (int(eng_sc) >= 60 and int(eng_sc) < 65):
        eng_gd = '2.00'
    elif (int(eng_sc) >= 55 and int(eng_sc) < 60):
        eng_gd = '1.50'
    elif (int(eng_sc) >= 50 and int(eng_sc) < 55):
        eng_gd = '1.00'
    else:
        eng_gd = '0.00'
    
    if (int(phy_sc) >= 80 and int(phy_sc) <= 100):
        phy_gd = '4.00'
    elif (int(phy_sc) >= 75 and int(phy_sc) < 80):
        phy_gd = '3.50'
    elif (int(phy_sc) >= 70 and int(phy_sc) < 75):
        phy_gd = '3.00'
    elif (int(phy_sc) >= 65 and int(phy_sc) < 70):
        phy_gd = '2.50'
    elif (int(phy_sc) >= 60 and int(phy_sc) < 65):
        phy_gd = '2.00'
    elif (int(phy_sc) >= 55 and int(phy_sc) < 60):
        phy_gd = '1.50'
    elif (int(phy_sc) >= 50 and int(phy_sc) < 55):
        phy_gd = '1.00'
    else:
        phy_gd = '0.00'

    if (int(bio_sc) >= 80 and int(bio_sc) <= 100):
        bio_gd = '4.00'
    elif (int(bio_sc) >= 75 and int(bio_sc) < 80):
        bio_gd = '3.50'
    elif (int(bio_sc) >= 70 and int(bio_sc) < 75):
        bio_gd = '3.00'
    elif (int(bio_sc) >= 65 and int(bio_sc) < 70):
        bio_gd = '2.50'
    elif (int(bio_sc) >= 60 and int(bio_sc) < 65):
        bio_gd = '2.00'
    elif (int(bio_sc) >= 55 and int(bio_sc) < 60):
        bio_gd = '1.50'
    elif (int(bio_sc) >= 50 and int(bio_sc) < 55):
        bio_gd = '1.00'
    else:
        bio_gd = '0.00'

    if (int(chem_sc) >= 80 and int(chem_sc) <= 100):
        chem_gd = '4.00'
    elif (int(chem_sc) >= 75 and int(chem_sc) < 80):
        chem_gd = '3.50'
    elif (int(chem_sc) >= 70 and int(chem_sc) < 75):
        chem_gd = '3.00'
    elif (int(chem_sc) >= 65 and int(chem_sc) < 70):
        chem_gd = '2.50'
    elif (int(chem_sc) >= 60 and int(chem_sc) < 65):
        chem_gd = '2.00'
    elif (int(chem_sc) >= 55 and int(chem_sc) < 60):
        chem_gd = '1.50'
    elif (int(chem_sc) >= 50 and int(chem_sc) < 55):
        chem_gd = '1.00'
    else:
        chem_gd = '0.00'
    
    if (int(art_sc) >= 80 and int(art_sc) <= 100):
        art_gd = '4.00'
    elif (int(art_sc) >= 75 and int(art_sc) < 80):
        art_gd = '3.50'
    elif (int(art_sc) >= 70 and int(art_sc) < 75):
        art_gd = '3.00'
    elif (int(art_sc) >= 65 and int(art_sc) < 70):
        art_gd = '2.50'
    elif (int(art_sc) >= 60 and int(art_sc) < 65):
        art_gd = '2.00'
    elif (int(art_sc) >= 55 and int(art_sc) < 60):
        art_gd = '1.50'
    elif (int(art_sc) >= 50 and int(art_sc) < 55):
        art_gd = '1.00'
    else:
        art_gd = '0.00'
    
    if (int(chinese_sc) >= 80 and int(chinese_sc) <= 100):
        chinese_gd = '4.00'
    elif (int(chinese_sc) >= 75 and int(chinese_sc) < 80):
        chinese_gd = '3.50'
    elif (int(chinese_sc) >= 70 and int(chinese_sc) < 75):
        chinese_gd = '3.00'
    elif (int(chinese_sc) >= 65 and int(chinese_sc) < 70):
        chinese_gd = '2.50'
    elif (int(chinese_sc) >= 60 and int(chinese_sc) < 65):
        chinese_gd = '2.00'
    elif (int(chinese_sc) >= 55 and int(chinese_sc) < 60):
        chinese_gd = '1.50'
    elif (int(chinese_sc) >= 50 and int(chinese_sc) < 55):
        chinese_gd = '1.00'
    else:
        chinese_gd = '0.00'

    total_sc = int(thai_sc) + int(math_sc) + int(sci_sc) + int(soc_sc) + int(eng_sc) + int(phy_sc) + int(bio_sc) + int(chem_sc) + int(art_sc) + int(chinese_sc)
    
    total_un = int(thai_unit) + int(math_unit) + int(sci_unit) + int(soc_unit) + int(eng_unit) + int(phy_unit) + int(bio_unit) + int(chem_unit) + int(art_unit) + int(chinese_unit)

    tot_sc_un = (float(math_gd) * int(math_unit)) + (float(thai_gd) * int(thai_unit)) + (float(sci_gd) * int(sci_unit)) + (float(soc_gd) * int(soc_unit)) + (float(eng_gd) * int(eng_unit)) + (float(phy_gd) * int(phy_unit)) + (float(bio_gd) * int(bio_unit)) + (float(chem_gd) * int(chem_unit)) + (float(art_gd) * int(art_unit)) + (float(chinese_gd) * int(chinese_unit))

    tot_grade = '{:.2f}'.format(tot_sc_un / total_un)

    if ((title_cbb.get() == '') or (name_ent.get() == '') or (surname_ent.get() == '') or (class_cbb.get() == '') or (number_ent.get() == '') or 
        (thai_ent.get() == '') or (math_ent.get() == '') or (sci_ent.get() == '') or (soc_ent.get() == '') or (eng_ent.get() == '') or 
        (phy_ent.get() == '') or (bio_ent.get() == '') or (chem_ent.get() == '') or (art_ent.get() == '') or (chinese_ent.get() == '') or 
        (u_thai_ent.get() == '') or (u_math_ent.get() == '') or (u_sci_ent.get() == '') or (u_soc_ent.get() == '') or (u_eng_ent.get() == '') or 
        (u_phy_ent.get() == '') or (u_bio_ent.get() == '') or (u_chem_ent.get() == '') or (u_art_ent.get() == '') or (u_chinese_ent.get() == '')):
        messagebox.showinfo('Update Status', 'All fields are empty.')
        clear()
        
    else:
        con = mysql.connect(host = "localhost", user = "root",password = "12345678", database="grade_project")
        cursor = con.cursor()
        cursor.execute("update score_table set title = '"+ title +"', name = '"+ name +"', surname = '"+ surname +"', section = '"+ section +"', total_name = '"+ total_name +"', grade = '"+ tot_grade +"', total_score = '"+ str(total_sc) +"', thai = '"+ thai_sc +"', math = '"+ math_sc +"', sci = '"+ sci_sc +"', soc = '"+ soc_sc +"', eng = '"+ eng_sc +"', phy = '"+ phy_sc +"', bio = '"+ bio_sc +"', chem = '"+ chem_sc +"', art = '"+ art_sc +"', chinese = '"+ chinese_sc +"' where number = '"+ number +"'")
        cursor.execute('commit')
        clear()
        messagebox.showinfo('Update Status', 'Update Successfully')
        con.close()

def show():
    con = mysql.connect(host = "localhost", user = "root",password = "12345678", database="grade_project")
    cursor = con.cursor()
    cursor.execute("select * from unit_grade")
    datas = cursor.fetchall()
    for data in datas:
        u_thai_txt.set(data[0])
        u_math_txt.set(data[1])
        u_sci_txt.set(data[2])
        u_soc_txt.set(data[3])
        u_eng_txt.set(data[4])
        u_phy_txt.set(data[5])
        u_bio_txt.set(data[6])
        u_chem_txt.set(data[7])
        u_art_txt.set(data[8])
        u_chinese_txt.set(data[9])

    con.close()

def unit():
    def set():
        if ((thai_e.get() == '') or (math_e.get() == '') or (sci_e.get() == '') or (soc_e.get() == '') or (eng_e.get() == '') or
            (phy_e.get() == '') or (bio_e.get() == '') or (chem_e.get() == '') or (art_e.get() == '') or (chinese_e.get() == '')):
            messagebox.showinfo('Set Unit Status', 'All fields are empty.')

        else:
            con = mysql.connect(host = "localhost", user = "root",password = "12345678", database="grade_project")
            cursor = con.cursor()
            cursor.execute("insert into unit_grade values ('"+ thai_e.get() +"', '"+ math_e.get() +"', '"+ sci_e.get() +"', '"+ soc_e.get() +"', '"+ eng_e.get() +"', '"+ phy_e.get() +"', '"+ bio_e.get() +"', '"+ chem_e.get() +"', '"+ art_e.get() +"', '"+ chinese_e.get() +"')")
            cursor.execute('commit')
            
            messagebox.showinfo('Set Unit Status', 'Set Unit Successfully')
            con.close()
            unit_tp.destroy()
    
    def update():
        if ((thai_e.get() == '') or (math_e.get() == '') or (sci_e.get() == '') or (soc_e.get() == '') or (eng_e.get() == '') or
            (phy_e.get() == '') or (bio_e.get() == '') or (chem_e.get() == '') or (art_e.get() == '') or (chinese_e.get() == '')):
            messagebox.showinfo('Update Unit Status', 'All fields are empty.')
            
        else:
            con = mysql.connect(host = "localhost", user = "root",password = "12345678", database="grade_project")
            cursor = con.cursor()
            cursor.execute('')
            con.close()
    
    unit_tp = Toplevel(main)
    unit_tp.title('Set Unit')
    unit_tp.geometry('700x300')
    
    thai_l = ttk.Label(unit_tp, text = 'Thai Unit :')
    thai_l.place(x = 10, y = 10)

    math_l = ttk.Label(unit_tp, text = 'Mathematic Unit :')
    math_l.place(x = 10, y = 50)

    sci_l = ttk.Label(unit_tp, text = 'Science Unit :')
    sci_l.place(x = 10, y = 90)

    soc_l = ttk.Label(unit_tp, text = 'Social Unit :')
    soc_l.place(x = 10, y = 130)

    eng_l = ttk.Label(unit_tp, text = 'English Unit :')
    eng_l.place(x = 10, y = 170)

    thai_t = StringVar()
    thai_e = ttk.Entry(unit_tp, textvariable = thai_t)
    thai_e.place(x = 130, y = 10)
    
    math_t = StringVar()
    math_e = ttk.Entry(unit_tp, textvariable = math_t)
    math_e.place(x = 130, y = 50)

    sci_t = StringVar()
    sci_e = ttk.Entry(unit_tp, textvariable = sci_t)
    sci_e.place(x = 130, y = 90)

    soc_t = StringVar()
    soc_e = ttk.Entry(unit_tp, textvariable = soc_t)
    soc_e.place(x = 130, y = 130)

    eng_t = StringVar()
    eng_e = ttk.Entry(unit_tp, textvariable = eng_t)
    eng_e.place(x = 130, y = 170)

    phy_l = ttk.Label(unit_tp, text = 'Physic Unit :')
    phy_l.place(x = 300, y = 10)

    bio_l = ttk.Label(unit_tp, text = 'Biology Unit :')
    bio_l.place(x = 300, y = 50)

    chem_l = ttk.Label(unit_tp, text = 'Chemistry Unit :')
    chem_l.place(x = 300, y = 90)

    art_l = ttk.Label(unit_tp, text = 'Art Unit :')
    art_l.place(x = 300, y = 130)

    chinese_l = ttk.Label(unit_tp, text = 'Chinese Unit :')
    chinese_l.place(x = 300, y = 170)

    phy_t = StringVar()
    phy_e = ttk.Entry(unit_tp, textvariable = phy_t)
    phy_e.place(x = 410, y = 10)

    bio_t = StringVar()
    bio_e = ttk.Entry(unit_tp, textvariable = bio_t)
    bio_e.place(x = 410, y = 50)

    chem_t = StringVar()
    chem_e = ttk.Entry(unit_tp, textvariable = chem_t)
    chem_e.place(x = 410, y = 90)

    art_t = StringVar()
    art_e = ttk.Entry(unit_tp, textvariable = art_t)
    art_e.place(x = 410, y = 130)

    chinese_t = StringVar()
    chinese_e = ttk.Entry(unit_tp, textvariable = chinese_t)
    chinese_e.place(x = 410, y = 170)

    set_unit_btn = ttk.Button(unit_tp, text = 'Set', command = set)
    set_unit_btn.place(x = 550, y = 10, width = 130, height = 50)

    update_unit_btn = ttk.Button(unit_tp, text = 'Update',command = "")
    update_unit_btn.place(x = 550, y = 70, width = 130, height = 50)
    
menubar = Menu(main)
edit_menu = Menu(menubar, tearoff = 0)
edit_menu.add_command(label = "Insert")
edit_menu.add_command(label = "Delete")
edit_menu.add_command(label = "Update")
edit_menu.add_command(label = "Clear", command = clear)
edit_menu.add_separator()
edit_menu.add_command(label = 'Unit', command = unit)
menubar.add_cascade(label = "Edit", menu = edit_menu)

table_menu = Menu(menubar, tearoff = 0)
table_menu.add_command(label = 'Matthayom 6/1')
table_menu.add_command(label = 'Matthayom 6/2')
table_menu.add_command(label = 'Matthayom 6/3')
table_menu.add_command(label = 'Matthayom 6/4')
menubar.add_cascade(label = 'Table', menu = table_menu)

help_menu = Menu(menubar, tearoff = 0)
help_menu.add_command(label = "Help")
help_menu.add_command(label = "Short Key")
help_menu.add_separator()
help_menu.add_command(label = "About", command = about)
menubar.add_cascade(label = "Help", menu = help_menu)

title_lbl = ttk.Label(main, text = "Title name :")
title_lbl.place(x = 10, y = 10)

name_lbl = ttk.Label(main, text = 'Name :')
name_lbl.place(x = 10, y = 50)

surname_lbl = ttk.Label(main, text = 'Surname :')
surname_lbl.place(x = 10, y = 90)

number_lbl = ttk.Label(main, text = "number :")
number_lbl.place(x = 10, y = 130)

class_lbl = ttk.Label(main, text = "Class :")
class_lbl.place(x = 10, y = 170)

title_name = ('Mr.', 'Ms.')
title_txt = StringVar()
title_cbb = ttk.Combobox(main, values = title_name, width = 7, textvariable = title_txt)
title_cbb.place(x = 90, y = 10)

name_txt = StringVar()
name_ent = ttk.Entry(main, textvariable = name_txt)
name_ent.place(x = 90, y = 50)

surname_txt = StringVar()
surname_ent = ttk.Entry(main, textvariable = surname_txt)
surname_ent.place(x = 90, y = 90)

number_txt = StringVar()
number_ent = ttk.Entry(main, textvariable = number_txt)
number_ent.place(x = 90, y = 130)

name_class = ('M.6/1', 'M.6/2', 'M.6/3', 'M.6/4')
class_txt = StringVar()
class_cbb = ttk.Combobox(main, values = name_class, width = 7, textvariable = class_txt)
class_cbb.place(x = 90, y = 170)

thai_lbl = ttk.Label(main, text = "Thai :")
thai_lbl.place(x = 280, y = 10)

math_lbl = ttk.Label(main, text = "Mathematics :")
math_lbl.place(x = 280, y = 50)

sci_lbl = ttk.Label(main, text = "Science :")
sci_lbl.place(x = 280, y = 90)

soc_lbl = ttk.Label(main, text = "Social :")
soc_lbl.place(x = 280, y = 130)

eng_lbl = ttk.Label(main, text = "English :")
eng_lbl.place(x = 280, y = 170)

phy_lbl = ttk.Label(main, text = "Physic :")
phy_lbl.place(x = 280, y = 210)

bio_lbl = ttk.Label(main, text = 'Biology :')
bio_lbl.place(x = 280, y = 250)

chem_lbl = ttk.Label(main, text = 'Chemistry :')
chem_lbl.place(x = 280, y = 290)

art_lbl = ttk.Label(main, text = 'Art :')
art_lbl.place(x = 280, y = 330)

chinese_lbl = ttk.Label(main, text = 'Chinese :')
chinese_lbl.place(x = 280, y = 370)

thai_txt = StringVar()
thai_ent = ttk.Entry(main, textvariable = thai_txt)
thai_ent.place(x = 380, y = 10)

math_txt = StringVar()
math_ent = ttk.Entry(main, textvariable = math_txt)
math_ent.place(x = 380, y = 50)

sci_txt = StringVar()
sci_ent = ttk.Entry(main, textvariable = sci_txt)
sci_ent.place(x = 380, y =90)

soc_txt = StringVar()
soc_ent = ttk.Entry(main, textvariable = soc_txt)
soc_ent.place(x = 380, y = 130)

eng_txt = StringVar()
eng_ent = ttk.Entry(main, textvariable = eng_txt)
eng_ent.place(x = 380, y = 170)

phy_txt = StringVar()
phy_ent = ttk.Entry(main, textvariable = phy_txt)
phy_ent.place(x = 380, y = 210)

bio_txt = StringVar()
bio_ent = ttk.Entry(main, textvariable = bio_txt)
bio_ent.place(x = 380, y = 250)

chem_txt = StringVar()
chem_ent = ttk.Entry(main, textvariable = chem_txt)
chem_ent.place(x = 380, y = 290)

art_txt = StringVar()
art_ent = ttk.Entry(main, textvariable = art_txt)
art_ent.place(x = 380, y = 330)

chinese_txt = StringVar()
chinese_ent = ttk.Entry(main, textvariable = chinese_txt)
chinese_ent.place(x = 380, y = 370)

u_thai_lbl = ttk.Label(main, text = 'Unit of Thai :')
u_thai_lbl.place(x = 590, y = 10)

u_math_lbl = ttk.Label(main, text = 'Unit of Mathematic :')
u_math_lbl.place(x = 590, y = 50)

u_sci_lbl = ttk.Label(main, text = 'Unit of Science :')
u_sci_lbl.place(x = 590, y = 90)

u_soc_lbl = ttk.Label(main, text = 'Unit of Social :')
u_soc_lbl.place(x = 590, y = 130)

u_eng_lbl = ttk.Label(main, text = 'Unit of English :')
u_eng_lbl.place(x = 590, y = 170)

u_phy_lbl = ttk.Label(main, text = 'Unit of Physic :')
u_phy_lbl.place(x = 590, y = 210)

u_bio_lbl = ttk.Label(main, text = 'Unit of Biology :')
u_bio_lbl.place(x = 590, y = 250)

u_chem_lbl = ttk.Label(main, text = 'Unit of Chemistry :')
u_chem_lbl.place(x = 590, y = 290)

u_art_lbl = ttk.Label(main, text = 'Unit of Art :')
u_art_lbl.place(x = 590, y = 330)

u_chinese_lbl = ttk.Label(main, text = 'Unit of Chinese :')
u_chinese_lbl.place(x = 590, y = 370)

u_thai_txt = StringVar()
u_thai_ent = ttk.Entry(main, textvariable = u_thai_txt)
u_thai_ent.place(x = 730, y = 10)

u_math_txt = StringVar()
u_math_ent = ttk.Entry(main, textvariable = u_math_txt)
u_math_ent.place(x = 730, y = 50)

u_sci_txt = StringVar()
u_sci_ent = ttk.Entry(main, textvariable = u_sci_txt)
u_sci_ent.place(x = 730, y = 90)

u_soc_txt = StringVar()
u_soc_ent = ttk.Entry(main, textvariable = u_soc_txt)
u_soc_ent.place(x = 730, y = 130)

u_eng_txt = StringVar()
u_eng_ent = ttk.Entry(main, textvariable = u_eng_txt)
u_eng_ent.place(x = 730, y = 170)

u_phy_txt = StringVar()
u_phy_ent = ttk.Entry(main, textvariable = u_phy_txt)
u_phy_ent.place(x = 730, y = 210)

u_bio_txt = StringVar()
u_bio_ent = ttk.Entry(main, textvariable = u_bio_txt)
u_bio_ent.place(x = 730, y = 250)

u_chem_txt = StringVar()
u_chem_ent = ttk.Entry(main, textvariable = u_chem_txt)
u_chem_ent.place(x = 730, y = 290)

u_art_txt = StringVar()
u_art_ent = ttk.Entry(main, textvariable = u_art_txt)
u_art_ent.place(x = 730, y = 330)

u_chinese_txt = StringVar()
u_chinese_ent = ttk.Entry(main, textvariable = u_chinese_txt)
u_chinese_ent.place(x = 730, y = 370)

insert_btn = ttk.Button(main, text = "Insert", command = insert)
insert_btn.place(x = 880, y = 10, width = 120, height = 80)

update_btn = ttk.Button(main, text = "Update",command = update)
update_btn.place(x = 880, y = 110, width = 120, height = 80)

delete_btn = ttk.Button(main, text = 'Delete', command = delete)
delete_btn.place(x = 880, y = 210, width = 120, height = 80)

clear_btn = ttk.Button(main, text = 'Clear', command = clear)
clear_btn.place(x = 880, y = 310, width = 120, height = 80)

ntb = ttk.Notebook(main,width =1000,height = 300)

m61_frm = ttk.Frame(ntb)
m62_frm = ttk.Frame(ntb)
m63_frm = ttk.Frame(ntb)
m64_frm = ttk.Frame(ntb)

ntb.add(m61_frm, text = 'Matthayom 6/1')
ntb.add(m62_frm, text = 'Matthayom 6/2')
ntb.add(m63_frm, text = 'Matthayom 6/3')
ntb.add(m64_frm, text = 'Matthayom 6/4')
ntb.place(x = 10,y =410)

cols = ('Number','Name-Surname', "Section", "Total Score", "Grade", 'Thai', "Math", "Science", "Social", "English", "Physic", "Biology", "Chemistry", "Art", "Chinese")
listBox = ttk.Treeview(m61_frm, show = 'headings', columns = cols)
listBox_2 = ttk.Treeview(m62_frm, show = 'headings', columns = cols)
listBox_3 = ttk.Treeview(m63_frm, show = 'headings', columns = cols)
listBox_4 = ttk.Treeview(m64_frm, show = 'headings', columns = cols)

for col in cols:
    listBox.heading(col, text = col)
    listBox_2.heading(col, text = col)
    listBox_3.heading(col, text = col)
    listBox_4.heading(col, text = col)

    listBox.column('Number', width = 100)
    listBox.column('Name-Surname',width = 160)
    listBox.column('Section',width = 100)
    listBox.column('Total Score',width = 100)
    listBox.column('Grade',width = 100)
    listBox.column('Thai',width = 100)
    listBox.column('Math',width = 100)
    listBox.column('Science',width = 100)
    listBox.column('Social',width = 100)
    listBox.column('English',width = 100)
    listBox.column('Physic',width = 100)
    listBox.column('Biology',width = 100)
    listBox.column('Chemistry',width = 100)
    listBox.column('Art',width = 100)
    listBox.column('Chinese',width = 120)

    listBox_2.column('Number', width = 100)
    listBox_2.column('Name-Surname',width = 160)
    listBox_2.column('Section',width = 100)
    listBox_2.column('Total Score',width = 100)
    listBox_2.column('Grade',width = 100)
    listBox_2.column('Thai',width = 100)
    listBox_2.column('Math',width = 100)
    listBox_2.column('Science',width = 100)
    listBox_2.column('Social',width = 100)
    listBox_2.column('English',width = 100)
    listBox_2.column('Physic',width = 100)
    listBox_2.column('Biology',width = 100)
    listBox_2.column('Chemistry',width = 100)
    listBox_2.column('Art',width = 100)
    listBox_2.column('Chinese',width = 120)

    listBox_3.column('Number', width = 100)
    listBox_3.column('Name-Surname',width = 160)
    listBox_3.column('Section',width = 100)
    listBox_3.column('Total Score',width = 100)
    listBox_3.column('Grade',width = 100)
    listBox_3.column('Thai',width = 100)
    listBox_3.column('Math',width = 100)
    listBox_3.column('Science',width = 100)
    listBox_3.column('Social',width = 100)
    listBox_3.column('English',width = 100)
    listBox_3.column('Physic',width = 100)
    listBox_3.column('Biology',width = 100)
    listBox_3.column('Chemistry',width = 100)
    listBox_3.column('Art',width = 100)
    listBox_3.column('Chinese',width = 120)

    listBox_4.column('Number', width = 100)
    listBox_4.column('Name-Surname',width = 160)
    listBox_4.column('Section',width = 100)
    listBox_4.column('Total Score',width = 100)
    listBox_4.column('Grade',width = 100)
    listBox_4.column('Thai',width = 100)
    listBox_4.column('Math',width = 100)
    listBox_4.column('Science',width = 100)
    listBox_4.column('Social',width = 100)
    listBox_4.column('English',width = 100)
    listBox_4.column('Physic',width = 100)
    listBox_4.column('Biology',width = 100)
    listBox_4.column('Chemistry',width = 100)
    listBox_4.column('Art',width = 100)
    listBox_4.column('Chinese',width = 120)

    listBox.grid(row = 1, column = 0, columnspan = 2)
    listBox_2.grid(row = 1, column = 0, columnspan = 2)
    listBox_3.grid(row = 1, column = 0, columnspan = 2)
    listBox_4.grid(row = 1, column = 0, columnspan = 2)

    listBox.place(x = 0, y = 0, height = 300, width = 1000)
    listBox_2.place(x = 0, y = 0, height = 300, width = 1000)
    listBox_3.place(x = 0, y = 0, height = 300, width = 1000)
    listBox_4.place(x = 0, y = 0, height = 300, width = 1000)

listBox_v_scb = ttk.Scrollbar(m61_frm, orient = "vertical", command = listBox.yview)
listBox_v_scb.pack(side = 'right', fill = 'y')
listBox.configure(yscrollcommand = listBox_v_scb.set)

listBox_2_v_scb = ttk.Scrollbar(m62_frm, orient = "vertical", command = listBox_2.yview)
listBox_2_v_scb.pack(side = 'right', fill = 'y')
listBox_2.configure(yscrollcommand = listBox_2_v_scb.set)

listBox_3_v_scb = ttk.Scrollbar(m63_frm, orient = "vertical", command = listBox_3.yview)
listBox_3_v_scb.pack(side = 'right', fill = 'y')
listBox_3.configure(yscrollcommand = listBox_3_v_scb.set)

listBox_4_v_scb = ttk.Scrollbar(m64_frm, orient = "vertical", command = listBox_4.yview)
listBox_4_v_scb.pack(side = 'right', fill = 'y')
listBox_4.configure(yscrollcommand = listBox_4_v_scb.set)

listBox_h_scb = ttk.Scrollbar(m61_frm, orient = 'horizontal', command = listBox.xview)
listBox_h_scb.pack(side = 'bottom', fill = 'x')
listBox.configure(xscrollcommand = listBox_h_scb.set)

listBox_2_h_scb = ttk.Scrollbar(m62_frm, orient = 'horizontal', command = listBox_2.xview)
listBox_2_h_scb.pack(side = 'bottom', fill = 'x')
listBox_2.configure(xscrollcommand = listBox_2_h_scb.set)

listBox_3_h_scb = ttk.Scrollbar(m63_frm, orient = 'horizontal', command = listBox_3.xview)
listBox_3_h_scb.pack(side = 'bottom', fill = 'x')
listBox_3.configure(xscrollcommand = listBox_3_h_scb.set)

listBox_4_h_scb = ttk.Scrollbar(m64_frm, orient = 'horizontal', command = listBox_4.xview)
listBox_4_h_scb.pack(side = 'bottom', fill = 'x')
listBox_4.configure(xscrollcommand = listBox_4_h_scb.set)

# test treeview and scrollbar work
'''test_value = ('Kittipod','M63','4','4','4','4','4','4','4','4',"4","4","45",'3.44')
for i in range(20):
    listBox.insert('','end',values = test_value)'''

name_total_score_lbl = ttk.Label(main, text = "Total Score :")
name_total_score_lbl.place(x = 10, y = 250)

name_total_unit_lbl = ttk.Label(main, text = "Total Unit :")
name_total_unit_lbl.place(x = 10, y = 310)

name_total_grade_lbl = ttk.Label(main, text = "Grade :")
name_total_grade_lbl.place(x = 10, y = 370)

total_score_lbl = ttk.Label(main, textvariable = total_score)
total_score_lbl.place(x = 100, y = 250)

total_unti_lbl = ttk.Label(main, textvariable = total_unit)
total_unti_lbl.place(x = 100, y = 310)

total_grade_lbl = ttk.Label(main, textvariable = total_grade)
total_grade_lbl.place(x = 100, y = 370)

u_thai_ent.config(state = 'disabled')
u_math_ent.config(state = 'disabled')
u_sci_ent.config(state = 'disabled')
u_soc_ent.config(state = 'disabled')
u_eng_ent.config(state = 'disabled')
u_phy_ent.config(state = 'disabled')
u_bio_ent.config(state = 'disabled')
u_chem_ent.config(state = 'disabled')
u_art_ent.config(state = 'disabled')
u_chinese_ent.config(state = 'disabled')

main.config(menu = menubar)
show()
main.mainloop()
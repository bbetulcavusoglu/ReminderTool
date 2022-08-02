from cProfile import label
from cgitb import text
from doctest import master
from msilib.schema import RadioButton
from tkinter import *
from tkinter.filedialog import asksaveasfile
from tracemalloc import start
from turtle import bgcolor, width
from pkg_resources import EntryPoint
from tkcalendar import DateEntry
import time


#PART-1
master= Tk()
master.title("Reminder Tool")
canvas = Canvas(master, width="800", height="500")
canvas.pack()

frame_ust= Frame(master, bg="#1c8dff")
frame_ust.place(relx=0, rely=0, relheight=0.25, relwidth=1)

frame_alt_sol= Frame(master, bg="#1c8dff")
frame_alt_sol.place(relx=0, rely=0.26, relheight=1, relwidth=0.70)

frame_alt_sag= Frame(master, bg="#1c8dff")
frame_alt_sag.place(relx=0.709, rely=0.26, relheight=1, relwidth=0.3)

hatirlatma_tipi_etiketi= Label(frame_ust, bg="#1c8dff", text="Hatırlatma Tipi: ", font="Verdana 12 bold")
hatirlatma_tipi_etiketi.pack(padx=10, pady=10, side=LEFT)

hatirlatma_tipi_secici= StringVar(frame_ust)
hatirlatma_tipi_secici.set("\t")

hatirlatma_tipi_menu= OptionMenu(
    frame_ust,
    hatirlatma_tipi_secici,
    "Dogum Gunu",
    "Alısveris",
    "Odeme",
    )
hatirlatma_tipi_menu.pack(padx=10, pady=10, side=LEFT)

##
hatirlatma_tarihi_secici=DateEntry(frame_ust,selectmode='day')
hatirlatma_tarihi_secici.pack(padx=20, pady=10, side=RIGHT)

r = IntVar()
pm_label= Radiobutton(frame_ust, text="PM", variable=r, value=2, bg="#1c8dff")
pm_label.pack(padx=2, pady=10, side=RIGHT)

am_label= Radiobutton(frame_ust, text="AM", variable=r, value=1, bg="#1c8dff")
am_label.pack(padx=2, pady=10, side=RIGHT)


second_input = Entry(frame_ust, width=2)
second_input.pack(padx=2, pady=10, side=RIGHT)

clon= Label(frame_ust, text=":", bg="#1c8dff")
clon.pack(padx=2, pady=10, side=RIGHT)

minute_input = Entry(frame_ust, width=2)
minute_input.pack(padx=2, pady=10, side=RIGHT)

clon= Label(frame_ust, text=":", bg="#1c8dff")
clon.pack(padx=2, pady=10, side=RIGHT)


hour_input = Entry(frame_ust, width=2)
hour_input.pack(padx=2, pady=10, side=RIGHT)



hatirlatma_tarihi_etiketi= Label(frame_ust, bg="#1c8dff",  text="Hatırlatma Tarihi: ", font="Verdana 12 bold")
hatirlatma_tarihi_etiketi.pack(padx=10, pady=10, side=RIGHT)


#PART-3

from tkinter import messagebox

def gonder():
    son_mesaj=""
    try:       
        if r.get():

                son_mesaj += "Mesaj Başarıyla sisteme kaydedildi"

                
                if hatirlatma_tipi_secici.get()=="Dogum Gunu":
                    tip="Dogum Gunu" 
                elif hatirlatma_tipi_secici.get()=="Alısveris":
                    tip="Alısveris" 
                elif hatirlatma_tipi_secici.get()=="Odeme":
                    tip="Odeme" 
                elif hatirlatma_tipi_secici.get()==" ":
                  tip="Genel"
                tarih=hatirlatma_tarihi_secici.get()
                mesaj=metin_alani.get("1.0", "end")
                saat=hour_input.get()
                dakika=minute_input.get()
                saniye=second_input.get()
                
                dosya=open("liste.txt","a")
                dosya.write(
                        '\n{} kategorisinde - {} - saat: {}:{}:{} tarihine:\n->{}\n'.format(
                            tip,
                            tarih,
                            saat,
                            dakika,
                            saniye,
                            mesaj
                        )
                    )
              
                dosya.close()

                
        else:
            son_mesaj += "Gerekli alanların doldurulduğundan emin olun"
            messagebox.showwarning("Yetersiz Bilgi", son_mesaj)
     
            
    except:
        son_mesaj += "İşlem Başarısız Oldu"
        messagebox.showerror("Başarısız İşlem", son_mesaj) 
        
    finally:
        master.destroy()

def dosya_ac():
    dosya = open("liste.txt", "r")
    stuff= dosya.read()

    not_alani.insert(END, stuff)
    dosya.close()

Label(frame_alt_sol, text="Hatırlatma Mesajı:", bg="#1c8dff",  font="Verdana 12 bold").pack(padx=10, pady=10, anchor=NW)


metin_alani=Text(frame_alt_sol, height=10, width=50)
metin_alani.tag_configure("style", foreground="gray", font="Verdana 7 bold")
metin_alani.pack()


karsilama_metni= "Mesajinizi buraya girin..."
metin_alani.insert(END, karsilama_metni, "style")

gonder_butonu = Button(frame_alt_sol, text="Gönder", command=gonder)
gonder_butonu.pack(anchor=S)

notlar = Button(frame_alt_sag, text="    notlar   ", command=dosya_ac)
notlar.pack(anchor=S) 

not_alani=Text(frame_alt_sag, height=50, width=27)
not_alani.tag_configure("style", foreground="gray", font="Verdana 7 bold")
not_alani.pack()


master.mainloop()




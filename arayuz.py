from tkinter import *  # ara yüz yapmak için genelde kullanılan bir kütüphane  # Tutorialspoint incele  
from tkcalendar import dateentry
master = Tk()   # Ana arayüz


canvas =Canvas(master,height=450 , width=750 ) # ara yzümüzün boyutlanırmasını yaptığımız alan önemli!!!
canvas.pack()
#pack
#grid
#place bunlar ara yüzümüze bir şeyler eklemek istediğimiz de kullandığımız komutlar

# Frame  ara yüz içerisinde yapıları yapabilmemiz için kullanmamız gerek frame yapısan geçtikten sonra master yerine frame yazabilirzi fraameler kendi içerisinde
# ana rolu oynayabiliyorlar
frame_ust = Frame(master,bg='#add8e6') 
frame_ust.place(relx=0.1,rely=0.1,relwidth=0.8,  relheight=0.1)           
frame_alt_sol = Frame(master,bg='#add8e6')
frame_alt_sol.place(relx=0.1,rely=0.21,relwidth=0.23,  relheight=0.5)
frame_alt_sag = Frame(master,bg='#add8e6')
frame_alt_sag.place(relx=0.34,rely=0.21,relwidth=0.56,  relheight=0.5 )

hatirlatma_tipi_etiket =Label(frame_ust,bg='#add8e6', text="Hatırlatma Tipi:", font='verdana 12 bold')
hatirlatma_tipi_etiket.pack(padx=10, pady=10, side=LEFT)

hatirlatma_tipi_opsisyonel = StringVar(frame_ust)
hatirlatma_tipi_opsisyonel.set("\t")

hatirlatma_tipi_acilir_menu = OptionMenu(frame_ust, hatirlatma_tipi_opsisyonel,"Dogun günü","Alışveriş","Ödeme")
hatirlatma_tipi_acilir_menu.pack(padx=10,pady=10,side=LEFT)

hatirlatma_tarih_secici = dateentry.DateEntry(frame_ust, width=12, background='orange', foreground='black', borderwidth=1)
hatirlatma_tarih_secici.pack(padx=10, pady=10, side=RIGHT)
hatirlatma_tarih_secici._top_cal.overrideredirect(False)

hatirlatma_tipi_etiket =Label(frame_ust,bg='#add8e6', text="Hatırlatma Tarihi:", font='verdana 12 bold')
hatirlatma_tipi_etiket.pack(padx=10, pady=10, side=RIGHT )



print(master.mainloop())         
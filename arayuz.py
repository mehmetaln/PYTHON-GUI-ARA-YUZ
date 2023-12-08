from tkinter import *  # ara yüz yapmak için genelde kullanılan bir kütüphane  # Tutorialspoint incele  
from tkcalendar import dateentry
master = Tk()   # Ana arayüz

# padx = x yörüngesinde konum belrtmek için kullandıgım terim yatay
# pady= y yörüngesinde konum belirtmek için kullandığım terim dikey
# side = padx ve pady ile belirlediğim konumdaki tam bölgemi bulmama yardımcı olan terim
canvas =Canvas(master,height=450 , width=750 ) # ara yzümüzün boyutlanırmasını yaptığımız alan önemli!!!
canvas.pack()
#pack
#grid
#place bunlar ara yüzümüze bir şeyler eklemek istediğimiz de kullandığımız komutlar
# Frame  ara yüz içerisinde yapıları yapabilmemiz için kullanmamız gerek frame yapısan geçtikten sonra master yerine frame yazabilirzi fraameler kendi içerisinde
# ana rolu oynayabiliyorlar
##########################################################################3 UP SİDE START ###########################################################################
frame_ust = Frame(master,bg='#add8e6')
frame_ust.place(relx=0.1,rely=0.1,relwidth=0.8,  relheight=0.1)           
frame_alt_sol = Frame(master,bg='#add8e6')
frame_alt_sol.place(relx=0.1,rely=0.21,relwidth=0.23,  relheight=0.5)
frame_alt_sag = Frame(master,bg='#add8e6')
frame_alt_sag.place(relx=0.34,rely=0.21,relwidth=0.56,  relheight=0.5 )

hatirlatma_tipi_etiket =Label(frame_ust,bg='#add8e6', text="Hatırlatma Tipi:", font='verdana 12 bold')
hatirlatma_tipi_etiket.pack(padx=10, pady=10, side=LEFT)

hatirlatma_tipi_opsiyonel = StringVar(frame_ust) #StringVar sınıfı, kullanıcı arayüzü öğeleri (örneğin, etiketler, düğmeler,
#giriş kutuları) gibi arayüzdeki metinleri dinamik olarak güncellemek ve takip etmek için kullanılır.
hatirlatma_tipi_opsiyonel.set("\t")

hatirlatma_tipi_acilir_menu = OptionMenu(frame_ust, hatirlatma_tipi_opsiyonel,"Dogun günü","Alışveriş","Ödeme") # secenekli Menu menü için OptionMenu methodunu kullanırız
hatirlatma_tipi_acilir_menu.pack(padx=10,pady=10,side=LEFT)
hatirlatma_tarih_secici = dateentry.DateEntry(frame_ust, width=12, background='orange', foreground='black', borderwidth=1)
# DateEntry", Tkinter kütüphanesinde bulunan bir kontrol öğesidir ve kullanıcının bir tarih seçmesini sağlar. 
hatirlatma_tarih_secici.pack(padx=10, pady=10, side=RIGHT)
hatirlatma_tarih_secici._top_cal.overrideredirect(False)
#
#overrideredirect metodu, Tkinter kütüphanesindeki Tk sınıfına ait bir metottur. Bu metot, bir pencerenin pencere yöneticisi (window manager) 
#tarafından yönetilip yönetilmeyeceğini belirlemek için kullanılır. Genellikle bu metot, pencereyi özel bir şekilde oluşturmak ve özelleştirmek amacıyla kullanılır.

hatirlatma_tipi_etiket =Label(frame_ust,bg='#add8e6', text="Hatırlatma Tarihi:", font='verdana 12 bold')
#label kullanıcı ara yüzünde bir etiket oluşturmak için kullanılan method  = "Label" kelimesi, bir kullanıcı arayüzünde metin veya resim gibi bilgileri 
#göstermek için kullanılan bir kontrol öğesini ifade eder. genelde metin için kullanılır

hatirlatma_tipi_etiket.pack(padx=10, pady=10, side=RIGHT )
##########################################################################3 UP SİDE END ###########################################################################
##########################################################################3 UNDER SİDE START ###########################################################################

Label(frame_alt_sol, text="Hatırlatma Yöntemi:  ",bg='#add8e6', font='verdana 10 bold').pack(padx=10, pady=10,anchor=NW) # anchor bir pusula görevi gösteriri nereye yaslamamız gerektiğini söyler

var = IntVar()
R1 = Radiobutton(frame_alt_sol,text="Sisteme Kaydet",variable=var,value=1,bg="#add8e6",font="verdana 10")
R1.pack(anchor=NW,pady=5,padx=15)
R2 = Radiobutton(frame_alt_sol,text="E-postaya Kaydet",variable=var,value=2,bg="#add8e6",font="verdana 10")
R2.pack(anchor=NW,pady=5,padx=15)


var1 = IntVar()
c1 = Checkbutton(frame_alt_sol,text="Bir Hafta Önce", variable=var1, onvalue=1, offvalue=0, bg="#add8e6",font="verdana 10")
c1.pack(anchor=NW,pady=5,padx=25)
c2 = Checkbutton(frame_alt_sol,text="Bir Gün Önce", variable=var1, onvalue=1    , offvalue=0, bg="#add8e6",font="verdana 10")
c2.pack(anchor=NW,pady=5,padx=25)
c3 = Checkbutton(frame_alt_sol,text="Aynı gün", variable=var1, onvalue=1, offvalue=0, bg="#add8e6",font="verdana 10")
c3.pack(anchor=NW,pady=5,padx=25)




Label(frame_alt_sag, text="Hatırlatma Mesajı  ",bg='#add8e6', font='verdana 10 bold').pack(padx=10, pady=10,anchor=NW) # anchor bir pusula görevi gösteriri nereye yaslamamız gerektiğini söyler

metin_alani = Text(frame_alt_sag,height=9 ,width=50)
metin_alani.tag_configure('style',foreground='#bfbfbf',font=('Verdana',9,'bold')) # özellik vermke için kullandığız yer
metin_alani.pack()
karsilasma_metni = "Mesajını buraya gir..."
metin_alani.insert(END,karsilasma_metni,'style')





############3 UNDER SİDE END ###########################################################################






print(master.mainloop())         
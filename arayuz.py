from tkinter import *  # ara yüz yapmak için genelde kullanılan bir kütüphane  # Tutorialspoint incele  

master = Tk()   # Ana arayüz


canvas =Canvas(master,height=450 , width=750 ) # ara yzümüzün boyutlanırmasını yaptığımız alan önemli!!!
#pack
#grid
#place bunlar ara yüzümüze bir şeyler eklemek istediğimiz de kullandığımız komutlar
print(canvas.pack())

# print(master.mainloop()) 
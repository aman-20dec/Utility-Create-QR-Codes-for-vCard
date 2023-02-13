from os import path
from tkinter import *
import qrcode
from PIL import Image, ImageTk


qr_img = ""

def generate_QR():
    global qr_img
    
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=3, 
        border=1,
    )
    qr.add_data(create_vCard())
    # qr_code = qrcode.make(create_vCard())

    img = qr.make_image(fill_color="black", back_color="white")
   
    img.save("qr1.png")
 
    qr_img = PhotoImage(file="qr1.png") 
    canvas.itemconfigure(img_container, image=qr_img)

    # qr_lbl.config(image=qr_img, width= 200, height= 200)
    

   


def create_vCard():
    first_name = fname_txt.get()
    last_name = lname_txt.get()
    phone = phone_txt.get()
    email = email_txt.get()

    str_vCard = f'''BEGIN:VCARD
VERSION:3.0
PRODID:-//Apple Inc.//macOS 11.6.8//EN
N:{last_name};{first_name};;;
FN:{first_name} {last_name}
EMAIL;type=INTERNET;type=HOME;type=pref:{email}
TEL;type=IPHONE;type=CELL;type=VOICE;type=pref:{phone}
ADR;type=HOME;type=pref:;;HeerStraße;Berlin;Berlin;14055;Germany
NOTE:This is a Test vCard
END:VCARD'''
    return str_vCard

    filename = f"{first_name} {last_name}.vcf"

    with open(filename, mode="w") as file:
        file.write(str_vCard)





##################### GUI ########################


window = Tk()
window.title("QR Code Generator") 
# window.minsize(width=300, height=300)
window.config(padx=50, pady=50)

qr_img = PhotoImage(file="qr.png")





###########Row 0###############
fname_lbl = Label(text="Please Enter Contact Card Info.", font=("Arial", 15, "bold"))
fname_lbl.grid(column=0, row=0, ipady=20)



###########Row 1###############
fname_lbl = Label(text="First Name:")
fname_lbl.grid(column=0, row=1)

fname_txt = Entry(width=20)
fname_txt.grid(column=1, row=1, columnspan=2)
fname_txt.focus()
###########Row 2###############
lname_lbl = Label(text="Last Name")
lname_lbl.grid(column=0, row=2)

lname_txt = Entry(width=20)
lname_txt.grid(column=1, row=2, columnspan=2)



###########Row 3###############
email_lbl = Label(text="Email")
email_lbl.grid(column=0, row=3)

email_txt = Entry(width=20)
email_txt.grid(column=1, row=3 )
email_txt.insert(0, "abc@gmail.com")

###########Row 4###############
phone_lbl = Label(text="Phone")
phone_lbl.grid(column=0, row=4)

phone_txt = Entry(width=20)
phone_txt.grid(column=1, row=4 )

###########Row 5###############
vcard_lbl = Label()
vcard_lbl.grid(column=0, row=5)

# vcard_lbl['text'] = 


###########Row 6###############
generate_pass_btn = Button(text="Generate QR", width=13, command= generate_QR)
generate_pass_btn.grid(column=1, row=6)


###########Row 7###############
canvas = Canvas(width= 200, height= 200, bg="#FFFBEB")

# colors - light yellow - #FFFBEB , light gray #E8E2E2

txt_container = canvas.create_text(100, 100, text='No QR Code\nAvailable', font=('Arial', 15), justify= 'center')
img_container = canvas.create_image(103,103)
canvas.grid(column=1, row=7)



###Working QR label
# qr_lbl = Label( text= 'No QR\nAvailable', font=('Arial', 15), bg="green", width= 25, height= 8)
# qr_lbl.grid(column=1, row=7)




window.mainloop()




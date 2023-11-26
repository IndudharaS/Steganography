import cv2
import os
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox


img_path_encrypt = ""
secret_message = ""
password = ""
c = {}  
d={}
img=""



def encrypt():
    global img_path_encrypt,secret_message,password,c,d,img
    window.destroy()
    encrypt_window()

def decrypt():
    global img_path_encrypt,secret_message,password,c,d,img
    window.destroy()
    decrypt_window()

def back_to_home():
    global img_path_encrypt,secret_message,password,c,d,img
    main_screen()

def encrypt_window():
    global img_path_encrypt,secret_message,password,c,d,img
    def select_image():
        global img_path_encrypt,secret_message,password,c,d
        folder_path = filedialog.askdirectory(title="Select Folder")
        img_path_encrypt = filedialog.askopenfilename(title="Select Image", initialdir=folder_path,
                                                       filetypes=[("Image files", "*.jpg;*.jpeg;*.png")])
        entry_selected_image.delete(0, END)
        entry_selected_image.insert(0, img_path_encrypt)

    def encrypt_message():
        global img_path_encrypt,secret_message,password,c,d,img
        img_path = img_path_encrypt
        img = cv2.imread(img_path)

        secret_message = entry_message.get()
        password = entry_password.get()

        if not c:  
            for i in range(255):
                d[chr(i)]=i
                c[i] = chr(i)

        m = 0
        n = 0
        z = 0

        for i in range(len(secret_message)):
            img[n, m, z] = d[secret_message[i]]
            n = n + 1
            m = m + 1
            z = (z + 1) % 3

        output_path = os.path.join(os.path.dirname(img_path), "Encrypted.jpg")
        cv2.imwrite(output_path, img)
        messagebox.showinfo("Encryption", "Image encrypted and saved as 'Encrypted.jpg'")
        

    encrypt_window = Tk()
    encrypt_window.title("Steganography - Encrypt")
    encrypt_window.geometry("500x400")

    label_heading = Label(encrypt_window, text="Steganography - Encrypt", font=("Helvetica", 16), pady=10)
    label_heading.pack()

    label_select_image = Label(encrypt_window, text="Select Image:", font=("Helvetica", 12))
    label_select_image.pack(pady=5)

    entry_selected_image = Entry(encrypt_window, width=30)
    entry_selected_image.pack(pady=5)

    btn_select_image = Button(encrypt_window, text="Browse", command=select_image)
    btn_select_image.pack(pady=5)

    label_message = Label(encrypt_window, text="Enter secret message:", font=("Helvetica", 12))
    label_message.pack(pady=5)

    entry_message = Entry(encrypt_window, width=30)
    entry_message.pack(pady=5)

    label_password = Label(encrypt_window, text="Enter password:", font=("Helvetica", 12))
    label_password.pack(pady=5)

    entry_password = Entry(encrypt_window, show="*", width=30)
    entry_password.pack(pady=5)

    btn_encrypt = Button(encrypt_window, text="Encrypt", command=encrypt_message)
    btn_encrypt.pack(pady=10)

    btn_back = Button(encrypt_window, text="Back to Home", command=back_to_home)
    btn_back.pack(pady=10)

    encrypt_window.mainloop()

def decrypt_window():
    global img_path_encrypt,secret_message,password,c,d,img
    def select_image_decrypt():
        global img_path_encrypt,secret_message,password,c,d,img
        folder_path = filedialog.askdirectory(title="Select Folder")
        img_path_decrypt = filedialog.askopenfilename(title="Select Encrypted Image", initialdir=folder_path,
                                                       filetypes=[("Image files", "*.jpg;*.jpeg;*.png")])
        entry_selected_image_decrypt.delete(0, END)
        entry_selected_image_decrypt.insert(0, img_path_decrypt)

    def decrypt_message():
        global img_path_encrypt,secret_message,password,c,d,img
        

        entered_password = entry_decryption_password.get()
        decrypted_message = ""

        n = 0
        m = 0
        z = 0

        if password == entered_password:
            for i in range(len(secret_message)):
                decrypted_message = decrypted_message + c[img[n, m, z]]
                DecryptMsg = decrypted_message
                n = n + 1
                m = m + 1
                z = (z + 1) % 3
            print(DecryptMsg)
            entry_decrypted_message.delete(1.0, END)
            entry_decrypted_message.insert(END, decrypted_message)
        else:
            entry_decrypted_message.delete(1.0, END)
            entry_decrypted_message.insert(END, "Invalid Password")

    decrypt_window = Tk()
    decrypt_window.title("Steganography - Decrypt")
    decrypt_window.geometry("500x400")

    label_heading = Label(decrypt_window, text="Steganography - Decrypt", font=("Helvetica", 16), pady=10)
    label_heading.pack()

    label_select_image = Label(decrypt_window, text="Select Encrypted Image:", font=("Helvetica", 12))
    label_select_image.pack(pady=5)

    entry_selected_image_decrypt = Entry(decrypt_window, width=30)
    entry_selected_image_decrypt.pack(pady=5)

    btn_select_image_decrypt = Button(decrypt_window, text="Browse", command=select_image_decrypt)
    btn_select_image_decrypt.pack(pady=5)

    label_decryption_password = Label(decrypt_window, text="Enter password for Decryption:", font=("Helvetica", 12))
    label_decryption_password.pack(pady=5)

    entry_decryption_password = Entry(decrypt_window, show="*", width=30)
    entry_decryption_password.pack(pady=5)

    btn_decrypt = Button(decrypt_window, text="Decrypt", command=decrypt_message)
    btn_decrypt.pack(pady=10)

    label_decrypted_message = Label(decrypt_window, text="Decrypted Message:", font=("Helvetica", 12))
    label_decrypted_message.pack(pady=5)

    entry_decrypted_message = Text(decrypt_window, height=5, width=30)
    entry_decrypted_message.pack(pady=5)

    btn_back = Button(decrypt_window, text="Back to Home", command=back_to_home)
    btn_back.pack(pady=10)

    decrypt_window.mainloop()

def main_screen():
    global window
    window = Tk()
    window.title("Steganography")
    window.geometry("300x200")

    label_heading = Label(window, text="Steganography", font=("Helvetica", 16), pady=20)
    label_heading.pack()

    btn_encrypt = Button(window, text="Encrypt", command=encrypt, width=20, height=2)
    btn_encrypt.pack(pady=10)

    btn_decrypt = Button(window, text="Decrypt", command=decrypt, width=20, height=2)
    btn_decrypt.pack(pady=10)

    window.mainloop()

main_screen()

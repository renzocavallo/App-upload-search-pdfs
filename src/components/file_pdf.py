from tkinter import Tk
from tkinter import Label
from tkinter import Entry
from src.components.card import Card
from src.components.bton import Bton
from src.components.btons_properties import bton_save_edit_p, bton_quit_p
from tkinter.messagebox import askyesno
from tkinter.messagebox import showinfo
import os
from os import system, rename
from shutil import move
from config.model_controller import delete_by_id, get_all_files, edit_file, get_file_by_id

class File_pdf():

    def __init__(self, root, file, i, j):   
        
        def click_bton(file_pdf):

            system(file_pdf[2])
        
        def click_delete():

            if askyesno("Eliminar Archivo", file[1]):
                showinfo("Si", "Archivo Eliminado") 

                for widget in root.winfo_children():
                    widget.destroy()
            
                move(file[2], './remove')
                delete_by_id(file[0])
                files = get_all_files()

                row = 0
                column= 0

                for i in range(len(files)):

                    File_pdf( root, files[i] , row , column)
                    column += 1

                    if column == 3:
                        row += 1
                        column = 0

        def click_edit():

            window = Tk()
            window.title("Editar PDF")
            window.geometry("250x250")
            window.config(bg="#E3E1EB")
            title_label = Label(window, text="Título :", bg="#E3E1EB", fg="#FA534A")
            title_label.pack()
            title_entry = Entry(window, width=30)
            title_entry.insert(0, file[1])
            title_entry.pack()
            creation_label = Label(window, text="Fecha de creación :", bg="#E3E1EB", fg="#FA534A")
            creation_label.pack()
            creation_entry = Entry(window)
            creation_entry.insert(0, file[4])
            creation_entry.pack()

            Bton(window, bton_save_edit_p, lambda : click_save_edit(title_entry, creation_entry, window))
  
            Bton(window, bton_quit_p, window.destroy) 

            window.mainloop()

        def click_save_edit(title, creation, window):     

            if askyesno("Confirmar Edición", 
                "Desea confirmar la edición ? " + 
                "\n" + title.get() + 
                "\n" + creation.get()):

                showinfo("Si", "Archivo Editado") 

                rename('./files/'+file[1], './files/'+ title.get())
                new_path = f"{os.path.abspath(os.getcwd())}"+"\\files\\" +  title.get().split("/").pop()
                edit_file(file[0], title.get(), new_path, creation.get())

                for widget in root.winfo_children():
                    widget.destroy()
                
                file_edit = get_file_by_id(file[0])
                print("file_edit----->", file_edit[0])
                Card(root, i , j, file_edit[0], lambda: click_bton(file_edit[0]), click_delete, click_edit)

                window.destroy()

            else:

                window.destroy()

        self.card = Card(root, i, j, file, lambda: click_bton(file) , click_delete, click_edit)
        self.card.get_card()
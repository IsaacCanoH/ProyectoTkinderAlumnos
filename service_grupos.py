import tkinter as tk
from tkinter import messagebox as mb
from database import grupos


def agregar_grupo(txt_cveGru, txt_nomGru):
    cveGru = txt_cveGru.get()
    nomGru = txt_nomGru.get()

    if cveGru == "" or nomGru == "":
        mb.showwarning("Campos vacíos", "Debes llenar todos los campos")
        return

    try:
        grupos.insert_one({
            "_id": cveGru,
            "cveGru": cveGru,
            "nomGru": nomGru
        })

        mb.showinfo("Éxito", "Grupo agregado correctamente")

        txt_cveGru.delete(0, tk.END)
        txt_nomGru.delete(0, tk.END)
        txt_cveGru.focus()

    except Exception as e:
        mb.showerror("Error", f"Ocurrió un error:\n{e}")


def modificar_grupo(txt_cveGru, txt_nomGru):
    cveGru = txt_cveGru.get().strip()
    nuevo_nomGru = txt_nomGru.get().strip()

    if cveGru == "" or nuevo_nomGru == "":
        mb.showwarning("Campos vacíos", "Debes llenar todos los campos")
        return

    try:
        resultado = grupos.update_one(
            {"cveGru": cveGru},
            {"$set": {"nomGru": nuevo_nomGru}}
        )

        if resultado.matched_count == 0:
            mb.showwarning("No encontrado", "No existe un grupo con esa clave")
            return

        mb.showinfo("Éxito", "Grupo actualizado correctamente")

        txt_cveGru.delete(0, tk.END)
        txt_nomGru.delete(0, tk.END)
        txt_cveGru.focus()

    except Exception as e:
        mb.showerror("Error", f"Ocurrió un error:\n{e}")


def eliminar_grupos():
    try:
        grupos.delete_many({})
        mb.showinfo("Éxito", "Grupos eliminados correctamente")
    except Exception as e:
        mb.showerror("Error", f"Ocurrió un error:\n{e}")

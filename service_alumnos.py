import tkinter as tk
from tkinter import messagebox as mb
from database import alumnos

def abrir_ventana_resultado(resultado):
    # Crea una nueva ventana secundaria
    ventana_emergente = tk.Toplevel()
    ventana_emergente.title("Resultado")
    ventana_emergente.geometry("250x150")
    ventana_emergente.resizable(0,0)
    ventana_emergente.config(cursor="hand2")

    datos = resultado[0]
    
    # Añade widgets a la ventana emergente

    lbl_CveGru=tk.Label(ventana_emergente,text=f"Clave de Grupo: {datos['cveGru']}",font=("Arial",11))
    lbl_CveGru.grid(row=1,column=0)

    lbl_NomGru=tk.Label(ventana_emergente,text=f"Nombre de Grupo: {datos['nomGru']}",font=("Arial",11))
    lbl_NomGru.grid(row=2,column=0)
    
    boton_cerrar = tk.Button(ventana_emergente, text="Cerrar", command=ventana_emergente.destroy)

def agregar_alumno(txt_cveAlu, txt_nomAlu, txt_edaAlu, txt_cveGru):
    cveAlu = txt_cveAlu.get().strip()
    nomAlu = txt_nomAlu.get().strip()
    edaAlu = txt_edaAlu.get().strip()
    cveGru = txt_cveGru.get().strip()

    if cveAlu == "" or nomAlu == "" or edaAlu == "" or cveGru == "":
        mb.showwarning("Campos vacíos", "Debes llenar todos los campos")
        return

    try:
        alumnos.insert_one({
            "_id": cveAlu,
            "cveAlu": cveAlu,
            "nomAlu": nomAlu,
            "edaAlu": edaAlu,
            "cveGru": cveAlu
        })

        mb.showinfo("Éxito", "Alumno agregado correctamente")

        txt_cveAlu.delete(0, tk.END)
        txt_nomAlu.delete(0, tk.END)
        txt_edaAlu.delete(0, tk.END)
        txt_cveGru.delete(0, tk.END)
        txt_cveAlu.focus()

    except Exception as e:
        mb.showerror("Error", f"Ocurrió un error:\n{e}")


def modificar_alumno(txt_cveAlu, txt_nomAlu, txt_edaAlu, txt_cveGru):
    cveAlu = txt_cveAlu.get().strip()
    nuevo_nomAlu = txt_nomAlu.get().strip()
    nuevo_edaAlu = txt_edaAlu.get().strip()
    nuevo_cveGru = txt_cveGru.get().strip()

    if cveAlu == "" or nuevo_nomAlu == "" or nuevo_edaAlu == "" or nuevo_cveGru == "":
        mb.showwarning("Campos vacíos", "Debes llenar todos los campos")
        return

    try:
        resultado = alumnos.update_one(
            {"cveAlu": cveAlu},
            {   "$set": {
                    "nomGru": nuevo_nomAlu,
                    "edaAlu": nuevo_edaAlu,
                    "cveGru": nuevo_cveGru,
                }
            }
        )

        if resultado.matched_count == 0:
            mb.showwarning("No encontrado", "No existe un alumno con esa clave")
            return

        mb.showinfo("Éxito", "Alumno actualizado correctamente")

        txt_cveAlu.delete(0, tk.END)
        txt_nomAlu.delete(0, tk.END)
        txt_edaAlu.delete(0, tk.END)
        txt_cveGru.delete(0, tk.END)
        txt_cveAlu.focus()

    except Exception as e:
        mb.showerror("Error", f"Ocurrió un error:\n{e}")

def eliminar_grupo(txt_cveGru, txt_nomGru):
    cveGru = txt_cveGru.get().strip()
    nomGru = txt_nomGru.get().strip()

    query = {}
    if cveGru:
        query = {"cveGru": cveGru}
    elif nomGru:
        query = {"nomGru": nomGru}

    if not query:
        mb.showwarning("Atención", "Ingresa la Clave o Nombre del grupo que desee Eliminar.")
        return

    try:
        resultado = alumnos.delete_one(query)
        
        if resultado.deleted_count > 0:
            mb.showinfo("Eliminado", f"Se eliminó el Grupo correctamente.")
            limpiar(txt_cveGru, txt_nomGru)
        else:
            mb.showerror("Error", "¡No se encontró el Grupo para Eliminar!")
            
    except Exception as e:
        mb.showerror("Error", f"Error al intentar eliminar en la base de datos:\n{e}")
       
def limpiar(txt_cveGru,txt_nomGru):
    txt_cveGru.delete(0, tk.END)
    txt_nomGru.delete(0, tk.END)
        
def buscar_grupo(txt_cveGru, txt_nomGru):
    cveGru = txt_cveGru.get().strip()
    nomGru = txt_nomGru.get().strip()
    
    query = {}
    if cveGru:
        query = {"cveGru": cveGru}
    elif nomGru:
        query = {"nomGru": nomGru}
    
    if not query:
        mb.showwarning("Campo vacío", "Ingresa Clave o Nombre para Buscar")
        return

    try:
        resultado = list(alumnos.find(query, {"_id": 0}))
        
        if resultado:
            abrir_ventana_resultado(resultado)
        else:
            mb.showwarning("Sin éxito", "No se encontraron coincidencias")
            
    except Exception as e:
        mb.showerror("Error", f"Falló la conexión o búsqueda en la base de datos:\n{e}")


def eliminar_alumnos():
    try:
        alumnos.delete_many({})
        mb.showinfo("Éxito", "Alumnos eliminados correctamente")
    except Exception as e:
        mb.showerror("Error", f"Ocurrió un error:\n{e}")
        


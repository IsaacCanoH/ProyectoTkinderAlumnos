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

    lbl_CveGru=tk.Label(ventana_emergente,text=f"Clave de Alumno: {datos['cveAlu']}",font=("Arial",11))
    lbl_CveGru.grid(row=1,column=0)

    lbl_NomGru=tk.Label(ventana_emergente,text=f"Nombre de Alumno: {datos['nomAlu']}",font=("Arial",11))
    lbl_NomGru.grid(row=2,column=0)
    
    lbl_NomGru=tk.Label(ventana_emergente,text=f"Edad de Alumno: {datos['edaAlu']}",font=("Arial",11))
    lbl_NomGru.grid(row=3,column=0)

    lbl_NomGru=tk.Label(ventana_emergente,text=f"Clave de Grupo: {datos['cveGru']}",font=("Arial",11))
    lbl_NomGru.grid(row=4,column=0)
    
    boton_cerrar = tk.Button(ventana_emergente, text="Cerrar", command=ventana_emergente.destroy)
    boton_cerrar.grid(row=5, column=0, pady=10)

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
                    "nomAlu": nuevo_nomAlu,
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

def eliminar_alumno(txt_cveAlu, txt_nomAlu, txt_edaAlu, txt_cveGru):
    cveAlu = txt_cveAlu.get().strip()
    nomAlu = txt_nomAlu.get().strip()

    query = {}
    if cveAlu:
        query = {"cveAlu": cveAlu}
    elif nomAlu:
        query = {"nomAlu": nomAlu}

    if not query:
        mb.showwarning("Atención", "Ingresa la Clave o Nombre del alumno que desee Eliminar.")
        return

    try:
        resultado = alumnos.delete_one(query)
        
        if resultado.deleted_count > 0:
            mb.showinfo("Eliminado", f"Se eliminó el Alumno correctamente.")
            limpiar(txt_cveAlu, txt_nomAlu, txt_edaAlu, txt_cveGru)
        else:
            mb.showerror("Error", "¡No se encontró el Alumno para Eliminar!")
            
    except Exception as e:
        mb.showerror("Error", f"Error al intentar eliminar en la base de datos:\n{e}")
       
def limpiar(txt_cveAlu,txt_nomAlu,txt_edaAlu,txt_cveGru):
    txt_cveAlu.delete(0, tk.END)
    txt_nomAlu.delete(0, tk.END)
    txt_edaAlu.delete(0, tk.END)
    txt_cveGru.delete(0, tk.END)
        
def buscar_alumno(txt_cveAlu, txt_nomAlu):
    cveAlu = txt_cveAlu.get().strip()
    nomAlu = txt_nomAlu.get().strip()
    
    query = {}
    if cveAlu:
        query = {"cveAlu": cveAlu}
    elif nomAlu:
        query = {"nomAlu": nomAlu}
    
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
        


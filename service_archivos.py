from tkinter import messagebox as mb, filedialog as fd
import subprocess as sp


def crear_backup():
    ruta = fd.askdirectory(
        title="Selecciona la carpeta donde guardar el backup"
    )

    if not ruta:
        return

    try:
        comando = [
            "mongodump",
            "--db=BD_GrupoAlumno",
            "--collection=Grupo",
            f"--out={ruta}"
        ]
        sp.run(comando, check=True)
        mb.showinfo("Exito", "Backup realizado con correctamente")
    except Exception as e:
        mb.showerror("Error", f"Ocurrio un error:\n{e}")
        
def restaurar_backup():

    ruta = fd.askdirectory(
        title="Selecciona la carpeta del backup"
    )

    if not ruta:
        return

    try:

        comando = [
            "mongorestore",
            "--db=BD_GrupoAlumno",
            f"--dir={ruta}"
        ]

        sp.run(comando, check=True)

        mb.showinfo("Éxito", "Backup restaurado correctamente")

    except Exception as e:

        mb.showerror("Error", f"Ocurrió un error:\n{e}")


def exportar_json():
    ruta = fd.asksaveasfilename(
        title="Guardar JSON",
        defaultextension=".json",
        filetypes=[("Archivos JSON", "*.json")]
    )

    if not ruta:
        return

    try:
        comando = [
            "mongoexport",
            "--db=BD_GrupoAlumno",
            "--collection=Grupo",
            f"--out={ruta}"
        ]
        sp.run(comando, check=True)
        mb.showinfo("Exito", "Exportacion de JSON realizada correctamente")
    except Exception as e:
        mb.showerror("Error", f"Ocurrio un error:\n{e}")


def importar_json():
    ruta = fd.askopenfilename(
        title="Importar JSON",
        filetypes=[("Archivos JSON", "*.json")]
    )

    if not ruta:
        return

    try:
        comando = [
            "mongoimport",
            "--db=BD_GrupoAlumno",
            "--collection=Grupo",
            f"--file={ruta}"
        ]
        sp.run(comando, check=True)
        mb.showinfo("Exito", "Importacion de JSON realizada correctamente")
    except Exception as e:
        mb.showerror("Error", f"Ocurrio un error:\n{e}")


def exportar_csv():
    ruta = fd.asksaveasfilename(
        title="Guardar CSV",
        defaultextension=".csv",
        filetypes=[("Archivos CSV", "*.csv")]
    )

    if not ruta:
        return

    try:
        comando = [
            "mongoexport",
            "--db=BD_GrupoAlumno",
            "--collection=Grupo",
            "--type=CSV",
            "--fields=_id,cveGru,nomGru",
            f"--out={ruta}"
        ]
        sp.run(comando, check=True)
        mb.showinfo("Exito", "Exportacion de CSV realizada correctamente")
    except Exception as e:
        mb.showerror("Error", f"Ocurrio un error:\n{e}")


def importar_csv():
    ruta = fd.askopenfilename(
        title="Importar CSV",
        filetypes=[("Archivos CSV", "*.csv")]
    )

    if not ruta:
        return

    try:
        comando = [
            "mongoimport",
            "--db=BD_GrupoAlumno",
            "--collection=Grupo",
            "--type=CSV",
            f"--file={ruta}",
            "--headerline"
        ]
        sp.run(comando, check=True)
        mb.showinfo("Exito", "Importacion de CSV realizada correctamente")
    except Exception as e:
        mb.showerror("Error", f"Ocurrio un error:\n{e}")

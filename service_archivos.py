from tkinter import messagebox as mb, filedialog as fd
import subprocess as sp
import os
import json
import xml.etree.ElementTree as ET


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

def exportar_xml():
    ruta = fd.asksaveasfilename(
        title="Guardar XML",
        defaultextension=".xml",
        filetypes=[("Archivos XML", "*.xml")]
    )

    if not ruta:
        return
    
    temp_json = "temp_export.json"

    try:
        comando = [
            "mongoexport",
            "--db=BD_GrupoAlumno",
            "--collection=Grupo",
            "--type=json",
            "--fields=_id,cveGru,nomGru",
            f"--out={temp_json}"
        ]
        sp.run(comando, check=True)

        root = ET.Element("Grupos")
        
        with open(temp_json, "r", encoding="utf-8") as archivo_json:
            for linea in archivo_json:
                datos = json.loads(linea.strip())
                grupo_xml = ET.SubElement(root, "Grupo")

                ET.SubElement(grupo_xml, "_id").text = str(datos.get("_id", ""))
                ET.SubElement(grupo_xml, "cveGru").text = str(datos.get("cveGru", ""))
                ET.SubElement(grupo_xml, "nomGru").text = str(datos.get("nomGru", ""))

        tree = ET.ElementTree(root)
        tree.write(ruta, encoding="utf-8", xml_declaration=True)

        mb.showinfo("Éxito", "Exportación de XML realizada correctamente")

    except Exception as e:
        mb.showerror("Error", f"Ocurrió un error:\n{e}")
        
    finally:
        if os.path.exists(temp_json):
            os.remove(temp_json)
            
def importar_xml():
    ruta = fd.askopenfilename(
        title="Importar XML",
        filetypes=[("Archivos XML", "*.xml")]
    )

    if not ruta:
        return

    temp_json = "temp_import.json"

    try:
        tree = ET.parse(ruta)
        root = tree.getroot()

        with open(temp_json, "w", encoding="utf-8") as archivo_json:
            for grupo in root:
                datos = {}

                for campo in grupo:
                    datos[campo.tag] = campo.text.strip() if campo.text else ""

                if datos:
                    archivo_json.write(json.dumps(datos, ensure_ascii=False) + "\n")

        comando = [
            "mongoimport",
            "--db=BD_GrupoAlumno",
            "--collection=Grupo",
            f"--file={temp_json}"
        ]
        sp.run(comando, check=True)

        mb.showinfo("Éxito", "Importación de XML realizada correctamente")

    except Exception as e:
        mb.showerror("Error", f"Ocurrió un error:\n{e}")

    finally:
        if os.path.exists(temp_json):
            os.remove(temp_json)
import tkinter as tk
from service_alumnos import (
    agregar_alumno, 
    eliminar_alumnos, 
    modificar_alumno, 
    buscar_alumno, 
    limpiar, 
    eliminar_alumno
    )
from service_archivos import (
    crear_backup, restaurar_backup,
    exportar_csv, importar_csv,
    exportar_json, importar_json,
    exportar_xml, importar_xml
)

# Funciones faltantes
ventana = tk.Tk()
ventana.title("Panel Administrativo Alumno")
ventana.geometry("390x315")

ventana.config(cursor="hand2")

# Etiquetas
lbl_cveAlu = tk.Label(ventana, text="Clave", font=("Arial", 11, "bold"))
lbl_cveAlu.grid(row=0, column=0)

lbl_nomAlu = tk.Label(ventana, text="Nombre", font=("Arial", 11, "bold"))
lbl_nomAlu.grid(row=1, column=0)

lbl_edaAlu = tk.Label(ventana, text="Edad", font=("Arial", 11, "bold"))
lbl_edaAlu.grid(row=2, column=0)

lbl_cveGru = tk.Label(ventana, text="Grupo", font=("Arial", 11, "bold"))
lbl_cveGru.grid(row=3, column=0)


# Entradas
txt_cveAlu = tk.Entry(ventana, width=20, font=("Arial", 11))
txt_cveAlu.grid(row=0, column=1, columnspan=2)

txt_nomAlu = tk.Entry(ventana, width=20, font=("Arial", 11))
txt_nomAlu.grid(row=1, column=1, columnspan=2)

txt_edaAlu = tk.Entry(ventana, width=20, font=("Arial", 11))
txt_edaAlu.grid(row=2, column=1, columnspan=2)

txt_cveGru = tk.Entry(ventana, width=20, font=("Arial", 11))
txt_cveGru.grid(row=3, column=1, columnspan=2)

# Botones derecha arriba
btn_buscar = tk.Button(
    ventana,
    text="Buscar",
    font=("Arial", 12, "bold"),
    bg="white", fg="black",
    command=lambda: buscar_alumno(txt_cveAlu, txt_nomAlu)
)
btn_buscar.grid(row=2, column=3)

btn_limpiar = tk.Button(
    ventana,
    text="Limpiar",
    font=("Arial", 12, "bold"),
    bg="white", fg="black",
    command=lambda: limpiar(txt_cveAlu, txt_nomAlu, txt_edaAlu, txt_cveGru)
)
btn_limpiar.grid(row=3, column=3)

btn_eliminar = tk.Button(
    ventana,
    text="Eliminar",
    font=("Arial", 12, "bold"),
    bg="white", fg="black",
    command=lambda: eliminar_alumno(txt_cveAlu, txt_nomAlu, txt_edaAlu, txt_cveGru)
)
btn_eliminar.grid(row=4, column=3)

# Fila de acciones principales
btn_agregar = tk.Button(
    ventana,
    text="Agregar",
    font=("Arial", 12, "bold"),
    bg="white", fg="black",
    command=lambda: agregar_alumno(txt_cveAlu, txt_nomAlu, txt_edaAlu, txt_cveGru)
)
btn_agregar.grid(row=4, column=0)

btn_modificar = tk.Button(
    ventana,
    text="Modificar",
    font=("Arial", 12, "bold"),
    bg="white", fg="black",
    command=lambda: modificar_alumno(txt_cveAlu, txt_nomAlu, txt_edaAlu, txt_cveGru)
)
btn_modificar.grid(row=4, column=1)

# Exportar
btn_exportar_csv = tk.Button(
    ventana,
    text="Exportar csv",
    font=("Arial", 12, "bold"),
    bg="white", fg="black",
    command=exportar_csv
)
btn_exportar_csv.grid(row=5, column=0)

btn_exportar_json = tk.Button(
    ventana,
    text="Exportar json",
    font=("Arial", 12, "bold"),
    bg="white", fg="black",
    command=exportar_json
)
btn_exportar_json.grid(row=5, column=1)

btn_exportar_xml = tk.Button(
    ventana,
    text="Exportar xml",
    font=("Arial", 12, "bold"),
    bg="white", fg="black",
    command=exportar_xml
)
btn_exportar_xml.grid(row=5, column=3)

# Importar
btn_importar_csv = tk.Button(
    ventana,
    text="Importar csv",
    font=("Arial", 12, "bold"),
    bg="white", fg="black",
    command=importar_csv
)
btn_importar_csv.grid(row=6, column=0)

btn_importar_json = tk.Button(
    ventana,
    text="Importar json",
    font=("Arial", 12, "bold"),
    bg="white", fg="black",
    command=importar_json
)
btn_importar_json.grid(row=6, column=1)

btn_importar_xml = tk.Button(
    ventana,
    text="Importar xml",
    font=("Arial", 12, "bold"),
    bg="white", fg="black",
    command=importar_xml
)
btn_importar_xml.grid(row=6, column=3)

# Botón backup
btn_ejecutar_backup = tk.Button(
    ventana,
    text="Ejecutar Backup",
    font=("Arial", 12, "bold"),
    bg="white", fg="black",
    command=crear_backup
)
btn_ejecutar_backup.grid(row=7, column=0, columnspan=4, sticky="ew")

# Botón eliminar todos
btn_eliminar_alumnos = tk.Button(
    ventana,
    text="Eliminar todos los Alumnos",
    font=("Arial", 12, "bold"),
    bg="white", fg="black",
    command=eliminar_alumnos
)
btn_eliminar_alumnos.grid(row=8, column=0, columnspan=4, sticky="ew")

# Botón restaurar
btn_restaurar_alumnos = tk.Button(
    ventana,
    text="Restaurar todos los Alumnos",
    font=("Arial", 12, "bold"),
    bg="white", fg="black",
    command=restaurar_backup
)
btn_restaurar_alumnos.grid(row=9, column=0, columnspan=4, sticky="ew")

ventana.mainloop()
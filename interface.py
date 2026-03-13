import tkinter as tk
from service_grupos import agregar_grupo, eliminar_grupos, modificar_grupo
from service_archivos import crear_backup, restaurar_backup, exportar_csv, importar_csv, exportar_json, importar_json, exportar_xml, importar_xml

ventana = tk.Tk()
ventana.title("Panel Administrativo Alumno")
ventana.geometry("400x200")

ventana.config(cursor="hand2")
lbl_cveGru = tk.Label(ventana, text="Clave", font=("Arial", 11, "bold"))
lbl_cveGru.grid(row=1, column=0)
lbl_nomGru = tk.Label(ventana, text="Nombre", font=("Arial", 11, "bold"))
lbl_nomGru.grid(row=2, column=0)

txt_cveGru = tk.Entry(ventana, width=20, font=("Arial", 11))
txt_cveGru.grid(row=1, column=1)
txt_nomGru = tk.Entry(ventana, width=20, font=("Arial", 11))
txt_nomGru.grid(row=2, column=1)

btn_agregar = tk.Button(ventana,
                        text="Agregar",
                        font=("Arial", 12, "bold"),
                        bg="white", fg="black",
                        command=lambda: agregar_grupo(txt_cveGru,txt_nomGru))

btn_agregar.grid(row=3, column=1)

btn_modificar = tk.Button(ventana,
                           text="Modificar",
                           font=("Arial", 12, "bold"),
                           bg="white", fg="black",
                           command=lambda: modificar_grupo(txt_cveGru,txt_nomGru))

btn_modificar.grid(row=3, column=2)


btn_exportar_json = tk.Button(ventana,
                                text="Exportar JSON",
                                font=("Arial", 12, "bold"),
                                bg="white", fg="black",
                                command=exportar_json)

btn_exportar_json.grid(row=4, column=1)

btn_importar_json = tk.Button(ventana,
                                text="Importar JSON",
                                font=("Arial", 12, "bold"),
                                bg="white", fg="black",
                                command=importar_json)

btn_importar_json.grid(row=5, column=1)

btn_ejecutar_backup = tk.Button(ventana,
                                text="Ejecutar Backup",
                                font=("Arial", 12, "bold"),
                                bg="white", fg="black",
                                command=crear_backup)

btn_ejecutar_backup.grid(row=6, column=1)

btn_eliminar_grupos = tk.Button(ventana,
                                text="Eliminar todos los Grupos",
                                font=("Arial", 12, "bold"),
                                bg="white", fg="black",
                                command=eliminar_grupos)

btn_eliminar_grupos.grid(row=7, column=1)

btn_restaurar_grupos = tk.Button(ventana,
                                text="Restaurar todos los Grupos",
                                font=("Arial", 12, "bold"),
                                bg="white", fg="black",
                                command=restaurar_backup)

btn_restaurar_grupos.grid(row=8, column=1)

btn_exportar_csv = tk.Button(ventana,
                                text="Exportar CSV",
                                font=("Arial", 12, "bold"),
                                bg="white", fg="black",
                                command=exportar_csv)

btn_exportar_csv.grid(row=4, column=2)

btn_importar_csv = tk.Button(ventana,
                                text="Importar CSV",
                                font=("Arial", 12, "bold"),
                                bg="white", fg="black",
                                command=importar_csv)

btn_importar_csv.grid(row=5, column=2)

btn_exportar_xml = tk.Button(ventana,
                                text="Exportar XML",
                                font=("Arial", 12, "bold"),
                                bg="white", fg="black",
                                command=exportar_xml)

btn_exportar_xml.grid(row=4, column=3)

btn_importar_xml = tk.Button(ventana,
                                text="Importar XML",
                                font=("Arial", 12, "bold"),
                                bg="white", fg="black",
                                command=importar_xml)

btn_importar_xml.grid(row=5, column=3)

ventana.mainloop()

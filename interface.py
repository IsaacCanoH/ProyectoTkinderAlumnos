import tkinter as tk
from tkinter import ttk  # Importamos ttk para un estilo más moderno

# Tus importaciones se mantienen intactas
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

# Configuración principal de la ventana
ventana = tk.Tk()
ventana.title("Panel Administrativo de Alumnos")
# Ajustamos el tamaño para acomodar los nuevos campos
ventana.geometry("590x480") 
ventana.configure(bg="#f4f5f7") 

# Estilo global para los elementos ttk
style = ttk.Style()
style.theme_use('clam')

# ==========================================
# SECCIÓN 1: DATOS DEL ALUMNO (Entradas)
# ==========================================
frame_datos = tk.LabelFrame(ventana, text="Datos del Alumno", bg="#f4f5f7", font=("Arial", 10, "bold"), padx=10, pady=10)
frame_datos.pack(fill="x", padx=20, pady=10)

# Etiquetas y Entradas
lbl_cveAlu = tk.Label(frame_datos, text="Clave:", font=("Arial", 11), bg="#f4f5f7")
lbl_cveAlu.grid(row=0, column=0, sticky="e", pady=5)
txt_cveAlu = ttk.Entry(frame_datos, width=25, font=("Arial", 11))
txt_cveAlu.grid(row=0, column=1, padx=10, pady=5)

lbl_nomAlu = tk.Label(frame_datos, text="Nombre:", font=("Arial", 11), bg="#f4f5f7")
lbl_nomAlu.grid(row=1, column=0, sticky="e", pady=5)
txt_nomAlu = ttk.Entry(frame_datos, width=25, font=("Arial", 11))
txt_nomAlu.grid(row=1, column=1, padx=10, pady=5)

lbl_edaAlu = tk.Label(frame_datos, text="Edad:", font=("Arial", 11), bg="#f4f5f7")
lbl_edaAlu.grid(row=2, column=0, sticky="e", pady=5)
txt_edaAlu = ttk.Entry(frame_datos, width=25, font=("Arial", 11))
txt_edaAlu.grid(row=2, column=1, padx=10, pady=5)

lbl_cveGru = tk.Label(frame_datos, text="Grupo:", font=("Arial", 11), bg="#f4f5f7")
lbl_cveGru.grid(row=3, column=0, sticky="e", pady=5)
txt_cveGru = ttk.Entry(frame_datos, width=25, font=("Arial", 11))
txt_cveGru.grid(row=3, column=1, padx=10, pady=5)

# Botones de Buscar y Limpiar (Ubicados a la derecha de los campos)
btn_buscar = tk.Button(frame_datos, text="🔍 Buscar", font=("Arial", 10, "bold"), bg="#4CAF50", fg="white", width=10, command=lambda: buscar_alumno(txt_cveAlu, txt_nomAlu))
btn_buscar.grid(row=0, column=2, rowspan=2, padx=10) # rowpan=2 para que ocupe más espacio vertical visualmente

btn_limpiar = tk.Button(frame_datos, text="🧹 Limpiar", font=("Arial", 10, "bold"), bg="#FF9800", fg="white", width=10, command=lambda: limpiar(txt_cveAlu, txt_nomAlu, txt_edaAlu, txt_cveGru))
btn_limpiar.grid(row=2, column=2, rowspan=2, padx=10)

# ==========================================
# SECCIÓN 2: ACCIONES BÁSICAS (CRUD)
# ==========================================
frame_acciones = tk.Frame(ventana, bg="#f4f5f7")
frame_acciones.pack(fill="x", padx=20, pady=5)

btn_agregar = tk.Button(frame_acciones, text="Agregar", font=("Arial", 11, "bold"), bg="#2196F3", fg="white", width=12, command=lambda: agregar_alumno(txt_cveAlu, txt_nomAlu, txt_edaAlu, txt_cveGru))
btn_agregar.pack(side="left", expand=True, padx=5)

btn_modificar = tk.Button(frame_acciones, text="Modificar", font=("Arial", 11, "bold"), bg="#FFC107", fg="black", width=12, command=lambda: modificar_alumno(txt_cveAlu, txt_nomAlu, txt_edaAlu, txt_cveGru))
btn_modificar.pack(side="left", expand=True, padx=5)

btn_borrar = tk.Button(frame_acciones, text="Borrar", font=("Arial", 11, "bold"), bg="#F44336", fg="white", width=12, command=lambda: eliminar_alumno(txt_cveAlu, txt_nomAlu, txt_edaAlu, txt_cveGru))
btn_borrar.pack(side="left", expand=True, padx=5)

# ==========================================
# SECCIÓN 3: IMPORTAR / EXPORTAR
# ==========================================
frame_archivos = tk.LabelFrame(ventana, text="Gestión de Archivos", bg="#f4f5f7", font=("Arial", 10, "bold"), padx=10, pady=10)
frame_archivos.pack(fill="x", padx=20, pady=10)

# Fila de Exportación
tk.Label(frame_archivos, text="Exportar:", bg="#f4f5f7", font=("Arial", 10)).grid(row=0, column=0, sticky="w", pady=5)
tk.Button(frame_archivos, text="JSON", width=12, bg="white", command=exportar_json).grid(row=0, column=1, padx=5, pady=5)
tk.Button(frame_archivos, text="CSV", width=12, bg="white", command=exportar_csv).grid(row=0, column=2, padx=5, pady=5)
tk.Button(frame_archivos, text="XML", width=12, bg="white", command=exportar_xml).grid(row=0, column=3, padx=5, pady=5)

# Fila de Importación
tk.Label(frame_archivos, text="Importar:", bg="#f4f5f7", font=("Arial", 10)).grid(row=1, column=0, sticky="w", pady=5)
tk.Button(frame_archivos, text="JSON", width=12, bg="white", command=importar_json).grid(row=1, column=1, padx=5, pady=5)
tk.Button(frame_archivos, text="CSV", width=12, bg="white", command=importar_csv).grid(row=1, column=2, padx=5, pady=5)
tk.Button(frame_archivos, text="XML", width=12, bg="white", command=importar_xml).grid(row=1, column=3, padx=5, pady=5)

# ==========================================
# SECCIÓN 4: BASE DE DATOS Y SISTEMA
# ==========================================
frame_sistema = tk.LabelFrame(ventana, text="Sistema de Base de Datos", bg="#f4f5f7", font=("Arial", 10, "bold"), padx=10, pady=10)
frame_sistema.pack(fill="x", padx=20, pady=10)

btn_backup = tk.Button(frame_sistema, text="💾 Ejecutar Backup", font=("Arial", 10, "bold"), width=18, command=crear_backup)
btn_backup.grid(row=0, column=0, padx=10, pady=5)

btn_restaurar = tk.Button(frame_sistema, text="🔄 Restaurar Backup", font=("Arial", 10, "bold"), width=18, command=restaurar_backup)
btn_restaurar.grid(row=0, column=1, padx=10, pady=5)

btn_eliminar_todos = tk.Button(frame_sistema, text="⚠️ Eliminar TODOS", font=("Arial", 10, "bold"), bg="#b71c1c", fg="white", width=18, command=eliminar_alumnos)
btn_eliminar_todos.grid(row=0, column=2, padx=10, pady=5)

ventana.mainloop()
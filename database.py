from pymongo import MongoClient as MC

client = MC("mongodb://localhost:27017/")
db = client["BD_GrupoAlumno"]
alumnos = db["Alumno"]
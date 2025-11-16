# -*- coding: utf-8 -*-
"""
Programador: Martínez Alfaro Felipe de Jesús

Este programa tiene el propocito de contar palabras en varios archivos.
"""

""" Ejemplo de Chat-GPT...
import os

carpeta = "/ruta/a/tu/carpeta"

for nombre_archivo in os.listdir(carpeta):
    ruta_archivo = os.path.join(carpeta, nombre_archivo)

    if os.path.isfile(ruta_archivo) and nombre_archivo.endswith((".txt", ".json")):
        with open(ruta_archivo, "r", encoding="utf-8") as f:
            contenido = f.read()
        print(f"Procesado: {nombre_archivo}")
"""

from ast import Tuple
import re;
import os;
import pandas as pd;



class Contador:
    c_language_elements = {
        # Palabras clave
        "auto": 0,
        "break": 0,
        "case": 0,
        "char": 0,
        "const": 0,
        "continue": 0,
        "default": 0,
        "do": 0,
        "double": 0,
        "else": 0,
        "enum": 0,
        "extern": 0,
        "float": 0,
        "for": 0,
        "goto": 0,
        "if": 0,
        "inline": 0,
        "int": 0,
        "long": 0,
        "register": 0,
        "restrict": 0,
        "return": 0,
        "short": 0,
        "signed": 0,
        "sizeof": 0,
        "static": 0,
        "struct": 0,
        "switch": 0,
        "typedef": 0,
        "union": 0,
        "unsigned": 0,
        "void": 0,
        "volatile": 0,
        "while": 0,
        #"_Alignas": 0,
        #"_Alignof": 0,
        #"_Atomic": 0,
        #"_Bool": 0,
        #"_Complex": 0,
        #"_Generic": 0,
        #"_Imaginary": 0,
        #"_Noreturn": 0,
        #"_Static_assert": 0,
        #"_Thread_local": 0,

        # Directivas del preprocesador
        "#include": 0,
        "#define": 0,
        "#undef": 0,
        "#ifdef": 0,
        "#ifndef": 0,
        "#if": 0,
        "#else": 0,
        "#elif": 0,
        "#endif": 0,
        "#error": 0,
        "#pragma": 0,
        "#line": 0
    }

    def __init__(self,carpeta:str,conteo_profunfo:bool = False):
        self.origin = carpeta
        self.deep  = conteo_profunfo
        pass;
    pass;

    def recorrer(self,do,ends:Tuple = ("", ".txt"),ruta:str = None):
        if ruta == None:
            ruta = self.origin
        for nombre_archivo in os.listdir(ruta):
            ruta_archivo = os.path.join(ruta, nombre_archivo)
            # Realizo un recorrido de todos los archivos...
            if os.path.isfile(ruta_archivo):        # Si es un documento.
                if nombre_archivo.endswith(ends):   # Termina con lo que me importa.
                    do(ruta_archivo)                # Realiza lo que yo le indique.
            elif self.deep:
                self.recorrer(do,ends,ruta_archivo)
        return;

    def ls(self,ends = ("","") ):
        print(self.origin + "...")
        self.recorrer(lambda x:print(x),ends)
        return;

    def contarPalabras(self,ruta:str):
        print(f"Procesado: {ruta.split('\\').pop()}")   # Indico archivo encontrado.
        with open(ruta, "r") as f:                      # Usando with me ahorro usar try (excepciones) y finally (cerrrar doc)
            contenido = f.read()
        palabras = contenido.split()                    # Separo por espacios las palabras "Hola Lola" -> ["Hola","Lola"]
        for key in self.c_language_elements:            # Realizo el conteo de cadenas que coinciden con la llave.
            self.c_language_elements[key] += palabras.count(key)    # Actualiza la frecuencia de la palabra.
        pass;

    def procesar(self,ends = ("","") ):
        print(self.origin + "...")
        self.recorrer(self.contarPalabras,ends)

    def printConteo(self):
        for key in sys_arch.c_language_elements:
            print(f" {key}: {sys_arch.c_language_elements[key]}")

    def saveCSV(self,name:str = "Count-C-DOOM.csv"):
        keys = []   # Indica las palabras reservadas del diccionario.
        counts = [] # Indica su frecuencia en el diccionario.
        # Reccorre el diccionario...
        for key in self.c_language_elements:
            keys.append(key)
            counts.append(self.c_language_elements[key])
        # Crea el pandas data frame...
        df = pd.DataFrame({
            "Palabra": keys,
            "Frecuencia": counts
        })
        # Guarda en CSV...
        df.to_csv(name, index=False, encoding="utf-8")

if __name__ == '__main__':
    sys_arch = Contador("DOOM-master",True)
    sys_arch.procesar((".c",".C",".h",".H"))
    sys_arch.saveCSV()
    pass;

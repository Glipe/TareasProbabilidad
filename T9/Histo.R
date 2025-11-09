# Programador: Felipe de Jesús Martínez Alfaro, con ayuda de Chat-GPT xD
# Nota: en la consola R primero insralar la libreria.
# install.packages("readxl")

# imports...
library(readxl)

# Seleccinar la ruta de trabajo...
setwd("D:/USER/Desktop/carpetas/CIC/SEM1/Prob/Tareas/T9")

# Leer el csv de la carpeta...
datos <- read.csv("Toronto_temp.csv")
# si es xls usar: datos <- read_excel("datos.xlsx")

head(datos)      	# Muestra las primeras filas.
names(datos)     	# Muestra los nombres de las columnas.
str(datos[[5]])	# Verificamos que detecta bien la info de la columna.

# Ejemplo, histogama 1...
#hist(datos[[5]],
#      main = "Histograma de la temperatura media en Toronto",
#      xlab = "Temperatura (°C)",
#      ylab = "Frecuencia",
#      col = "skyblue",
#      border = "white")

# Limpio datos que me generan ruido...
datos <- datos[!(datos[[4]] %in% c(1,2,3,4, 31)), ]

# Grafico los días seleccionados aleratoriamente, para medir temperaturas...
hist(datos[[4]],
      main = "Histograma del numero del día de mes en el registro de Toronto",
      xlab = "Día",
      ylab = "Frecuencia",
      col = "skyblue",
      border = "white")
# Se muestra un histograma con una distribución uniforme.




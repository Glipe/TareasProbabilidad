library(readxl)
setwd("D:/USER/Desktop/carpetas/CIC/SEM1/Prob/Tareas/T10")

# Leer el CSV
datos <- read.csv("Count-C-DOOM.csv", header = TRUE, stringsAsFactors = FALSE)

# Ordenar de mayor a menor según Conteo
datos_ordenados <- datos[order(-datos$Frecuencia), ]

print(datos_ordenados)

# Gráfico de barras con datos ordenados
barplot(datos_ordenados$Frecuencia,
        names.arg = datos_ordenados$Palabra,
        main = "Conteo por palabra reservada de C (ordenado)",
        xlab = "Palabra",
        ylab = "Frecuencia",
        col = "skyblue",
        #horiz = TRUE,       # Barras horizontales.
        las = 2,            # 1 Letras horiz, con 2 es verticales.
        width = 2,          # Ancho de las barras
        border = "white")

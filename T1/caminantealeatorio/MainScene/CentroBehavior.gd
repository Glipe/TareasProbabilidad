"""
Programadores:
	Felipe de Jesús Martínez Alfaro.
Descripción:
Niveles de comentarios:
#0 Indica lo que hace la siguiente linea o sección...
										#1 Indica lo que hace la linea actual.
																				#2 Indica lo que hace la linea actual.
																									#3 Indica lo que hace la linea actual.
"""
"""##############################################################################################"""
class_name CentroBehavior extends Node2D

## Numero de muestreo para cambiar la direción.
@export var muestreo: int = 20000
@export var ancho_linea: float = 0.5
@export var tam_paso: float  = 2
@export var frame_a_frame: bool = true
@export var lineas_xframe:int = 10
var conteo:int = 0
var arista: Line2D = Line2D.new()
var pos_actual: Vector2 = Vector2(0,0)

## Crea una nueva dirección (angulo) aleatoria.
func novoVertice() -> Vector2:
	var rand = RandomNumberGenerator.new()
	var angulo = rand.randf_range(0,2*PI)
	return tam_paso * Vector2(cos(angulo),sin(angulo));
	
func _ready() -> void:
	arista.add_point(pos_actual)
	arista.width = ancho_linea
	if not frame_a_frame:
		var novo_punto: Vector2
		for i in range(muestreo):
			novo_punto = novoVertice()
			pos_actual = pos_actual + novo_punto
			arista.add_point(pos_actual)
		conteo = muestreo
		print("Último punto:",pos_actual, "\nDistancia: ", pos_actual.length() )
	add_child(arista)
	pass;
	
func _process(delta: float) -> void:
	if conteo < muestreo:
		var novo_punto
		for i in range(lineas_xframe):
			novo_punto = novoVertice()
			pos_actual = pos_actual + novo_punto
			arista.add_point(pos_actual)
			conteo += 1
		#print("conteo: ",conteo)
		print("Último punto:",pos_actual, "\nDistancia: ", pos_actual.length() )
	pass;

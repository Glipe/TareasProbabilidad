"""
Programadores:
	Felipe de Jesús Martínez Alfaro.
Descripción:
Niveles de comentarios:
#0 Indica lo que hace la siguiente linea o sección...
										#1 Indica lo que hace la linea actual.
															# 2
																				#3 Indica lo que hace la linea actual.
																									#3 Indica lo que hace la linea actual.
"""
"""##############################################################################################"""
class_name TrinaguloBehavior extends Node2D

@export var perimetro:Line2D
@export var solo_distribucion:bool = false
@export var solo_primer_figura:bool = false
@export var per_ancho:float = 0.5
@export var iteraciones:int = 20000
@export var n_vert: int = 3
@export var radio_fig:float = 10
@export var cargar_dado:bool = false
@export var fuerza_densidad_carga : Vector2 = Vector2(1.5,1.5)
@export var ancho_punto: float = 2
var puntos:Array = []

## Crea una figura geometrica de n vertices
func crearFig(vertices:int,radio:float,per:float)->Line2D:
	var aristas = Line2D.new()
	var ang = (2*PI)/vertices
	aristas.width = per
	for i in range(vertices+1):
		aristas.add_point( radio*Vector2(cos(ang*i),sin(ang*i)) )
	add_child(aristas)
	return aristas;

func getPoint(cargar:int = -1)->Vector2:
	# Variables...
	var vertices = perimetro.points.size()-1
	var rand = RandomNumberGenerator.new()
	var m_:Array = []
	var m:float = 0
	var w:float
	var pos: Vector2 = Vector2(0,0)
	# Obtengo las ponderaciones de cada vertice y calculo el peso total...
	for i in range(vertices):
		m_.append( rand.randf_range(0,1) )
		if cargar > -1 and cargar==i: m_[i] += vertices*fuerza_densidad_carga.x	# cargo el dado.
		m += m_[i]
		pass
	# Calculo la influencia o peso de cada vertice y promedio la pos...
	for i in range(vertices):
		w = m_[i]/m
		pos += w*perimetro.points[i]
	return pos;
	
func t1():
	var rand = RandomNumberGenerator.new()
	var punto:Vector2
	var medio:Vector2
	var esquina:int
	for i in range(iteraciones):
		if cargar_dado and i >= iteraciones/fuerza_densidad_carga.y :
			punto = getPoint(i%perimetro.points.size())
		else:
			punto = getPoint()
		if  not solo_distribucion:
			esquina = rand.randi_range(0,perimetro.points.size()-1)
			medio = (perimetro.points[esquina] + punto)/2
		puntos.append( punto if solo_distribucion else medio)
	pass;

func tn():
	var rand = RandomNumberGenerator.new()
	var punto:Vector2
	var medio:Vector2
	var esquina:int
	if cargar_dado :
		punto = getPoint( rand.randi_range(0,perimetro.points.size()-1) )
	else:
		punto = getPoint()
	for i in range(iteraciones):
		esquina = rand.randi_range(0,perimetro.points.size()-1)
		medio = (perimetro.points[esquina] + punto)/2
		puntos.append(medio)
		punto = medio
	pass;
	
func _ready() -> void:
	if(perimetro == null):
		perimetro = crearFig(n_vert,radio_fig,per_ancho)
	if solo_distribucion or solo_primer_figura:
		t1()
		return;
	tn()
	#queue_redraw()

func _draw() -> void:
	for i in range(puntos.size()):
		draw_circle(puntos[i],ancho_punto,Color.CHARTREUSE)
		

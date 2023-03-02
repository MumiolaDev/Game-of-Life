extends TileMap

const celda_size = 16 # Tamaño del sprite
# Cantidad de celdas de ancho y de alto
var ancho = 56
var alto = 33

var corriendo = false
var tablero = []
func _ready():
	# Tamaño en pixeles del tablero
	var ancho_pix = ancho*celda_size
	var alto_pix = alto*celda_size
	# Centramos la camara para que cubra todo el tablero
	$Camera2D.position = Vector2(ancho_pix,alto_pix)/2
	$Camera2D.zoom = Vector2(ancho_pix,alto_pix)/Vector2(1920,1080)
	tablero = []
	# Se inicializa el tablero vacio.
	for x in range(ancho):
		var tmp = []
		for y in range(alto):
			tmp.append(0)
			set_cell(x,y,0)
		tablero.append(tmp)

func _input(event):
	## TECLA ENTER DETIENE Y REANUDA LA SIMULACION
	if event.is_action_pressed("enter"):
		corriendo = !corriendo
	## CON EL CLICK ISQUIERDO SE CREAN Y DESTRUYEN CELDAS
	if event.is_action_pressed("click"):
		var pos = (get_local_mouse_position()/celda_size).floor()
		set_cellv(pos,1-get_cellv(pos))

func _process(delta):
	if !corriendo: # Si la simulacion no esta corriendo no se procesa nada
		return
	
	## Pasamos por todas las celdas del tablero
	for x in range(ancho):
		for y in range(alto):
			# Contaremos el total de vecinos vivos que tiene la celda (x,y)
			var total = 0
			for i in [-1,0,1]:
				for j in [-1,0,1]:
					# Revisamos toda la cuadricula de 3x3 menos la celda del centro
					if Vector2(i,j) != Vector2(0,0):
						if get_cell(x+i,y+j) == 1: # si la celda está activa
							total += 1 # se suma al total
			# Vemos si la celda evaluada esta activa o inactiva
			if get_cell(x,y) == 1:
				# Si la celda esta viva
				if total in [2,3]:
					# Sobrevive si tiene 2 o 3 vecinos
					tablero[x][y] = 1
				else:
					# Muere de lo contrario
					tablero[x][y] = 0
			else:
				# Si la celda ya está muerta
				if total == 3:
					# Nace una nueva celda si tiene exactamente 3 vecinos
					tablero[x][y] = 1
				else:
					# No pasa  nada de lo contrario
					tablero[x][y] = 0
	# Ahora actualizamos el Tilemap con el tablero actualizado
	for x in range(ancho):
		for y in range(alto):
			set_cell(x,y,tablero[x][y])






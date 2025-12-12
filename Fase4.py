# mesma situação que a fase3, porém, com o else e atualizações no código.

while True:
	if can_harvest():
		harvest()
		move(North) # após colher, move para o norte.
		plant.(Entities.Bush) # e planta o Bush.
		
		

	#se ele não pode colher, move para o norte, voltando para o ínicio do código e repetindo tudo novamente.
	else:
		move(North)

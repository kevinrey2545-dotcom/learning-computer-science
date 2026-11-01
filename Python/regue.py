import random #se importa la librería de python random

sujetos = ["mami", "bebé", "princess", "mami","linda", "bandida","morena","mi niña","reina","chiquita"]  #se define una listasta
intenciones = ["yo quiero", "yo puedo", "yo vengo a", "voy a","yo deseo", "ando buscando", "yo quiero me hagas"]
verbos = ["encendelte", "amalte", "ligal", "jugal", "tocalte", "besalte", "acariciarte", "chingal", "bailal", "perrear", "seducirte", "provocarte"]
advs = ["suave", "lento", "lápido", "fuelte","con pasion", "con deseo", "con hambre", "con ganas", "con fuerza", "con ritmo", "con sabor", "con estilo","poco a poco",]
complementos_uno = ["hasta que salga el sol", "toda la noche", "hasta el amanecer", "todo el día", "bajo la luna", "en la playa","en la disco", "en la cama", "en el sofá", "en el auto", "en la ducha", "en la piscina", "en el balcón"]
complementos_dos = ["sin anestesia", "sin compromiso", "feis to feis","sin afan", "sin miedo", "sin prisa","sin descanso","sin limites","sin pausa","sin control","sin reglas"]

sujeto_seleccionado = random.choice(sujetos) #se utiliza la librería para seleccionar un elemento al azar de la lista sujetos
intencion_seleccionada = random.choice(intenciones)
verbo_seleccionado = random.choice(verbos)
adv_seleccionado = random.choice(advs)
compl1s_seleccionado = random.choice(complementos_uno)
compl2s_seleccionado = random.choice(complementos_dos)

print("letra generada: " + sujeto_seleccionado + " " + intencion_seleccionada + " " + verbo_seleccionado + " " 
      + adv_seleccionado + " " + compl1s_seleccionado + " " + compl2s_seleccionado) #se imprime la canción
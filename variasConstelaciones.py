import random

def escogerConstelacion():
    #numeros = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
    osaMenor = [[120,230],[240,210],[310,250],[400,290],[420,380],[560,390],[600,290]]
    osaMenorCoordenadas = [[2,5.5],[4,6],[5.1,5.2],[6.6,4.6],[7,3.1],[9.3,3],[10,4.7]]
    aries = [[180,390],[420,330],[520,330],[540,340]]
    ariesCoordenadas = [[3,3],[7,4],[8.6,4],[9,3.8]]
    auriga = [[300,450],[240,330],[360,150],[380,270],[380,420],[301,450]]
    aurigaCoordenadas = [[5,2],[4,4],[6,7],[6.5,5],[6.5,2.5],[5,2]]
    camaleon = [[660,330],[360,340],[180,330],[170,390],[350,390],[640,340]]
    camaleonCoordenadas = [[11,4],[6,3.9],[3,4],[2.9,3],[5.8,3],[10.8,3.8]]
    dorado = [[540,210],[420,270],[300,280],[180,390],[120,400],[130,480],[180,391],[420,270]]
    doradoCoordenadas = [[9,6],[7,5],[5,4.9],[3,3],[2,2.8],[2.2,1.6],[3,3],[7,5]]
    equulus = [[420,450],[430,230],[480,210]]
    equulusCoordenadas = [[7,2],[7.1,5.8],[8,6]]
    horologium = [[240,150],[480,270],[480,300],[470,330],[420,390],[420,460]]
    horologiumCoordenadas = [[4,7],[8,5],[8,4.5],[7.9,4],[7,3],[7,1.8]]
    vela = [[180,330],[240,210],[360,150],[600,310],[480,420],[300,400],[180,331]]
    velaCoordenadas = [[3,4],[4,6],[6,7],[10,4.4],[8,2.7],[5,2.8],[3,4]]
    leoMenor = [[540,210],[420,310],[300,330],[180,450],[340,400],[420,311]]
    leoMenorCoordenadas = [[9,6],[7,4.3],[5,4],[3,2],[5.7,2.8],[7,4.3]]
    trianguloAustral = [[240,450],[360,210],[500,390],[240,451]]
    trianguloAustralCoordenadas = [[4,2],[6,6],[8.4,3],[4,2]]
    lagarto = [[420,450],[360,390],[380,320],[360,290],[380,210]]
    lagartoCoordenadas = [[7,2],[6,3],[6.3,4.2],[6,4.6],[6.3,6]]
    lyra = [[480,210],[360,270],[240,270],[120,450],[240,450],[360,271]]
    lyraCoordenadas = [[8,6],[6,5],[4,5],[2,2],[4,2],[6,5]]
    prueba = [[120,510],[180,450],[240,390]]
    pruebaCoordenadas = [[2,1],[3,2],[4,3]]
    pruebaCoordenadas2 = [[4,3],[5,4],[6,5],[7,6]]
    prueba2 = [[240,390],[300,330],[420,270],[480,210]]
    numeroConstelacion = 0
    coordenadas = []
    listaConstelacion = random.sample(range(1,13),1)
    nombreConstelacion = ""
    imagen = ""
    for i in listaConstelacion:
        numeroConstelacion = i
    constelacion = []
    if numeroConstelacion == 1:
        constelacion = auriga
        coordenadas = aurigaCoordenadas
        nombreConstelacion = "Auriga"
        imagen = "auriga.jpg"
    elif numeroConstelacion == 2:
        constelacion = camaleon
        coordenadas = camaleonCoordenadas
        nombreConstelacion = "Camaleon"
        imagen = "camaleon.jpg"
    elif numeroConstelacion == 3:
        constelacion = osaMenor
        coordenadas = osaMenorCoordenadas
        nombreConstelacion = "Osa Menor"
        imagen = "osaMenor.jpg"
    elif numeroConstelacion == 4:
        constelacion = aries
        coordenadas = ariesCoordenadas
        nombreConstelacion = "Aries"
        imagen = "aries.jpg"
    elif numeroConstelacion == 5:
        constelacion = dorado
        coordenadas = doradoCoordenadas
        nombreConstelacion = "Dorado"
        imagen = "dorado.jpg"
    elif numeroConstelacion == 6:
        constelacion = equulus
        coordenadas = equulusCoordenadas
        nombreConstelacion = "Equulus"
        imagen = "equulus.jpg"
    elif numeroConstelacion == 7:
        constelacion = horologium
        coordenadas = horologiumCoordenadas
        nombreConstelacion = "Horologium"
        imagen = "horologium.jpg"
    elif numeroConstelacion == 8:
        constelacion = vela
        coordenadas = velaCoordenadas
        nombreConstelacion = "Vela"
        imagen = "vela.jpg"
    elif numeroConstelacion == 9:
        constelacion = leoMenor
        coordenadas = leoMenorCoordenadas
        nombreConstelacion = "Leo Menor"
        imagen = "leoMenor.jpg"
    elif numeroConstelacion == 10:
        constelacion = trianguloAustral
        coordenadas = trianguloAustralCoordenadas
        nombreConstelacion = "Triangulo Austral"
        imagen = "trianguloAustral.jpg"
    elif numeroConstelacion == 11:
        constelacion = lagarto
        coordenadas = lagartoCoordenadas
        nombreConstelacion = "Lagarto"
        imagen = "lacerta.jpg"
    elif numeroConstelacion == 12:
        constelacion = lyra
        coordenadas = lyraCoordenadas
        nombreConstelacion = "Lyra"
        imagen = "lyra.jpg"
    #print(numeroConstelacion)
    #print(constelacion)
    #print(coordenadas)
    return constelacion,numeroConstelacion, coordenadas, nombreConstelacion,imagen
#escogerConstelacion()

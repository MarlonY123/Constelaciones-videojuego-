import pygame
import random
import variasConstelaciones
#from pygame import *
import sys, time

from pygame.constants import KEYDOWN, K_d

pygame.init()


def drawBoard():
    pygame.draw.line(screen, (255, 255, 255), (0, 570), (800, 570), 5)
    pygame.draw.line(screen, (255, 255, 255), (20, 0), (20, 600), 5)
    posicionEjeX = 60
    for a in range(13):
        pygame.draw.line(screen, (255, 255, 255), (posicionEjeX, 555),
                         (posicionEjeX, 590), 3)
        pygame.draw.line(screen, (155, 155, 155), (posicionEjeX, 0),
                         (posicionEjeX, 600), 1)
        texto = myfontIntro.render(str(a + 1), True, (255, 255, 255))
        screen.blit(texto, (posicionEjeX + 2, 570))
        posicionEjeX += 60
    posicionEjeY = 510
    for b in range(10):
        pygame.draw.line(screen, (255, 255, 255), (10, posicionEjeY),
                         (30, posicionEjeY), 5)
        pygame.draw.line(screen, (155, 155, 155), (0, posicionEjeY),
                         (800, posicionEjeY), 1)
        texto = myfontIntro.render(str(b + 1), True, (255, 255, 255))
        screen.blit(texto, (3, posicionEjeY))
        posicionEjeY -= 60


x, y = 0, 0
pygame.mixer.music.load('Constelaciones/pegasus.wav')
pygame.mixer.music.play(-1)
screen = pygame.display.set_mode((800, 600))
fondo = pygame.image.load("Constelaciones/espacio.jpg")
fondo = pygame.transform.scale(fondo, (800, 600))
myfontIntro = pygame.font.SysFont("Calibri", 26)
myfontTitulo = pygame.font.Font("Constelaciones/titulo1.ttf", 83)
myfontTitulo2 = pygame.font.Font("Constelaciones/titulo1.ttf", 50)
myfontIntro = pygame.font.Font("Constelaciones/coordenadas2.ttf", 26)
myfontIntro2 = pygame.font.Font("Constelaciones/coordenadas2.ttf", 20)
myfontIntro3 = pygame.font.Font("Constelaciones/coordenadas2.ttf", 27)
myfontIntro4 = pygame.font.Font("Constelaciones/coordenadas2.ttf", 27)
intro = 1
iniciar = pygame.Rect(200, 350, 150, 50)
tutorial = pygame.Rect(630, 530, 150, 50)
jugar = pygame.Rect(600, 30, 150, 50)
jugarContrarreloj = pygame.Rect(600, 390, 150, 50)
contrarreloj = pygame.Rect(400, 350, 150, 50)
puntos = []
correctos = 0
incorrectos = 0
total = 0
usados = []
carpetaImagenes = "Constelaciones/ImagenesConstelaciones/"
posicionCoordenadasy = 300
instruccionesJuego = "En este juego deberas completar seis constelaciones dando clic"
instruccionesJuego2 = "en las coordenadas que se muestran en pantalla siguiendo el orden dado."
bienHecho = "BIEN HECHO"
malHecho = "INTENTA DE NUEVO"
#gameOver = "GAME OVER"
#intro()
#constelacion = random.randint()
constelacion, numeroConstelacion, coordenadas, nombreConstelacion, nombreImagen = variasConstelaciones.escogerConstelacion(
)
constelacionesCompletadas = 0
constelacionImagen = ""
constelacionImagen += carpetaImagenes + nombreImagen
imagenConstelacion = pygame.image.load(constelacionImagen)
imagenConstelacion = pygame.transform.scale(imagenConstelacion, (480, 270))
contador2 = -1
contadorUsuario = 0
contadorEquivocaciones = 0
aux = 1
inicial = time.time()
contadorMinutos = 0
#contadorPuntos = 0
pygame.mixer.music.set_volume(0.1)
print(constelacionImagen)
while True:
    if intro == 1:
        screen.blit(fondo, (0, 0))
        titulo = myfontTitulo.render("Cielo Nocturno", True, (255, 255, 255))
        screen.blit(titulo, (60, 210))
        for e in pygame.event.get():
            if e.type == pygame.QUIT: sys.exit()
            if e.type == pygame.KEYDOWN and e.key == K_d:
                intro = 3
            if e.type == pygame.MOUSEBUTTONDOWN and e.button == 1:
                x, y = pygame.mouse.get_pos()
                print(x, y)
        pygame.draw.rect(screen, (157, 149, 147), iniciar, 0)
        texto = myfontIntro.render("Normal", True, (255, 255, 255))
        screen.blit(texto,
                    (iniciar.x + (iniciar.width - texto.get_width()) / 2,
                     iniciar.y + (iniciar.height - texto.get_height()) / 2))
        pygame.draw.rect(screen, (157, 149, 147), contrarreloj, 0)
        contra = myfontIntro.render("Contrarreloj", True, (255, 255, 255))
        screen.blit(
            contra,
            (contrarreloj.x + (contrarreloj.width - contra.get_width()) / 2,
             contrarreloj.y + (contrarreloj.height - contra.get_height()) / 2))
        #localizar rectabgulo intro
        if x <= 350 and x >= 200 and y <= 400 and y >= 348:
            intro = 3
            pygame.mixer.music.load('Constelaciones/ryusenken.wav')
            pygame.mixer.music.play(-1)
            pygame.mixer.music.set_volume(0.1)
        #localizar rectangulo contrarreloj
        if x <= 550 and x >= 400 and y <= 400 and y >= 348:
            intro = 6
            inicial = time.time()
            contadorMinutos = 0
            usados = []
            puntos = []
            contadorUsuario = 0
            pygame.mixer.music.load('Constelaciones/contrarrelojTheme.wav')
            pygame.mixer.music.play(-1)
            pygame.mixer.music.set_volume(0.1)
        pygame.draw.rect(screen, (157, 149, 147), tutorial, 0)
        textoTutorial = myfontIntro.render("Tutorial", True, (255, 255, 255))
        screen.blit(
            textoTutorial,
            (tutorial.x + (tutorial.width - textoTutorial.get_width()) / 2,
             tutorial.y + (tutorial.height - textoTutorial.get_height()) / 2))
        if x <= 778 and x >= 630 and y <= 579 and y >= 500:
            intro = 2
        pygame.display.flip()

    elif intro == 2:
        screen.blit(fondo, (0, 0))
        for e in pygame.event.get():
            if e.type == pygame.QUIT: sys.exit()
            if e.type == pygame.MOUSEBUTTONDOWN and e.button == 1:
                x, y = pygame.mouse.get_pos()
                print(x, y)
        pygame.draw.rect(screen, (157, 149, 147), jugar, 0)
        pygame.draw.rect(screen, (157, 149, 147), jugarContrarreloj, 0)
        textoJugar = myfontIntro2.render("Normal", True, (255, 255, 255))
        screen.blit(textoJugar,
                    (jugar.x + (jugar.width - textoJugar.get_width()) / 2,
                     jugar.y + (jugar.height - textoJugar.get_height()) / 2))
        textoJugarContrarreloj = myfontIntro2.render("Contrarreloj", True,
                                                     (255, 255, 255))
        screen.blit(textoJugarContrarreloj, (
            jugarContrarreloj.x +
            (jugarContrarreloj.width - textoJugarContrarreloj.get_width()) / 2,
            jugarContrarreloj.y +
            (jugarContrarreloj.height - textoJugarContrarreloj.get_height()) /
            2))
        bienvenida = myfontTitulo2.render("Bienvenido", True, (255, 255, 255))
        screen.blit(bienvenida, (250, 90))
        modoNormal = myfontIntro2.render("Modo Normal: ", True,
                                         (255, 255, 255))
        screen.blit(modoNormal, (30, 150))
        instrucciones = myfontIntro2.render(instruccionesJuego, True,
                                            (255, 255, 255))
        screen.blit(instrucciones, (20, 200))
        instrucciones2 = myfontIntro2.render(instruccionesJuego2, True,
                                             (255, 255, 255))
        screen.blit(instrucciones2, (20, 240))
        instrucciones3 = myfontIntro2.render(
            "/**Tienes tres intentos para fallar en cada constelacion**/",
            True, (255, 255, 255))
        screen.blit(instrucciones3, (20, 290))
        pygame.draw.line(screen, (255, 255, 255), (0, 330), (800, 330), 2)
        modoContrarreloj = myfontIntro2.render("Modo Contrarreloj: ", True,
                                               (255, 255, 255))
        screen.blit(modoContrarreloj, (30, 350))
        instruccionesContrarreloj = myfontIntro2.render(
            "En este modo tienes 2 minutos para hacer la mayor cantidad de ",
            True, (255, 255, 255))
        screen.blit(instruccionesContrarreloj, (20, 390))
        instruccionesContrarreloj2 = myfontIntro2.render(
            "constelaciones posibles de que el tiempo acabe.", True,
            (255, 255, 255))
        screen.blit(instruccionesContrarreloj2, (20, 430))
        instruccionesContrarreloj3 = myfontIntro2.render(
            "/**Tienes tres intentos para fallar en cada constelacion**/",
            True, (255, 255, 255))
        screen.blit(instruccionesContrarreloj3, (20, 480))
        if x <= 750 and x >= 600 and y <= 78 and y >= 29:
            intro = 3
            pygame.mixer.music.load('Constelaciones/ryusenken.wav')
            pygame.mixer.music.play(-1)
            pygame.mixer.music.set_volume(0.1)
        if x <= 750 and x >= 600 and y <= 440 and y >= 390:
            intro = 6
            inicial = time.time()
            pygame.mixer.music.load('Constelaciones/contrarrelojTheme.wav')
            pygame.mixer.music.play(-1)
            pygame.mixer.music.set_volume(0.1)
        pygame.display.flip()

    elif intro == 3:
        #print("Modo normal")
        screen.blit(fondo, (0, 0))
        drawBoard()
        for e in pygame.event.get():
            if e.type == pygame.QUIT: sys.exit()
            if e.type == pygame.MOUSEBUTTONDOWN and e.button == 1:
                x, y = pygame.mouse.get_pos()
                puntos.append([x, y])
                restax = abs(puntos[contadorUsuario][0] -
                             constelacion[contadorUsuario][0])
                restay = abs(puntos[contadorUsuario][1] -
                             constelacion[contadorUsuario][1])
                contador2 = contador2 + 1
                contadorUsuario += 1
                if restax < 20 and restay < 20:  #cambie el rango
                    correctos += 1
                else:
                    intentaNuevo = myfontIntro.render(malHecho, True,
                                                      (255, 255, 255))
                    screen.blit(intentaNuevo, (40, 390))
                    puntos = []
                    contadorUsuario = 0
                    correctos = 0
                    contador2 = -1
                    contadorEquivocaciones += 1
                    if contadorEquivocaciones == 3:
                        intro = 5
                        pygame.mixer.music.load('Constelaciones/gameOver.wav')
                        pygame.mixer.music.play(-1)
                        pygame.mixer.music.set_volume(0.1)
                    pygame.display.update()
                    pygame.time.wait(1500)
                print(contadorUsuario)

            if e.type == pygame.KEYDOWN and e.key == pygame.K_z and len(
                    puntos) > 0 and contador2 >= 0:
                puntos.pop(contador2)
                contador2 -= 1
        #MUESTRA COORDENADAS A LA DERECHA
        for x in range(len(coordenadas)):
            i = x + 1
            compuesto = str(i) + " " + str(coordenadas[x])
            #coor = myfontIntro.render(str(coordenadas[x]),True,(255,255,255))
            coorde = myfontIntro3.render(compuesto, True, (255, 255, 255))
            datos = myfontIntro3.render("Orden X  Y", True, (255, 255, 255))
            screen.blit(datos, (630, 8))
            screen.blit(coorde, (670, posicionCoordenadasy))
            posicionCoordenadasy += 30
        #MUESTRA LA CANTIDAD DE CONSTELACIONES COMPLETADAS Y EL NOMBRE DE LA CONSTELACION
        textoConstelacionesCompletadas = myfontIntro.render(
            str(constelacionesCompletadas), True, (255, 255, 255))
        textoConstelacion = myfontIntro3.render("Constelaciones: ", True,
                                                (255, 255, 255))
        nombreDeConstelacion = myfontIntro3.render(nombreConstelacion, True,
                                                   (255, 255, 255))
        screen.blit(textoConstelacionesCompletadas, (265, 30))
        screen.blit(textoConstelacion, (60, 30))
        screen.blit(nombreDeConstelacion, (360, 30))
        #DIBUJA LAS LINEAS DE LOS PUNTOS DEL USUARIO
        if len(puntos) <= len(constelacion):
            for k in range(len(puntos) - 1):  #le quite el -1
                pygame.draw.line(screen, (255, 255, 255),
                                 (puntos[k][0], puntos[k][1]),
                                 (puntos[k + 1][0], puntos[k + 1][1]), 6)
                #print(x,y)

        if correctos == len(constelacion):
            mensajeCompletado = myfontIntro.render(bienHecho, True,
                                                   (255, 255, 255))
            screen.blit(mensajeCompletado, (240, 90))
            screen.blit(imagenConstelacion, (300, 130))
            #print("FELICIDADES")
            #print(puntos)
            #print(constelacion)
            correctos = 0
            #contador = -1
            contadorUsuario = 0
            contadorEquivocaciones = 0
            #print(puntos)
            pygame.display.update()
            #print(puntos)
            usados.append(numeroConstelacion)
            pygame.time.wait(4000)
            #contadorPuntos = 0
            puntos = []
            constelacion, numeroConstelacion, coordenadas, nombreConstelacion, nombreImagen = variasConstelaciones.escogerConstelacion(
            )
            constelacionesCompletadas += 1
            if constelacionesCompletadas == 6:#modo normal con 6 constelaciones
                intro = 4
                pygame.mixer.music.load('Constelaciones/completadoTheme.wav')
                pygame.mixer.music.play(-1)
                pygame.mixer.music.set_volume(0.1)
            elif constelacionesCompletadas > 6:#modo normal cambiar para demostracion
                while numeroConstelacion in usados:
                    constelacion, numeroConstelacion, coordenadas, nombreConstelacion, nombreImagen = variasConstelaciones.escogerConstelacion(
                    )
            constelacionImagen = ""
            constelacionImagen += carpetaImagenes + nombreImagen
            imagenConstelacion = pygame.image.load(constelacionImagen)
            imagenConstelacion = pygame.transform.scale(
                imagenConstelacion, (460, 270))
        posicionCoordenadasy = 30
        pygame.display.flip()

    elif intro == 4:
        screen.blit(fondo, (0, 0))
        for e in pygame.event.get():
            if e.type == pygame.QUIT: sys.exit()
            if e.type == pygame.MOUSEBUTTONDOWN and e.button == 1:
                x, y = pygame.mouse.get_pos()
                #print(x,y)
        pygame.draw.rect(screen, (157, 149, 147), jugar, 0)
        textoJugar = myfontIntro.render("Jugar", True, (255, 255, 255))
        screen.blit(textoJugar,
                    (jugar.x + (jugar.width - textoJugar.get_width()) / 2,
                     jugar.y + (jugar.height - textoJugar.get_height()) / 2))
        bienvenida = myfontTitulo2.render("JUEGO COMPLETADO", True,
                                          (255, 255, 255))
        screen.blit(bienvenida, (240, 270))
        puntuacion = constelacionesCompletadas * 1000
        consCompletas = myfontIntro.render(
            "Constelaciones completadas: " + str(constelacionesCompletadas),
            True, (255, 255, 255))
        screen.blit(consCompletas, (60, 390))
        score = myfontIntro.render("Score: " + str(puntuacion), True,
                                   (255, 255, 255))
        screen.blit(score, (60, 450))

        usados = []
        if x <= 750 and x >= 600 and y <= 78 and y >= 29:
            intro = 1
            constelacionesCompletadas = 0
            pygame.mixer.music.load('Constelaciones/pegasus.wav')
            pygame.mixer.music.play(-1)
            pygame.mixer.music.set_volume(0.1)
        pygame.display.flip()

    elif intro == 5:
        screen.blit(fondo, (0, 0))
        for e in pygame.event.get():
            if e.type == pygame.QUIT: sys.exit()
            if e.type == pygame.MOUSEBUTTONDOWN and e.button == 1:
                x, y = pygame.mouse.get_pos()
                #print(x,y)
        pygame.draw.rect(screen, (157, 149, 147), jugar, 0)
        textoJugar = myfontIntro.render("Jugar", True, (255, 255, 255))
        screen.blit(textoJugar,
                    (jugar.x + (jugar.width - textoJugar.get_width()) / 2,
                     jugar.y + (jugar.height - textoJugar.get_height()) / 2))
        gameOver = myfontTitulo.render("GAME OVER", True, (255, 255, 255))
        screen.blit(gameOver, (300, 270))
        puntuacion = constelacionesCompletadas * 1000
        consCompletas = myfontIntro.render(
            "Constelaciones completadas: " + str(constelacionesCompletadas),
            True, (255, 255, 255))
        screen.blit(consCompletas, (60, 390))
        score = myfontIntro.render("Score: " + str(puntuacion), True,
                                   (255, 255, 255))
        screen.blit(score, (60, 450))
        #constelacionesCompletadas = 0
        contadorEquivocaciones = 0
        usados = []
        if x <= 750 and x >= 600 and y <= 78 and y >= 29:
            intro = 1
            pygame.mixer.music.load('Constelaciones/pegasus.wav')
            pygame.mixer.music.play(-1)
            pygame.mixer.music.set_volume(0.1)
            constelacionesCompletadas = 0
        pygame.display.flip()

    elif intro == 6:
        #print("Modo contrarreloj")
        screen.blit(fondo, (0, 0))
        drawBoard()
        for e in pygame.event.get():
            if e.type == pygame.QUIT: sys.exit()
            if e.type == pygame.MOUSEBUTTONDOWN and e.button == 1:
                x, y = pygame.mouse.get_pos()
                puntos.append([x, y])
                restax = abs(puntos[contadorUsuario][0] -
                             constelacion[contadorUsuario][0])
                restay = abs(puntos[contadorUsuario][1] -
                             constelacion[contadorUsuario][1])
                contador2 = contador2 + 1
                contadorUsuario += 1
                if restax < 20 and restay < 20:  #cambie el rango
                    correctos += 1
                else:
                    intentaNuevo = myfontIntro.render(malHecho, True,
                                                      (255, 255, 255))
                    screen.blit(intentaNuevo, (40, 390))
                    puntos = []
                    contadorUsuario = 0
                    correctos = 0
                    contador2 = -1
                    contadorEquivocaciones += 1
                    if contadorEquivocaciones == 3:
                        intro = 7
                        pygame.mixer.music.load('Constelaciones/gameOver.wav')
                        pygame.mixer.music.play(-1)
                        pygame.mixer.music.set_volume(0.1)
                    pygame.display.update()
                    pygame.time.wait(500)
                print(contadorUsuario)

            if e.type == pygame.KEYDOWN and e.key == pygame.K_z and len(
                    puntos) > 0 and contador2 >= 0:
                puntos.pop(contador2)
                contador2 -= 1
        actual = time.time()
        tiempo = actual - inicial
        tiempo = round(tiempo, 0)

        tiempoSegundos = int(tiempo % 10)
        tiempo = int(tiempo // 10)
        tiempo1 = myfontIntro.render(
            str(contadorMinutos) + ":" + str(tiempo) + str(tiempoSegundos),
            True, (255, 255, 255))
        screen.blit(tiempo1, (60, 60))
        if tiempo > 5.9:
            inicial = time.time()
            contadorMinutos += 1
            if contadorMinutos == 2:
                intro = 8
                pygame.mixer.music.load('Constelaciones/completadoTheme.wav')
                pygame.mixer.music.play(-1)
                pygame.mixer.music.set_volume(0.1)
                contadorMinutos = 0
                usados = []
                puntos = []
                contadorUsuario = 0
                correctos = 0
                contadorEquivocaciones = 0

        #segundos = pygame.time.get_ticks()//1000
        #contador = myfontIntro.render(str(segundos),True,(255,255,255))
        #screen.blit(contador,(300,5))
        #MUESTRA COORDENADAS A LA DERECHA
        for x in range(len(coordenadas)):
            i = x + 1
            compuesto = str(i) + " " + str(coordenadas[x])
            #coorde = myfontIntro.render(str(coordenadas[x]),True,(255,255,255))
            coorde = myfontIntro.render(compuesto, True, (255, 255, 255))
            datos = myfontIntro.render("Orden X  Y", True, (255, 255, 255))
            screen.blit(datos, (630, 8))
            screen.blit(coorde, (670, posicionCoordenadasy))
            posicionCoordenadasy += 30
        #MUESTRA LA CANTIDAD DE CONSTELACIONES COMPLETADAS Y EL NOMBRE DE LA CONSTELACION
        textoConstelacionesCompletadas = myfontIntro.render(
            str(constelacionesCompletadas), True, (255, 255, 255))
        textoConstelacion = myfontIntro.render("Constelaciones: ", True,
                                               (255, 255, 255))
        nombreDeConstelacion = myfontIntro.render(nombreConstelacion, True,
                                                  (255, 255, 255))
        screen.blit(textoConstelacionesCompletadas, (265, 30))
        screen.blit(textoConstelacion, (60, 30))
        screen.blit(nombreDeConstelacion, (360, 30))
        #DIBUJA LAS LINEAS DE LOS PUNTOS DEL USUARIO
        if len(puntos) <= len(constelacion):
            for k in range(len(puntos) - 1):  #le quite el -1
                pygame.draw.line(screen, (255, 255, 255),
                                 (puntos[k][0], puntos[k][1]),
                                 (puntos[k + 1][0], puntos[k + 1][1]), 6)
        if correctos == len(constelacion):
            mensajeCompletado = myfontIntro.render(bienHecho, True,
                                                   (255, 255, 255))
            screen.blit(mensajeCompletado, (240, 90))
            screen.blit(imagenConstelacion, (300, 130))
            correctos = 0
            contadorUsuario = 0
            contadorEquivocaciones = 0
            pygame.display.update()
            usados.append(numeroConstelacion)
            pygame.time.wait(1000)
            puntos = []
            constelacion, numeroConstelacion, coordenadas, nombreConstelacion, nombreImagen = variasConstelaciones.escogerConstelacion(
            )
            constelacionesCompletadas += 1
            if constelacionesCompletadas == 12:
                intro = 4
            elif constelacionesCompletadas > 12:
                while numeroConstelacion in usados:
                    constelacion, numeroConstelacion, coordenadas, nombreConstelacion, nombreImagen = variasConstelaciones.escogerConstelacion(
                    )
            constelacionImagen = ""
            constelacionImagen += carpetaImagenes + nombreImagen
            imagenConstelacion = pygame.image.load(constelacionImagen)
            imagenConstelacion = pygame.transform.scale(
                imagenConstelacion, (480, 270))
        posicionCoordenadasy = 30
        pygame.display.flip()

    elif intro == 7:
        screen.blit(fondo, (0, 0))
        for e in pygame.event.get():
            if e.type == pygame.QUIT: sys.exit()
            if e.type == pygame.MOUSEBUTTONDOWN and e.button == 1:
                x, y = pygame.mouse.get_pos()
                #print(x,y)
        pygame.draw.rect(screen, (157, 149, 147), jugar, 0)
        textoJugar = myfontIntro.render("Jugar", True, (255, 255, 255))
        screen.blit(textoJugar,
                    (jugar.x + (jugar.width - textoJugar.get_width()) / 2,
                     jugar.y + (jugar.height - textoJugar.get_height()) / 2))
        gameOver = myfontTitulo.render("GAME OVER", True, (255, 255, 255))
        screen.blit(gameOver, (300, 270))
        puntuacion = constelacionesCompletadas * 1000
        consCompletas = myfontIntro.render(
            "Constelaciones completadas: " + str(constelacionesCompletadas),
            True, (255, 255, 255))
        screen.blit(consCompletas, (60, 390))
        score = myfontIntro.render("Score: " + str(puntuacion), True,
                                   (255, 255, 255))
        screen.blit(score, (60, 450))
        contadorEquivocaciones = 0
        usados = []
        if x <= 750 and x >= 600 and y <= 78 and y >= 29:
            intro = 1
            inicial = time.time()
            constelacionesCompletadas = 0
            pygame.mixer.music.load('Constelaciones/pegasus.wav')
            pygame.mixer.music.play(-1)
            pygame.mixer.music.set_volume(0.1)
        pygame.display.flip()

    elif intro == 8:
        screen.blit(fondo, (0, 0))
        for e in pygame.event.get():
            if e.type == pygame.QUIT: sys.exit()
            if e.type == pygame.MOUSEBUTTONDOWN and e.button == 1:
                x, y = pygame.mouse.get_pos()
                #print(x,y)
        pygame.draw.rect(screen, (157, 149, 147), jugar, 0)
        textoJugar = myfontIntro.render("Jugar", True, (255, 255, 255))
        screen.blit(textoJugar,
                    (jugar.x + (jugar.width - textoJugar.get_width()) / 2,
                     jugar.y + (jugar.height - textoJugar.get_height()) / 2))
        TerminoTiempo = myfontTitulo2.render("Tiempo terminado!!!", True,
                                             (255, 255, 255))
        screen.blit(TerminoTiempo, (300, 270))
        puntuacion = constelacionesCompletadas * 1000
        consCompletas = myfontIntro.render(
            "Constelaciones completadas: " + str(constelacionesCompletadas),
            True, (255, 255, 255))
        screen.blit(consCompletas, (60, 390))
        score = myfontIntro.render("Score: " + str(puntuacion), True,
                                   (255, 255, 255))
        screen.blit(score, (60, 450))
        contadorEquivocaciones = 0
        usados = []
        if x <= 750 and x >= 600 and y <= 78 and y >= 29:
            intro = 1
            inicial = time.time()
            constelacionesCompletadas = 0
            contadorMinutos = 0
            puntos = []
            usados = []
            contadorUsuario = 0
            pygame.mixer.music.load('Constelaciones/pegasus.wav')
            pygame.mixer.music.play(-1)
            pygame.mixer.music.set_volume(0.1)
        pygame.display.flip()

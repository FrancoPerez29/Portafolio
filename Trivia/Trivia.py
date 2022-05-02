from time import sleep
from datetime import datetime

print("Bienvenido a la Trivia")
nombre = input("Introduce tu nombre: \n")
sleep(1)
print("¿Que categoria quieres jugar?\n")


historia = print("1°...Historia...")
deporte = print("2°...Deportes...")
ciancia = print("3°...Ciencia...")
frases_peliculas = print("4°...Frases de peliculas...")
geografia = print("5°...Geografia...")
print("6°...para salir de la trivia...")
sleep(1)


lista=["historia","deporte","ciancia","frases_peliculas","geografia"]

categoria = int(input(" \n  introduce un numero...\n "))
instanteInicial = datetime.now()
respuesta = " "
while True:
    if categoria == 1:
            cont = 0
            print("...Veremos cuanto sabes de Historia...\n")
            sleep(1)
            pregunta1=int(input("""1.Las denominadas “Reformas Borbónicas” repercutieron de manera importante en la América Hispana y se tradujeron en un profundo cambio político-administrativo.
En este sentido, con la creación del Virreinato del Río de la Plata (1776) se buscaba:
1) Acentuar la centralización política en esta parte de los dominios españoles.
2) Contener la expansión portuguesa.
3) Hacer frente a la expansión británica en el Atlántico Sur.
4) Todas las opciones anteriores son correctas.\n"""))
            if pregunta1 == 4:
                cont +=10
                sleep(1)
                print("Correcto siguiente pregunta...\n")
            elif pregunta1 != 4:
                print("Fallaste siguiente pregunta...\n")
            sleep(1)
            
            pregunta2=int(input("""¿Ante la amenaza del avance portugués, laReal Ordenanza de Intendentes de Ejército y Provincia de1782 establecióla creación de gobiernos políticos-militaresen:
1)Montevideo y Misiones.
2)Montevideo, Misiones, Moxos y Chiquitos.
3)Montevideo, Misiones y Chiquitos.
4)Potosí y Charcas.\n"""))
            sleep(1)
            if pregunta2 == 2:
                cont +=10
                print("Correcto siguiente pregunta...\n")
            elif pregunta2 != 2:
                print("Fallaste siguiente pregunta...\n")
                sleep(1)
                
            pregunta3 = int(input("""Luego dela Reconquista de Buenos Aires en agosto de 1806, un Cabildo Abierto deesa ciudad, exigió:
1)La militarización de la ciudad y puerto de Buenos Aires.
2)La delegación del mando virreinal de Sobremonte en Baltasar Hidalgo de Cisneros. 
3)La delegación del mando virreinal de Sobremonte en el capitán de navío Santiago de Liniers. 
4)La rendición incondicional del Teniente General John Whitelocke, a cargo de la fuerza invasora.\n"""))
            sleep(1)
            if pregunta3 == 3:
                cont +=10
                print("Correcto siguiente pregunta...\n")
                sleep(1)
            elif pregunta3 != 3:
                print("Fallaste siguiente pregunta...\n")
            sleep(1)
            
            pregunta4 = int(input("""Los principales centros universitarios del Virreinato del Río de la Plata se encontraban en las ciudades de:
1)Buenos Aires y Córdoba.
2)Salta y Charcas.
3)Córdoba y Charcas. 
4)Santa Fe y San Miguel del Tucumán.\n"""))
            sleep(1)
            if pregunta4 == 3:
                cont +=10
                print("Correcto siguiente pregunta...\n")
            elif pregunta4 != 3:
                print("Fallaste siguiente pregunta...\n")
                sleep(1)
                
            pregunta5 = int(input("""Bajo  el  gobierno  del  virrey  Baltasar  Hidalgo  Cisneros,  entre  1809 y  1810,  se  implementaron  medidas económicas que estuvieron orientadas a:
1)Liberar el régimen comercial.
2)Fortalecer el monopolio español.
3)Favorecer los intereses de los sectores ganaderos.
4)Las opciones a)y c)son correctas.\n"""))
            sleep(1)
            if pregunta5 == 4:
                cont +=10
                print("Correcto siguiente pregunta...\n")
                sleep(1)
            elif pregunta5 != 4:
                print("Fallaste siguiente pregunta...\n")
                sleep(1)
                
            pregunta6 = int(input("""Entre 1810 y 1815, los gobiernos que siguieron a la Revolución de Mayo debieron hacer frente a los focos de reacción realista desatados en:
1)Entre Ríos, Corrientes y Santa Fe.
2)Alto Perú, Paraguay y Montevideo.
3)San Miguel de Tucumán y Mendoza.
4)Tucumán, La Rioja y Salta.\n"""))
            if pregunta6 == 2:
                cont +=10
                print("Correcto siguiente pregunta...\n")
                sleep(1)
            elif pregunta6 != 2:
                print("Fallaste siguiente pregunta...\n")
                sleep(1)
                
            pregunta7 = int(input("""Constituida  la  Primera  Junta  de  Gobierno o  Junta  Provisional  Gubernativa,  no  tardó  en  manifestarse sistemáticamente la oposición política de:
1)El Cabildo de Buenos Aires.
2)La Audiencia de Buenos Aires.
3)El ex virrey, Baltasar Hidalgo de Cisneros.
4)Todas las opciones anteriores son correctas.\n"""))
            if pregunta7 == 4:
                cont +=10
                print("Correcto siguiente pregunta...\n")
                sleep(1)
            elif pregunta7 !=4:
                print("Fallaste siguiente pregunta...\n")
                sleep(1)
                
            pregunta8 = int(input("""El reglamento del 10 de febrero de 1811, por iniciativa del Deán Gregorio Funes, estableció la creación de las Juntas Provinciales. 
Dicho reglamento permaneció vigente hasta al inicio del gobierno del:
1)Primer Triunvirato.
2)Segundo Triunvirato.
3)Directorio de Gervasio Antonio de Posadas.
4)Ninguna de las opciones anteriores es correcta.\n"""))
            if pregunta8 == 1:
                cont +=10
                print("Correcto siguiente pregunta...\n")
                sleep(1)
            elif pregunta8 !=1:
                print("Fallaste siguiente pregunta...\n")
                sleep(1)
                
            pregunta9 = int(input("""Durante los primeros gobiernos revolucionarios, una mayor apertura política a la participación de los pueblos del interior, tuvo lugar bajo el gobierno de:
1)La  Primera Junta.
2)La Junta Grande.
3)El Primer Triunvirato.
4)Ninguna de las opcionesanteriores escorrecta\n"""))
            if pregunta9 == 2:
                cont +=10
                print("Correcto siguiente pregunta...\n")
                sleep(1)
            elif pregunta9 !=2:
                print("Fallaste siguiente pregunta...\n")
                sleep(1)
            
            pregunta10 = int(input("""La Constitución de 1819 fue aprobada por el Congreso Constituyente reunido en la ciudad de: 
1)San Miguel de Tucumán.
2)Salta.
3)Buenos Aires.
4)Santa Fe.\n"""))
            if pregunta10 ==3:
                cont +=10
                print("Correcto siguiente pregunta...\n")
                sleep(1)
            elif pregunta10 !=3:
                print("Fallaste siguiente pregunta...\n")
                sleep(1)
            print(nombre," TU PUNTUACION DE HISTORIA ES DE: ",cont)
            
            instanteFinal = datetime.now()
            tiempo = instanteFinal - instanteInicial # Devuelve un objeto timedelta
            segundos = tiempo.seconds
            print("Te tomo ",segundos, " segundo en terminar la categoria.\n")
            respuesta= input("¿Quieres volver a empezar? si o no \n")
            if respuesta=="si":
                continue
            elif respuesta == "no":
                break

            break
            
#################################################################################################
    elif categoria == 2:
            cont = 0
            print("...Veremos cuanto sabes de Deportes...\n")
            sleep(1)
            pregunta1=int(input("""¿Cual es el deporte mas practicado en el mundo:
1)La natacion
2)El basquet
3)Futbol Americano
4)Ciclismo\n"""))
            if pregunta1 == 1:
                cont +=10
                sleep(1)
                print("Correcto siguiente pregunta...\n")
            elif pregunta1 != 1:
                print("Fallaste siguiente pregunta...\n")
            sleep(1)
            
            pregunta2=int(input("""¿Que arte marcial fue creado para parecerse a un baile?:
1)Boxeo.
2)karate.
3)Judo.
4)La Capoeira.\n"""))
            sleep(1)
            if pregunta2 == 4:
                cont +=10
                print("Correcto siguiente pregunta...\n")
            elif pregunta2 != 4:
                print("Fallaste siguiente pregunta...\n")
                sleep(1)
                
            pregunta3 = int(input("""¿Donde se invento el tenis de mesa? :
1)Corea del Sur.
2)China.
3)Japon. 
4)Inglaterra.\n"""))
            sleep(1)
            if pregunta3 == 4:
                cont +=10
                print("Correcto siguiente pregunta...\n")
                sleep(1)
            elif pregunta3 != 4:
                print("Fallaste siguiente pregunta...\n")
            sleep(1)
            
            pregunta4 = int(input("""Campeon de Boxeo de pesos pesados que nunca perdio:
1)Rocky Balboa.
2)Floyd Mayweather.
3)Mike Tyson.
4)Rocky Marciano.\n"""))
            sleep(1)
            if pregunta4 == 4:
                cont +=10
                print("Correcto siguiente pregunta...\n")
            elif pregunta4 != 4:
                print("Fallaste siguiente pregunta...\n")
                sleep(1)
                
            pregunta5 = int(input("""¿Cual ha sido el partido de tenis más largo de la historia:
1)Nadal vs Federer
2)Nadal vs Djokovic
3)Del Potro vs Federer
4)John Isner vs Nicolas Mahut\n"""))
            sleep(1)
            if pregunta5 == 4:
                cont +=10
                print("Correcto siguiente pregunta...\n")
                sleep(1)
            elif pregunta5 != 4:
                print("Fallaste siguiente pregunta...\n")
                sleep(1)
                
            pregunta6 = int(input("""¿Cuantos jugadores componen un equipo de Rugby?:
1)14
2)15
3)11
4)7\n"""))
            if pregunta6 == 2:
                cont +=10
                print("Correcto siguiente pregunta...\n")
                sleep(1)
            elif pregunta6 != 2:
                print("Fallaste siguiente pregunta...\n")
                sleep(1)
                
            pregunta7 = int(input("""Si jugas en la NFL ¿que deporte practicas?:
1)Futbol soccer.
2)Futbol Americano.
3)Beisbol.
4)Natacion Federal.\n"""))
            if pregunta7 == 2:
                cont +=10
                print("Correcto siguiente pregunta...\n")
                sleep(1)
            elif pregunta7 !=2:
                print("Fallaste siguiente pregunta...\n")
                sleep(1)
                
            pregunta8 = int(input("""¿Que es un Decatlon?:
1)Competencia de Tiro al blanco.
2)Correr 200m.
3)Competicion que consta de 10 pruebas combinadas.
4)Ninguna de las opciones anteriores es correcta.\n"""))
            if pregunta8 == 3:
                cont +=10
                print("Correcto siguiente pregunta...\n")
                sleep(1)
            elif pregunta8 !=3:
                print("Fallaste siguiente pregunta...\n")
                sleep(1)
                
            pregunta9 = int(input("""¿Cuando y donde se celebró el primer mundial de Futbol?:
1)14 de julio de 1931 en Argentina.
2)28 de febrero de 1930 en Uruguay.
3)13 de julio de 1930 en Paraguay
4)13 de julio de 1930 en Uruguay\n"""))
            if pregunta9 == 4:
                cont +=10
                print("Correcto siguiente pregunta...\n")
                sleep(1)
            elif pregunta9 !=4:
                print("Fallaste siguiente pregunta...\n")
                sleep(1)
            
            pregunta10 = int(input("""¿Qeue seleccion de Futbol ha ganado mas Mundiales?: 
1)Alemania.
2)Italia.
3)Argentina.
4)Brasil.\n"""))
            if pregunta10 ==4:
                cont +=10
                print("Correcto siguiente pregunta...\n")
                sleep(1)
            elif pregunta10 !=4:
                print("Fallaste siguiente pregunta...\n")
                sleep(1)
            print(nombre," TU PUNTUACION DE DEPORTES ES DE: ",cont)            
            
            instanteFinal = datetime.now()
            tiempo = instanteFinal - instanteInicial # Devuelve un objeto timedelta
            segundos = tiempo.seconds
            
            print("Te tomo ",segundos, " segundo en terminar la categoria.\n")
            respuesta= input("¿Quieres volver a empezar? si o no \n")
            if respuesta=="si":
                continue
            elif respuesta == "no":
                break

            break
            
            
#################################################################################################
    elif categoria == 3:
            cont = 0
            print("...Veremos cuanto sabes de Ciencia...\n")
            sleep(1)
            pregunta1=int(input("""La vida se desarrolla en habitats que brindan las condiciones abioticas necesarias, a esta zona la denominamos?
1)Atmosfera.
2)Geosfera.
3)Biosfera.
4)Troposfera."""))
            if pregunta1 == 3:
                cont +=10
                sleep(1)
                print("Correcto siguiente pregunta...\n")
            elif pregunta1 != 3:
                print("Fallaste siguiente pregunta...\n")
            sleep(1)
            
            pregunta2=int(input("""La evolucion es una propiedad de los seres vivos que se da como consecuancia de:
1)La influencia de cambios ambientales.
2)La capacidad de adaptacion.
3)La capacidad para asegurar la continuidad de la especie.
4)La teoria de la seleccion natural propuesta por Charles Darwin.\n"""))
            sleep(1)
            if pregunta2 == 4:
                cont +=10
                print("Correcto siguiente pregunta...\n")
            elif pregunta2 != 4:
                print("Fallaste siguiente pregunta...\n")
                sleep(1)
                
            pregunta3 = int(input("""¿Como se denominan los organismos que son capaces de fabricar o sintetizar sus propio alimento a partir de sustancias inorganicas como dioxido de carbono, agua y sales minerales?? :
1)Autotrofos.
2)Heterotrofos.
3)Homotrofos.
4)Simbiontes.\n"""))
            sleep(1)
            if pregunta3 == 1:
                cont +=10
                print("Correcto siguiente pregunta...\n")
                sleep(1)
            elif pregunta3 != 1:
                print("Fallaste siguiente pregunta...\n")
            sleep(1)
            
            pregunta4 = int(input("""¿Como se denominan los organismos que son incapaces de producir su alimento e ingieren las sustancias sintetizadas?:
1)Homotrofos
2)Quimiotrofos.
3)Autotrofos.
4)Heterotrofos.\n"""))
            sleep(1)
            if pregunta4 == 4:
                cont +=10
                print("Correcto siguiente pregunta...\n")
            elif pregunta4 != 4:
                print("Fallaste siguiente pregunta...\n")
                sleep(1)
                
            pregunta5 = int(input("""La Entomologia es la Ciencia que estudia los:
1)Insectos.
2)Aves.
3)Peces.
4)Anfibios. \n"""))
            sleep(1)
            if pregunta5 == 1:
                cont +=10
                print("Correcto siguiente pregunta...\n")
                sleep(1)
            elif pregunta5 != 1:
                print("Fallaste siguiente pregunta...\n")
                sleep(1)
                
            pregunta6 = int(input("""señale la opcion incorrecta: los principios inmediatos organicos que estan presentes en los seres vivos son:
1)Los glucidos.
2)Los lipidos.
3)Las sales minerales.
4)Las proteinas. \n"""))
            if pregunta6 == 4:
                cont +=10
                print("Correcto siguiente pregunta...\n")
                sleep(1)
            elif pregunta6 != 4:
                print("Fallaste siguiente pregunta...\n")
                sleep(1)
                
            pregunta7 = int(input("""La ictiologia es la ciencia que estudia:
1)Las aves.
2)Los peces.
3)Los insectos.
4)Los anfibios.\n"""))
            if pregunta7 == 2:
                cont +=10
                print("Correcto siguiente pregunta...\n")
                sleep(1)
            elif pregunta7 !=2:
                print("Fallaste siguiente pregunta...\n")
                sleep(1)
                
            pregunta8 = int(input("""La Ornitologia es la ciencia que estudia:
1)Los Tiburones blancos
2)Los insectos.
3)Las aves.
4)Ninguna de las opciones anteriores es correcta.\n"""))
            if pregunta8 == 3:
                cont +=10
                print("Correcto siguiente pregunta...\n")
                sleep(1)
            elif pregunta8 !=3:
                print("Fallaste siguiente pregunta...\n")
                sleep(1)
                
            pregunta9 = int(input("""La ciencia que estudia los hongos es:
1)La micologia.
2)La briologia.
3)La algologia.
4)La miologia. \n"""))
            if pregunta9 == 1:
                cont +=10
                print("Correcto siguiente pregunta...\n")
                sleep(1)
            elif pregunta9 !=1:
                print("Fallaste siguiente pregunta...\n")
                sleep(1)
            
            pregunta10 = int(input("""La no validez de la teoria de la generacion espontanea fue demostrada con los experimentos realizados por: 
1)Aristoteles.
2)Louis Pasteur.
3)Robert Hooke.
4)Leewenhoke.\n"""))
            if pregunta10 ==2:
                cont +=10
                print("Correcto siguiente pregunta...\n")
                sleep(1)
            elif pregunta10 !=2:
                print("Fallaste siguiente pregunta...\n")
                sleep(1)
            print(nombre," TU PUNTUACION DE CIANCIA ES DE: ",cont)   
            
            instanteFinal = datetime.now()
            tiempo = instanteFinal - instanteInicial # Devuelve un objeto timedelta
            segundos = tiempo.seconds
            
            print("Te tomo ",segundos, " segundo en terminar la categoria.\n")
            respuesta= input("¿Quieres volver a empezar? si o no \n")
            if respuesta=="si":
                continue
            elif respuesta == "no":
                break

            break
              
#################################################################################################
    elif categoria == 4:
            cont = 0
            print("...Veremos cuanto sabes de Frases de peliculas...\n")
            sleep(1)
            pregunta1=int(input("""¿Cual es la frase del Maestro Yoda en el imperio contraataca:
1)Hazlo o no lo hagas.
2)Hazlo o no lo hagas, pero intentalo.
3)Hazlo o no lo hagas, pero no lo intentes.
4)Ninguna es correcta. \n"""))
            if pregunta1 == 3:
                cont +=10
                sleep(1)
                print("Correcto siguiente pregunta...\n")
            elif pregunta1 != 3:
                print("Fallaste siguiente pregunta...\n")
            sleep(1)
            
            pregunta2=int(input("""¿Cual es la frase de Buzz lightyear en toy story?:
1)Eres un juguete.
2)hay una serpiente en mi vota.
3)Hasta el infinito y mas alla.
4)luke, soy tu padre.\n"""))
            sleep(1)
            if pregunta2 == 3:
                cont +=10
                print("Correcto siguiente pregunta...\n")
            elif pregunta2 != 3:
                print("Fallaste siguiente pregunta...\n")
                sleep(1)
                
            pregunta3 = int(input("""Frase de Terminator 2:
1)good bye, baby.
2)Hasta la vista, baby.
3)recorcholis hombre fusion.
4)ninguna es correcta.\n"""))
            sleep(1)
            if pregunta3 == 2:
                cont +=10
                print("Correcto siguiente pregunta...\n")
                sleep(1)
            elif pregunta3 != 2:
                print("Fallaste siguiente pregunta...\n")
            sleep(1)
            
            pregunta4 = int(input("""apollo 13:
1)Houston, tenemos un problema.
2)Houston, tenemos un plan.
3)Houston, we´ve had a problem.
4)2 y 3 son correctas.\n"""))
            sleep(1)
            if pregunta4 == 4:
                cont +=10
                print("Correcto siguiente pregunta...\n")
            elif pregunta4 != 4:
                print("Fallaste siguiente pregunta...\n")
                sleep(1)
                
            pregunta5 = int(input("""Frase de Darth Vader en el Imperio Contraataca:
1)luke, yo soy tu padre.
2)no, yo soy tu padre
3)luke no, tu padre soy yo
4)ninguna es correcta\n"""))
            sleep(1)
            if pregunta5 == 2:
                cont +=10
                print("Correcto siguiente pregunta...\n")
                sleep(1)
            elif pregunta5 != 2:
                print("Fallaste siguiente pregunta...\n")
                sleep(1)
                
            pregunta6 = int(input("""Frase mitica de CasaBlaca:
1)Hasta la vista baby.
2)siempre tendremos houston.
3)simpre tendremos Paris
4)siempre nos quedara Paris\n"""))
            if pregunta6 == 4:
                cont +=10
                print("Correcto siguiente pregunta...\n")
                sleep(1)
            elif pregunta6 != 4:
                print("Fallaste siguiente pregunta...\n")
                sleep(1)
                
            pregunta7 = int(input("""taxi driver:
1)are you talking to me.
2)Hablas conmigo?.
3)Estas hablando conmigo?
4)ninguna es correcta.\n"""))
            if pregunta7 == 1:
                cont +=10
                print("Correcto siguiente pregunta...\n")
                sleep(1)
            elif pregunta7 !=1:
                print("Fallaste siguiente pregunta...\n")
                sleep(1)
                
            pregunta8 = int(input("""Forrest Gump vs jenny:
1)Puede que no sea muy listo, pero se lo que es el amor.
2)sere el capitan de un barco camaronero.
3)Mi mama dice que tonto es el que hace tonterias.
4)2 y 3 son correctas.\n"""))
            if pregunta8 == 1:
                cont +=10
                print("Correcto siguiente pregunta...\n")
                sleep(1)
            elif pregunta8 !=1:
                print("Fallaste siguiente pregunta...\n")
                sleep(1)
                
            pregunta9 = int(input("""El Gladiador:
1)1La muerte nos sonrie a todos, devolvamosle la sonrisa.
2)Esta noche cenaremos en el ades.
3)Tierra y agua, ahi abajo la puedes encontrar
4)ninguna es correcta.\n"""))
            if pregunta9 == 1:
                cont +=10
                print("Correcto siguiente pregunta...\n")
                sleep(1)
            elif pregunta9 !=1:
                print("Fallaste siguiente pregunta...\n")
                sleep(1)
            
            pregunta10 = int(input("""el sexto sentido: 
1)Veo gente de la campora.
2)veo gente muerta.
3)te veo.
4)ninguna de las anteriores.\n"""))
            if pregunta10 ==2:
                cont +=10
                print("Correcto siguiente pregunta...\n")
                sleep(1)
            elif pregunta10 !=2:
                print("Fallaste siguiente pregunta...\n")
                sleep(1)
            print(nombre," TU PUNTUACION DE FRASES DE PELICULAS ES DE: ",cont)
            
            instanteFinal = datetime.now()
            tiempo = instanteFinal - instanteInicial # Devuelve un objeto timedelta
            segundos = tiempo.seconds
            
            print("Te tomo ",segundos, " segundo en terminar la categoria.\n")
            respuesta= input("¿Quieres volver a empezar? si o no \n")
            if respuesta=="si":
                continue
            elif respuesta == "no":
                break

            break
            
#################################################################################################
    elif categoria == 5:
            cont = 0
            print("...Veremos cuanto sabes de Geografia...\n")
            sleep(1)
            pregunta1=int(input("""El aconcagua es el pico mas alto del pais, ¿Cual es el segundo?:
1)tupungato.
2)ojos del salado.
3)monte pissis
4)ninguna es correcta\n"""))
            if pregunta1 == 3:
                cont +=10
                sleep(1)
                print("Correcto siguiente pregunta...\n")
            elif pregunta1 != 3:
                print("Fallaste siguiente pregunta...\n")
            sleep(1)
            
            pregunta2=int(input("""¿Cuanto mide de alto el Glaciar Perito Moreno:
1)60m.
2)70m.
3)80m.
4)150m.\n"""))
            sleep(1)
            if pregunta2 == 1:
                cont +=10
                print("Correcto siguiente pregunta...\n")
            elif pregunta2 != 1:
                print("Fallaste siguiente pregunta...\n")
                sleep(1)
                
            pregunta3 = int(input("""¿Cuanto mide el Salto union, el mas alto de las cataratas del Iguazu?:
1)60m.
2)70m.
3)150m. 
4)80m.\n"""))
            sleep(1)
            if pregunta3 == 4:
                cont +=10
                print("Correcto siguiente pregunta...\n")
                sleep(1)
            elif pregunta3 != 4:
                print("Fallaste siguiente pregunta...\n")
            sleep(1)
            
            pregunta4 = int(input("""En que provincia se encuentra la isla MArtin Garcia?:
1)santa cruz.
2)buenos aires.
3)santa cruz.
4)neuquen.\n"""))
            sleep(1)
            if pregunta4 == 2:
                cont +=10
                print("Correcto siguiente pregunta...\n")
            elif pregunta4 != 2:
                print("Fallaste siguiente pregunta...\n")
                sleep(1)
                
            pregunta5 = int(input("""En que provincia se encuentra el lago traful:
1)Neuquen.
2)Rio negro.
3)Santa cruz.
4)Jujuy.\n"""))
            sleep(1)
            if pregunta5 == 1:
                cont +=10
                print("Correcto siguiente pregunta...\n")
                sleep(1)
            elif pregunta5 != 1:
                print("Fallaste siguiente pregunta...\n")
                sleep(1)
                
            pregunta6 = int(input("""¿Cual es la anchura maxima del Rio de la plata?:
1)119km.
2)219km.
3)319km.
4)ninguna es correcta.\n"""))
            if pregunta6 == 2:
                cont +=10
                print("Correcto siguiente pregunta...\n")
                sleep(1)
            elif pregunta6 != 2:
                print("Fallaste siguiente pregunta...\n")
                sleep(1)
                
            pregunta7 = int(input("""Cual rio argentino es mas extenso?:
1)Parana.
2)Bermejo.
3)Salado del norte.
4)Amazonas.\n"""))
            if pregunta7 == 3:
                cont +=10
                print("Correcto siguiente pregunta...\n")
                sleep(1)
            elif pregunta7 !=3:
                print("Fallaste siguiente pregunta...\n")
                sleep(1)
                
            pregunta8 = int(input("""¿Cuantos volcanes activos hay en el pais?:
1)8..
2)19.
3)37.
4)45.\n"""))
            if pregunta8 == 3:
                cont +=10
                print("Correcto siguiente pregunta...\n")
                sleep(1)
            elif pregunta8 !=3:
                print("Fallaste siguiente pregunta...\n")
                sleep(1)
                
            pregunta9 = int(input("""El gran bajo de San julian, en santa cruz es la maxima depresion del pais.¿Cuantos metros bajo el nivel del mar tiene?:
1)100m.
2)105m.
3)125m.
4)150m.\n"""))
            if pregunta9 == 2:
                cont +=10
                print("Correcto siguiente pregunta...\n")
                sleep(1)
            elif pregunta9 !=2:
                print("Fallaste siguiente pregunta...\n")
                sleep(1)
            
            pregunta10 = int(input("""¿Cual es el lago o laguna mas grande del pais?: 
1)Laguna mar chiquita.
2)Lago argentino.
3)lago nahuel huapi.
4)ninguna es correcta.\n"""))
            if pregunta10 ==1:
                cont +=10
                print("Correcto siguiente pregunta...\n")
                sleep(1)
            elif pregunta10 !=1:
                print("Fallaste siguiente pregunta...\n")
                sleep(1)
            print(nombre," TU PUNTUACION DE DEPORTES ES DE: ",cont)
            
            
            instanteFinal = datetime.now()
            tiempo = instanteFinal - instanteInicial # Devuelve un objeto timedelta
            segundos = tiempo.seconds
            
            print("Te tomo ",segundos, " segundo en terminar la categoria.\n")
            respuesta= input("¿Quieres volver a empezar? si o no \n")
            if respuesta=="si":
                continue
            elif respuesta == "no":
                break

            break
            
#################################################################################################
    elif  categoria == 6:
        print("Saliste de la trivia")
        break
    
    
    else:
            print("No tengo registrada esa categoria")
            break

   
    
        
        


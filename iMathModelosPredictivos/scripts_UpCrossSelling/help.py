'''
Created on 11/06/2015

@author: andrea
'''

def showShortHelp(command):
    if command == 'createModel':
        print "    Uso: crearModelo_UpCrossSelling <fichero entrada> <nombre modelo>"
        print "    Ejemplo: crearModelo_UpCrossSelling train_data.csv UCmodel"
        print "    Mas info: crearModelo_UpCrossSelling --help"
    elif command == 'testModel':
        print "    Uso: testearModelo_UpCrossSelling <fichero entrada> <nombre modelo> <fichero salida>"
        print "    Ejemplo: testearModelo_UpCrossSelling train_data.csv SVCmodel result.txt"
        print "    Mas info: testearModelo_UpCrossSelling --help"
    elif command == 'predictModel':
        print "    Uso: recomendarModelo_UpCrossSelling <fichero entrada> <nombre modelo> <fichero salida>"
        print "    Ejemplo: recomendarModelo_UpCrossSelling predict_data.csv SVCmodel result.txt"
        print "    Mas info: recomendarModelo_UpCrossSelling --help"

def showExtendedHelp(command):
    if command == 'createModel':
        print "    Uso: crearModelo_UpCrossSelling <fichero entrada> <nombre modelo>"
        print "    Parametros:"
        print "        <fichero entrada>  : path completo del fichero que contiene los datos para crear el modelo"
        print "        <nombre modelo>    : nombre que sera asociado al modelo creado. Este nombre seraaaaaaa usado mas tarde en el"
        print "                             testeo del modelo o prediccion de nuevas muestras "
        print "    Ejemplo: crearModelo_UpCrossSelling train_data.csv UCmodel"
    elif command == 'testModel':
        print "    Uso: testearModelo_UpCrossSelling <fichero entrada> <nombre modelo> <fichero salida>"
        print "    Parametros:"
        print "        <fichero entrada>  : path completo del fichero que contiene los datos para testear el modelo"
        print "        <nombre modelo>    : nombre dado al modelo previamente creado"
        print "        <fichero salida>   : path completo del fichero donde los resultos del testing son almacenados"
        print "    Ejemplo: testearModelo_UpCrossSelling train_data.csv SVCmodel result.txt"
    elif command == 'predictModel':
        print "    Uso: recomendarModelo_UpCrossSelling <fichero entrada> <nombre modelo> <fichero salida>"
        print "    Parametros:"
        print "        <fichero entrada>  : path completo del fichero que contiene las muestras de datos para ser clasificadas"
        print "        <nombre modelo>    : nombre dado al modelo previamente creado"
        print "        <fichero salida>   : path completo del fichero donde los resultos de la prediccion son almacenados"
        print "    Ejemplo: recomendarModelo_UpCrossSelling predict_data.csv SVCmodel result.txt"

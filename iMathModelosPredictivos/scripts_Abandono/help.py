'''
Created on 11/06/2015

@author: andrea
'''

def showShortHelp(command):
    if command == 'createModel':
        print "    Uso: crearModelo_Abandono <fichero entrada> <clasificador> <nombre modelo>"
        print "    Ejemplo: crearModelo_Abandono train_data.csv SVC SVCmodel"
        print "    Mas info: crearModelo_Abandono --help"
    elif command == 'testModel':
        print "    Uso: testearModelo_Abandono <fichero entrada> <nombre modelo> <fichero salida>"
        print "    Ejemplo: testearModelo_Abandono train_data.csv SVCmodel result.txt"
        print "    Mas info: testearModelo_Abandono --help"
    elif command == 'predictModel':
        print "    Uso: predecirModelo_Abandono <fichero entrada> <nombre modelo> <fichero salida>"
        print "    Ejemplo: predecirModelo_Abandono predict_data.csv SVCmodel result.txt"
        print "    Mas info: predecirModelo_Abandono --help"

def showExtendedHelp(command):
    if command == 'createModel':
        print "    Uso: crearModelo_Abandono <fichero entrada> <clasificador> <nombre modelo>"
        print "    Parametros:"
        print "        <fichero entrada>  : path completo del fichero que contiene los datos para crear el modelo"
        print "        <clasificador>     : determina la tecnica a emplear para crear el modelo. Los valores posible de este"
        print "                             parametro son: DecisionTreeClassifier, SVC, RandomForestClassifier"
        print "        <nombre modelo>    : nombre que sera asociado al modelo creado. Este nombre sera usado mas tarde en el"
        print "                             testeo del modelo o prediccion de nuevas muestras "
        print "    Ejemplo: crearModelo_Abandono train_data.csv SVC SVCmodel"
    elif command == 'testModel':
        print "    Uso: testearModelo_Abandono <fichero entrada> <nombre modelo> <fichero salida>"
        print "    Parametros:"
        print "        <fichero entrada>  : path completo del fichero que contiene los datos para testear el modelo"
        print "        <nombre modelo>    : nombre dado al modelo previamente creado"
        print "        <fichero salida>   : path completo del fichero donde los resultos del testing son almacenados"
        print "    Ejemplo: testearModelo_Abandono train_data.csv SVCmodel result.txt"
    elif command == 'predictModel':
        print "    Uso: predecirModelo_Abandono <fichero entrada> <nombre modelo> <fichero salida>"
        print "    Parametros:"
        print "        <fichero entrada>  : path completo del fichero que contiene las muestras de datos para ser clasificadas"
        print "        <nombre modelo>    : nombre dado al modelo previamente creado"
        print "        <fichero salida>   : path completo del fichero donde los resultos de la prediccion son almacenados"
        print "    Ejemplo: predecirModelo_Abandono predict_data.csv SVCmodel result.txt"
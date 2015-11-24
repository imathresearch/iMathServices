'''
Created on 28/09/2015

@author: iMath
'''

def showShortHelp(command):
    if command == 'createModel':
        print "    Uso: crearModelo_Abandono <fichero entrada> <clasificador> <nombre modelo>"
        print "    Ejemplo: crearModelo_Abandono train_data.csv SVC SVCmodel"
        print "    Mas info: crearModelo_Abandono --help"
    
def showExtendedHelp(command):
    if command == 'createModel':
        print "    Uso: crearModelo_Abandono <fichero entrada> <clasificador> <nombre modelo>"
        print "    Parametros:"
        print "        <fichero entrada>  : path completo del fichero que contiene los datos para crear el modelo"
        print "        <clasificador>     : determina la tecnica a emplear para crear el modelo. Los valores posible de este"
        print "                             parametro son: DecisionTreeClassifier, SVC, RandomForestClassifier"
        print "        <nombre modelo>    : nombre que será asociado al modelo creado. Este nombre será usado mas tarde en el"
        print "                             testeo del modelo o prediccion de nuevas muestras "
        print "    Ejemplo: crearModelo_Abandono train_data.csv SVC SVCmodel"

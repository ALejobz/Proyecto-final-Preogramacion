from flask import Flask, request, g, redirect, url_for, render_template, flash, session
import flask
import sys
from flask import json

app = Flask(__name__)

#inicializacion de variables
registro = "registro.txt"
loginTemp = []
error = ""
usuario = ""
origenTemp = ""
destinoTemp = ""
aerolineaTemp = ""
vueloTemp = []

#llamamos la pagina principal
@app.route('/',methods = ['GET','POST'])
def main():
    
    return render_template('inicio.html')

#pagina para el login y el registro
@app.route('/procesoIniciar',  methods = ['GET','POST'])
def procesoIniciar():
    
    if request.method == 'POST':
        #con el boton el cual ingresamos a nuestra pagina de reservas
        if(request.form['boton'] == "Login"):
            vi = []
            #se piden ususarios y contraseña
            nombreUsuario = request.form['user']
            contraseña = request.form['password']
            #se abre el archivo donde estan los registros
            arch = open(registro, 'r+')
            for line in arch:
                v = line.split()
                vi.append(v)
            #se busca el usuario y la contraseña para ver si coinciden
            for i in range(0,len(vi)):
                if vi[i+1][0] == nombreUsuario and vi[i+1][2] == contraseña:
                   usuario = nombreUsuario
                   return redirect(url_for('reservo'))
            
                else: 
                  error = "Usuario o contraseña incorrectos"
                  return render_template('inicio.html', error = error)
            arch.close()
        #opcion para registrsrnos 
        elif(request.form['boton'] == "Registro"):
            return redirect(url_for('registrarse'))
        
        
#Template para podernos registrar
@app.route('/registrar',methods = ['GET','POST'])
def registrarse():

    return render_template('registro.html')

#Proceso de registro 
@app.route('/procesoRegistrarse',methods = ['GET','POST'])
def procesoRegistrarse():
    # en esta parte nos registramos para acceder a 
        if request.form['but'] == "Registrarse":
            if request.form['user'] != "" or request.form['pass'] != "":
                username = request.form['user']
                password = request.form['pass']
                #se abre el archivo y se le escriben el username y el password
                archivo = open(registro,'a')
                archivo.write(username + " | " + password + "\n")
                archivo.close()
                return render_template('inicio.html')
            else:
                flash('Relllena bien los campos!')
                return redirect(url_for('registrarse'))

@app.route('/reservo',methods = ['GET','POST'])
def reservo():

    return render_template('login.html', usuario=usuario)

@app.route('/reservar',methods = ['GET','POST'])
def reservar():

    global vueloTemp,datos,lenDatos
    
    if request.method == 'POST':
        if request.form['boton'] == "Reservar":
                    archivo = "vuelos.txt"
                    vuelos = []
                    datos = []
                    vueloTemp = []
                    
                    e = open(archivo,'r+')
                    for line in e:
                        vuelos += ([line][0:44])

                    for i in range(0,len(vuelos)):
                        datos += [{'aerolinea':vuelos[i][0:2],'vuelo':vuelos[i][3:6],
                              'origen':vuelos[i][8:11],'horaSalida':vuelos[i][12:17],
                              'llegada':vuelos[i][19:22],'horaLlegada':vuelos[i][23:28],
                              'comida':vuelos[i][30:32],'paradas':vuelos[i][36:37],
                              'avion':vuelos[i][41:44]}]

                    e.close()

                    origen = request.form['salida']
                    destino = request.form['llegada']
                    paradas = request.form['Confirm']

                    if origen == "Albuquerque":
                        origen = "ABQ"
                    elif origen == "Atlanta":
                        origen = "ATL"
                    elif origen == "Nashville":
                        origen = "BNA"
                    elif origen == "Boston":
                        origen = "BOS"
                    elif origen == "Washington":
                        origen = "DCA"
                    elif origen == "Denver":
                        origen = "DEN"
                    elif origen == "Dallas":
                        origen = "DFW"
                    elif origen == "Detroit":
                        origen = "DTW"
                    elif origen == "Houston":
                        origen = "HOU"
                    elif origen == "New York":
                        origen = "JFK"
                    elif origen == "Los Angeles":
                        origen = "ALX"
                    elif origen == "Miami":
                        origen = "MIA"
                    elif origen == "Minneapolis":
                        origen = "MSP"
                    elif origen == "New Orleans":
                        origen = "MSY"
                    elif origen == "Chicago":
                        origen = "ORD"
                    elif origen == "Philadelphia":
                        origen = "PHL"
                    elif origen == "Phoenix":
                        origen = "PHX"
                    elif origen == "Providence":
                        origen = "PVD"
                    elif origen == "Raleigh":
                        origen = "RDU"
                    elif origen == "Seattle":
                        origen = "SEA"
                    elif origen == "San Francisco":
                        origen = "SFO"
                    elif origen == "St Louis":
                        origen = "STL"
                    elif origen == "Tampa":
                        origen = "TPA"
                    else:
                        print("Introduzca bien los datos")

                    if destino == "Albuquerque":
                        destino = "ABQ"
                    elif destino == "Atlanta":
                        destino = "ATL"
                    elif destino == "Nashville":
                        destino = "BNA"
                    elif destino == "Boston":
                        destino = "BOS"
                    elif destino == "Washington":
                        destino = "DCA"
                    elif destino == "Denver":
                        destino = "DEN"
                    elif destino == "Dallas":
                        destino = "DFW"
                    elif destino == "Detroit":
                        destino = "DTW"
                    elif destino == "Houston":
                        destino = "HOU"
                    elif destino == "New York":
                        destino = "JFK"
                    elif destino == "Los Angeles":
                        destino = "ALX"
                    elif destino == "Miami":
                        destino = "MIA"
                    elif destino == "Minneapolis":
                        destino = "MSP"
                    elif destino == "New Orleans":
                        destino = "MSY"
                    elif destino == "Chicago":
                        destino = "ORD"
                    elif destino == "Philadelphia":
                        destino = "PHL"
                    elif destino == "Phoenix":
                        destino = "PHX"
                    elif destino == "Providence":
                        destino = "PVD"
                    elif destino == "Raleigh":
                        destino = "RDU"
                    elif destino == "Seattle":
                        destino = "SEA"
                    elif destino == "San Francisco":
                        destino = "SFO"
                    elif destino == "St Louis":
                        destino = "STL"
                    elif destino == "Tampa":
                        destino = "TPA"
                    else:
                        print("Introduzca bien los datos")

                    for i in range(0,len(datos)):
                        if datos[i]['origen'] == origen and datos[i]['llegada'] == destino:
                            vueloTemp.append(datos[i])

                    for i in range(0,len(vueloTemp)):
                        vueloTemp[i]['horaSalida'] = (vueloTemp[i]['horaSalida'][0:2] + ":" + vueloTemp[i]['horaSalida'][2:4] + " " + vueloTemp[i]['horaSalida'][4] + "M")
                        vueloTemp[i]['horaLlegada'] = (vueloTemp[i]['horaLlegada'][0:2] + ":" + vueloTemp[i]['horaLlegada'][2:4] + " " + vueloTemp[i]['horaLlegada'][4] + "M")

                    lenDatos = len(vueloTemp)
                    return redirect(url_for('reserva'))
        else:
            error2 = "Introduzca datos validos"
            return redirect(url_for('reserva',error2=error2))
            
        

@app.route('/muestraReserva',methods = ['GET','POST'])
def reserva():

    global vueloTemp, datos, lenDatos

    return render_template('reserva.html',vueloTemp=vueloTemp, lenDatos=lenDatos)





                
                    
                
            
if __name__ == '__main__':
    app.run(debug = True)


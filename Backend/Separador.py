from xml.etree import ElementTree as ET
import re
import matplotlib.pyplot as plt
global conteo_todo
class analizar:
    def expresiones(self):
        x = open("entrada.xml", "r")
        tree = ET.parse(x)
        root = tree.getroot()
        fecha = r"([\d.]+/[\d.]+/[\d.]+)"
        correo = r"([\w.%+-]+@[\w.-]+.[a-zA-Z])"
        horrror = r"(E[\w.]+:\s[\d.]+)"
        fechas = []
        correos = []
        errores = []
        keys = []
        horrores = []
        nueva_fecha = []
        todo = []
        tupla = []
        fechas_listas = []
        reportados = []
        solo_reportados  = []
        para_todo = []
        en_posicion0 = []
        global conteo_todo
        conteo_todo = []
        conteo_todo_con_user = []
        escritura = []
        primera_posicion = []
        el_resto = []
        totales = []
        contUsuario = 0
        contError = 0
        contUser = 0

        for elemento in root:
            texto = elemento.text
            fechas_encontradas = re.findall(fecha, texto)
            fechas.append(fechas_encontradas)
            #################################################
            correo_encontradas = re.findall(correo, texto)
            correos.append(correo_encontradas)
            #################################################
            errores_encontradas = re.findall(horrror, texto)
            sp = errores_encontradas[0]
            spl = sp.split(":")
            tt = correo_encontradas[1]
            #################################################
            todo.append([fechas_encontradas[0], correo_encontradas[0], spl[1]])
        for i in fechas:
            for j in i:
                fechas_listas.append(j)
        tuplaa = dict.fromkeys(fechas_listas).keys()
        for k in tuplaa:
            keys.append(k) #Array de fechas sin repetir
        for corre in correos:
            reportados.append(corre[0])

        tupla_report = dict.fromkeys(reportados).keys()
        for l in tupla_report:
            solo_reportados.append(l)  #Array de nombre sin repetir

        Longitud_todo = len(todo)
        for sub in keys:
            for i in range(Longitud_todo):
                current = todo[i]
                if sub == current[0]:
                    user = current[1]
                    error = current[2]
                    dimUser = len(user)
                    dimError = len(error)
                    if dimUser != 0 and dimError != 0:
                        contUsuario += 1
                        contError += 1
            conteo_todo_con_user.append([sub, contUsuario,contError])
            totales.append(contUsuario)
            contUsuario = 0
            contError = 0
        for sub in solo_reportados:
            for subDate in keys:
                for i in range(Longitud_todo):
                    current = todo[i]
                    if subDate == current[0]:
                        if sub == current[1]:
                            user = current[1]
                            contUser += 1
                if contUser != 0:
                    conteo_todo.append([subDate, sub, contUser])
                    contUser = 0
        for i in conteo_todo:
            print("Fecha: "+ str(i[0]) +"\n"+"Email: "+ str(i[1])+ "\n" + "Canridad Mensajes:"+ str(i[2]))

        for i, j, k  in zip(conteo_todo, conteo_todo_con_user, todo):
            nuevo = '''\t<ESTADISTICA>
                <FECHA>'''+str(i[0])+'''</FECHA>
                <CANTIDAD_MENSAJES>'''+str(j[1])+'''</CANTIDAD_MENSAJES>
                <REPORTADO_POR>
                <USUARIO>
                    <EMAIL>'''+str(i[1])+'''</EMAIL>
                    <CANTIDAD_MENSAJES>'''+str(i[2])+'''</CANTIDAD_MENSAJES>
                </USUARIO>
                </REPORTADO_POR>
                <AFECTADOS>
                    <AFECTADO></AFECTADO>
                </AFECTADOS>
                <ERRORES>
                    <ERROR>
                        <CODIGO>'''+k[2]+'''</CODIGO>
                        <CANTIDAD_MENSAJES></CANTIDAD_MENSAJES>
                    </ERROR>
                </ERRORES>
            </ESTADISTICA>\n'''
            escritura.append(nuevo)
        myfile = open("estadisticas.xml", "w")
        myfile.write('<ESTADISTICAS>'+ "\n")
        for r in escritura:
            myfile.write( str(r))
        myfile.write("\n"+'</ESTADISTICAS>')

    def peticion_fechas(self, fecha):
        correos_grafica = []
        numero_n_veces = []
        global conteo_todo
        for p in conteo_todo:
            j = str(p).find(str(fecha))
            if j >= 2:
                correos_grafica.append(p[1])
                numero_n_veces.append(p[2])

        colores = ['#025DE0', '#0BC1B9', '#ACDC0A', '#F6920B', '#F0FF00', '#E01002', '#3C3B3D']
        fechas = correos_grafica
        primas = numero_n_veces
        plt.bar(range(len(correos_grafica)), primas, edgecolor='black', color=colores)
        plt.xticks(range(len(correos_grafica)), fechas, rotation=60)
        plt.title(str(fecha))
        plt.ylim(min(primas) - 1, max(primas) + 1)
        plt.savefig("C:/Users/Carlos Rangel/Documents/GitHub/IPC2_Proyecto3_201907636/App/Aplicacion/static/Grafica_fechas.png")











import requests as req
import os
import time as t

os.system('cls')
url = 'https://s3.amazonaws.com/archivo.computo/actas/'
# https://computo.oep.org.bo/



#Santa Cruz = 70001/79016
scz = True
sczPathDo = 'SantaCruz/'
sczInicio = 71805
sczFinals = 79016

#Tarija = 60001/61856
trja = False
trjaPathDo = 'Tarija/'
trjaInicio = 60001
trjaFinals = 61856

#Cochabamba = 30001/36390
cbba = False
cbbaPathDo = 'cbba/'
cbbaInicio = 30000
cbbaFinals = 36390

# ===========================================================
if scz == True:
    Inicio = sczInicio
    Finals = sczFinals
    PathDo = sczPathDo
elif trja == True:
    Inicio = trjaInicio
    Finals = trjaFinals
    PathDo = trjaPathDo
# ===========================================================
tope = Inicio + 2
while (Inicio <= Finals):
    documento = str(Inicio)+'.jpg'
    web = req.get(url+documento)
    
    si_es_valido = web.status_code
    os.system('echo '+str(si_es_valido)+' '+str(Inicio) + '>> '+PathDo+'log')
    if (si_es_valido == 200):
        if (os.path.isfile(PathDo+documento)):
            print ('Ya existe.....:', documento)
        else:
            with open(str(PathDo)+documento, 'wb') as f:
                f.write(web.content)
            print ('Archivo creado.:', documento)
    # ===========================================
    #t.sleep(1)
    #if (Inicio == tope):
    #    break
    Inicio = Inicio + 1
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
import random;

def seleccion(arreglo):
    random.shuffle(arreglo);
    ultimo=len(integrantes)-1
    aux=[];
    for i in range (len(arreglo)):
        if (i==ultimo):
            if (arreglo[0]['nombre'] in arreglo[ultimo]['excepciones']):
                aux.clear();
                seleccion(arreglo);
            else:
                aux.append([arreglo[ultimo],arreglo[0]]);
              
                    
        else:
            if (arreglo[i+1]['nombre'] in arreglo[i]['excepciones']):
                aux.clear();
                seleccion(arreglo);
            else:
                aux.append([arreglo[i],arreglo[i+1]]);
           
    return(aux);     

integrantes=[{'nombre':'Integrante1','regalos':'Regalos1\nRegalos1.1','excepciones':['Integrante2'],'correo':'Integrante1@gmail.com'},
             
             {'nombre':'Integrante2','regalos':'Regalos2','excepciones':['Integrante3','Integrante1'],'correo':'Integrante2@gmail.com'},
             
             {'nombre':'Integrante3','regalos':'Sin sugerencias','excepciones':[],'correo':'Integrante3@gmail.com'},
             
             {'nombre':'Integrante4','regalos':'Regalo3\nRegalo3.1\nRegalo3.2','excepciones':[],'correo':'Integrante4@gmail.com'}]



#Se pueden poner cuantos integrantes se deseen siempre cumpliendo la estructura del diccionario

#Para crear una excepción o más, solo hace falta introducir el/los nombre/s de los integrantes exactamente como estén registrados respectivamente



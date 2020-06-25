#importacion de modulo casos -> Documento casos.py; contiene los casos A y B en cadena de texto
import casos as caso
#importacion de modulos Estandar
import json,os
#Clase Principal
class principal:
    #Definicion de propiedades principales para la clase
    def __init__(self):
        #Alfabeto completo
        self._alfabeto = ["s","x","o","c","q","n","m","w","p","f","y","h","e","l","j","r","d","g","u","i"]
        #Clasificacion de alfabeto
        #Foo letras
        self._foo_letras = ["u","d","x","s","m","p","f"]
        #Letras de barra
        #Comprehension de lista para definir las letras que se encuntran en el alfabeto que son diferentes a la lista de Foo letras
        self._letras_de_barra = [item for item in self._alfabeto if not item in self._foo_letras]
        self._numero_bonito = 81827
    #Llamados Get para propiedades de la clase
    @property
    def get_alfabeto(self):
        return self._alfabeto
    @property
    def get_letras_barra(self):
        return self._letras_de_barra
    @property
    def get_foo_letras(self):
        return self._foo_letras
    

    #Funcion que devuelve 
    #verdadero si una palabra es una preposicion
    #falso si la palabra no es una preposicion 
    def preposiciones(self,palabra):
        #Propiedad foo_letra
        foo_letra = self._foo_letras
        #tamaño de la palabra
        tamano_palabra = len(str(palabra))
        #condicional para verificar tamaño adecuado del verbo
        if (tamano_palabra == 6):
            #verificar ultima letra en foo letras
            if(palabra[tamano_palabra-1] in foo_letra):
                contador_letras = 0
                for letra_palabra in palabra:
                    #verificar u dentro de la palabra
                    if letra_palabra == "u":
                        return False
                    contador_letras += 1
                    if contador_letras == tamano_palabra:
                        return True
        else:
            return False
    
    #Funcion que devuelve 
    #1 si una palabra es un verbo 
    #2 si la palabra ademas de ser verbo el se flexiona en su forma subjuntiva
    #0 si la palabra no es verbo
    def verbos(self,palabra):
        #tamaño de la palabra
        tamano_palabra = len(str(palabra))
        #condicional para verificar tamaño adecuado del verbo
        if (tamano_palabra >= 6):
            #si ultima letra de la palbra esta en la lista de letras de barra
            if(palabra[tamano_palabra-1] in self._letras_de_barra):
                #si primera letra de la palbra esta en la lista de letras de barra
                if(palabra[0] in self._letras_de_barra):
                    return 2
                else:
                    return 1
            else:
                return 0
        else:
            return 0

    #Funcion que devuelve 
    #Valor de numero en Heroglon
    def numeros(self,numeros):
        #sumatoria total de numero heroglonm
        sumatoria_numero = 0
        #Multiplicador por unidades vigecimales etc... 1, 20, 400 etc...
        multiplicador = 1
        #Iteracion en numeros
        for numero in numeros:
            contador_numeros = 0
            #Iteracion para captar valor de numero en alfabeto
            for item in self._alfabeto:
                if(numero == item):
                    nuevo_numero = contador_numeros * multiplicador
                    sumatoria_numero = sumatoria_numero + nuevo_numero
                contador_numeros += 1
            multiplicador *= 20
        #Retorno de valor total
        return sumatoria_numero



    #Funcion que devuele
    #Verdadero si el numero se considera un numero bonito en herogun
    #Falso si el numero no se considera un numero bonito en herogun
    def numero_bonito(self,numero):
        #Condicion con valor en  propiedad = 81827 y si es multiplo de 3
        if(numero >= self._numero_bonito and numero % 3 == 0):
           return True
        else:
            return False


    #Funcion de limpieza para la entrada de palabras para lista que se enviara a ordenar
    #Segun alfabeto
    def limpieza_palabras(self,lista_palabras):
        lista_limpia = []
        for letra_palabra in lista_palabras:
            if(letra_palabra != '\n' and letra_palabra != ''):
                letra_palabra = letra_palabra.replace("\n","")
                letra_palabra = letra_palabra.replace("\u200b","")
                lista_limpia.append(letra_palabra)
        return lista_limpia


    #Funcion para determinar las palabras en orden ascendente segun alfabeto 
    #Devuleve lista con dos elementos
    #palabra con menor valor en orden ascendente, palabra con mayor valor en orden ascendente  
    def palabra_mayor(self,palabra_a,palabra_b):
        #lista vacia para asignar la palabra con menos caracteres a la izquierda
        #y con mas caracteres a la derecha
        lista_palabras = []
        #condicionale para determinar el orden de las palabras con menos y mas caracteres
        #con el fin de iterar sobre la palabra que tenga menos caracteres
        if int(len(palabra_a)) > int(len(palabra_b)):
            lista_palabras.append(palabra_b)
            lista_palabras.append(palabra_a)
        if int(len(palabra_a)) <= int(len(palabra_b)):
            lista_palabras.append(palabra_a)
            lista_palabras.append(palabra_b)
        #Iteracion de palabra con menos caracteres
        for index_palabra in range(0,len(lista_palabras[0])):
            #Comprehension de lista que trae los valores de cada letra en su ubicacion en el alfabeto
            valor_letra_palabra_a = [i for i in range(0,len(self._alfabeto)) if lista_palabras[0][index_palabra] == self._alfabeto[i]]
            valor_letra_palabra_b = [i for i in range(0,len(self._alfabeto)) if lista_palabras[1][index_palabra] == self._alfabeto[i]]
            #Verificacion de valor mayor o menor en cada letra para retornar lista
            #con palabra con menor valor ascendente a la izquierda
            #y mayor valor a la derecha segun alfabeto
            if(valor_letra_palabra_a < valor_letra_palabra_b):
                return [lista_palabras[0],lista_palabras[1]]
            if(valor_letra_palabra_b < valor_letra_palabra_a):
                return [lista_palabras[1],lista_palabras[0]]
        return [lista_palabras[0],lista_palabras[1]]

    #funcion de ordenamiento
    #recibe lista de palabras en donde se devuelve el valor menor de la lista
    #segun orden en alfabeto
    def ordenamiento_alfabetico(self,lista_palabras):
        #variable que guarda valor menor temporal
        menor = ""
        #iteracion 
        for palabra_compara in lista_palabras:
            #En caso de estar vacia la variable menor se asigna
            #la primera palabra de la lista
            if(menor == ""):
                menor = palabra_compara
            else:
                #El proceso continua asignando la palabra de menor val,or ascendente
                #segun alfabeto por cada letra de la lista
                lista_menor = self.palabra_mayor(palabra_compara,menor)
                #se asigna la primera posicion de la lista resultante, en este caso seria la palabra menor
                menor = lista_menor[0]
        #retorno de palabra menor al pasar por toda la lista
        return menor
        

#Proceso que crea instancias de la clase proncipal y envia procesos por cada instancia
if __name__ == '__main__':
    #Funcion de procesamiento 
    #primer parametro variable con caso de script importado
    #Segundo parametro booleano en donde se especifica si el resultado sobreescribe o no
    #Los resultados guardados en el docuemnto Json
    #Tercer parametro titulo de la fuente (Casos)
    def procesar(caso,borrar_resultados,titulo):
        #Contadores para resultados
        contador_preposiciones = 0
        contador_verbos = 0
        contador_verbos_forma_subjuntiva = 0
        contador_verbos_forma_no_subjuntiva = 0
        contador_numeros_bonitos = 0

        #listas para ordenamiento de palabras
        lista_vocabulario = []
        lista_vocabulario_ordenado = []
        lista_numeros_bonitos = []
        #instancia de clase para proceso
        heroglon_ejemplo = principal()
        #Separacion de palabras por espacios entre cada una
        palabras_entrada_a_revisar = str(caso).split(" ")
        #Se pasa la lista a funcion de limpieza de texto
        lista_vocabulario = heroglon_ejemplo.limpieza_palabras(palabras_entrada_a_revisar)
        # Se traen valores de alfabeto
        alfabeto = heroglon_ejemplo.get_alfabeto
        #Lista para guardar valores de ordenamiento de vocavulario
        lista_procesada = []
        #Validacion hasta que la lista vocabulario se encuentre vacia
        #Se usa para crear iteracion de ciclos de ordenamiento hasta que todos los valores 
        #queden ordenados, se usa la lista vocabulario como medidor de valores que no han sido ordenados aun
        ordenar = True
        #lista total en donde se guardan los valores originales de la lista vocabulario
        #Para Depuracion
        lista_total = lista_vocabulario
        #Ciclo mientras haya valores en la lista vocabulario este continua enviando
        #Funcion de ordenamiento en lista sobrante
        while(ordenar):
            #Resultado de ordenamiento de lista vocabulario
            #Devuelve la palabra con menor valor ascendente en el alfabeto
            ordenada = heroglon_ejemplo.ordenamiento_alfabetico(lista_vocabulario)
            #Si la variable de la cadena de texto ya se encuentra en la lista procesada
            #la cual es la lista que guarda todas las palabras ordenadas de manera ascendente
            #Se elimina de la lista vocabulario y no se adiciona a la lista procesada
            if ordenada in lista_procesada:
                lista_vocabulario.remove(ordenada)
            #En caso de que la variable ordenada no se encuentre en la lista procesada
            #Se adiciona a la lista procesada y se elimina en la lista de vocabulario
            else:
                lista_procesada.append(ordenada)
                lista_vocabulario.remove(ordenada)
            #Si la lista vocabulario ya no contiene palabras se cambia valor de varible ordenar
            #Para terminar ciclo While
            if len(lista_vocabulario) == 0:
                ordenar =False
        #Envio hacia funciones de validacion de palabras y numeros
        #iteracion de la lista procesada
        for item_lista_palabras in lista_procesada:
            #Validacion de Preposiciones
            resultado_preposiciones = heroglon_ejemplo.preposiciones(item_lista_palabras)
            #En caso de devolver un verdadero desde la funcion se suma contador de preposiciones
            if resultado_preposiciones == True:
                contador_preposiciones += 1

            #Validacion de Verbos
            resultado_verbos = heroglon_ejemplo.verbos(item_lista_palabras)
            #En caso de devolver un 1 desde la funcion se suma contador_verbos_forma_no_subjuntiva
            if resultado_verbos == 1:
                contador_verbos_forma_no_subjuntiva += 1
            #En caso de devolver un 2 desde la funcion se suma contador_verbos_forma_no_subjuntiva
            if resultado_verbos == 2:
                contador_verbos_forma_subjuntiva += 1
            #Sumatoria de vervos con forma subjuntiva y sin forma subjuntiva
            contador_verbos_total = contador_verbos_forma_no_subjuntiva + contador_verbos_forma_subjuntiva


            #Conversion de palabrta en numero Heruglon
            resultado_numeros = heroglon_ejemplo.numeros(item_lista_palabras)
            #validacion si el resultado de numero se considera numero bonito
            resultado_numeros_bonitos = heroglon_ejemplo.numero_bonito(resultado_numeros)
            #si la funcion numero bonito devuelve verdadero 
            if resultado_numeros_bonitos == True:
                #Si el numero no se encuentra en la lista de numeros bonitos 
                #se suma el contador de numeros bonitos y 
                #se adiciona este numero a la lista de numeros bonitos para futuras validaciones
                if not resultado_numeros in lista_numeros_bonitos: 
                    contador_numeros_bonitos += 1
                    lista_numeros_bonitos.append(resultado_numeros)
        #impresion de Resultados
        print("Vocabulario Ordenado "+str(lista_procesada))
        print("Preposiciones "+str(contador_preposiciones))
        print("Verbos no Subjuntivos "+str(contador_verbos_forma_no_subjuntiva))
        print("Verbos Subjuntivos "+str(contador_verbos_forma_subjuntiva))
        print("Verbos "+str(contador_verbos_total))
        print("Numeros Bonitos "+str(contador_numeros_bonitos))
        print("_"*20)
        resultados={
            "fuente":str(titulo),
            "Vocabulario ordenado":lista_procesada,
            "Preposiciones":str(contador_preposiciones),
            "Verbos no Subjuntivos":str(contador_verbos_forma_no_subjuntiva),
            "Verbos Subjuntivos ":str(contador_verbos_forma_subjuntiva),
            "Verbos":str(contador_verbos_total),
            "Numeros Bonitos":str(contador_numeros_bonitos)
            }
        if borrar_resultados == True:
            with open(os.getcwd()+'\\resultados.json', 'w') as fileresultados:
                objdoc = {"resultados":[]}
                json.dump(objdoc, fileresultados,indent=5)
        with open(os.getcwd()+'\\resultados.json', 'r') as fileresultados:
            objdoc = json.load(fileresultados)

        with open(os.getcwd()+'\\resultados.json', 'w') as fileresultados:
            objdoc['resultados'].append(resultados)
            json.dump(objdoc, fileresultados,indent=5)
    
    #Envio de proceso para cada caso, se envia parrametro de variable con cada caso
    #El resultado se exporta a un json y se imprime por pantalla
    #
    #El segundo parametro es para sobreescribir el documento
    #
    #Tercer parametro titulo de la fuente (Casos)
    procesar(caso.a,True,"caso A")
    procesar(caso.b,False,"caso B")




# -*- coding: utf-8 -*-
#!/usr/bin/python

from itertools import product

# Circuito1
# circuito1
# CircuitoSolucao= [ (1, 'XOR', 1, [(0, 1), (0, 1)]),
#             (2, 'XOR', 2, [(1, 2), (0, 2)]),
#             (3, 'AND', 2, [(1, 3), (0, 3)]),
#             (4, 'AND', 2, [(0, 4), (0, 4)]),
#             (5, 'OR', 3, [(3, 4), (4, 4)])
#             ]
# probC1 = (2*0.4)+

# camadas = 3 
# portas = 4 
# # Circuito2
# # circuito2 G 16
# CircuitoSolucao= [ (1, 'XNOR', 1, [(0, 1), (0, 1)]),
#             (2, 'XOR', 2, [(1, 2), (0, 2)]),
#             (3, 'NOT', 2, [(2, 3), (2, 3)]),
#             (4, 'NAND', 3, [(1, 4), (2, 4)]) ]

# camadas = 3
# portas = 5 
# # circuito2 G 17
# CircuitoSolucao= [ (1, 'NAND', 1, [(0, 1), (0, 1)]),
#             (2, 'XOR', 2, [(0, 2), (0, 2)]),
#             (3, 'NAND', 2, [(2, 3), (2, 3)]),
#             (4, 'NAND', 2, [(2, 4), (0, 4)]),
#             (5, 'NAND', 3, [(2, 4), (3, 4)])  ]


# camadas = 1
# portas = 3 
# # circuito3 P1
# CircuitoSolucao= [ (1, 'NAND', 1, [(0, 1), (0, 1)]),     
#             (2, 'OR', 1, [(0, 2), (0, 2)]),            
#             (3, 'OR', 2, [(1, 2), (2, 3)])]


# camadas = 1
# portas = 5 
# # circuito3 P2
# CircuitoSolucao= [ (1, 'OR', 1, [(0, 1), (0, 1)]),            
#             (2, 'AND', 1, [(0, 2), (0, 2)]),
#             (3, 'OR', 2, [(1, 3), (2, 3)]),
#             (3, 'NAND', 1, [(0, 4), (0, 4)]),
#             (5, 'OR', 3, [(3, 5), (4, 5)])]

# camadas = 1
# portas = 4 
#  # circuito4 P1
# CircuitoSolucao= [ (1, 'NAND', 1, [(0, 1), (0, 1)]),            
#             (2, 'NAND', 1, [(0, 2), (0, 2)]),
#             (3, 'NAND', 2, [(0, 3), (1, 3)]),
#             (4, 'NAND', 3, [(1, 4), (3, 4)])]


camadas = 1
portas = 4
 # circuito4 P2
CircuitoSolucao= [ (1, 'AND', 1, [(0, 1), (0, 1)]),            
            (2, 'AND', 2, [(1, 2), (0, 2)]),
            (3, 'AND', 2, [(0, 3), (1, 3)]),
            (4, 'AND', 3, [(2, 4), (3, 4)])]














import numpy as np
def sigmoid(x):
    s = 1/(1+np.exp(-x))
    return s
# probC1 = np.log10((2*0.4) + 0.2+(2* 0.2+0.1 )) 
# probC1 = ((2*0.4) + 0.2+(2* 0.2+0.1 )) 
probC1 = sigmoid(  (2*0.4) + 0.2 )

probC1


def simular_Circuito(Circuito, vector_entrada, con_def, puertas_defectuosas):
    
    vetor_saida = []  
    for porta in range(len(Circuito)):
        numPorta = Circuito[porta][0]
        # Tipo de porta
        tipo = Circuito[porta][1]
        # camada
        camada = Circuito[porta][2]
        # conexoes
        conexoes = Circuito[porta][3]
        # entradas, por defecto a cero
        entrada1 = 0
        entrada2 = 0
        
        # En primer lugar si la porta pertenece al conjunto de portas marcadas como defectuosas
        # podemos establecer que su salida será cero.
        if numPorta in puertas_defectuosas:
            # Añadimos al vector salida el correspondiente vector (numPorta, valor)
            vetor_saida.append(0)
            
        # En caso contrario la porta no estará dañada luego comprobamos el valor de sus entradas
        else:
            # Primera entrada
            # De nuevo comprobamos si la conexion a esta porta esta dañada en ese caso, el valor
            # de la entrada será cero, por lo tanto no modificamos la entrada.
            
            # En el siguiente caso si la entrada se corresponde con una conexión a 0 quiere decir que o bien está
            # en la camada 1 o no tiene una salida asignada, en cuyo caso la entrada tendrá valor cero. De nuevo 
            # Tampoco modificamos la entrada
            
            # Si la porta se encuentra en la camada 1 le introducimos el valor del vector entrada correspondiente
            if camada == 1:
                entrada1 = vector_entrada[porta]
            # Si la conexión no se encuentra en la camada 1, no es defectuosa, y no es 0, le asignamos el valor de la
            # porta que tenga asociada
            elif camada != 1 and conexoes[0] not in con_def and conexoes[0][0] != 0:
                # Para la lista de valores de portas
                # Encontramos el valor de la porta correspondiente
                val = conexoes[0][0]
                entrada1 = vetor_saida[val - 1]
            # Segunda entrada
            # De manera análoga con la segunda entrada
            if camada == 1:
                entrada2 = vector_entrada[porta]
            # Si la conexión no se encuentra en la camada 1, no es defectuosa, y no es 0, le asignamos el valor de la
            # porta que tenga asociada
            elif camada != 1 and conexoes[1] not in con_def and conexoes[1][0] != 0:
                # Para la lista de valores de portas
                # Encontramos el valor de la porta correspondiente
                    val2 = conexoes[1][0]
                    entrada2 = vetor_saida[val2 - 1]
            # Ahora que ya tenemos definidos los valores de las entradas pasamos 
            # a definir el valor de las salidas de las portas
            vetor_saida.append(calcular_Saida(entrada1, entrada2, tipo))
    #Devolvemos las salidas de las n última portas  
    return vetor_saida[-portas:]  

def calcular_Saida(entrada1, entrada2, tipoPorta):
    
    saida = 0
    
    if tipoPorta == 'OR':
        if entrada1 == 1:
            saida = 1
        elif entrada2 == 1:
            saida = 1
        else:
            saida = 0
    elif tipoPorta == 'AND':
        if entrada1 == 1 and entrada2 == 1:
            saida = 1
        else:
            saida = 0
    elif tipoPorta == 'NOT':
        if entrada2 == 0:
            saida = 1
        else:
            saida = 0
    elif tipoPorta == 'NAND':
        if entrada1 == 1 and entrada2 == 1:
            saida = 0
        else:
            saida = 1
    elif tipoPorta == 'XOR':
        if entrada1 != entrada2:
            saida = 1
        else:
            saida = 0
    elif tipoPorta == 'XNOR':
        if entrada1 == entrada2:
            saida = 1
        else:
            saida = 0
    elif tipoPorta == 'NOR':
        if entrada1 == 0 and entrada2 == 0:
            saida = 1
        else: 
            saida = 0
    return saida



#Método que genera os pares de vetores (entradas, salidas esperadas)
#Con la posibilidad de generarlas con portas/conexao dañadas
def geracao_colecaoPares(circuito, conexao_defeituosa, portas_defeituosas):
    geracao_colecaoPares = []
    combinacao = [0 , 1]
    colecao = list(product(combinacao, repeat=portas))
    for entrada in colecao:
        geracao_colecaoPares.append((entrada, simular_Circuito(circuito, entrada, conexao_defeituosa, portas_defeituosas,)))
        
    return geracao_colecaoPares
    
# Método de autodiagnóstico que compara pares de referência para saber se um
#circuit tem defeitos, ou saber que há falhas entre pares de referência
# de circuitos diferentes

def auto_diagnostico(circuito, circuito2, conexao_defeituosa, portas_defeituosas):
    # Criação de coleção pares de referência sem falhas
    colecaoCoreta = geracao_colecaoPares(circuito, [],[])
    falhas = 0
    
    for n in range(len(colecaoCoreta)):
        # Para cada vetor de entrada simulamos o vetor de saída aplicando os defeitos
        colecaoDefeituosa = simular_Circuito(circuito2, colecaoCoreta[n][0], conexao_defeituosa, portas_defeituosas)
        # Para cada elemento do vetor saida
        for com in range(len(colecaoDefeituosa)):
           # Comparamos o resultado esperado com o saida obtido com defeitos
            if colecaoDefeituosa[com]!=colecaoCoreta[n][1][com]:
           
               #Se eles não combinam aumentamos as falhas
                falhas+=1
    
    return falhas
    
    
















import random
from deap import base, creator, tools, algorithms
import numpy


########### OBJETIVO ESPECÍFICO 4 ##############
# Use o mecanismo do pacote deap para declarar o atributo
#fitness de avaliação para indivíduos, com peso -1 como é
# de um problema de minimização


creator.create('Fitness', base.Fitness, weights=(-1.0,))

#Definimos ahora la clase individuo
creator.create('Individuo', list, fitness = creator.Fitness)

#Asi como la toolbox donde registraremos todos os elementos necesarios para poder aplicar un algoritmo genético.
base_de_eventos_ferramentas = base.Toolbox()


# Agora vamos gerar a função do gene

# Informações consultadas sobre os genes.
#https://www.researchgate.net/publication/255599933_Logic_Circuits_Synthesis_Through_Genetic_Algorithms

# Para cada cromossomo, neste caso portas, teremos 3 genes que serão: tipo de portal, entrada1 e entrada2
# Para a geração dos genes então, primeiro para as portas, vamos escolher um número aleatório entre o número
#que mais tarde será atribuído. Por outro lado, para os portas

from functools import wraps

# Criamos uma função de decorador para retornar o número de vezes
#que o método creacao_Genes foi chamado, neste caso por registro
def counter(func):
    @wraps(func)
    def tmp(*args, **kwargs):
        tmp.count += 1
        return func(*args, **kwargs)
    tmp.count = 0
    return tmp


# método auxiliar que retorna a camada do porta
def numeroCamada(contador):
    camada = camadas
    for n in range(1,camadas+1):
        if contador >= ((n*(portas*3))-((portas*3)-1)) and contador <= (n*(portas*3)):
            camada = n
    return camada

@counter
def creacao_Genes():
#Para saber que tipo de gene está sendo criado em cada comentário (portal, entrada)
# Vamos implementar um método (decorador) que nos dê o número de vezes que
#the método é chamado, desde que você não pode entrar em um contador no método.
# Com esse contador, definimos o número da ninhada e se tipo de gene.
    if creacao_Genes.count == (3*portas*camadas):
        creacao_Genes.count = 0
    contador = creacao_Genes.count
    gen = 0
    camada = numeroCamada(contador)
# Se o gene que está sendo tratado é um tipo de portador, então
# Atribuímos um número aleatório do conjunto de tipos de slides
    if (contador-1) % 3 == 0:
        Tipo = [1,2,3,4,5,6,7]
        gen = random.choice(Tipo)
# Se forem genes relacionados a entradas, serão atribuídos
#values aleatórios dentro do seu conjunto permitido

    elif (contador-1) % 3 != 0 and camada == 1:
        #Si la camada es la 1
        gen = 0
    elif (contador-1) % 3 != 0 and camada == 2:
        #Si es de la camada 2
        minimo = (((camada-1)*portas)-(portas-1))
        maximo = ((camada-1)*portas)
        rango2 = []
        rango2.append(0)
        for a in range(minimo,maximo+1):
            rango2.append(a)
        gen = random.choice(rango2)        
    elif (contador-1) % 3 != 0 and camada > 2: 
        #Si es de una camada superior a la 2
        minimo = (((camada-2)*portas)-(portas-1))
        maximo = ((camada-1)*portas)
        rango = []
        rango.append(0)
        for a in range(minimo,maximo+1):
            rango.append(a)
        gen = random.choice(rango)        
    return gen
    
#Ahora si podemos registrar en la toolbox la función creacao_Genes()
base_de_eventos_ferramentas.register('gen', creacao_Genes)

#Registramos ahora en la caja de herramientas la funcion individuo que devuelve
#un individuo aleatorio, definiendo n como el número de genes del que se compone
#el individuo.
base_de_eventos_ferramentas.register('individuo', tools.initRepeat, container = creator.Individuo,
                             func = base_de_eventos_ferramentas.gen, n= camadas*portas*3)

#Ahora con una lista de individuos podemos crear también una población
#Definiendo n como el número de individuos de la población.
base_de_eventos_ferramentas.register('populacao', tools.initRepeat, container = list,
                             func = base_de_eventos_ferramentas.individuo, n = 20)

#Ahora vamos a registrar la función que evalua el fenotipo de cada individuo
def fenotipo(individuo):
    #Devolveremos un fenotipo que este caso debe seguir la estructura de un circuito
    fenotipo = []
    contadorCapa = 0
    #Número de camada de la porta, empieza en 1
    camada = 1 
    #número de porta
    porta = 1
    #vamos a parsear os genes del individuo para formar el fenotipo
    for gen in range(0, len(individuo), 3):
        #Parseamos el número de tipo de porta al nombre del tipo
        tipoPorta = tipo_de_porta(individuo[gen])
        
        fenotipo.append((porta, tipoPorta, camada, [(individuo[gen+1], porta),(individuo[gen+2], porta)]))
        porta+=1
        contadorCapa += 1
        #Si el contador es igual al número de portas, es decir, se han creado todas las portas de una camada
    
        if contadorCapa == portas:
            #Aumenta el número de camada
            camada+=1
            #Contador se resetea
            contadorCapa=0
    return fenotipo

#método auxiliar para obtener el tipo de porta según el número de gen
def tipo_de_porta(numero):
    porta = 'NOR'
    if numero == 1:
        porta = 'OR'
    elif numero == 2:
        porta = 'AND'
    elif numero == 3:
        porta = 'NOT'
    elif numero == 4:
        porta = 'NAND'
    elif numero == 5:
        porta = 'XOR'
    elif numero == 6:
        porta == 'XNOR'
    return porta
    
    
    
def avalia_individuo(individuo):
    
    #Fenotipo para o individuo
    circuito = fenotipo(individuo)

    # Agora nós levamos em conta o circuito que primeiro pegamos como um circuito de solução, supondo que esteja danificado
#     e nós comparamos com o fenótipo do indivíduo. Nós usamos o função de autodiagnóstico que implementamos antes
    
    return [auto_diagnostico(CircuitoSolucao, circuito, [], [])]
    
    
#Incluimos na toolbox a função de evaliação    
base_de_eventos_ferramentas.register('evaluate', avalia_individuo)
# Da mesma forma que incluímos o operador de recombinação uniforme, estabeleceremos
# a probabilidade de troca em 30%
base_de_eventos_ferramentas.register('mate', tools.cxUniform,  indpb=0.3)




















#Por outro lado temos a mutação que para nosso problema está claro que o operador mais coerente e o de mutaçaõ uniforme,
#  já que se pode  especificar um intervalo, em nosso caso segundo a camada na porta especificaremos um intervalo ou outro.



#método auxiliar para criar margens para a mutação
def creaMargenes():
    lowerBound = []
    upperBound = []
    for n in range(portas*camadas*3):
        camada = numeroCamada(n+1)
        if n % 3 == 0:
            lowerBound.append(1)
            upperBound.append(7)
        elif n % 3 != 0 and camada == 1:
            lowerBound.append(0)
            upperBound.append(0)
        elif n % 3 != 0 and camada == 2:
            minimo = (((camada-1)*portas)-(portas-1))
            maximo = ((camada-1)*portas)
           # Temos que parar de incluir 0 como possibilidade de entrada nas portas
#               Como as sequências de margem introduziriam valores inviáveis em os genótipos.
            lowerBound.append(minimo)
            upperBound.append(maximo)        
        elif n % 3 != 0 and camada > 2: 
            minimo = (((camada-2)*portas)-(portas-1))
            maximo = ((camada-1)*portas)
            lowerBound.append(minimo)
            upperBound.append(maximo)
    return [lowerBound,upperBound]

bounds = creaMargenes()

base_de_eventos_ferramentas.register('mutate', tools.mutUniformInt,low = bounds[0],up = bounds[1], indpb=0.1)

def prog():
    # Alternativamente à estratégia de seleção por torneio vamos
    #a também inclui a estratégia elitista
    base_de_eventos_ferramentas.register('select', tools.selBest)



    # Nós já temos todas as ferramentas para aplicar um algoritmo genético
    # Faremos isso aplicando a função do módulo Algorithms.

    # Estatísticas sobre a aptidão dos indivíduos: mínimo, médio e máximo
    # Nota: usamos as funções numpy correspondentes para isso, porque
    # valores de aptidão são armazenados em tuplas
    estadísticas = tools.Statistics(lambda ind: ind.fitness.values)
    estadísticas.register("mínimo", numpy.min)
    estadísticas.register("media", numpy.mean)
    estadísticas.register("máximo", numpy.max)

    # Salón de la fama para recopilar os tres mejores individuos de todas las generaciones
    salon_fama = tools.HallOfFame(1)

    random.seed(12345)
    populacao_inicial = base_de_eventos_ferramentas.populacao()
    populacao, registro = algorithms.eaSimple(populacao_inicial,
                                            base_de_eventos_ferramentas,
                                            cxpb=0.5, # Probabilidade de que dois indivíduos contíguos se cruzam
                                            mutpb=0.3, # Probabilidade de um indivíduo silenciar
                                            ngen= 20,#40, # Número de gerações
                                            stats=estadísticas,
                                            halloffame=salon_fama)
    print('-----------------------------------------------')
    print('A melhor solução encontrada foi:')
    for individuo in salon_fama:
        print('-----------------------------------------------')
        print('Individuo: {1}; Fitness: {0}'.format(
            individuo.fitness.values[0], fenotipo(individuo)))
    print('-----------------------------------------------')
    print('Vamos verificar as saídas do circuito comparadas'
        +' com os do circuito de solução.')
    print('-----------------------------------------------')
    print('Este é o nosso circuito de solução:')
    print(CircuitoSolucao)
    print('-----------------------------------------------')
    col1 = geracao_colecaoPares(CircuitoSolucao,[],[])
    fenot = salon_fama[0]
    circuitoAlternativo = fenotipo(fenot)
    col2 = geracao_colecaoPares(circuitoAlternativo,[],[])
    print('Estas são as tuplas de saida dos circuitos.')
    for n in range(len(col1)): 
        print(col1[n][1], col2[n][1])    
        
    print('-----------------------------------------------')
    print('Nós obtivemos um circuito alternativo com {0} '
        'erros \nem relação ao circuito da solução'.format(individuo.fitness.values[0]))
    print('-----------------------------------------------')
    print('Portanto, o desempenho do nosso algoritmo tem sido {:.1f}%'
        .format((((pow(2,portas)*portas)-salon_fama[0].fitness.values[0])/(pow(2,portas)*portas))*100))
    return circuitoAlternativo

prog()










































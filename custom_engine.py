arbol_de_reglas = {
    "cancer de mama lobulillar": {
        "borde_nuclear":"irregular",
        "arquitectura": "ductos rudimentarios,conglomerados de celulas,monomorfa",
        "canibalismo": "presente"
    },
    "cancer de mama mucinoso":{
        "nucleo":"mitosis en estallido",
        "nucleo_citoplasma": "aumentado",
        "arquitectura":"lagos de mucinas",
        "canibalismo": "presente"

    },
    "cancer de mama ductal":{        
        "nucleo": "mitosis en estallido,hipercromaticos,irregulares,amoldamiento",
        "citoplasma": "vacuolado,pleomorfismo,rosado",
        "canibalismo": "presente",
        "borde_nuclear": "irregular",
        "arquitectura": "ductos rudimentarios"
    },
    "tumor phyllodes benigno":{
        "canibalismo":"ausente",
        "borde_nuclear":"bien definido",
        "necrosis":"normal"
    },
    
    "cancer de mama papilar":{
        "nucleo":"hipercromaticos,irregulares,amoldamiento",
        "citoplasma":"pleomorfismo,rosado",
        "canibalismo":"presente",
        "borde_nuclear":"mal definido",
        "arquitectura":"papila con microcalcificacion",
        "nucleo_citoplasma":"aumentado"
    },
    "tumor phyllodes maligno":{
        "nucleo":"mitosis en estallido,hipercromaticos,irregulares,amoldamiento",
        "citoplasma":"pleomorfismo",
        "canibalismo":"presente",
        "borde_nuclear":"irregular",
        "arquitectura":"celulas fusocelulares",
        "nucleo_citoplasma":"aumentado"
    }
}

def run(bag):
    resultados = {
        "seguro":[],
        "posiblemente":[],
        "no tiene":[]
    }
    for c in arbol_de_reglas:
        descartar = False
        cumple_todas = len(arbol_de_reglas[c])
        for k in arbol_de_reglas[c]:        
            if k in bag: 
                if bag[k] == arbol_de_reglas[c][k]:
                    cumple_todas -= 1
                else:
                    descartar = True
                     


        if descartar == 1:        
            resultados['no tiene'].append(c)
        elif cumple_todas == 0:
            resultados['seguro'].append(c)
        else:
            resultados['posiblemente'].append(c)
    return resultados

def ask_expert(bn="",arq="",canibalismo="",n="",nc="",c="",necro=""):
    bag = {}
    if bn != "": bag['borde_nuclear'] = bn
    if arq != "": bag['arquitectura'] = arq
    if canibalismo != "": bag['canibalismo'] = canibalismo
    if n != "": bag['nucleo'] = n
    if nc != "": bag['nucleo_citoplasma'] = nc
    if c != "": bag['citoplasma'] = c
    if necro != "": bag['necrosis'] = necro  
    results = run(bag)
    
    if len(results['seguro'])!= 0:
        print(f"El paciente padece de {results['seguro'][0]}")        
    elif len(results['posiblemente']) != 0:        
        for n in results['posiblemente']:
            print(f"Existe aun la posibilidad de que el paciente padezca {n}")
    else:
        print("Dadas las caracteristicas no logramos distinguir si el tumor corresponde a los tipos de cancer conocidos por el experto.")
    return 
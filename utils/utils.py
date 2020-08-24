from engine.engine import *

def ask_expert(bn=NADA,arq=NADA,canibalismo=NADA,n=NADA,nc=NADA,c=NADA,necro=NADA):
    engine = RuleEngine()
    engine.RESPUESTA = [[],[]]
    engine.reset()
    engine.declare(*declare_params(bn=bn,arq=arq,canibalismo=canibalismo,n=n,nc=nc,c=c,necro=necro))
    engine.run()
    if len(engine.RESPUESTA[1])==0 and len(engine.RESPUESTA[0])==0:
        print("Dadas las caracteristicas no logramos distinguir si el tumor corresponde a los tipos de cancer conocidos por el experto.")
    else:
        if len(engine.RESPUESTA[1])!=0:
            print(f"El paciente padece de {engine.RESPUESTA[1][0]}")
        else:
            for n in set(engine.RESPUESTA[0]):
                print(f"Existe aun la posibilidad de que el paciente padezca {n}")
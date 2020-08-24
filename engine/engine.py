from experta import *
from engine.facts import *
NADA = "NADA"

class RuleEngine(KnowledgeEngine):
    @Rule(AND(AS.borde_nuclear << BordeNuclear(tipo=L("irregular") | L(NADA)),
              AS.arq << Arquitectura(tipo=L("ductos rudimentarios,conglomerados de celulas,monomorfa") | L(NADA)),
              AS.canibalismo << Canibalismo(tipo=L("presente") | L(NADA))
              ))
    def cancer_lobulillar(self, borde_nuclear, arq, canibalismo):
        l = [borde_nuclear, arq, canibalismo]
        self.check_ans(l, "cancer de mama lobulillar")

    @Rule(AND(AS.nucleo << Nucleo(tipo=L("mitosis en estallido") | L(NADA)),
              AS.nucleo_citoplasma << NucleoCitoplasma(tipo=L("aumentado") | L(NADA)),
              AS.arq << Arquitectura(tipo=L("lagos de mucinas") | L(NADA))
              ))
    def cancer_mucinoso(self, nucleo, nucleo_citoplasma, arq):
        l = [nucleo, nucleo_citoplasma, arq]
        self.check_ans(l, "cancer de mama mucinoso")

    @Rule(AND(AS.nucleo << Nucleo(tipo=L("mitosis en estallido,hipercromaticos,irregulares,amoldamiento") | L(NADA)),
              AS.citoplasma << Citoplasma(tipo=L("vacuolado,pleomorfismo,rosado") | L(NADA)),
              AS.canibalismo << Canibalismo(tipo=L("presente") | L(NADA)),
              AS.borde_nuclear << BordeNuclear(tipo=L("irregular") | L(NADA)),
              AS.arq << Arquitectura(tipo=L("ductos rudimentarios") | L(NADA))
              ))
    def cancer_ductal(self, nucleo, citoplasma, canibalismo, borde_nuclear, arq):
        l = [nucleo, citoplasma, canibalismo, borde_nuclear, arq]
        self.check_ans(l, "cancer de mama ductal")

    @Rule(AND(AS.nucleo << Nucleo(tipo=L("mitosis en estallido,hipercromaticos,irregulares,amoldamiento") | L(NADA)),
              AS.citoplasma << Citoplasma(tipo=L("vacuolado,pleomorfismo") | L(NADA)),
              AS.canibalismo << Canibalismo(tipo=L("ausente") | L(NADA)),
              AS.borde_nuclear << BordeNuclear(tipo=L("bien definido") | L(NADA)),
              AS.arq << Arquitectura(tipo=L("ductos rudimentarios, celulas fusocelulares") | L(NADA)),
              AS.nucleo_citoplasma << NucleoCitoplasma(tipo=L("normal") | L(NADA)),
              ))
    def tumor_phyllodes_benigno(self, nucleo, citoplasma, canibalismo, borde_nuclear, arq, nucleo_citoplasma):
        l = [nucleo, citoplasma, canibalismo, borde_nuclear, arq, nucleo_citoplasma]
        self.check_ans(l, "tumor phyllodes benigno")

    @Rule(AND(AS.nucleo << Nucleo(tipo=L("hipercromaticos,irregulares,amoldamiento") | L(NADA)),
              AS.citoplasma << Citoplasma(tipo=L("pleomorfismo,rosado") | L(NADA)),
              AS.canibalismo << Canibalismo(tipo=L("presente") | L(NADA)),
              AS.borde_nuclear << BordeNuclear(tipo=L("mal definido") | L(NADA)),
              AS.arq << Arquitectura(tipo=L("papila con microcalcificacion") | L(NADA)),
              AS.nucleo_citoplasma << NucleoCitoplasma(tipo=L("aumentado") | L(NADA)),
              ))
    def cancer_papilar(self, nucleo, citoplasma, canibalismo, borde_nuclear, arq, nucleo_citoplasma):
        l = [nucleo, citoplasma, canibalismo, borde_nuclear, arq, nucleo_citoplasma]
        self.check_ans(l, "cancer de mama papilar")

    @Rule(AND(AS.canibalismo << Canibalismo(tipo=L("ausente") | L(NADA)),
              AS.borde_nuclear << BordeNuclear(tipo=L("bien definido") | L(NADA)),
              AS.necrosis_tumoral << Necrosis(tipo=L("normal") | L(NADA))
              ))
    def tumor_phyllodes_benigno2(self, canibalismo, borde_nuclear, necrosis_tumoral):
        l = [canibalismo, borde_nuclear, necrosis_tumoral]
        self.check_ans(l, "tumor phyllodes benigno")

    @Rule(AND(AS.nucleo << Nucleo(tipo=L("mitosis en estallido,hipercromaticos,irregulares,amoldamiento") | L(NADA)),
              AS.citoplasma << Citoplasma(tipo=L("pleomorfismo") | L(NADA)),
              AS.canibalismo << Canibalismo(tipo=L("presente") | L(NADA)),
              AS.borde_nuclear << BordeNuclear(tipo=L("irregular") | L(NADA)),
              AS.arq << Arquitectura(tipo=L("celulas fusocelulares") | L(NADA)),
              AS.nucleo_citoplasma << NucleoCitoplasma(tipo=L("aumentado") | L(NADA)),
              ))
    def cancer_phyllodes_maligno(self, nucleo, citoplasma, canibalismo, borde_nuclear, arq, nucleo_citoplasma):
        l = [nucleo, citoplasma, canibalismo, borde_nuclear, arq, nucleo_citoplasma]
        self.check_ans(l, "tumor phyllodes maligno")

    def check_ans(self, l, name):
        a = []
        for c in l:
            a += [1 if c[x] == NADA else 0 for x in c if x != '__factid__']
        if sum(a) == 0:
            self.RESPUESTA[1].append(name)
            # print(f"El paciente padece de {name}")
        else:
            self.RESPUESTA[0].append(name)
            # print(f"Existe aun la posibilidad de que el paciente padezca {name}")

def declare_params(bn=NADA,arq=NADA,canibalismo=NADA,n=NADA,nc=NADA,c=NADA,necro=NADA):
    bn = BordeNuclear(tipo = bn)
    arq = Arquitectura(tipo = arq)
    canibalismo = Canibalismo(tipo = canibalismo)
    n = Nucleo(tipo = n)
    nc = NucleoCitoplasma(tipo = nc)
    c = Citoplasma(tipo = c)
    necro = Necrosis(tipo = necro)
    return [bn,arq,canibalismo,n,nc,c,necro]

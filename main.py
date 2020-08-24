from utils.utils import *

#Opciones validas
opts_borde_nuclear = ["irregular","bien definido","mal definido"]
opts_arq = ["ductos rudimentarios","ductos rudimentarios,conglomerados de celulas,monomorfa","lagos de mucinas",
            "ductos rudimentarios celulas fusocelulares","celulas fusocelulares","papila con microcalcificacion"]
opts_canibalismo=["presente","ausente"]
opts_nucleo=["mitosis en estallido","mitosis en estallido,hipercromaticos,irregulares,amoldamiento","hipercromaticos,irregulares,amoldamiento"]
opts_nucleo_citoplasma=["aumentado","normal"]
opts_citoplasma =["vacuolado,pleomorfismo,rosado","vacuolado,pleomorfismo","pleomorfismo,rosado","pleomorfismo"]
opts_necrosis_tumoral=["normal"]

ask_expert(bn="irregular",
           arq="ductos rudimentarios,conglomerados de celulas,monomorfa",
           canibalismo="presente")
ask_expert(n="mitosis en estallido",nc="aumentado",arq="lagos de mucinas")
ask_expert(n="mitosis en estallido,hipercromaticos,irregulares,amoldamiento",
           c="vacuolado,pleomorfismo,rosado",
           canibalismo="presente",
           bn="irregular",
           arq="ductos rudimentarios")

ask_expert(n="mitosis en estallido,hipercromaticos,irregulares,amoldamiento",
           c="vacuolado,pleomorfismo",
           nc="normal",
           canibalismo="ausente",
           bn="bien definido",
           arq="ductos rudimentarios, celulas fusocelulares")
ask_expert(n="hipercromaticos,irregulares,amoldamiento",
           c="pleomorfismo,rosado",
           nc="aumentado",
           canibalismo="presente",
           bn="mal definido",
           arq="papila con microcalcificacion")
ask_expert(canibalismo="ausente",bn="bien definido",necro="normal")

ask_expert(n="mitosis en estallido,hipercromaticos,irregulares,amoldamiento",
                               c="pleomorfismo",
                               nc="aumentado",
                               canibalismo="presente",
                               bn="irregular",
                               arq="celulas fusocelulares")
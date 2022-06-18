import re

def retornaHoraMinutoDeTexto(texto):
    tempos = re.findall(r"[\d]?\d:\w+", texto)

    somaHoras = 0
    somaMinutos = 0

    for tempo in tempos:
        horas = tempo[0:2]
        minutos = tempo[3:5]
        somaHoras += int(horas)
        somaMinutos += int(minutos)

    minutosFinais = somaMinutos % 60
    horasFinais = somaHoras + somaMinutos // 60

    return (horasFinais,minutosFinais)

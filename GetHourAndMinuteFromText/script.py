import re

def getHourAndMinuteFromText(text):
    matches = re.findall(r"[\d]?\d:\w+", text)
    hoursSum = 0
    minutesSum = 0

    for match in matches:
        hours = match[0:match.index(':')]
        minutes = match[match.index(':')+1:]
        hoursSum += int(hours)
        minutesSum += int(minutes)

    totalMinutes = minutesSum % 60
    totalHours = hoursSum + minutesSum // 60

    return (totalHours,totalMinutes)

[hours, minutes ] = getHourAndMinuteFromText("""Introdução
  Apresentação (1:00)
Entendendo o ASP.NET MVC
  Contexto histórico (4:00)
  Pipeline do ASP.NET MVC 5 (9:00)
  ASP.NET vs ASP.NET Core (5:00)
  Para que eu posso utilizar ASP.NET? (3:00)
   O padrão MVC (5:00)
  O básico sobre HTTP (6:00)
  Minha primeira aplicação MVC 5 (10:00)
  O básico da Web (11:00)
  Teste os seus conhecimentos (2:00)
Controllers
  Convenções do MVC (9:00)
  Action Results (17:00)
  Rotas em ação (15:00)
  Rotas por atributo (12:00)
   Passagem de parâmetros na controller (22:00)
  Teste os seus conhecimentos (3:00)
Trabalhando com Modelos
  O que é uma model? (4:00)
  Trabalhando com DataAnnotations (8:00)
  Validação de modelos (10:00)
  Teste os seus conhecimentos (3:00)
Views e Razor
  Introdução (7:00)
  Trabalhando com HtmlHelpers (10:00)
  Validação de dados (10:00)
  Validação via jQuery (11:00)
  Utilizando Partial Views (10:00)
  Proteção contra CSRF (13:00)
  Teste os seus conhecimentos (3:00)
Gerenciando Scripts
   A importância da gestão dos scripts (8:00)
  Implementando Bundling e Minification (19:00)
  Teste os seus conhecimentos (3:00)
Trabalhando com Entity Framework
  Introdução (11:00)
  Configurando o EF na aplicação (21:00)
  Operações no banco com EF (18:00)
  Teste os seus conhecimentos (3:00)
Desenvolvendo uma aplicação funcional
  Novo projeto (7:00)
  Conhecendo o ASP.NET Identity (15:00)
  Utilizando Scaffold (13:00)
  Customizando a implementação padrão (16:00)
  Customizações visuais (21:00)
  Manutenção de estado (13:00)
  Action Filters (9:00)
  Finalização (3:00)
  Teste os seus conhecimentos (3:00)""")

print("Total: {0} hours and {1} minutes.".format(hours,minutes))

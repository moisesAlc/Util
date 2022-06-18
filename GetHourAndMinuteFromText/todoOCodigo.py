import re

txt = """Introdução
  Apresentação (1:00)
  Objetivos do curso (3:00)
Modelando a arquitetura
  Proposta de Arquitetura (4:00)
  Realizando o setup do projeto (13:00)
Modelando a camada de negócios
  Definindo o conceito de entidade (9:00)
  Escrevendo entidades de negócio (10:00)
  Interfaces de acesso a dados (13:00)
Mapeando o banco de dados
  Configurando o DbContext (6:00)
  Trabalhando com FluentAPI (18:00)
  Otimizando a modelagem via contexto (12:00)
  Generic Repository Pattern (13:00)
  Repositórios especializados (13:00)
Validações, serviços e processos de negócios
  Introdução (4:00)
  Validação com FluentValidation (9:00)
  Validando entidades (11:00)
  Implementando serviços de negócios (20:00)
  Testando o funcionamento do serviço (9:00)
  Desenvolvendo os demais serviços (6:00)
  Notificação de erros (6:00)
  Implementando a notificação de erros (18:00)
Setup da camada de apresentação
  Introdução (4:00)
  Modelando as ViewModels (13:00)
  Trabalhando com Scaffolding (15:00)
  Implementando Automapper (22:00)
  Finalizando a Controller (10:00)
  Configurando o SimpleInjector (27:00)
  Utilizando o Startup.cs da forma certa (7:00)
  Execução e ajustes de configurações (15:00)
Implementando funcionalidades no MVC
  Introdução (4:00)
  Implementando a Controller Fornecedores (16:00)
  Implementando Views de Fornecedores (17:00)
  Implementando Views de Fornecedores pt II (6:00)
  Trabalhando com Partial Views (6:00)
  Trabalhando com JavaScript e JQuery (14:00)
  Trabalhando com ModalView (18:00)
  Trabalhando com ModalView pt II (11:00)
  Implementando extensões do Razor (15:00)
  Implementando DropDownList (18:00)
  Implementando a cultura local (24:00)
Finalizando a aplicação
  Definindo data automática no EF (7:00)
  Lidando com limitações do EF (5:00)
  Upload de imagens - front-end (13:00)
  Upload de imagens - back end (19:00)
  Exibindo erros de negócio (19:00)
  Configurando o Identity (11:00)
  Negando acesso aos usuários (11:00)
  Trabalhando com Claims (22:00)
  Validando as Claims via Razor (15:00)
  Tratamento de erros (15:00)
  Compilação e Deploy (15:00)
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
  Teste os seus conhecimentos (3:00)"""

txtRocket = """Chapter I
Fundamentos do NodeJS
Fundamentos do NodeJS
01:14:03 em 9 aulas
Nesse módulos nós vamos conhecer os conceitos do Node.js, como é o seu funcionamento e os motivos pelo qual ele foi criado. Iremos estudar sobre os conceitos e regras por trás de uma API Rest, os métodos HTTPs, os principais códigos de retornos e tipos de parâmetros de uma requisição.

100% completo
Primeiro projeto com Node.js
Primeiro projeto com Node.js
01:13:41 em 11 aulas
Nesse módulo iremos criar nosso primeiro projeto com Node.js do total zero, colocando em prática todos os conceitos estudados no módulo inicial.

27% completo
DESAFIOS PRINCIPAIS

Desafio: Conceitos do Node.js
Nesse desafio, você deverá criar uma aplicação para treinar o que aprendeu até agora no Node.js!

INSTRUÇÕES
ENVIAR DESAFIO
DESAFIOS COMPLEMENTARES

Desafio: Trabalhando com Middlewares
Nesse desafio você irá trabalhar mais a fundo com middlewares no Express. Dessa forma você será capaz de fixar mais ainda os conhecimentos obtidos até agora.

INSTRUÇÕES
ENVIAR DESAFIO
DESAFIOS COMPLEMENTARES

Desafio: Corrigindo o código
Nesse desafio, temos uma aplicação Node.js que está em processo de desenvolvimento mas que já possui os testes necessários para fazer toda a validação dos requisitos (você não deve mexer nos testes).

INSTRUÇÕES
ENVIAR DESAFIO
Chapter II
Iniciando a API
Iniciando a API
04:36:56 em 37 aulas
Aqui aprenderemos a criar aplicações utilizando TypeScript seguindo padrões de código e princípios do SOLID. Aprenderemos conceitos importantes como casos de uso, repositórios, models, streams do Node.js e documentação de APIs com Swagger.

0% completo
DESAFIOS PRINCIPAIS

Desafio: Introdução ao SOLID
Nesse desafio, você irá criar uma API seguindo a estrutura de arquitetura limpa aprendida até agora.

INSTRUÇÕES
ENVIAR DESAFIO
DESAFIOS COMPLEMENTARES

Desafio: Documentando com Swagger
Nesse desafio, você irá documentar, com o Swagger, a API desenvolvida no desafio anterior.

INSTRUÇÕES
ENVIAR DESAFIO
Chapter III
The Great Leap
Aprenda a aprender e vá mais longe. Conheça e domine o método responsável por acelerar sua curva de aprendizado e carreira.

Assistir vídeo
Continuando a aplicação
Continuando a aplicação
05:15:05 em 30 aulas
Daremos início à nossa aplicação principal criando a base do app com autenticação, cadastro, upload de avatar, etc. utilizando um banco de dados relacional e conheceremos conceitos e ferramentas como Docker, TypeORM, JWT e bcrypt.

0% completo
DESAFIOS PRINCIPAIS

Desafio: Database Queries
Nesse desafio você irá treinar os três tipos de queries usando o TypeORM: usando ORM, usando query builder e raw query.

INSTRUÇÕES
ENVIAR DESAFIO
DESAFIOS COMPLEMENTARES

Desafio: Modelagem do banco de dados
Nesse desafio você irá praticar um pouco da modelagem de banco de dados, partindo da aplicação desenvolvida no desafio anterior.

INSTRUÇÕES
ENVIAR DESAFIO
Chapter IV
Testes e regras de negócio
Testes e regras de negócio
08:01:20 em 34 aulas
Criaremos grande parte das funcionalidades e regras de negócio da nossa aplicação utilizando testes automatizados com Jest e supertest, criando a documentação completa das funcionalidades com Swagger.

0% completo
DESAFIOS PRINCIPAIS

Desafio: Testes unitários
Nesse desafio você irá construir os testes unitários para uma API pronta usando tudo que aprendeu até agora!

INSTRUÇÕES
ENVIAR DESAFIO
DESAFIOS COMPLEMENTARES

Desafio: Testes de integração
Nesse desafio você irá construir os testes de integração para adicionar ainda mais cobertura de testes na Fin API.

INSTRUÇÕES
ENVIAR DESAFIO
Advance and Explore
Chegando na reta final do Ignite, e você passou por vários desafios, aprendendo a aprender. Chegou a hora de colocar a insegurança de lado e continuar a pilotar o foguete para a missão final do Ignite.

Assistir vídeo
Chapter V
Trabalhando com refresh_token e e-mail
Trabalhando com refresh_token e e-mail
04:30:20 em 22 aulas
Nesse capítulo vamos concluir as funcionalidades da nossa aplicação, aprender como utilizar refresh_token da nossa aplicação e como enviar e-mail, utilizando a biblioteca nodemailer.

0% completo
DESAFIOS COMPLEMENTARES

Desafio: Transferências com a FinAPI
Nesse desafio, você irá implementar uma nova feature na FinAPI. Agora será possível realizar transferências de valores.

INSTRUÇÕES
ENVIAR DESAFIO
Chapter VI
Deploy
Deploy
04:52:33 em 24 aulas
Nesse capítulo vamos aprender como fazer o deploy da nossa aplicação em produção, utilizando CI/CD para automatizar o deploy.

0% completo
Serverless
Serverless
01:52:59 em 14 aulas
Nesse capítulo vamos aprender o que é Serverless e vamos criar uma aplicação utilizando Serverless. Vamos ver também os conceitos por trás da arquitetura de microsserviços e como tem sido utilizado no mercado.

0% completo
DESAFIOS COMPLEMENTARES

Desafio: Construindo com serverless
Nesse desafio você irá reaplicar os conceitos aprendidos sobre serverless usando o Serverless framework.

INSTRUÇÕES
ENVIAR DESAFIO
The Expanding Universe
Como no New Horizons, missão não tripulada da Nasa, você chegou na missão final e cumpriu seus objetivos no Ignite. Chegou a hora de continuar para uma nova missão, agora para fora da nossa galáxia."""

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

print(retornaHoraMinutoDeTexto(txtRocket))

'''
tempos = re.findall(r"[\d]?\d:\w+", txtRocket)

somaHoras = 0
somaMinutos = 0

print("SomaHoras: ", somaHoras)
print("somaMinutos: ", somaMinutos)

for tempo in tempos:
    horas = tempo[0:2]
    minutos = tempo[3:5]
    print(tempo)
    print("horas =",horas)
    print("minutos =",minutos)
    somaHoras += int(horas)
    somaMinutos += int(minutos)
    print("SomaHoras: ", somaHoras)
    print("somaMinutos: ", somaMinutos)

print("SomaHoras: ", somaHoras)
print("somaMinutos: ", somaMinutos)
print("Dando...")
minutosFinais = somaMinutos % 60
horasFinais = somaHoras + somaMinutos // 60

print(horasFinais,"h",minutosFinais)'''





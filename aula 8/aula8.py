'''
Até agora você sabe fazer:

if idade >= 18:

Mas imagine que precisamos verificar duas condições ao mesmo tempo.

Por exemplo:
A pessoa pode entrar se tiver 18 anos ou mais E tiver ingresso.
Precisamos dos operadores lógicos.

and — E
idade = 20
tem_ingresso = True

if idade >= 18 and tem_ingresso:
    print("Pode entrar")

As duas condições precisam ser verdadeiras.

or — OU
tem_ingresso = False
nome_lista = True

if tem_ingresso or nome_lista:
    print("Pode entrar")

Basta uma das condições ser verdadeira.

not — NÃO

Inverte o resultado:

tem_ingresso = False

print(not tem_ingresso)

Resultado:
True

Porque:
not False = True
'''
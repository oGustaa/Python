### dando introdução ao python pelo w3schools
### https://www.w3schools.com/python/python_intro.asp
### https://www.w3schools.com/python/python_syntax.asp



print("********Introduzindo********")

nome = input("Qual seu nome?") ### -> interagindo com usuário ~ os dados serão 
                                ### armazenados nesta var.

idade = input("Agora, sua idade") ### °..


gen = input("Nos diga seu gênero inserindo M para masculino e F para feminino. Para outro, digite O")

Mas = 'Masculino'
Fem = 'Feminino'
Outr = str

if gen == 'M':
    gen = Mas
    print("Aqui estão suas informações")
    print(nome)
    print(idade)
    print(gen)

elif gen == 'F':
    gen = Fem
    print("Aqui estão suas informações")
    print(nome)
    print(idade)
    print(gen)

elif gen == 'O':
    gen = Outr
    gen = input("Nos apresente seu gênero")
    print("Sendo assim, aqui estão suas informações")
    print(nome)
    print(idade)
    print(gen)

else:
    print("Digite novamente!")
        





    




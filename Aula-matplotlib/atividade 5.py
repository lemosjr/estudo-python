#5. Jogo de personagens
#Um jogo precisa controlar personagens.
#• Todo personagem tem nome e vida.
#• Um guerreiro deve ter mais vida e um ataque físico.
#• Um mago deve ter menos vida, mas pode lançar magia que causa mais
#dano.
#Questão:
#Crie uma classe base Personagem e, a partir dela, crie as classes Guerreiro e
#Mago usando herança. Simule uma batalha entre um guerreiro e um mago.

# POO - Exemplo 4: Jogo de Personagens
print("--- 4. Jogo de Personagens ---")

class Personagem:
    def __init__(self, nome, vida):
        self.nome = nome
        self.vida = vida

    def atacar(self, alvo):
        pass

    def mostrar_status(self):
        print(f"{self.nome} - Vida: {self.vida}")

class Guerreiro(Personagem):
    def __init__(self, nome, vida, forca):
        super().__init__(nome, vida)
        self.forca = forca

    def atacar(self, alvo):
        dano = self.forca
        alvo.vida -= dano
        print(f"{self.nome} ataca {alvo.nome} com a espada, causando {dano} de dano!")

class Mago(Personagem):
    def __init__(self, nome, vida, magia):
        super().__init__(nome, vida)
        self.magia = magia

    def atacar(self, alvo):
        dano = self.magia
        alvo.vida -= dano
        print(f"{self.nome} lança uma bola de fogo em {alvo.nome}, causando {dano} de dano!")

# Cenário de Teste
heroi_guerreiro = Guerreiro("claudio", 120, 15)
vilao_mago = Mago("tomas", 80, 25)

heroi_guerreiro.atacar(vilao_mago)
vilao_mago.mostrar_status()                      
vilao_mago.atacar(heroi_guerreiro)
heroi_guerreiro.mostrar_status()
print("\n")            
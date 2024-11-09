#ABSTRAÇÃO
class Conteudo:
    def __init__(self,titulo,genero)
    self.titulo = titulo
    self.titulo = titulo
    
    def descrever():
        return f'self {self.titulo} - {self.genero}'
    
#HERANÇA
class Filme(Conteudo):
    def __init__(self, titulo, genero, duracao):
        super().__init__(titulo, genero)
        self.duracao = duracao
    def descrever(self):
    # 15 POLIMORFISMO
        return f'{super().descrever()}, Duração: {self.duracao} minutos'
    
class Serie(Conteudo):
    def __init__(self, titulo, genero, episodios):
        super().__init__(titulo, genero)
        self.episodios = episodios
    def descrever(self)
    # 21 POLIMORFISMO
        return f'{super().descrever()} Episodios {self.episodios}'
#ENCAPSULAMENTO
class Usuario:
    def __init__(self, nome, email):
        self.__nome = nome
        self.__email = email
        self.historico = []
        
    def get_nome(self):
        return self.__nome
    def get_email(self):
        return self.__email

# USUARIOS: 
usuario1 = Usuario('Alice', 'alice@gmail.com')
usuario2 = Usuario('Alice1', 'alice1@gmail.com')
usuario3 = Usuario('Alice2', 'alice2@gmail.com') 
# CRIAR FILMES E SERIES:
filme1 = Filme('Jogos Vorazes', 'Ação')
Serie1 = Filme('Breaking Bad', '')

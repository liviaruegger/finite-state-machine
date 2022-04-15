class Estado:
    def __init__(self, label) -> None:
        self.label = label


class Transicao:
    def __init__(self, hora, estado_anterior, proximo_estado) -> None:
        self.hora = hora
        self.estado_atual = estado_anterior
        self.proximo_estado = proximo_estado


class MEF:
    ''' A MEF contém:
        - estados      -> uma lista de estados (class Estado)
        - transicoes   -> uma lista de transições (class Transicao)
        - estado_atual -> um índice da lista de estados (int)
    '''

    def __init__(self, estados=None, transicoes=None, estado_inicial=0) -> None:
        ''' Por padrão, a MEF se inicia com os estados e transições propostos.
        É possível instanciar uma MEF diferente apresentando como parâmetros
        uma lista de estados e uma lista de transições.
        '''
        
        if type(estados) == list:
            self.estados = estados
            self.estado_atual = estado_inicial
        else:
            self.estados = [
                Estado('acordado'),
                Estado('trabalhando'),
                Estado('descansando'),
                Estado('dormindo')
            ]
            self.estado_atual = 3

        if type(transicoes) == list:
            self.transicoes = transicoes
        else:
            self.transicoes = [
                Transicao('08:00', 'dormindo', 'trabalhando'),
                Transicao('12:00', 'trabalhando', 'descansando'),
                Transicao('13:00', 'descansando', 'trabalhando'),
                Transicao('18:00', 'trabalhando', 'acordado'),
                Transicao('22:00', 'acordado', 'dormindo')
            ]


    def __proximo_estado(self, hora: str) -> str:
        ''' Dada uma transição, retorna qual o próximo estado.
        '''
        for transicao in self.transicoes:
            if transicao.hora == hora:
                return transicao.proximo_estado


    def __indice(self, estado: str) -> int:
        ''' Dado um estado, retorna seu índice na lista de estados da MEF.
        '''
        for i in range(len(self.estados)):
            if self.estados[i].label == estado:
                return i


    def listar_estado_atual(self) -> str:
        ''' Retorna o estado atual da MEF.
        '''
        return self.estados[self.estado_atual].label


    def listar_transicoes_possiveis(self) -> list:
        ''' Retorna uma lista de transições possíveis a partir do estado
        atual da MEF.
        '''
        estado_atual = self.listar_estado_atual()
        transicoes_possiveis = []

        for transicao in self.transicoes:
            if transicao.estado_atual == estado_atual:
                transicoes_possiveis.append(transicao.hora)
        
        return transicoes_possiveis


    def atualizar_estado(self, transicao: str) -> str:
        ''' Atualiza o estado atual da MEF e retorna o novo estado.
        '''
        if transicao not in self.listar_transicoes_possiveis():
            print('Transição indisponível') #TODO: tratar erro
        else:
            proximo = self.__proximo_estado(transicao)
            self.estado_atual = self.__indice(proximo)
            return self.listar_estado_atual()
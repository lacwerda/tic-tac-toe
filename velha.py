"""Análises de um estado particular do Jogo da Velha.

    Construído para tirarmos conclusões de diferentes estados do Jogo da Velha,
    a fim de automatizarmos a verificação das posições escolhidas pelos
    jogadores participantes. Exemplo de uso:

    jogo = JogoDaVelha(
        [
            [2, 0, 1],
            [0, 2, 0],
            [1, 0, 1]
        ]
    )
    resultado = jogo.checar_resultado()
"""

class JogoDaVelha:
    """Um estado de um Jogo da Velha.

    O objeto armazena o tabuleiro do Jogo da Velha, assim como suas
    características número de linhas, número de colunas e número de
    diagonais (que é sempre 2).

    Attributes:
        tabuleiro: Lista de listas (matriz) que indica onde estão localizados
        os X e O presentes no estado do jogo.
        numero_linhas: Quantidade de linhas presentes no tabuleiro.
        numero_colunas: Quantidade de colunas presentes no tabuleiro.
        numero_diagonais: Quantidade de diagonais presentes no tabuleiro. Esse
        número é sempre 2.
    """

    def __init__(self, tabuleiro: list):
        """Inicializa a classe JogoDaVelha.

        Constrói a classe ao exigir como parametro o tabuleiro demarcando as
        posições ocupadas e vazias (0). Posições preenchidas com 1 correspondem
        ao X, posições preenchidas com 2 correspondem ao O e posições
        preenchidas com 0 correspondem a um espaço vazio.

        Args:
            tabuleiro: Lista de listas (matriz) representando os espaços.
            preenchidos por X (1), O (2) ou vazios (0).
        """
        self.tabuleiro = self.verificacao_tipo(tabuleiro)
        self.numero_linhas = len(self.tabuleiro)
        self.numero_colunas = len(self.tabuleiro[0])
        self.numero_diagonais = 2

    @staticmethod
    def verificacao_tipo(matriz) -> list:
        """Verifica se o argumento é uma lista de listas.

        Usa funções de checagem de tipo para garantir que o parametro em
        questão é uma lista de listas (formato correto do tabuleiro do Jogo da
        Velha).

        Args:
            matriz: Uma lista de listas.

        Returns:
            A lista de lista verificada.

        Raises:
            TypeError: Tipo Invalido. Tipo Esperado: Lista de Listas.
        """
        if (not isinstance(matriz, list) or
            not all(isinstance(linhas, list)
            for linhas in matriz)):
            raise TypeError('Tipo Invalido. Tipo Esperado: Lista de Listas.')
        return matriz

    def set_tabuleiro(self, tabuleiro: list):
        """Atribui um novo tabuleiro ao atributo Tabuleiro.

        Torna possível a troca do atributo Tabuleiro da classe sem que haja
        a criação de outra instância. O valor anterior do atributo é substituído
        pelo novo valor atribuído no parametro da função.

        Args:
            self: Os atributos da classe JogoDaVelha.
            tabuleiro: O novo tabuleiro a ser substituído pelo anterior.
        """
        self.tabuleiro = self.verificacao_tipo(tabuleiro)

    def __analisar_linhas(self) -> int:
        """Analisa se houve um ganhador em alguma das linhas.

        Itera pelas linhas, verifica se a quantidade de X ou O completa a
        linha e conta o número de ganhadores. A escolha de contar a quantidade
        de ganhadores se dá pelo fato de isso não ser possível de acordo com
        as regras da Velha, tornando o jogo inválido.

        Args:
            self: Os atributos da classe JogoDaVelha.

        Returns:
            Caso haja mais de um ganhador, o jogo é considerado inválido. Por
            isso, o método retorna -1. No entanto, caso haja apenas um ganhador,
            o método retorna 1 (se o ganhador for X) ou 2 (se o ganhador for O).
            No caso de não encontrarmos nenhum ganhador, o método retorna 0.
        """
        numero_ganhadores, ganhador = 0, 0
        for linhas in self.tabuleiro:
            if linhas.count(1) == self.numero_colunas:
                ganhador = 1
                numero_ganhadores += 1
            if linhas.count(2) == self.numero_colunas:
                ganhador = 2
                numero_ganhadores += 1
        return ganhador if numero_ganhadores < 2 else -1

    def __analisar_colunas(self) -> int:
        """Analisa se houve um ganhador em alguma das colunas.

        Itera pelas colunas, verifica se a quantidade de X ou O completa a
        coluna e conta o número de ganhadores. A escolha de contar a quantidade
        de ganhadores se dá pelo fato de isso não ser possível de acordo com
        as regras da Velha, tornando o jogo inválido.

        Args:
            self: Os atributos da classe JogoDaVelha.

        Returns:
            Caso haja mais de um ganhador, o jogo é considerado inválido. Por
            isso, o método retorna -1. No entanto, caso haja apenas um ganhador,
            o método retorna 1 (se o ganhador for X) ou 2 (se o ganhador for O).
            No caso de não encontrarmos nenhum ganhador, o método retorna 0.
        """
        numero_ganhadores, ganhador = 0, 0
        for colunas in range(self.numero_colunas):
            coluna_atual = [self.tabuleiro[linhas][colunas]
                            for linhas in range(self.numero_linhas)]
            if coluna_atual.count(1) == self.numero_linhas:
                ganhador = 1
                numero_ganhadores += 1
            if coluna_atual.count(2) == self.numero_linhas:
                ganhador = 2
                numero_ganhadores += 1
        return ganhador if numero_ganhadores < 2 else -1

    def __analisar_diagonais(self) -> int:
        """Analisa se houve um ganhador em alguma das diagonais.

        Itera pelas diagonais, verifica se a quantidade de X ou O completa a
        diagonal e conta o número de ganhadores. A escolha de contar a quantidade
        de ganhadores se dá pelo fato de isso não ser possível de acordo com
        as regras da Velha, tornando o jogo inválido.

        Args:
            self: Os atributos da classe JogoDaVelha.

        Returns:
            Caso haja mais de um ganhador, o jogo é considerado inválido. Por
            isso, o método retorna -1. No entanto, caso haja apenas um ganhador,
            o método retorna 1 (se o ganhador for X) ou 2 (se o ganhador for O).
            No caso de não encontrarmos nenhum ganhador, o método retorna 0.
        """
        diagonal_1, diagonal_2 = [], []
        coluna_diagonal_2 = self.numero_colunas-1
        for index in range(self.numero_linhas):
            diagonal_1.append(self.tabuleiro[index][index])
            diagonal_2.append(self.tabuleiro[index][coluna_diagonal_2])
            coluna_diagonal_2 -= 1
        diagonais = [diagonal_1, diagonal_2]

        numero_ganhadores, ganhador = 0, 0
        for diagonal in diagonais:
            if diagonal.count(1) == self.numero_linhas:
                ganhador = 1
                numero_ganhadores += 1
            if diagonal.count(2) == self.numero_linhas:
                ganhador = 2
                numero_ganhadores += 1
        return ganhador if numero_ganhadores < 2 else -1

    def __checar_se_nao_vazio(self):
        """Verifica se o tabuleiro está vazio.

        Itera pelas linhas e verifica se todos os elementos da linha são zeros.
        A contagem da quantidade de zeros é somada em todas as linhas, visto que
        o objetivo final é verificar se todos os elementos de todas as linhas
        são zero.

        Args:
            self: Os atributos da classe JogoDaVelha.

        Returns:
            True: Caso o tabuleiro não esteja vazio.
            False: Caso o tabuleiro esteja vazio.
        """
        quantidade_vazios = 0
        for linha in self.tabuleiro:
            quantidade_vazios += linha.count(0)
        return quantidade_vazios < self.numero_colunas * self.numero_linhas

    def __checar_se_possivel(self) -> bool:
        """Verifica se o jogo é possível.

        Utiliza-se de métodos construídos anteriormente para estabelecer se o
        jogo inserido como atributo é possível ou não. Dessa forma, são
        considerados impossíveis jogos que fazem parte de pelo menos uma das
        condições listadas:
            - A diferença entre a quantidade de peças dos dois jogadores é menor
            que dois (um participante não pode jogar dois turnos seguidos);
            - Não há mais de um ganhador;
            - O tabuleiro não está vazio.

        Args:
            self: Os atributos da classe JogoDaVelha.

        Returns:
            True: Caso o jogo seja possível.
            False: Caso o jogo seja impossível.
        """
        quantidade_x, quantidade_o = 0, 0
        for linha in self.tabuleiro:
            quantidade_x += linha.count(1)
            quantidade_o += linha.count(2)

        analise_tabuleiro = [self.__analisar_linhas(),
                             self.__analisar_colunas(),
                             self.__analisar_diagonais()]

        so_um_ganhador = (-1 not in analise_tabuleiro
                          and analise_tabuleiro.count(0) > 1)

        return (abs(quantidade_x - quantidade_o) < 2
                and self.__checar_se_nao_vazio()
                and so_um_ganhador)

    def __checar_se_ha_ganhador(self):
        """Verifica se existe um ganhador.

        Utiliza-se de métodos construídos anteriormente para estabelecer se
        existe um ganhador. Caso contrário, o jogo pode ser classificado como
        indefinido ou empate.

        Args:
            self: Os atributos da classe JogoDaVelha.

        Returns:
            Caso não haja um ganhador, o método retorna 0. Caso haja um
            ganhador, o método retorna 1 (se o ganhador for X) ou 2 (se o
            ganhador for 0).
        """
        return (self.__analisar_diagonais()
                or self.__analisar_colunas()
                or self.__analisar_linhas())

    def __checar_se_completo(self) -> bool:
        """Verifica se o tabuleiro está inteiramente preenchido.

        Itera pelas linhas e conta a quantidade de espaços vazios no tabuleiro.
        Caso o tabuleiro esteja inteiramente preenchido e não haja um ganhador,
        utilizamos esse método para classificar o jogo como empate.

        Args:
            self: Os atributos da classe JogoDaVelha.

        Returns:
            True: Caso o tabuleiro esteja completo.
            False: Caso o tabuleiro ainda tenha espaços vazios.
        """
        quantidade_zeros = 0
        for linha in self.tabuleiro:
            quantidade_zeros += linha.count(0)
        return quantidade_zeros == 0

    def checar_resultado(self):
        """Verifica o estado do jogo.

        Utiliza-se de métodos construídos anteriormente para classificar o jogo
        atribuído ao atributo Tabuleiro. Primeiro, checa se o jogo é possível
        impondo as condições estabelecidas anteriormente. Caso não seja possível
        retornamos -2. Adiante, checa se existe um ganhador. Caso haja um
        ganhador, retorna 1 (se for X) ou 2 (se for O). Caso não haja um
        ganhador, verifica se o tabuleiro está completo. Se estiver completo,
        retorna um empate (0). Caso o contrário retorna que o jogo ainda está
        indefinido (-1).

        Args:
            self: Os atributos da classe JogoDaVelha.

        Returns:
            2: Caso o ganhador seja O.
            1:Caso o ganhador seja X.
            0: Caso haja um empate entre os jogadores.
            -1: Caso o jogo ainda esteja indefinido.
            -2: Caso o jogo seja impossível.
        """
        if not self.__checar_se_possivel():
            return -2
        if self.__checar_se_ha_ganhador():
            return self.__checar_se_ha_ganhador()
        return 0 if self.__checar_se_completo() else -1

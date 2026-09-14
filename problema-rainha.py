from aigyminsper.search.graph import State
from aigyminsper.search.search_algorithms import BuscaProfundidade, BuscaLargura


class NRainhas(State):
    """Estado do problema das N-Rainhas."""

    # Guarda o estado objetivo localizado pela busca para exibir o tabuleiro.
    solucao_encontrada = None

    def __init__(self, op, dimensao, rainhas=()):
        super().__init__(op)
        self.dimensao = dimensao
        self.rainhas = tuple(rainhas)

    def posicao_segura(self, coluna_nova):
        """Verifica se a nova rainha não é atacada pelas anteriores."""
        linha_nova = len(self.rainhas)

        for linha_existente, coluna_existente in enumerate(self.rainhas):
            # Mesma coluna.
            if coluna_nova == coluna_existente:
                return False

            # Mesma diagonal.
            distancia_linhas = linha_nova - linha_existente
            distancia_colunas = abs(coluna_nova - coluna_existente)

            if distancia_linhas == distancia_colunas:
                return False

        return True

    def successors(self):
        """Coloca uma rainha segura na próxima linha do tabuleiro."""
        sucessores = []
        linha_nova = len(self.rainhas)

        # Um estado completo não possui sucessores.
        if linha_nova == self.dimensao:
            return sucessores

        for coluna in range(self.dimensao):
            if self.posicao_segura(coluna):
                novas_rainhas = self.rainhas + (coluna,)
                operacao = (
                    f'colocar rainha na linha {linha_nova + 1}, '
                    f'coluna {coluna + 1}'
                )

                sucessores.append(
                    NRainhas(operacao, self.dimensao, novas_rainhas)
                )

        return sucessores

    def is_goal(self):
        """O objetivo é ter exatamente N rainhas sem ataques."""
        encontrou = len(self.rainhas) == self.dimensao

        if encontrou:
            NRainhas.solucao_encontrada = self.rainhas

        return encontrou

    def description(self):
        return f'Problema das {self.dimensao}-Rainhas'

    def cost(self):
        return 1

    def env(self):
        # Identificação única do estado, usada pela poda da busca.
        return str(self.rainhas)


def mostrar_tabuleiro(dimensao, rainhas):
    """Exibe uma solução usando R para rainha e . para casa vazia."""
    for linha in range(dimensao):
        casas = []

        for coluna in range(dimensao):
            if rainhas[linha] == coluna:
                casas.append('R')
            else:
                casas.append('.')

        print(' '.join(casas))


def resolver(dimensao, algoritno=BuscaProfundidade):
    """Executa a BP para uma dimensão e imprime a solução encontrada."""
    estado_inicial = NRainhas('', dimensao)
    algoritmo = algoritno()
    NRainhas.solucao_encontrada = None

    # A profundidade máxima é N, pois cada passo coloca uma rainha.
    resultado = algoritmo.search(
        estado_inicial,
        m=dimensao,
        pruning='general'
    )

    print('=' * 35)
    print(f'Tabuleiro {dimensao} x {dimensao}')

    if resultado is None or NRainhas.solucao_encontrada is None:
        print('Nenhuma solução encontrada.')
        return

    print(f'Solução encontrada com Busca em {algoritmo.__class__.__name__}:')
    mostrar_tabuleiro(dimensao, NRainhas.solucao_encontrada)
    print('Colunas das rainhas:', NRainhas.solucao_encontrada)


def main():
    # Dimensões exigidas no enunciado: 4, 5, 6, 7 e 8.
    for dimensao in range(4, 9):
        resolver(dimensao)
        resolver(dimensao, algoritno=BuscaLargura)


if __name__ == '__main__':
    main()

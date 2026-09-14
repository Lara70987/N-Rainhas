# APS 03 — Problema das N-Rainhas

Implementação do problema das **N-Rainhas** para tabuleiros de dimensões **4, 5, 6, 7 e 8**, utilizando algoritmos de Busca em Largura e Busca em Profundidade.

## Integrantes

**Arthur Alexandre** 

**Lara Abduni** 


## Objetivo

O problema das N-Rainhas consiste em posicionar `N` rainhas em um tabuleiro de dimensão `N x N` de maneira que nenhuma rainha possa atacar outra.

Portanto, duas rainhas não podem estar:

* na mesma linha;
* na mesma coluna;
* na mesma diagonal.

Neste projeto, o problema foi implementado para tabuleiros de dimensões:

* 4 x 4;
* 5 x 5;
* 6 x 6;
* 7 x 7;
* 8 x 8.

## Algoritmos utilizados

O programa utiliza os seguintes algoritmos:

### Busca em Largura — BL

A Busca em Largura explora os estados nível por nível. No problema das N-Rainhas, cada nível da árvore de busca representa a colocação de uma nova rainha no tabuleiro.

### Busca em Profundidade — BP

A Busca em Profundidade explora um ramo da árvore até encontrar uma solução ou atingir o limite de profundidade.

O limite utilizado é `N`, pois cada movimento coloca uma rainha no tabuleiro e uma solução completa possui exatamente `N` rainhas.

Os dois algoritmos utilizam a poda `general`, disponibilizada pela biblioteca `aigyminsper`, para evitar a exploração repetida do mesmo estado.

## Representação dos estados

Cada estado é representado por uma tupla contendo as colunas das rainhas já posicionadas.

O índice de cada elemento da tupla representa a linha da rainha.

Por exemplo:

```text
(1, 3, 0, 2)
```

Essa tupla representa as seguintes posições:

```text
Linha 0, coluna 1
Linha 1, coluna 3
Linha 2, coluna 0
Linha 3, coluna 2
```

Como cada nova rainha é colocada na próxima linha disponível, não é possível colocar duas rainhas na mesma linha.

Antes de criar um novo estado, o programa verifica se a nova rainha entraria em conflito de coluna ou diagonal com alguma rainha já posicionada.

## Estrutura do projeto

```text
.
├── problema_rainha.py
└── README.md
```

## Requisitos

Para executar o projeto, é necessário ter:

* Python 3;
* biblioteca `aigyminsper`.

A biblioteca pode ser instalada com o seguinte comando:

```bash
pip install aigyminsper
```

## Como executar

No terminal, acesse a pasta do projeto e execute:

```bash
python problema_rainha.py
```

O programa executará a Busca em Largura e a Busca em Profundidade para todas as dimensões entre 4 e 8.

## Formato da saída

Na representação dos tabuleiros:

* `R` representa uma rainha;
* `.` representa uma posição vazia.

Exemplo de uma solução para o tabuleiro 4 x 4:

```text
. R . .
. . . R
R . . .
. . R .
```

A tupla correspondente é:

```text
(1, 3, 0, 2)
```

## Resultados obtidos

Os dois algoritmos encontraram soluções válidas para todas as dimensões solicitadas.

| Dimensão | Busca em Profundidade      | Busca em Largura           |
| -------- | -------------------------- | -------------------------- |
| 4 x 4    | `(2, 0, 3, 1)`             | `(1, 3, 0, 2)`             |
| 5 x 5    | `(4, 2, 0, 3, 1)`          | `(0, 2, 4, 1, 3)`          |
| 6 x 6    | `(4, 2, 0, 5, 3, 1)`       | `(1, 3, 5, 0, 2, 4)`       |
| 7 x 7    | `(6, 4, 2, 0, 5, 3, 1)`    | `(0, 2, 4, 6, 1, 3, 5)`    |
| 8 x 8    | `(7, 3, 0, 2, 5, 1, 6, 4)` | `(0, 4, 7, 5, 2, 6, 1, 3)` |

A Busca em Largura e a Busca em Profundidade podem encontrar soluções diferentes porque percorrem o espaço de estados em ordens diferentes.

Isso não representa um erro, pois o problema das N-Rainhas pode possuir várias soluções válidas para a mesma dimensão.

## Exemplo completo para N = 4

### Busca em Profundidade

```text
. . R .
R . . .
. . . R
. R . .

Colunas das rainhas: (2, 0, 3, 1)
```

### Busca em Largura

```text
. R . .
. . . R
R . . .
. . R .

Colunas das rainhas: (1, 3, 0, 2)
```

## Conclusão

O programa resolveu corretamente o problema das N-Rainhas para tabuleiros de dimensões 4, 5, 6, 7 e 8.

A geração dos sucessores considera apenas posições seguras, evitando conflitos entre as rainhas. Tanto a Busca em Largura quanto a Busca em Profundidade conseguiram encontrar soluções válidas para todas as dimensões testadas.
from velha import JogoDaVelha
import pytest

def testar_erro_tipo():
    with pytest.raises(TypeError):
        teste = JogoDaVelha(2)

def testar_impossivel_vazio():
    teste = JogoDaVelha(
        [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ]
    )
    assert teste.checar_resultado() == -2

def testar_desbalanceado():
    teste = JogoDaVelha(
        [
            [1, 1, 1],
            [0, 2, 1],
            [1, 0, 2]
        ]
    )
    assert teste.checar_resultado() == -2

def testar_dois_ganhadores():
    teste = JogoDaVelha(
        [
            [1, 1, 2],
            [1, 2, 2],
            [1, 0, 2]
        ]
    )
    assert teste.checar_resultado() == -2

def testar_x_ganha_linha():
    teste = JogoDaVelha(
        [
            [1, 1, 1],
            [0, 2, 0],
            [0, 0, 2]
        ]
    )
    assert teste.checar_resultado() == 1

def testar_x_ganha_coluna():
    teste = JogoDaVelha(
        [
            [0, 1, 0],
            [0, 1, 2],
            [2, 1, 0]
        ]
    )
    assert teste.checar_resultado() == 1

def testar_x_ganha_diagonal():
    teste = JogoDaVelha(
        [
            [1, 0, 2],
            [0, 1, 0],
            [2, 0, 1]
        ]
    )
    assert teste.checar_resultado() == 1

def testar_o_ganha_linha():
    teste = JogoDaVelha(
        [
            [1, 0, 0],
            [2, 2, 2],
            [0, 0, 1]
        ]
    )
    assert teste.checar_resultado() == 2

def testar_o_ganha_coluna():
    teste = JogoDaVelha(
        [
            [0, 0, 2],
            [1, 1, 2],
            [0, 0, 2]
        ]
    )
    assert teste.checar_resultado() == 2

def testar_o_ganha_diagonal():
    teste = JogoDaVelha(
        [
            [1, 1, 2],
            [0, 2, 1],
            [2, 0, 0]
        ]
    )
    assert teste.checar_resultado() == 2

def testar_indefinido_um():
    teste = JogoDaVelha(
        [
            [1, 2, 1],
            [2, 2, 1],
            [2, 1, 0]
        ]
    )
    assert teste.checar_resultado() == -1

def testar_indefinido_dois():
    teste = JogoDaVelha(
        [
            [1, 2, 1],
            [2, 2, 1],
            [0, 1, 0]
        ]
    )
    assert teste.checar_resultado() == -1

def testar_empate():
    teste = JogoDaVelha(
        [
            [1, 2, 1],
            [2, 2, 1],
            [1, 1, 2]
        ]
    )
    assert teste.checar_resultado() == 0

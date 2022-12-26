from codigo.Funcionario import Funcionario
import pytest
from pytest import mark

class TestClass:
    def test_quando_idade_recebe_13_03_2000_deve_retornar_22(self):
        entrada = '13/03/2000' #Given - Contexto
        esperado = 22

        funcionario_teste = Funcionario('teste', entrada, 1111)
        resultado = funcionario_teste.idade() #When - Ação

        assert resultado == esperado #Then - Desfecho

    def test_quando_sobrenome_recebe_Lucas_Carvalho_deve_retornar_Carvalho(self):
        #Given
        entrada = 'Lucas Carvalho'
        esperado = 'Carvalho'

        #When
        lucas = Funcionario(entrada, '11/11/2000', 1111)
        resultado = lucas.sobrenome()
        
        #Then
        assert resultado == esperado

    def test_quando_decrescimo_salario_recebe_100000_deve_retornar_90000(self):
       #Given
        entrada_salario = 100000
        entrada_nome = 'Paulo Bragança'
        esperado = 90000

        #When
        funcionario_teste = Funcionario(entrada_nome, '11/11/2000', entrada_salario )
        funcionario_teste.decrescimo_salario()
        resultado = funcionario_teste.salario

        #Then
        assert resultado == esperado

    @mark.calcular_bonus
    def test_quando_salario_for_igual_a_1000_recebe_100(self):
        #Given
        entrada = 1000
        esperado = 100

        #When
        funcionario_teste = Funcionario('Teste', '19/05/2003', entrada)
        resultado = funcionario_teste.calcular_bonus()

        #Then
        assert resultado == esperado 

    @mark.calcular_bonus
    def test_quando_calcular_bonus_recebe_1000000_retorna_exception(self):
        with pytest.raises(Exception):
            #Given
            entrada = 1000000
            #When
            funcionario_teste = Funcionario('Teste', '19/05/2003', entrada)
            resultado = funcionario_teste.calcular_bonus()

            #Then
            assert resultado

    # def test_retorno_da_funcao_str(self):
    #     with pytest.raises(Exception):
    #         #Given
    #         nome, data_nascimento, salario = 'Teste', '19/05/2003', 1000
    #         esperado = 'Funcionario(Teste, 19/05/2003, 1000'
    #         #When
    #         funcionario_teste = Funcionario(nome, data_nascimento, salario)
    #         resultado = funcionario_teste.__str__()

    #         #Then
    #         assert resultado == esperado



    #Para fazer com que a biblioteca pyest-cov funcione, escrevemos no terminal:pytest --cov=(Nome da pasta / arquivo) tests/
    # Assim, devolvendo o resultado somento no arquivo específicado
    
    # Usando o comnado: pytest --cov=codigo tests/ --cov-report term-missing
    # Conseguimos fazer com que o pytest nos devolva em qual linha está faltando um teste, que nesse caso, não faz muito sentido pois é a função --str--

#     ---------- coverage: platform win32, python 3.10.8-final-0 -----------
# Name                    Stmts   Miss  Cover   Missing
# -----------------------------------------------------
# codigo\Funcionario.py      35      0   100%
# -----------------------------------------------------
# TOTAL                      35      0   100%

#Usaando o comando: pytest --cov=codigo tests/ --cov-report html, fazemos com que um arquivo HTML seja gerado, facilitando a visualização do nosso código


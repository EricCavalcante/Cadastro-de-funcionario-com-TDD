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

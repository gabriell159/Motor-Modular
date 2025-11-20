
def projetar_crescimento(populacao_inicial, taxa, periodos):
    historico = []
    valor_atual = populacao_inicial

    for ano in range(periodos):
        crescimento = valor_atual * taxa
        valor_atual += crescimento
        historico.append(valor_atual)

    return historico


def teto_crescimento(inicial, taxa, periodos, limite_maximo):
    historico = []
    atual = inicial

    for i in range(periodos):

        """Se atualmente tenho 100 vagas ocupadas de um espaço de 1000 vagas, 
        temos : (1 - 0,1) = 0,9 -> (1 que equivale a 100%(espaço total) e 0,1 que equivale 10%(espaço ocupado).
        Isso significa que tenho 90% do espaço disponível e consigo crescer com velocidade,
        tenho uma curva de crescimento grande."""

        """"Se tenho 900 vagas ocupadas de um espaço de 1000 vagas,
        temos : (1 - 0,9) = 0,1. Isso significa que tenho 10% do espaço disponivel, ainda tenho curva de crescimento,
        mas, com uma inclinação menor e mais lenta"""


        percentual_ocupado = atual / limite_maximo
        freio = 1 - percentual_ocupado

        # Simula o crescimento com muito valocidade ou pouca velocidade, baseado no freio
        ganho = atual * taxa * freio

        atual = atual + ganho
        historico.append(atual)

    return historico

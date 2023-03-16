"""Universidade Federal de Santa Catarina.
   CTC - Centro Tecnologico - http://ctc.ufsc.br
   INE - Departamento de Informatica e Estatistica - http://inf.ufsc.br
"""


class Ordenacao():

    def __init__(self, array_para_ordenar: []):
        """Recebe o array com o conteudo a ser ordenado"""
        self.arranjo = array_para_ordenar

    def ordena(self):
        """Realiza a ordenacao do conteudo do array recebido no construtor"""
        novo_arranjo = [min(self.arranjo)]
        self.arranjo.pop(self.arranjo.index(min(self.arranjo)))
        tamanho = len(self.arranjo)
        for n in range(tamanho):
            novo_arranjo.append(min(self.arranjo))
            self.arranjo.pop(self.arranjo.index(min(self.arranjo)))
        self.arranjo = novo_arranjo.copy()
        novo_arranjo, tamanho = None, None

        return self.arranjo

    def toString(self):
        """Converte o conteudo do array em String formatado
           Exemplo:
           Para o conteudo do array: [1,2,3,4,5]
           Retorna: "1,2,3,4,5"
           @return String com o conteudo do array formatado
     """
        para_string = str(self.arranjo[0])
        self.arranjo.pop(0)
        for numero in self.arranjo:
            para_string += "," + str(numero)

        return para_string

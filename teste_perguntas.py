import unittest
from html2text import unifiable_n
from robo import *


class TesteInformacoesBasicas(unittest.TestCase):

    def setUp(self):
        self.robo = iniciar()

    def testar_localizacao(self):
        mensagens = [ "quais as delegacias da minha cidade?", "qual a delegacia mais proxima?" ]

        for mensagem in mensagens:
            print(f"testando a mensagem: {mensagem}")

            resposta = self.robo.get_response(mensagem)
            self.assertGreaterEqual(resposta.confidence, CONFIANCA_MINIMA)
            self.assertIn(
                "O link a seguir possui o mapa com as delegacias e postos Políciais da sua cidade", resposta.text)

    def testar_informacoes(self):
        mensagens = [ "O que precisa para entrar para a Polícia?", "quando sera o proximo concurso para a Polícia?", "o que precisa para entrar para a Polícia?",
                "preciso ter ensino superior para entrar para a Polícia ?" ]

        for mensagem in mensagens:
            print(f"testando a mensagem: {mensagem}")

            resposta = self.robo.get_response(mensagem)
            self.assertGreaterEqual(resposta.confidence, CONFIANCA_MINIMA)
            self.assertIn("Neste link você pode encontrar informações sobre novos editais, o que precisa e entre outros. Vale lembrar que para entrar para a Polícia os requisitos minimos são ensino medio completo, ser maior de 18 anos, não possuir ficha criminal.", resposta.text)

    def testar_roubo_celular(self):
        mensagens = [ "fui roubado o que devo fazer?", "roubaram o meu celular", "como abrir um b.o por roubo ?" ]

        for mensagem in mensagens:
            print(f"testando a mensagem: {mensagem}")

            resposta = self.robo.get_response(mensagem)
            self.assertGreaterEqual(resposta.confidence, CONFIANCA_MINIMA)
            self.assertIn("Neste link você pode abrir um Boletim de Ocorrencia, por favor informe local e hora, caracteristicas fisicas do assaltante (ex: possui tatuagem, altura, aparencia), modelo e o IMEI do aparelho caso tenha acesso.", resposta.text)

    def testar_denuncia(self):
        mensagens = [ "como denunciar som alto ?", "meu vizinho não desliga o som", "quero abrir um b.o por pertubação do sossego", "meu vizinho ta com o som muito alto" ]

        for mensagem in mensagens:
            print(f"testando a mensagem: {mensagem}")

            resposta = self.robo.get_response(mensagem)
            self.assertGreaterEqual(resposta.confidence, CONFIANCA_MINIMA)
            self.assertIn("Neste link você pode abrir um Boletim de Ocorrencia, lembrando que nesse caso, caso haja vontade de representar conta a outra parte, os dois individos serão levados ao cartorio, caso não, será realizada a orientação do individuo.", resposta.text)

    def testar_socorro(self):
        mensagens = [ "preciso de uma viatura para meu endereço", "preciso da Polícia aqui", "preciso de um Polícial!", "preciso da policia", "socorro", "me ajuda" ]

        for mensagem in mensagens:
            print(f"testando a mensagem: {mensagem}")

            resposta = self.robo.get_response(mensagem)
            self.assertGreaterEqual(resposta.confidence, CONFIANCA_MINIMA)
            self.assertIn("preferencialmente ligue 190, mas caso não consiga Acesse este link para chamar uma viatura com urgencia.", resposta.text)


if __name__ == "__main__":
    carregador = unittest.TestLoader()
    testes = unittest.TestSuite()

    testes.addTest(carregador.loadTestsFromTestCase(TesteInformacoesBasicas))

    executor = unittest.TextTestRunner()
    executor.run(testes)

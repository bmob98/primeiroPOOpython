# importei a classe violao para o arquivo principal
from modules.violao import Violao

# por padrão deve usar a nomeclarura __main__ na aplicação
# caso não se o nome do arquivo a aplicação não rodará
if __name__ == "__main__":
    try:
        # criei um objeto e defini os tipos dos atributos
        # o usuario devera preencher o que for pedido
        # depois a informação será intaciada ao objeto
        violao1 = Violao(cor=str, tamanho=str, cordas=int, modelo=str, uso=str)

        cor = input("Digite a cor do seu violão: ")
        violao1.set_cor(cor)
        tamanho = input("Digite o tamanho do seu violão: ")
        violao1.set_tamanho(tamanho)
        cordas = input("Digite quantas cordas tem seu violão: ")
        violao1.set_cordas(cordas)
        modelo = input("Digite o modelo do seu violão: ")
        violao1.set_modelo(modelo)
        uso = input("Digite se o seu violão é usado , novo ou seminovo: ")
        violao1.set_uso(uso)

    except Exception as e:
        print("Tratamento de erros ativado!")
        print(str(e))

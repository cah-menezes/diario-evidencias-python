"""Registra evidências de conformidade em um arquivo de texto,
combinando controles e responsáveis com data de verificação."""

from datetime import datetime

ARQUIVO_EVIDENCIAS = "evidencias.txt"

#Lista
controles = ["Revisão de firewall", "Gestão de senhas", "Monitoramento de rede"]
responsaveis = ["Bruno", "Mariana", "Carolina"]

#Funções
def registrar_evidencias(listas):
    hoje = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    with open(listas, "a") as arquivo:
        for (lista_1, lista_2) in zip(controles, responsaveis):
            arquivo.write(f"{hoje}: {lista_1} | {lista_2}\n")

#Programa Principal
if __name__ == "__main__":
    registro = registrar_evidencias(ARQUIVO_EVIDENCIAS)
#!/usr/bin/env python3
# Gerenciador criado por Marcelo Rocha | m.rocha@outlook.com.br

import os

def update_packages():
    os.system("sudo xbps-install -Suvy")
    os.system("update-grub")
    print("Pacotes atualizados com sucesso!")

def search_packages():
    search = input("Digite o nome do pacote: ")
    if search:
        output = os.popen(f"sudo xbps-query -Rs {search}").read()
        if output:
            print(output)
        else:
            print("Nenhum pacote encontrado.")

def install_packages():
    install = input("Digite o nome do pacote a ser instalado: ")
    if install:
        os.system(f"sudo xbps-install -y {install}")
        print(f"Pacote {install} instalado com sucesso!")

def remove_packages():
    remove = input("Digite o nome do pacote a ser removido: ")
    if remove:
        os.system(f"sudo xbps-remove -y {remove}")
        print(f"Pacote {remove} removido com sucesso!")

def clean_packages():
    os.system("sudo xbps-remove -Ooy")
    os.system("sudo vkpurge rm all")
    print("Pacotes limpos com sucesso!")

def main():
    while True:
        # Exibe o menu principal
        print("Escolha uma opção:")
        print("1 - Atualizar pacotes")
        print("2 - Pesquisar pacotes")
        print("3 - Instalar pacotes")
        print("4 - Remover pacotes")
        print("5 - Limpar pacotes")
        print("6 - Sair")
        choice = input("Opção: ")

        if choice == "1":
            update_packages()
        elif choice == "2":
            search_packages()
        elif choice == "3":
            install_packages()
        elif choice == "4":
            remove_packages()
        elif choice == "5":
            clean_packages()
        elif choice == "6":
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()

# Gerenciador criado por Marcelo Rocha | m.rocha@outlook.com.br
# Void_Installer_KDE

Este é um utilitário para auxiliar na instalação do ambiente Plasma / KDE completo, com (ou sem) driver Nvidia, configurar os serviços essenciais, e instalar vários utilitários para pentest e segurança no Void Linux (Opcional)!
Obs.: Para utilizar o programa é necessário realizar a instalação básica do Void Linux primeiro.
Para instalar o sistema siga o link:https://docs.voidlinux.org/installation/live-images/guide.html

Após instalar o Void e iniciar o sistema pela primeira vez, siga os comandos para instalar o ambiente:
$ sudo xbps-install -Syu ; sudo xbps-install -y python3 git
$ cd /home/$USER/ ; git clone https://github.com/zombyh/Void_Installer_KDE.git ; cd Void_Installer_KDE
$ sudo python3 Void_Installer_KDE.py


Funcionamento do utilitário:

Escolha uma opção:
1 - Instalar ambiente Plasma/KDE ⇾ Essa opção instala o ambiente completo do Plasma/KDE, e seu utilitários.
2 - Instalar driver Nvidia (Opcional) ⇾ Essa opção instala o driver Nvidia mais atual, e inicia o serviço 'nvidia-powerd'.
3 - Configurar inicialização de serviços (Obrigatório) ⇾ Essa opção inicia os serviços essenciais para o Void funcionar.
4 - Configurar grub para reconhecer dualboot Linux/Windows (Opcional) ⇾ Essa opção configura o grub caso você tenha dualboot
5 - Instalar ferramentas de segurança e pentest (Opcional) ⇾ Essa opção instala diversas ferramentas como Wireshark, nmap, etc.
0 - Sair ⇾ Essa opção fecha o utilitário.


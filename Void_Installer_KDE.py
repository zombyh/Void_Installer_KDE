# Gerenciador criado por Marcelo Rocha | m.rocha@outlook.com.br
import os

def install_packages(packages):
    os.system("xbps-install -Suy")
    os.system("xbps-install -u xbps")
    os.system("xbps-install -Suy")
    os.system("xbps-install -y " + packages)

def create_service_link(service):
    os.system("ln -s /etc/sv/{0} /var/service".format(service))

def configure_plasma():
    packages = "void-repo-nonfree void-repo-multilib void-repo-multilib-nonfree nano qbittorrent ruby nodejs vscode wireless_tools inetutils-ifconfig pipewire pulseaudio cmake git cppcheck indent colord-kde flatpak-kcm gwenview kdegraphics-thumbnailers kdewebkit krename ksolid kwrite void-updates vpnd plasma-desktop xorg base-devel kde5 kde5-baseapps plasma-browser-integration firefox-esr wireplumber colord preload gimp vlc papirus-icon-theme p7zip ntfs-3g ark kcalc ntp libreoffice aspell-pt_BR firefox-esr-i18n-pt-BR hunspell-pt_BR libreoffice-i18n-pt-BR manpages-pt-br git xtools okular wget spectacle screenFetch openjdk curl xz unzip gptfdisk mtools mlocate fuse-exfat bash-completion linux-headers ffmpeg htop autoconf automake bison curl m4 make libtool flex meson ninja optipng sassc cronie partitionmanager python3-pip"
    install_packages(packages)
    create_service_link("sddm")

def install_nvidia_driver():
    packages = "void-repo-nonfree void-repo-multilib void-repo-multilib-nonfree nvidia Vulkan-Headers nvidia-opencl nvidia-firmware nvtop"
    install_packages(packages)
    create_service_link("nvidia-powerd")

def configure_services():
    services = [
        "NetworkManager",
        "boltd",
        "colord",
        "crond",
        "cronie",
        "dbus",
        "dmeventd",
        "elogind",
        "polkitd",
        "preload",
        "rtkit",
        "udevd",
        "uuidd",
        "ntpd",
    ]
    for service in services:
        create_service_link(service)

def configure_grub():
    os.system("echo GRUB_DISABLE_OS_PROBER=false >> /etc/default/grub")
    os.system("os-prober")
    os.system("update-grub")

def install_security_tools():
    packages = "wireshark wireshark-qt terminator proxychains-ng xterm dnsmasq pixiewps hostapd reaver hcxdumptool lighttpd aircrack-ng outguess netcat tcpdump john kismet ettercap scapy whois thc-hydra tor sqlmap lynis zenmap nmap hashcat hashcat-utils bettercap"
    install_packages(packages)

def main():
    while True:
        # Menu principal
        print("Escolha uma opção:")
        print("1 - Instalar ambiente Plasma/KDE")
        print("2 - Instalar driver Nvidia (Opcional)")
        print("3 - Configurar inicialização de serviços (Obrigatório)")
        print("4 - Configurar grub para reconhecer dualboot Linux/Windows (Opcional)")
        print("5 - Instalar ferramentas de segurança e pentest (Opcional)")
        print("0 - Sair")
        choice = input("Opção: ")

        if choice == '1':
            configure_plasma()
        elif choice == '2':
            install_nvidia_driver()
        elif choice == '3':
            configure_services()
        elif choice == '4':
            configure_grub()
        elif choice == '5':
            install_security_tools()
        elif choice == '0':
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()

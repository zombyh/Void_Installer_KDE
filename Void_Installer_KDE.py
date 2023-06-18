import os

while True:
    # Menu principal
    print("Escolha uma opção:")
    print("1 - Instalar ambiente Plasma/KDE")
    print("2 - Instalar driver Nvidia (Opcional)")
    print("3 - Configurar inicialização de serviços (Obrigatório)")
    print("4 - Configurar grub para reconhecer dualboot Linux/Windows (Opcional)")
    print("5 - Sair")
    choice = input("Opção: ")
    if choice == '1':  # Instalar ambiente Plasma/KDE
        os.system("xbps-install -Suy")
        os.system("xbps-install -u xbps")
        os.system("xbps-install -Suy")
        os.system("xbps-install -y void-repo-nonfree void-repo-multilib void-repo-multilib-nonfree")
        os.system("xbps-install -Suy")
        os.system("xbps-install -yf nano inetutils-ifconfig pipewire pulseaudio cmake git cppcheck indent colord-kde flatpak-kcm gwenview kdegraphics-thumbnailers kdewebkit krename ksolid kwrite void-updates vpnd plasma-desktop xorg base-devel kde5 kde5-baseapps firefox wireplumber  colord preload gimp vlc papirus-icon-theme unrar p7zip ntfs-3g ark kcalc ntp libreoffice aspell-pt_BR firefox-i18n-pt-BR hunspell-pt_BR libreoffice-i18n-pt-BR manpages-pt-br git xtools okular wget spectacle screenFetch openjdk curl xz unzip gptfdisk mtools mlocate fuse-exfat bash-completion linux-headers ffmpeg htop autoconf automake bison curl m4 make libtool flex meson ninja optipng sassc cronie partitionmanager")
        os.system("ln -s /etc/sv/sddm /var/service")
    elif choice == '2':  # Instalar driver Nvidia (Opcional)
        os.system("xbps-install -Suy")
        os.system("xbps-install -u xbps")
        os.system("xbps-install -Suy")
        os.system("xbps-install -y void-repo-nonfree void-repo-multilib void-repo-multilib-nonfree")
        os.system("xbps-install -Suy")
        os.system("xbps-install -y nvidia")
        os.system("ln -s /etc/sv/nvidia-powerd /var/service")
    elif choice == "3":
        # Configurar inicialização de serviços (Obrigatório)
        os.system("ln -s /etc/sv/NetworkManager /var/service")
        os.system("ln -s /etc/sv/boltd /var/service")
        os.system("ln -s /etc/sv/colord /var/service")
        os.system("ln -s /etc/sv/crond /var/service")
        os.system("ln -s /etc/sv/cronie /var/service")
        os.system("ln -s /etc/sv/dbus /var/service")
        os.system("ln -s /etc/sv/dmeventd /var/service")
        os.system("ln -s /etc/sv/elogind /var/service")
        os.system("ln -s /etc/sv/polkitd /var/service")
        os.system("ln -s /etc/sv/preload /var/service")
        os.system("ln -s /etc/sv/rtkit /var/service")
        os.system("ln -s /etc/sv/udevd /var/service")
        os.system("ln -s /etc/sv/uuidd /var/service")
        os.system("ln -s /etc/sv/ntpd /var/service")
        os.system("ln -s /etc/sv/wireplumber /var/service")
    elif choice == "4":
        # Configurar grub para reconhecer dualboot Linux/Windows (Opcional)
        os.system("echo GRUB_DISABLE_OS_PROBER=false >> /etc/default/grub")
        os.system("os-prober")
        os.system("update-grub")
    elif choice == "5":
        # Sai do script
        break
    else:
        print("Opção inválida.")

import os

while True:
    # Menu principal
    print("Escolha uma opção:")
    print("1 - Instalar ambiente Plasma / KDE (Obrigatório)")
    print("2 - Instalar driver Nvidia (Opcional)")
    print("3 - Configurar inicialização de serviços (Obrigatório)")
    print("4 - Alterar terminal padrão para bash (Recomendado)")
    print("5 - Configurar grub para reconhecer dualboot Linux/Windows (Opcional)")
    print("6 - Sair")
    choice = input("Opção: ")

    if choice == '1':  # Instalar ambiente Plasma / KDE (Obrigatório)
        os.system("xbps-install -Suy")
        os.system("xbps-install -u xbps")
        os.system("xbps-install -Suy")
        os.system("xbps-install -y void-repo-nonfree void-repo-multilib void-repo-multilib-nonfree")
        os.system("xbps-install -Suy")
        os.system("xbps-install -y nano plasma-desktop xorg base-devel kde5 kde5-baseapps firefox wireplumber pulseaudio colord preload gimp vlc papirus-icon-theme unrar p7zip ntfs-3g ark kcalc ntp libreoffice aspell-pt_BR firefox-i18n-pt-BR hunspell-pt_BR libreoffice-i18n-pt-BR manpages-pt-br git xtools okular wget spectacle screenFetch openjdk curl xz unzip gptfdisk mtools mlocate fuse-exfat bash-completion linux-headers ffmpeg htop autoconf automake bison m4 make libtool flex meson ninja optipng sassc pulseaudio-utils pulsemixer cronie partitionmanager")
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
        os.system("ln -s /etc/sv/ntpd /var/service")
        os.system("ln -s /etc/sv/polkitd /var/service")
        os.system("ln -s /etc/sv/preload /var/service")
        os.system("ln -s /etc/sv/rtkit /var/service")
        os.system("ln -s /etc/sv/sddm /var/service")
        os.system("ln -s /etc/sv/udevd /var/service")
        os.system("ln -s /etc/sv/uuidd /var/service")
        os.system("ln -s /etc/sv/wireplumber /var/service")
    elif choice == "4":
        # Alterar terminal padrão para bash (Recomendado)
        os.system("chsh -s /bin/bash ; su")
    elif choice == "5":
        # Configurar grub para reconhecer dualboot Linux/Windows
        os.system("echo GRUB_DISABLE_OS_PROBER=false >> /etc/default/grub")
        os.system("os-prober")
        os.system("update-grub")
    elif choice == "6":
        # Sai do script
        break
    else:
        print("Opção inválida.")

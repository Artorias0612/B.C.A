import os
import time

wallpaperlist = ['wallpaper.jpeg', 'wallpaper2.jpeg', 'wallpaper3.jpeg', 'wallpaper4.jpg', 'wallpaper5.jpg',
                 'wallpaper6.jpeg']

while True:

    for chosen in wallpaperlist:

        os.system(f'gsettings set org.gnome.desktop.background picture-uri file:////home/funlife/Pictures/Wallpapers/{chosen}')
        time.sleep(60)

from pytube import YouTube
import os
from art import *

def header():
    print("\n▪====================================================================================================================================================▪\n")
    tprint("Julien  Youtube   Downloader")
    print( "▪====================================================================================================================================================▪\n")

def youtube_video_download():

    yt = YouTube(str(input("Entrez le lien de la vidéo youtube : ")))

    video = yt.streams.filter(only_audio=True).first()

    # choix du chemin du type : C:\Users\Chadow4-PC\Desktop

    destination = str(input("Entrez le chemin dans lequel vous voulez mettre le fichier audio (ou enter pour le répertoire courant) : ")) or '.'

    out_file = video.download(output_path=destination)

    base, ext = os.path.splitext(out_file)

    new_file = base + '.mp3'

    os.rename(out_file, new_file)

    print("`\nTitre de la video: ",yt.title)
    print("\nNombre de vues: ",yt.views)
    print("\nLongueur de la video: ",yt.length)

    print("\nVotre musique a était téléchargé !")

def credit():
    print("\nmerci d'avoir utilisé ce downloader :)")
    print("\ncréateur : https://github.com/chadow4")

header()
youtube_video_download()
credit()

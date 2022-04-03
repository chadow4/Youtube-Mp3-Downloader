from pytube import YouTube
import os

yt = YouTube(str(input("Entrez le lien de la vidéo youtube : \n ")))

video = yt.streams.filter(only_audio=True).first()

# choix du chemin du type : C:\Users\Chadow4-PC\Desktop

print("Entrez le chemin dans lequel vous voulez mettre le fichier audio (ou enter pour le répertoire courant)")

destination = str(input(" ")) or '.'

out_file = video.download(output_path=destination)

base, ext = os.path.splitext(out_file)

new_file = base + '.mp3'

os.rename(out_file, new_file)

print("Titre de la video: ",yt.title)
print("Nombre de vues: ",yt.views)
print("Longueur de la video: ",yt.length)

print(" Votre musique a était téléchargé !")
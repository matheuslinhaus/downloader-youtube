from pytube import YouTube
import moviepy.editor as mp
import os
import re
import unicodedata

# # A remoção de acentos foi baseada em uma resposta no Stack Overflow.
# # http://stackoverflow.com/a/517974/3464573
def removerAcentosECaracteresEspeciais(palavra):
    # Unicode normalize transforma um caracter em seu equivalente em latin.
    nfkd = unicodedata.normalize('NFKD', palavra)
    palavraSemAcento = u"".join([c for c in nfkd if not unicodedata.combining(c)])
    # Usa expressão regular para retornar a palavra apenas com números, letras e espaço
    return re.sub('[^a-zA-Z0-9 \\\]', '', palavraSemAcento)

tgt_folder = "C:/MP3/"
url = str(input("URL: "))
# download a file with only audio, to save space
# if the final goal is to convert to mp3
youtube_link = url
y = YouTube(youtube_link)
t = y.streams.filter(only_audio=True).all()
name = removerAcentosECaracteresEspeciais(y.title).replace("  ", " ")
print(name)
t[0].download(output_path=tgt_folder, filename=name)


for file in [n for n in os.listdir(tgt_folder) if re.search('mp4',n)]:
    full_path = os.path.join(tgt_folder, file)
    output_path = os.path.join(tgt_folder, os.path.splitext(file)[0] + '.mp3')
    clip = mp.AudioFileClip(full_path).subclip(10,)
    clip.write_audiofile(output_path)
    os.remove(tgt_folder+file)




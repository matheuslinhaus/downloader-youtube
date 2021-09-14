from tkinter import *
from pytube import YouTube
import moviepy.editor as mp
import os
import re
import unicodedata

def yt_download():
    tgt_folder = "C:/MP3/"
    youtube_link = url_text.get('1.0', 'end')
    y = YouTube(youtube_link)
    t = y.streams.filter(only_audio=True).all()
    name = removerAcentosECaracteresEspeciais(y.title).replace("  ", " ")
    t[0].download(output_path=tgt_folder, filename_prefix=name)
    for file in [n for n in os.listdir(tgt_folder) if re.search('mp4',n)]:
        full_path = os.path.join(tgt_folder, file)
        output_path = os.path.join(tgt_folder, os.path.splitext(file)[0] + '.mp3')
        clip = mp.AudioFileClip(full_path).subclip(10,)
        clip.write_audiofile(output_path)
        os.remove(tgt_folder+file)

def removerAcentosECaracteresEspeciais(palavra):
        # Unicode normalize transforma um caracter em seu equivalente em latin.
        nfkd = unicodedata.normalize('NFKD', palavra)
        palavraSemAcento = u"".join([c for c in nfkd if not unicodedata.combining(c)])
        # Usa expressão regular para retornar a palavra apenas com números, letras e espaço
        return re.sub('[^a-zA-Z0-9 \\\]', '', palavraSemAcento)

janela = Tk()

janela.title('YouTube Download')

texto_descricao = Label(janela, text='Insira a URL para download')
texto_descricao.grid(column=0 , row=0)

texto_url = Label(janela, text='URL: ')
texto_url.grid(column=0, row=1)

url_text = Text(janela,height = 1,width = 23)
url_text.grid(column=1, row=1)

botao_download = Button(janela, text='Download', command=yt_download)
botao_download.grid(column=1, row=2)

janela.mainloop()
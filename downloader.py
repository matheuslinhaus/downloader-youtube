from pytube import YouTube
import moviepy.editor as mp
import os
import re
import unicodedata
import tela

diretorio = "C:/MP3/"

def baixa_arquivo_youtube():
    dados_video = YouTube(tela.url_text.get('1.0', 'end'))
    download_video = dados_video.streams.filter(only_audio=True).all()
    titulo_video = removerAcentosECaracteresEspeciais(dados_video.title).replace("  ", " ")
    download_video[0].download(output_path=diretorio, filename_prefix=titulo_video)

def converte_arquivo_mp3():
    for arquivo in [n for n in os.listdir(diretorio) if re.search('mp4', n)]:
            full_path = os.path.join(diretorio, arquivo)
            output_path = os.path.join(
                diretorio, os.path.splitext(arquivo)[0] + '.mp3')
            clip = mp.AudioFileClip(full_path).subclip()
            clip.write_audiofile(output_path)
            os.remove(diretorio+arquivo)

def download_button():
    tela.texto_mensagem.grid(column=1, row=2, pady=(0, 6))
    try:
        baixa_arquivo_youtube()
        converte_arquivo_mp3()
        tela.texto_mensagem.configure(text="Download concluído com sucesso!!", fg='#008000', font=('Arial', 9, 'bold'))
    except:
        tela.texto_mensagem.configure(text="Informe uma URL válida do YouTube para download", fg='#f00', font=('Arial', 9, 'bold'))

# # A remoção de acentos foi baseada em uma resposta no Stack Overflow.
# # http://stackoverflow.com/a/517974/3464573

def removerAcentosECaracteresEspeciais(palavra):
    # Unicode normalize transforma um caracter em seu equivalente em latin.
    nfkd = unicodedata.normalize('NFKD', palavra)
    palavraSemAcento = u"".join(
        [c for c in nfkd if not unicodedata.combining(c)])
    # Usa expressão regular para retornar a palavra apenas com números, letras e espaço
    return re.sub('[^a-zA-Z0-9 \\\]', '', palavraSemAcento)
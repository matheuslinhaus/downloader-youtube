from tkinter import *
from downloader import *

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
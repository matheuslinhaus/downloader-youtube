from tkinter import *
from tkinter.ttk import Progressbar
from downloader import *

janela = Tk()

janela.title('YouTube Download')

imagem = PhotoImage(file="youtube-logo-9-2048x456.png")
imagem = imagem.subsample(23)
logo = Label(janela, image=imagem)
logo.grid(column=1, row=0, pady=(10, 0))


texto_descricao = Label(janela, text='')
texto_descricao.grid(column=0, row=0)

texto_url = Label(janela, text='URL: ', font=('Helvetica', 11, 'bold'))
texto_url.grid(column=0, row=1, sticky=W)

url_text = Text(janela, height=1, width=50)
url_text.grid(column=1, row=1, sticky=W, padx=(5, 8), pady=10)

botao_download = Button(janela, text='Download', command=yt_download)
botao_download.grid(column=1, row=3, pady=(0, 6))

janela.mainloop()
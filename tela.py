from tkinter import *
import downloader

janela = Tk()

janela.title('YouTube Download')

imagem = PhotoImage(file="youtube-logo-9-2048x456.png")
imagem = imagem.subsample(23)
logo = Label(janela, image=imagem)
logo.grid(column=1, row=0, pady=(10, 0))

texto_descricao = Label(janela, text='')
texto_descricao.grid(column=0, row=0)

texto_url = Label(janela, text='URL: ', font=('Arial', 10, 'bold'))
texto_url.grid(column=0, row=1, sticky=W)

url_text = Text(janela, height=1, width=50)
url_text.grid(column=1, row=1, sticky=W, padx=(5, 8), pady=10)

texto_mensagem = Label(janela, text="")

photo = PhotoImage(file = "icon-download.png")
photoimage = photo.subsample(30, 30)

botao_download = Button(janela, text='Download', command=downloader.download_button, image = photoimage, compound='left')
botao_download.grid(column=1, row=3, pady=(0, 6))

janela.mainloop()
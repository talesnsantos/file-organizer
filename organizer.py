# @AUTHOR: Tales L N Santos

import os
import time
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler
from watchdog.events import LoggingEventHandler
from watchdog.events import FileSystemEventHandler

class organizer():
    def __init__(self):
        pass

    
 
    # pega a extensão dos arquivos na pasta
    def get_extension(self,name):
        index = name.rfind('.')
        return name[index:]

    #organiza os arquivos nas pastas
    def organizar(self,directory):
        #listas com a extensão de cada arquivo
        audio = ['.MP3','.AAC','.WMA','.ALAC', '.FLAC', '.AIFF', '.PCM', '.WAV']
        video = ['.avi', '.mp4', '.m4v', '.mov', '.mpg', '.mpeg', '.wmv','.mkv']
        doc = ['.DOC','.docx', '.pdf', '.PPT', '.xlsx','.txt']
        program = ['.exe','.gz', '.txz', '.sh']

        #montando o endereço de cada pasta
        AUDIO_DIR = os.path.join(directory,"audios")
        VIDEO_DIR = os.path.join(directory,"videos")
        DOC_DIR = os.path.join(directory,"documentos")
        PROGRAM_DIR = os.path.join(directory,"programas")
        OTHERS_DIR = os.path.join(directory,"Outros")

        directories = [AUDIO_DIR,
        VIDEO_DIR ,
        DOC_DIR ,
        PROGRAM_DIR,
        OTHERS_DIR ]

        #lista todos os itens no endereço escolhido
        files = os.listdir(directory)

        #verifica se a pasta ja existe e se n~ao existir ele cria
        for value in directories:
            if not os.path.isdir(value):
                os.mkdir(value)

        temp = ''
        # pega a extensão de cada arquivo e coloca cada um em sua pasta 
        for File in files:
            extension = str.lower(self.get_extension(File))
            if os.path.isdir(File):
                print(f'Isso é uma pasta {File}')
                continue
            else:
               
                print('  ------->    ',File)
        
                if extension in audio:
                    temp = AUDIO_DIR
                    print(f'arquivo {File} organizado na pasta {temp}')
                elif extension in video:
                    temp = VIDEO_DIR
                    print(f'arquivo {File} organizado na pasta {temp}')
                elif extension in program:
                    temp = PROGRAM_DIR
                    print(f'arquivo {File} organizado na pasta {temp}')
                elif extension in doc:
                    temp = DOC_DIR
                    print(f'arquivo {File} organizado na pasta {temp}')
                else:
                    temp = OTHERS_DIR
                    print(f'arquivo {File} organizado na pasta {temp}')

                    #move o arquivo pra pasta certa
                os.rename(os.path.join(directory,File),os.path.join(temp,File))

    

class observe(FileSystemEventHandler):
    
    #quando algo é criado
    @staticmethod
    def on_created(event):
        print(f" arquivo criado foi criado com sucesso na pasta {event.src_path} !\n\n")
        time.sleep(5)
        organizer().organizar(path)
        

    #caso algo é deletado
    @staticmethod
    def on_deleted(event):
        print(f"A pasta {event.src_path} foi Deletada com Sucesso !\n\n")
        time.sleep(5)
        organizer().organizar(path)

    #quando algo é modificado
    @staticmethod
    def on_modified(event):
        print(f"A Pasta {event.src_path} Foi modificado\n\n")
        time.sleep(5)
        organizer().organizar(path)

    #quando algo for movido
    @staticmethod
    def on_moved(event):
        print(f"{event.src_path} Arquivo movido para {event.dest_path}\n\n")
        time.sleep(5)
        organizer().organizar(path)

# Iniciando Observador
path = input('Digite o endereço da pasta que sera observada e organizada \n ')
go_recursively = True
my_handler = observe()
my_observer = Observer()
my_observer.schedule(my_handler, path, recursive=go_recursively)
my_observer.start()
print('''
----------------------------
|                          |
|  Observador Iniciado...  |
|                          |
----------------------------

''')
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    my_observer.stop()
    my_observer.join()


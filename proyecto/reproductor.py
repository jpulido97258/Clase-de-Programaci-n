from tkinter import *                       #tkinter es una libreria funciona para realizar aplicaciones de escritorio
from audioplayer import AudioPlayer         # * se usa para que los modulos esten disponibles
import os

archivos=os.listdir()
root=Tk()                                    #root es una libreria 
root.title('AudioPlayer')                    #root.title se utiliza para dar nombre a la aplicación

global a
a=1
print(a)

player_frame=Frame(root)          
player_frame.pack(fill='both', pady=20, padx=30)           #frame y las extensiones de este se usan para dar la forma de la app
player_frame.config(bg='purple',width='200',height='300')  #both operador igualitario

control_frame=Frame(root)
control_frame.pack(fill='both', padx=20, pady=20)

global song_to_play
song_to_play=AudioPlayer("./shine.mp3" )

def play():
    song_to_play.play(loop=True, block=False)
def pause():
   song_to_play.pause()
def resume():
    song_to_play.resume()
def stop():
    song_to_play.stop()
def next():
    stop()
    global a 
    a +=1
    global song_to_play
    song_to_play=AudioPlayer("./Rammstein.mp3") 
    play()

play_button=Button(control_frame, text='play' , width=6, height=4, command=play, bg="lightpink")
play_button.grid(row=1, column=1)

pause_button=Button(control_frame, text='pause' , width=6, height=4, command=pause,bg="lightblue")
pause_button.grid(row=1, column=2)

resume_button=Button(control_frame, text='resume' , width=6, height=4, command=resume,bg="lightpink")
resume_button.grid(row=1, column=3)

stop_button=Button(control_frame, text='stop' , width=6, height=4, command=stop,bg="lightblue")
stop_button.grid(row=1, column=4)

next_button=Button(control_frame, text='next' , width=6, height=4, command=next,bg="lightpink")
next_button.grid(row=1, column=5)

root.mainloop() #la función de mainloop se utiliza para que todas las extensiones de tk funcionen

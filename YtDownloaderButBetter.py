from pytube import YouTube
import os
import tkinter as tk

TK_SILENCE_DEPRECATION=1
root = tk.Tk()
root.title('YouTube Downloader')
root.geometry('800x400')

frame=tk.Frame(root)
frame.pack(pady=20,padx=60,fill='both',expand=True)

entry1 = tk.Entry(master=frame,text='Enter URL here',bg='white',fg='lightgray')
entry1.pack(pady=12,padx=10)
entry2 = tk.Entry(master=frame)
entry2.pack(pady=12,padx=10)
entry2.insert(0,'Enter path here')
def download(url:str,path:str):
    yt = YouTube(url)
    if checkbox.instate(['selected']):
        audio = yt.streams.filter(only_audio=True).first()
        audio.download(path)
    else:
        video = yt.streams.filter(progressive=True, file_extension='mp4').get_highest_resolution()
        video.download(path)
    print('Successfully downloaded :', yt.title)
    entry1.delete(0,'end')
    entry2.delete(0,'end')
    entry1.insert(0,'Enter URL here')
    entry2.insert(0,'Enter path here')
button=tk.Button(master=frame,text='Download',command=lambda: download(entry1.get(),entry2.get()))
button.pack(pady=12,padx=10)
checkbox = tk.Checkbutton(master=frame,text='Download audio only')
checkbox.pack(pady=12,padx=10)

root.mainloop()
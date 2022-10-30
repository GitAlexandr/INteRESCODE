from pytube import YouTube

PATH = "/Users/sasha/Desktop/gg/video"
URL = input("Введите ссылку на видео: ")
NAME = input("Введите любое название файла: ")

try:

    video_url = YouTube(URL)

    video_streams = (video_url.streams.filter(progressive=True, 
file_extension='mp4'))
    
video_streams.get_highest_resolution().download(filename=f'{NAME}.mp4', 
output_path=PATH)

    print('Успех!!!')
except Exception as e:
    print(e)

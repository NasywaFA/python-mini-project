import time
from threading import Thread, Lock
import sys

lock = Lock()

def animate_text(text, delay=0.1):
    with lock:
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(delay)
        print()

def sing_lyric(lyric, delay, speed):
    time.sleep(delay)
    animate_text(lyric, speed)

def sing_song():
    lyrics = [
        ("\n""We fell in love in October", 0.1),
        ("That's why I love fall", 0.2),
        ("Looking at the stars", 0.1),
        ("Admiring from afar", 0.2),
        
        ("\n""My girl, my girl, my girl", 0.1),
        
        ("\n""You will be my girl", 0.07),
        ("My girl, my girl, my girl", 0.1),
        
        ("\n""You will be my world", 0.07),
        ("My world, my world, my world", 0.1),
        
        ("\n""You will be my girl", 0.1),
        
        ("\n""Lop u mmih, feron, mamah, capje, kniy <3", 0.07)
    ]
    delays = [0.3, 4.25, 8.47, 12.5, 15.11, 20.24, 22.75, 27.87, 29.99, 35.14, 36.0]
    
    threads = []
    for i in range(len(lyrics)):
        lyric, speed = lyrics[i]
        t = Thread(target=sing_lyric, args=(lyric, delays[i], speed))
        threads.append(t)
        t.start()
    
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    sing_song()
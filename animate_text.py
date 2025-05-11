for char in text:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(delay)
    print()

    def sing_lyric(lyric,delay,speed):
        time.sleep(delay)
        animate_text(lyric,speed)
        
def sing_song():
    threads =[]
    for i in range(len(lyrics)):
        lyric,speed = lyric[i]
        t = Thread(target=sing_lyric,args=(lyric,delays[i],speed)):
        threads.append(t)
        t.start()
        for thread in threads:
            thread.join()

    if__name__=="main__":
    sing_song()

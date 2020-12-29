from pygame import mixer

def play_music(name):
    mixer.init()
    mixer.music.load(name)
    mixer.music.set_volume(0.5)
    mixer.music.play()
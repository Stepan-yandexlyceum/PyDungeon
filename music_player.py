from pygame import mixer
import random


def play_music(name):
    mixer.init()
    mixer.music.load(name)
    mixer.music.set_volume(0.5)
    mixer.music.play()


def injure_sound():
    injure = mixer.Sound(
        random.choice(["data\music\pain1.wav", "data\music\pain2.wav", "data\music\pain3.wav", "data\music\pain4.wav",
                       "data\music\pain5.wav", "data\music\pain6.wav"]))
    injure.play()


def door_sound():
    door = mixer.Sound(
        random.choice(
            ["data\music\door-01.flac", "data\music\door-02.flac", "data\music\door-03.flac", "data\music\door-04.flac",
             "data\music\door-05.flac", "data\music\door-06.flac", "data\music\door-07.flac"]))
    door.play()


def step_sound():
    step = mixer.Sound(
        random.choice(["data\music\step1.flac", "data\music\step2.flac"])
    )
    step.play()


def inventory_sound(type="other"):
    if type == "weapon":
        sound = mixer.Sound("data\music\metal-clash.wav")
    else:
        sound = mixer.Sound(
            random.choice(["data\music\leather_inventory.wav", "data\music\cloth-inventory.wav"]))
    sound.play()

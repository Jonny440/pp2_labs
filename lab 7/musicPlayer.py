import pygame
import os

pygame.init()
pygame.mixer.init()

MUSIC_FOLDER = "lab 7"
tracks = [f for f in os.listdir(MUSIC_FOLDER) if f.endswith((".mp3", ".wav"))]
current_track = 0

def load_track(index):
    pygame.mixer.music.load(os.path.join(MUSIC_FOLDER, tracks[index]))
    pygame.mixer.music.play()

if tracks:
    load_track(current_track)

screen = pygame.display.set_mode((400, 200))
pygame.display.set_caption("Music Player")

running = True
paused = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:   
                if pygame.mixer.music.get_busy():
                    pygame.mixer.music.pause()
                    paused = True
                else:
                    pygame.mixer.music.unpause()
                    paused = False

            elif event.key == pygame.K_s:
                pygame.mixer.music.stop()

            elif event.key == pygame.K_n:
                current_track = (current_track + 1) % len(tracks)
                load_track(current_track)

            elif event.key == pygame.K_p:
                current_track = (current_track - 1) % len(tracks)
                load_track(current_track)

pygame.quit()

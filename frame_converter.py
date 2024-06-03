from PIL import Image
import os
import time

# Frames are 13y by 41x text pixels
chars = ["⠀", "░", "▒", "▓", "█"]
chars2 = ["⠀", "█"]

start = time.time()
for filename in os.listdir("frames"):
    frame = Image.open(f"frames\\{filename}")
    frame = frame.resize((72, 23))
    file = open(f"text_frames_no_blur\\{filename[:-4]}.txt", 'w', encoding='utf-8')
    print(f"Treating image: {filename}")
    for y in range(frame.height):
        for x in range(frame.width):
            colour = frame.getpixel((x, y))
            file.write(chars2[max(0, round((colour[0] + colour[1] + colour[2]) / 382.5) - 1)])
        file.write("\n")

print(f"Took {time.time() - start} seconds")

from PIL import Image
import os

# Frames are 13y by 41x text pixels
chars = ["⠀", "░", "▒", "▓", "█"]
# each text pixel is 27y by 12x pixels

# for filename in os.listdir("\\frames"):
frame = Image.open("frames\\resized.png")
file = open("text_frames\\newfile.txt", 'w', encoding='utf-8')
for y in range(frame.height):
    for x in range(frame.width):
        colour = frame.getpixel((x, y))
        file.write(chars[max(0, round(colour / 51) - 1)])
    file.write("\n")

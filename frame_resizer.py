from PIL import Image

frame = Image.open("frames\\330.png")
frame = frame.resize((72, 23))

chars = ["⠀", "░", "▒", "▓", "█"]
# each text pixel is 27y by 12x pixels

# for filename in os.listdir("frames"):
file = open("text_frames_with_blur\\330.txt", 'w', encoding='utf-8')
for y in range(frame.height):
    for x in range(frame.width):
        colour = frame.getpixel((x, y))
        file.write(chars[max(0, round((colour[0] + colour[1] + colour[2]) / 153) - 1)])
    file.write("\n")

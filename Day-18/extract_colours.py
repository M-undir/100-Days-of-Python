import colorgram
colors = colorgram.extract('image.jpg', 30)
colours = []
for i in range(len(colors)):
    r_g_b = (colors[i].rgb.r, colors[i].rgb.g, colors[i].rgb.b)
    colours.append(r_g_b)

# What I did to extract the colours from the image and append to a list

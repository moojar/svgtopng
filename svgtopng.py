import os
from datetime import datetime
import cairosvg as c

# settings
path = "PATH/TO/SVG/FILES"
outputpath = "output/"

startTime = datetime.now()
iterations = 0

for filename in os.listdir(path):
    print ("CONVERTING SVG:" + str(filename) + " to PNG")
    base, ext = os.path.splitext(filename)

    filepath = os.path.join(path, filename)
    output = outputpath + base + ".png"

    try:
        c.svg2png(url=filepath, write_to=output)
    except:
        print ("ERROR - unable to open: " + str(filepath) + "\n")
    else:
        iterations += 1
        print ("SUCCESS.\n")

print (str(iterations) + " files converted.")
print("DONE: " + str(datetime.now() - startTime))
import os, sys

image_filepath = r"C:\Users\Tim.Golden\Pictures\sheep.png"
html = """<html>
<head><title>A Picture</title></head>
<body>
<img src="file:///c:/users/tim.golden/pictures/sheep.png" />
</body>
</html>
"""
with open("image.html", "w") as f:
    f.write(html)

os.startfile("image.html")

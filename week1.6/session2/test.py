from image import Image

image=Image.read("./images/coins.pgm")
image.create_pixels(10, 5)
image.write_pgm("test.pgm")


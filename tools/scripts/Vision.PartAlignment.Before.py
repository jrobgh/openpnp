width = part.getPackage().getFootprint().getBodyWidth()
height = part.getPackage().getFootprint().getBodyHeight()

length = max([width,height])

print("NEODEN UP camera part size:", length)

camera = machine.getCameras()[0]

if length < 4:
	camera.width = 256
	camera.height = 256
	camera.shiftX = 384
	camera.shiftY = 384
	print("NEODEN UP camera selected small")
elif length < 10:
	camera.width = 512
	camera.height = 512
	camera.shiftX = 256
	camera.shiftY = 256
	print("NEODEN UP camera selected medium")
else:
	camera.width = 1024
	camera.height = 1024
	camera.shiftX = 0
	camera.shiftY = 0
	print("NEODEN UP camera selected big")

width = part.getPackage().getFootprint().getBodyWidth()
height = part.getPackage().getFootprint().getBodyHeight()

length = max([width,height])

print("NEODEN DOWN camera part size:", length)

camera = machine.defaultHead.defaultCamera

if length < 1.5:
	camera.width = 256
	camera.height = 256
	camera.shiftX = 384
	camera.shiftY = 384
	print("NEODEN DOWN camera selected small")
elif length < 3:
	camera.width = 512
	camera.height = 512
	camera.shiftX = 256
	camera.shiftY = 256
	print("NEODEN DOWN camera selected medium")
else:
	camera.width = 1024
	camera.height = 1024
	camera.shiftX = 0
	camera.shiftY = 0
	print("NEODEN DOWN camera selected big")

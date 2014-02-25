from time import sleep

seconds = 0

while seconds < 1000:
	m, s = divmod(seconds, 60)
	h, m = divmod(m, 60)
	time = "%d:%02d:%02d" % (h, m, s)
	length = len(time)

	while length > 0:
		print("\r", end="")
		length -= 1

	print (time, end="")
	sleep(1)
	seconds += 1
	
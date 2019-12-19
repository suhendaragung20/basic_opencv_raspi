import cv2

vs = cv2.VideoCapture(0)


while True:

	ret, image = vs.read()

	cv2.namedWindow("Plant detector", cv2.WINDOW_KEEPRATIO)
	cv2.setWindowProperty("Plant detector", cv2.WND_PROP_ASPECT_RATIO, cv2.WINDOW_KEEPRATIO)
	cv2.imshow('Plant detector', image)


	# Press any key to close the image
	key = cv2.waitKey(1) & 0xFF

	# if the `q` key was pressed, break from the loop
	if key == ord("q"):
		break


# Clean up
cv2.destroyAllWindows()
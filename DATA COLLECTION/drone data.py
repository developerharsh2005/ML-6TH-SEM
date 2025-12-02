import cv2

stream_url = "http://192.168.1.10:8080/video"

cap = cv2.VideoCapture(stream_url)

fourcc = cv2.VideoWriter_fourcc(*"XVID")
out = cv2.VideoWriter("drone_video.avi", fourcc, 20.0, (640, 480))

while True:
    ret, frame = cap.read()
    if not ret:
        break

    out.write(frame)
    cv2.imshow("Drone Stream", frame)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()

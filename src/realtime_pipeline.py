import cv2
import time

cap = cv2.VideoCapture(0)

prev = 0

while True:

    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    edges = cv2.Canny(gray,100,200)

    time_now = time.time()
    fps = 1/(time_now-prev) if prev else 0
    prev = time_now

    cv2.putText(edges,f"FPS: {int(fps)}",(20,40),
                cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,255),2)

    cv2.imshow("Realtime Edge Detection",edges)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

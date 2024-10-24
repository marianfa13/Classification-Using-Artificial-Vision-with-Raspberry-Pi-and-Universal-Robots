from picamera2 import Picamera2
import cv2
from ultralytics import YOLO
import numpy as np
import sm_4rel4in as sm
import time
import socket

HOST = "192.168.2.108"
PORT = 30000


def box_label(imagen, box):
    p1 = (int(box[0]), int(box[1]))
    p2 = (int(box[2]), int(box[3]))
    cv2.rectangle(imagen, p1, p2, (0, 255, 0))


def send_info(xc_mm, yc_mm):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((HOST, PORT))
        s.listen(1)  # Listening for a single connection
        print("Waiting for a connection...")
        c, addr = s.accept()
        print("Connection established with:", addr)

        while True:
            msg = c.recv(64)
            print("msg:", msg)
            if msg == b"asking_for_data":
                p = f"({xc_mm},{yc_mm},0,0,0,0)"
                print("String to send:", p)
                c.send(p.encode("utf-8"))
                break  # Exit loop after sending data
    except Exception as e:
        print("Error:", e)
    finally:
        c.close()
        s.close()


def box_centre(box):
    x1, y1, x2, y2 = box
    xc = x1 + (x2 - x1) / 2
    yc = y1 + (y2 - y1) / 2
    xref1, yref1 = 106, 67
    xref2, yref2 = 438, 401
    pixeles_mm_x = (xref2 - xref1) / 100
    pixeles_mm_y = (yref2 - yref1) / 100
    xc_mm = int(xc / pixeles_mm_x)
    yc_mm = int(yc / pixeles_mm_y)
    return xc_mm, yc_mm


def plot_box(image, boxes):
    for box in boxes:
        print("Box:", box)
        xc_mm, yc_mm = box_centre(box)
        print("xc, yc mm:", xc_mm, yc_mm)
        send_info(xc_mm, yc_mm)
        if int(box[5]) == 47:  # Corrected condition
            print('Manzana')
            rel.set_relay(1, 1)
            time.sleep(10)
            rel.set_relay(1, 0)
        elif int(box[5]) == 49:
            print('Naranja')
            rel.set_relay(2, 1)
            time.sleep(10)
            rel.set_relay(2, 0)

        box_label(image, box)
        cv2.imshow("Vision Robot", image)
        key = cv2.waitKey(1) & 0xFF
        if key == ord('s'):
            break


cam = Picamera2()
cam.start()
rel = sm.SM4rel4in(0)
model = YOLO('yolov8m.pt')

try:
    while True:
        t_init = time.time()
        image = cam.capture_array()
        image = cv2.cvtColor(image, cv2.COLOR_RGBA2BGR)
        results = model.predict(image)

        for result in results:
            plot_box(image, result.boxes.data)

finally:
    cam.stop()
    cam.close()
    cv2.destroyAllWindows()

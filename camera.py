import cv2

class VideoCamera(object):
    def __init__(self):
        # Uso de OpenCV para capturar desde el dispositivo 0. Si tiene problemas para capturar
        # desde una cámara web, comente la línea a continuación y use un archivo de video
        # en su lugar.
        self.video = cv2.VideoCapture(0)
        # Si decide usar video.mp4, debe tener este archivo en la carpeta
        # Como la main.py.
        # self.video = cv2.VideoCapture ('video.mp4')
    
    def __del__(self):
        self.video.release()
    
    def get_frame(self):
        success, image = self.video.read()
        # Estamos usando Motion JPEG, pero OpenCV está predeterminado para capturar imágenes en bruto,
        # por lo que debemos codificarlo en JPEG para mostrar correctamente el
        # Video en directo.
        ret, jpeg = cv2.imencode('.jpg', image)
        return jpeg.tobytes()

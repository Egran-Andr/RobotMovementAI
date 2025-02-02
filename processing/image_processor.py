import cv2

class ImageProcessor:
    def resize_image(self, image, width, height):
        return cv2.resize(image, (width, height))

    def normalize_image(self, image):
        return image / 255.0
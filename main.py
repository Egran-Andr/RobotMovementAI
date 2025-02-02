from detection.object_detector import ObjectDetector
from detection.segmentation import ImageSegmenter
from processing.image_processor import ImageProcessor
from processing.video_processor import VideoProcessor

def main():
    # Инициализация компонентов
    object_detector = ObjectDetector("path_to_model")
    image_segmenter = ImageSegmenter("path_to_model")
    image_processor = ImageProcessor()
    video_processor = VideoProcessor(0)  # 0 - индекс камеры
    route_planner = RoutePlanner("map_data")

    while True:
        ret, frame = video_processor.cap.read()
        if not ret:
            break

        # Обработка кадра
        processed_frame = image_processor.resize_image(frame, 640, 480)
        detected_objects = object_detector.detect_objects(processed_frame)
        segmented_image = image_segmenter.segment_image(processed_frame)

        # Планирование маршрута
        route = route_planner.plan_route(start_position, end_position)

        # Отображение результатов
        cv2.imshow("Processed Frame", processed_frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    video_processor.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
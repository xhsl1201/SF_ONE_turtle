import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2
import os
from rclpy.qos import QoSProfile, ReliabilityPolicy, HistoryPolicy, DurabilityPolicy

class ImageSubscriber(Node):
    def __init__(self):
        super().__init__('image_subscriber')

        qos_profile = QoSProfile(
            reliability=ReliabilityPolicy.BEST_EFFORT,
            history=HistoryPolicy.KEEP_LAST,
            depth=1,
            durability=DurabilityPolicy.VOLATILE
        )

        self.subscription = self.create_subscription(
            Image,
            '/image_raw',
            self.listener_callback,
            qos_profile)

        self.bridge = CvBridge()
        self.window_name = "TurtleBot_View"
        self.get_logger().info('이미지 구독 노드가 시작되었습니다.')

    def listener_callback(self, data):
        try:
            # 원본 데이터 가져오기
            cv_image = self.bridge.imgmsg_to_cv2(data, desired_encoding='passthrough')

            # YUV 인코딩 처리
            if data.encoding in ['yuv422', 'yuyv', 'yuv422_yuy2']:
                cv_image = cv2.cvtColor(cv_image, cv2.COLOR_YUV2BGR_YUYV)
            elif data.encoding == 'rgb8':
                cv_image = cv2.cvtColor(cv_image, cv2.COLOR_RGB2BGR)

            if cv_image is not None and cv_image.size > 0:
                self.get_logger().info('화면 출력 중 입니다.')
                cv2.imshow(self.window_name, cv_image)
                cv2.waitKey(1)

        except Exception as e:
            self.get_logger().error(f'이미지 처리 에러: {e}')

def main(args=None):
    os.environ['QT_X11_NO_MITSHM'] = '1'
    rclpy.init(args=args)
    image_subscriber = ImageSubscriber()

    try:
        rclpy.spin(image_subscriber)
    except KeyboardInterrupt:
        pass
    finally:
        cv2.destroyAllWindows()
        image_subscriber.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()

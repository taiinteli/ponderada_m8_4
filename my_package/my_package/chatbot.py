import rclpy
from std_msgs.msg import String
from my_package.my_node import processar_comando
def callback(msg):
    resposta = processar_comando(msg.data)
    print(resposta)
def main():
    rclpy.init()
    node = rclpy.create_node('chatbot_node')
    subscriber = node.create_subscription(String, 'comando_usuario', callback, 10)
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    node.destroy_node()
    rclpy.shutdown()
if __name__ == '__main__':
    main()
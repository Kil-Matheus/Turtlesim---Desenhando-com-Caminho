import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import math # Para conversão de graus para radianos
import time # Para pausar a execução


class TurtleController(Node):
    def __init__(self):
        super().__init__('turtle_controller')
        self.publisher_ = self.create_publisher(Twist, 'turtle1/cmd_vel', 10)
        self.timer_ = self.create_timer(0.1, self.move_turtle)
        self.twist_msg_ = Twist()

    def move_turtle(self):
        # Configurações de velocidade
        self.twist_msg_.linear.x = 3.0
        self.twist_msg_.angular.z = 0.0

        # Desenha a estrela de 5 pontas
        for i in range(5):
            self.publisher_.publish(self.twist_msg_)
            time.sleep(1.0)

            self.twist_msg_.linear.x = 0.0
            self.twist_msg_.angular.z = math.radians(144)
            self.publisher_.publish(self.twist_msg_)
            time.sleep(1.0)

            self.twist_msg_.linear.x = 3.0
            self.twist_msg_.angular.z = 0.0

        # Para a tartaruga
        self.twist_msg_.linear.x = 0.0
        self.twist_msg_.angular.z = 0.0
        self.publisher_.publish(self.twist_msg_)
        time.sleep(1.0)
        exit()


def main(args=None):
    rclpy.init(args=args)
    turtle_controller = TurtleController()
    rclpy.spin(turtle_controller)
    turtle_controller.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()

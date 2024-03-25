import rclpy
from rclpy.node import Node
from std_msgs.msg import Int16 

class MyNode(Node):
    def __init__(self):
        super().__init__("kvadriranje_broja")
        self.subscription = self.create_subscription(
            Int16, 
            'topic', 
            self.listener_callback, 
            10
        )
        self.publisher_ = self.create_publisher(Int16, 'topic1', 10)
    
    def listener_callback(self, msg: Int16):
        x = msg.data
        y = Int16()
        y.data = x*x
        self.publisher_.publish(y)
        
    def timer_callback(self):
        self.count += 1
        y = Int16()
        y.data = self.count
        self.publisher_.publish(y)

def main(args=None):
    rclpy.init(args=args)

    #stvaranje cvora
    kvadriranje_broja = MyNode()

    #koristenje cvora
    rclpy.spin(kvadriranje_broja)

    #zatvaranje cvora
    kvadriranje_broja.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()
        
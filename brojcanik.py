import rclpy
from rclpy.node import Node
from std_msgs.msg import Int16 

class MyNode(Node):
    def __init__(self):
        super().__init__("brojcanik")
        self.publisher_ = self.create_publisher(Int16, 'topic', 10)
        timer_period = 1.0
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.count = 0


    def timer_callback(self):
        self.count += 1
        y = Int16()
        y.data = self.count
        self.publisher_.publish(y)



def main(args=None):
    rclpy.init(args=args)

    #stvaranje cvora1``
    brojcanik = MyNode()

    #koristenje cvora
    rclpy.spin(brojcanik)

    #zatvaranje cvora
    bnode = destroy_node()
    rcply.shutdown()
    
if __name__ == "__main__":
    main()

import math

import rclpy
from rclpy.node import Node
from rclpy.qos import DurabilityPolicy, QoSProfile, ReliabilityPolicy
from std_msgs.msg import Int32MultiArray
from std_srvs.srv import Empty
from turtlesim.msg import Pose
from turtlesim.srv import SetPen, TeleportAbsolute

N = 8
DIGIT_SPACING = 1.4
STEP = 0.05  # makin kecil makin lambat


class MemberNode(Node):
    def __init__(self, member_id, color, slot, digits):
        super().__init__(f'member_{member_id}')
        self.id, self.color, self.slot, self.digits = member_id, color, slot, digits
        self.last_number = 0
        self.pending = 1 if member_id == 1 else None
        self.pose = None
        # transient_local: anggota yang telat start tetap menerima token terakhir
        qos = QoSProfile(depth=1, reliability=ReliabilityPolicy.RELIABLE,
                         durability=DurabilityPolicy.TRANSIENT_LOCAL)
        self.pub = self.create_publisher(Int32MultiArray, '/relay_turn', qos)
        self.create_subscription(Int32MultiArray, '/relay_turn', self.on_turn, qos)
        self.create_subscription(Pose, '/turtle1/pose', self.on_pose, 10)
        self.pen = self.create_client(SetPen, '/turtle1/set_pen')
        self.teleport = self.create_client(TeleportAbsolute, '/turtle1/teleport_absolute')
        self.clear = self.create_client(Empty, '/clear')

    def on_pose(self, msg):
        self.pose = msg

    def on_turn(self, msg):
        # data = [current_number, active_member]
        current_number, active_member = msg.data
        # cek nomor agar token lama dari publisher lain tidak diproses ulang
        if active_member == self.id and current_number > self.last_number:
            self.pending = current_number

    def call(self, client, request):
        client.wait_for_service()
        future = client.call_async(request)
        rclpy.spin_until_future_complete(self, future)

    def set_pen(self, off):
        r, g, b = self.color
        self.call(self.pen, SetPen.Request(r=r, g=g, b=b, width=3, off=off))

    def goto(self, x, y):
        while self.pose is None:
            rclpy.spin_once(self)
        x0, y0 = self.pose.x, self.pose.y
        steps = max(1, int(math.hypot(x - x0, y - y0) / STEP))
        for i in range(1, steps + 1):
            tx, ty = x0 + (x - x0) * i / steps, y0 + (y - y0) * i / steps
            self.call(self.teleport, TeleportAbsolute.Request(x=float(tx), y=float(ty), theta=0.0))
            # teleport baru diproses pada update turtlesim, jadi tunggu pose sampai
            while math.hypot(self.pose.x - tx, self.pose.y - ty) > 0.02:
                rclpy.spin_once(self)

    def draw(self, number):
        for i, char in enumerate(str(number)):
            x0 = self.slot[0] + i * DIGIT_SPACING
            for stroke in self.digits[char]:
                self.set_pen(1)
                self.goto(x0 + stroke[0][0], self.slot[1] + stroke[0][1])
                self.set_pen(0)
                for x, y in stroke[1:]:
                    self.goto(x0 + x, self.slot[1] + y)
        self.set_pen(1)

    def run(self):
        while rclpy.ok():
            rclpy.spin_once(self)
            if self.pending is None:
                continue
            number, self.pending = self.pending, None
            self.last_number = number
            if number == N + 1:
                self.call(self.clear, Empty.Request())
            self.draw(number)
            if number < 2 * N:  # setelah 2N token berhenti, semua node idle
                self.pub.publish(Int32MultiArray(data=[number + 1, self.id % N + 1]))


def run_member(member_id, color, slot, digits):
    rclpy.init()
    try:
        MemberNode(member_id, color, slot, digits).run()
    except KeyboardInterrupt:
        pass

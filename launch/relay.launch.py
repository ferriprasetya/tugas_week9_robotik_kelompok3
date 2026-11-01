from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    return LaunchDescription([
        Node(package='turtlesim', executable='turtlesim_node'),
        *[Node(package='digit_relay', executable=f'member_{i}', output='screen')
          for i in range(1, 9)],
    ])

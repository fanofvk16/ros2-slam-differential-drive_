from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import ExecuteProcess
from ament_index_python.packages import get_package_share_directory
import os

def generate_launch_description():

    pkg_path = get_package_share_directory('swarm_robot')
    urdf_file = os.path.join(pkg_path, 'urdf', 'swarm_bot.urdf')

    return LaunchDescription([

        ExecuteProcess(
            cmd=[
                'gazebo', '--verbose',
                os.path.join(pkg_path, 'worlds', 'obstacle.world'),
                '-s', 'libgazebo_ros_init.so',
                '-s', 'libgazebo_ros_factory.so'
            ],
            output='screen'
        ),

        # 🔥 ADD THIS
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            name='robot_state_publisher',
            output='screen',
            parameters=[{
                'use_sim_time': True,
                'robot_description': open(urdf_file).read()
            }]
        ),

        Node(
            package='gazebo_ros',
            executable='spawn_entity.py',
            arguments=[
                '-entity', 'swarm_bot',
                '-file', urdf_file
            ],
            output='screen'
        ),
    ])
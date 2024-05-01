from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    ld = LaunchDescription()

    odometry_node = Node(
        package='mini_challenges',
        executable='odometry_node',
        name='odometry_node',
        output='screen'
    )

    path_generator_c4 = Node(
        package='mini_challenges',
        executable='path_generator_c4',
        name='path_generator_c4',
        output='screen'
    )

    color_id = Node(
        package='mini_challenges',
        executable='color_id',
        name='color_id',
        output='screen'
    )

    ld.add_action(odometry_node)
    ld.add_action(path_generator_c4)
    ld.add_action(color_id)

    return ld
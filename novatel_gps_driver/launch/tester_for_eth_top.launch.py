"""Launch an example driver that communicates using TCP"""

from launch import LaunchDescription
import launch_ros.actions


def generate_launch_description():
    container = launch_ros.actions.ComposableNodeContainer(
        node_name='novatel_gps_container',
        node_namespace='',
        package='rclcpp_components',
        node_executable='component_container',
        composable_node_descriptions=[
            launch_ros.descriptions.ComposableNode(
                package='novatel_gps_driver',
                node_plugin='novatel_gps_driver::NovatelGpsNode',
                node_name='novatel_gps',
                parameters=[{
                    'connection_type': 'tcp',
                    'device': '10.42.0.61:3001',
                    'verbose': True,
                    'imu_sample_rate': -1.0,
                    'use_binary_messages': True,
                    'publish_novatel_positions': True,
                    'publish_imu_messages': True,
                    'publish_novatel_velocity': False,
                    'publish_novatel_psrdop2': False,
                    'imu_frame_id': '/imu',
                    'frame_id': '/gps'
                }]
            )
        ],
        output='screen'
    )

    return LaunchDescription([container])

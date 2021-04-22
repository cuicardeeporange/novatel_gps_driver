"""Launch an example driver that communicates using USB"""

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
                plugin='novatel_gps_driver::NovatelGpsNode',
                name='novatel_gps',
                namespace='novatel_top',
                parameters=[{
                    'connection_type': 'serial',
                    'device': '/dev/ttyUSB0',
                    'verbose': True,
                    'imu_sample_rate': -1.0,
                    'publish_novatel_positions': True,
                    'publish_novatel_psrdop2': False,
                    'publish_novatel_velocity': False,
                    'publish_imu_messages': True,
                    'use_binary_messages':True,
                    'imu_frame_id':'/imu',
                    'frame_id': '/gps'
                }]
            ),
            launch_ros.descriptions.ComposableNode(
                package='novatel_gps_driver',
                plugin='novatel_gps_driver::NovatelGpsNode',
                name='novatel_gps',
                namespace='novatel_bottom',
                parameters=[{
                    'connection_type': 'serial',
                    'device': '/dev/ttyUSB1',
                    'verbose': True,
                    'imu_sample_rate': -1.0,
                    'publish_novatel_positions': True,
                    'publish_novatel_psrdop2': False,
                    'publish_novatel_velocity': False,
                    'publish_imu_messages': True,
                    'use_binary_messages':True,
                    'imu_frame_id':'/imu',
                    'frame_id': '/gps'
                }]
            )
        ],
        output='screen'
    )

    return LaunchDescription([container])

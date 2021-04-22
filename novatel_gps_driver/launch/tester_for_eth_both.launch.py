"""Launch an example driver that communicates using TCP"""

from launch import LaunchDescription
import launch_ros.actions


def generate_launch_description():
    container = launch_ros.actions.ComposableNodeContainer(
        name='novatel_gps_container',
        namespace='novatel_bottom',
        package='rclcpp_components',
        executable='component_container',
        composable_node_descriptions=[
            launch_ros.descriptions.ComposableNode(
                package='novatel_gps_driver',
                plugin='novatel_gps_driver::NovatelGpsNode',
                name='novatel_gps',
                namespace='novatel_top',
                parameters=[{
                    'connection_type': 'tcp',
                    'device': '10.42.0.61:3001',
                    'verbose': True,
                    'imu_sample_rate': -1.0,
                    'use_binary_messages': True,
                    'publish_novatel_positions': True,
                    'publish_imu_messages': True,
                    'publish_novatel_velocity': True,
                    'publish_novatel_psrdop2': True,
                    'imu_frame_id': '/imu',
                    'frame_id': '/gps'
                }]
            ),
            launch_ros.descriptions.ComposableNode(
                package='novatel_gps_driver',
                plugin='novatel_gps_driver::NovatelGpsNode',
                name='novatel_gps',
                namespace='novatel_bottom',
                parameters=[{
                    'connection_type': 'tcp',
                    'device': '10.42.0.60:3001',
                    'verbose': True,
                    'imu_sample_rate': -1.0,
                    'use_binary_messages': True,
                    'publish_novatel_positions': True,
                    'publish_imu_messages': True,
                    'publish_novatel_velocity': True,
                    'publish_novatel_psrdop2': True,
                    'imu_frame_id': '/imu',
                    'frame_id': '/gps'
                }]
            )
        ],
        output='screen'
    )

    return LaunchDescription([container])

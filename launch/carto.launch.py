from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import DeclareLaunchArgument
from launch.substitutions import FindExecutable, PathJoinSubstitution
from launch_ros.substitutions import FindPackageShare
from launch.substitutions import LaunchConfiguration

def generate_launch_description():
    use_sim_time = LaunchConfiguration('use_sim_time', default='true')

    return LaunchDescription([
        # Robot Description Parameter
        DeclareLaunchArgument(
            name='robot_description',
            default_value=PathJoinSubstitution([
                FindPackageShare('cartographer_ros'), 'urdf', 'backpack_2d.urdf'
            ])
        ),
        DeclareLaunchArgument(
            'use_sim_time',
            default_value='true',
            description='Use simulation (Gazebo) clock if true'),
        
        #Robot State Publisher Node
        # Node(
        #     package='robot_state_publisher',
        #     executable='robot_state_publisher',
        #     name='robot_state_publisher',
        #     parameters=[{
        #         'robot_description': PathJoinSubstitution([
        #             FindPackageShare('cartographer_ros'), 'urdf', 'backpack_2d.urdf'
        #         ])
        #     }]
        # ),
        
        # Cartographer Node
        Node(
            package='cartographer_ros',
            executable='cartographer_node',
            name='cartographer_node',
            output='screen',
            arguments=[
                '-configuration_directory', PathJoinSubstitution([
                    FindPackageShare('robot_control'), 'config'
                ]),
                '-configuration_basename', 'carto_config.lua'
            ],
            parameters=[{'use_sim_time': use_sim_time}],
        ),
        
        # Cartographer Occupancy Grid Node
        Node(
            package='cartographer_ros',
            executable='cartographer_occupancy_grid_node',
            name='cartographer_occupancy_grid_node',
            parameters=[{'use_sim_time': use_sim_time}],
            output='screen',
            arguments=['-resolution', '0.05']
        )
    ])

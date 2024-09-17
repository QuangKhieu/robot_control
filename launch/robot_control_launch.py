import launch
from launch.substitutions import Command, LaunchConfiguration
import launch_ros
import os

def generate_launch_description():
    pkg_share = launch_ros.substitutions.FindPackageShare(package='robot_control').find('robot_control')
    default_model_path = os.path.join(pkg_share, 'urdf/burger.urdf.xacro')
    default_rviz_config_path = os.path.join(pkg_share, 'rviz/urdf2.rviz')
    default_map_config_path = os.path.join(pkg_share, 'config/nav2_map.yaml')
    world_path = os.path.join(pkg_share, 'worlds/smap3.world')
    use_sim_time = LaunchConfiguration('use_sim_time', default='true')

    robot_state_publisher_node = launch_ros.actions.Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        parameters=[{'robot_description': Command(['xacro ', LaunchConfiguration('model')])},
                   {'use_sim_time': use_sim_time} ]
    )
    
    joint_state_publisher_node = launch_ros.actions.Node(
        package='joint_state_publisher',
        executable='joint_state_publisher',
        name='joint_state_publisher',
        parameters=[{'use_sim_time': use_sim_time}]
    )

    spawn_entity = launch_ros.actions.Node(
        package='gazebo_ros',
        executable='spawn_entity.py',
        arguments=['-entity', 'my_burger', '-topic', 'robot_description'],
        output='screen'
    )

    joy_node_run = launch_ros.actions.Node(
        package = 'joy',
        executable='joy_node' ,
    )

    control_run = launch_ros.actions.Node(
        package='robot_control',
        executable='robot_control_ex',
        name='control_robot_node'
    )
    rviz_node = launch_ros.actions.Node(
        package='rviz2',
        executable='rviz2',
        name='rviz2',
        output='screen',
        arguments=['-d', LaunchConfiguration('rvizconfig')],
        parameters=[{'use_sim_time': use_sim_time}],
    )

    cmap_node = launch_ros.actions.Node(
        package='nav2_costmap_2d',
        executable='nav2_costmap_2d',
        name='costmap',
        output='screen',
        parameters=[default_map_config_path],
    ) 

    return launch.LaunchDescription([
        launch.actions.DeclareLaunchArgument(
            'use_sim_time',
            default_value='false',
            description='Use simulation (Gazebo) clock if true'),
        launch.actions.DeclareLaunchArgument(name='model', default_value=default_model_path,
                                            description='Absolute path to robot urdf file'),
        launch.actions.ExecuteProcess(cmd=['gazebo', '--verbose', '-s', 'libgazebo_ros_init.so', '-s', 'libgazebo_ros_factory.so',world_path], output='screen'),
        launch.actions.DeclareLaunchArgument(name='rvizconfig', default_value=default_rviz_config_path,
                                            description='Absolute path to rviz config file'),
        #joint_state_publisher_node,
        robot_state_publisher_node,
        spawn_entity,
        rviz_node,
        #cmap_node,
        #joy_node_run,
        #control_run,
    ])
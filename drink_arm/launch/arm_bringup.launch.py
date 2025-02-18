#!/usr/bin/env python3

from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
import os

from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    base_launch_path = os.path.join(
        get_package_share_directory('open_manipulator_x_bringup'),
        'launch',
        'base.launch.py'
    )
    
    moveit_launch_path = os.path.join(
        get_package_share_directory('open_manipulator_x_moveit_config'),
        'launch',
        'moveit_core.launch.py'
    )
    
    arm_launch = IncludeLaunchDescription(
            PythonLaunchDescriptionSource(base_launch_path),
            launch_arguments={
                'use_fake_hardware': 'True',
                'fake_sensor_commands' : 'True',
                'use_sim': 'False'
            }.items()
    )     
    
    moveit_launch = IncludeLaunchDescription(
            PythonLaunchDescriptionSource(moveit_launch_path)
    )  
            
    return LaunchDescription([
            arm_launch,
            moveit_launch
    ])
# cmake_minimum_required(VERSION 3.8)
# project(robot_control)

# if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
#   add_compile_options(-Wall -Wextra -Wpedantic)
# endif()

# # find dependencies
# find_package(ament_cmake REQUIRED)
# find_package(rclcpp REQUIRED)
# find_package(std_msgs REQUIRED)
# find_package(sensor_msgs REQUIRED)
# find_package(geometry_msgs REQUIRED)
# find_package(xacro REQUIRED)

# include_directories(include/robot_control)


# add_executable(robot_control_ex src/joy_to_vel.cpp )

# ament_target_dependencies(robot_control_ex rclcpp std_msgs sensor_msgs geometry_msgs xacro )


# install (TARGETS
# robot_control_ex
# DESTINATION lib/${PROJECT_NAME}

# )

# install(
#   DIRECTORY launch  rviz urdf
#   DESTINATION share/${PROJECT_NAME}
# )
# ament_package()
cmake_minimum_required(VERSION 3.5)
project(robot_control)


# Default to C99
if(NOT CMAKE_C_STANDARD)
  set(CMAKE_C_STANDARD 99)
endif()

# Default to C++14
if(NOT CMAKE_CXX_STANDARD)
  set(CMAKE_CXX_STANDARD 14)
endif()

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# find dependencies
find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(std_msgs REQUIRED)
find_package(sensor_msgs REQUIRED)
find_package(geometry_msgs REQUIRED)

include_directories(include/robot_control)


add_executable(robot_control_ex src/joy_to_vel.cpp )

ament_target_dependencies(robot_control_ex rclcpp std_msgs sensor_msgs geometry_msgs  )


install (TARGETS
robot_control_ex
DESTINATION lib/${PROJECT_NAME}

)

# uncomment the following section in order to fill in
# further dependencies manually.
# find_package(<dependency> REQUIRED)


# Install launch files.
install(DIRECTORY
  launch
  urdf
  rviz
  config
  worlds
  DESTINATION share/${PROJECT_NAME}/
)



ament_package()

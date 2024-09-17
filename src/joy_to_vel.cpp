#include "joytovel.hpp"


JtoV::JtoV() : Node("joytovel_node") 
{
    this->declare_parameter("v_max", 1.0);
    this->declare_parameter("w_max",1.0);

    this->get_parameter("v_max",v_max_);
    this->get_parameter("w_max",w_max_);


    subJoy_ = this->create_subscription<joy_>("/joy", 10, std::bind(&JtoV::callback_,this, std::placeholders::_1));
    pubVel_ = this->create_publisher<tw_>("/cmd_vel",10);

}

JtoV::~JtoV(){}

void JtoV::callback_(const joy_ &joy_data )
{
    tw_ vel_data ;
    // 3 w, 4 v
    vel_data.linear.x = joy_data.axes[4];
    vel_data.angular.z = joy_data.axes[3];

    pubVel_->publish(vel_data);

}

int main (int argc, char *argv[])
{
    rclcpp::init(argc, argv);
    rclcpp::spin(std::make_shared<JtoV>());
    rclcpp::shutdown();
    return 0;
}



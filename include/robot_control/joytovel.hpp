#include "rclcpp/rclcpp.hpp"
#include "sensor_msgs/msg/joy.hpp"
#include "geometry_msgs/msg/twist.hpp"

using tw_  = geometry_msgs::msg::Twist;
using joy_ = sensor_msgs::msg::Joy;
class JtoV : public rclcpp::Node
{
    public:
        JtoV();
        ~JtoV();
    private:
        rclcpp::Publisher<tw_>::SharedPtr pubVel_;
        rclcpp::Subscription<joy_>::SharedPtr subJoy_;
        void callback_(const joy_ &joy_data);
        float v_max_;
        float w_max_;
};



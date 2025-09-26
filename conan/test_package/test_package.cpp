#include <iostream>
#include "std_msgs.pb.h"
#include "geometry_msgs.pb.h"
#include "sensor_msgs.pb.h"

int main() {
    std::cout << "Testing jr-msgs Conan package..." << std::endl;
    
    // Test std_msgs
    std_msgs::Header header;
    header.set_seq(1);
    header.set_frame_id("test_frame");
    
    std_msgs::String msg;
    msg.set_data("Hello from jr-msgs!");
    
    // Test geometry_msgs
    geometry_msgs::Point point;
    point.set_x(1.0);
    point.set_y(2.0);
    point.set_z(3.0);
    
    geometry_msgs::Pose pose;
    pose.mutable_position()->CopyFrom(point);
    pose.mutable_orientation()->set_w(1.0);
    
    // Test sensor_msgs
    sensor_msgs::LaserScan scan;
    scan.mutable_header()->CopyFrom(header);
    scan.set_angle_min(-3.14159);
    scan.set_angle_max(3.14159);
    scan.set_angle_increment(0.01);
    scan.set_range_min(0.1);
    scan.set_range_max(10.0);
    scan.add_ranges(1.0);
    scan.add_ranges(1.5);
    scan.add_ranges(2.0);
    
    // Test serialization
    std::string serialized_data;
    scan.SerializeToString(&serialized_data);
    
    std::cout << "✓ All message types created successfully" << std::endl;
    std::cout << "✓ Serialization works (size: " << serialized_data.size() << " bytes)" << std::endl;
    std::cout << "✓ Package test completed successfully!" << std::endl;
    
    return 0;
}

# ROS Messages as Protobuf

This repository contains Protocol Buffer (protobuf) definitions for common ROS message types. These .proto files can be used to generate language-specific bindings for ROS message types using protobuf.

## Files Overview

### Core Message Types

- **`std_msgs.proto`** - Standard ROS message types including:
  - Basic data types (Bool, Int32, Float64, String, etc.)
  - Multi-dimensional arrays
  - Header message
  - Time and Duration messages

- **`geometry_msgs.proto`** - Geometric message types including:
  - Points, Vectors, and Poses
  - Quaternions and Transforms
  - Twists and Accelerations
  - Inertia and Wrench messages

- **`sensor_msgs.proto`** - Sensor message types including:
  - Camera messages (Image, CameraInfo, CompressedImage)
  - Point clouds (PointCloud, PointCloud2)
  - IMU data
  - Laser scans
  - Joint states
  - GPS/Navigation satellite messages
  - Environmental sensors (temperature, humidity, pressure)

### Navigation and Planning

- **`nav_msgs.proto`** - Navigation message types including:
  - Occupancy grids for mapping
  - Path planning messages
  - Odometry data
  - Map services

### Action and Control

- **`actionlib_msgs.proto`** - Action library message types for:
  - Goal management
  - Status tracking
  - Action feedback

- **`trajectory_msgs.proto`** - Trajectory message types for:
  - Joint trajectories
  - Multi-DOF joint trajectories

### Visualization and Diagnostics

- **`visualization_msgs.proto`** - Visualization message types including:
  - Markers for RViz
  - Interactive markers
  - Image markers

- **`diagnostic_msgs.proto`** - Diagnostic message types for:
  - System health monitoring
  - Self-test functionality

## Usage

### Generating Language Bindings

To generate protobuf bindings for your preferred language:

```bash
# For Python
protoc --python_out=. *.proto

# For C++
protoc --cpp_out=. *.proto

# For Java
protoc --java_out=. *.proto

# For Go
protoc --go_out=. *.proto
```

### Example Usage

```python
# Python example
import std_msgs_pb2
import geometry_msgs_pb2

# Create a header message
header = std_msgs_pb2.Header()
header.frame_id = "base_link"
header.seq = 1

# Create a pose message
pose = geometry_msgs_pb2.Pose()
pose.position.x = 1.0
pose.position.y = 2.0
pose.position.z = 3.0
pose.orientation.w = 1.0

# Create a stamped pose
stamped_pose = geometry_msgs_pb2.PoseStamped()
stamped_pose.header.CopyFrom(header)
stamped_pose.pose.CopyFrom(pose)
```

## Key Differences from ROS Messages

1. **Field numbering**: Protobuf requires explicit field numbers (1, 2, 3, etc.)
2. **No default values**: Protobuf doesn't support ROS-style default values
3. **Import structure**: Dependencies are handled through import statements
4. **Package naming**: Uses protobuf package syntax instead of ROS namespaces

## Dependencies

- `std_msgs.proto` - Base message types (imported by most other files)
- `geometry_msgs.proto` - Geometric types (imported by sensor_msgs, nav_msgs, etc.)

## Notes

- All message types maintain compatibility with their ROS counterparts
- Field names and types are preserved where possible
- Some ROS-specific features (like default values) are handled differently in protobuf
- Multi-dimensional arrays use repeated fields in protobuf
- Time and duration are represented as separate sec/nsec fields

## Contributing

When adding new message types:
1. Follow the existing naming conventions
2. Include proper field numbering
3. Add appropriate imports
4. Update this README with new message descriptions

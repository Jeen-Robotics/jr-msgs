cmake_minimum_required(VERSION 3.17)
project(jr_msgs VERSION 1.0.0 LANGUAGES CXX)

# Set C++ standard
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# Find required packages
find_package(protobuf REQUIRED)

# Find all proto files
file(GLOB PROTO_FILES "*.proto")

# Generate protobuf sources
set(PROTO_SRCS)
set(PROTO_HDRS)

foreach(PROTO_FILE ${PROTO_FILES})
    get_filename_component(PROTO_NAME ${PROTO_FILE} NAME_WE)
    set(PROTO_SRC "${CMAKE_CURRENT_BINARY_DIR}/${PROTO_NAME}.pb.cc")
    set(PROTO_HDR "${CMAKE_CURRENT_BINARY_DIR}/${PROTO_NAME}.pb.h")
    
    list(APPEND PROTO_SRCS ${PROTO_SRC})
    list(APPEND PROTO_HDRS ${PROTO_HDR})
    
    add_custom_command(
        OUTPUT ${PROTO_SRC} ${PROTO_HDR}
        COMMAND ${Protobuf_PROTOC_EXECUTABLE}
        ARGS --cpp_out=${CMAKE_CURRENT_BINARY_DIR} --proto_path=${CMAKE_CURRENT_SOURCE_DIR} ${PROTO_FILE}
        DEPENDS ${PROTO_FILE}
        COMMENT "Generating protobuf sources for ${PROTO_NAME}"
        VERBATIM
    )
endforeach()

# Create the library
add_library(jr_msgs ${PROTO_SRCS} ${PROTO_HDRS})

# Set target properties
set_target_properties(jr_msgs PROPERTIES
    VERSION ${PROJECT_VERSION}
    SOVERSION ${PROJECT_VERSION_MAJOR}
    PUBLIC_HEADER "${PROTO_HDRS}"
)

# Link protobuf
target_link_libraries(jr_msgs PUBLIC protobuf::libprotobuf)

# Include directories for the library
target_include_directories(jr_msgs PUBLIC
    $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/include>
    $<BUILD_INTERFACE:${CMAKE_CURRENT_BINARY_DIR}>
    $<INSTALL_INTERFACE:include>
)

# Install targets
install(TARGETS jr_msgs
    EXPORT jr_msgsConfig
    LIBRARY DESTINATION lib
    ARCHIVE DESTINATION lib
    RUNTIME DESTINATION bin
    PUBLIC_HEADER DESTINATION include
)

# Install proto files
install(FILES ${PROTO_FILES} DESTINATION proto)

# Install generated protobuf headers
install(FILES ${PROTO_HDRS} DESTINATION include)

# Create and install export targets
install(EXPORT jr_msgsConfig
    FILE jr_msgsConfig.cmake
    NAMESPACE jr_msgs::
    DESTINATION lib/cmake/jr_msgs
)

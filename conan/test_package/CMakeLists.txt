cmake_minimum_required(VERSION 3.17)
project(test_package LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

find_package(jr_msgs REQUIRED)

add_executable(test_package test_package.cpp)
target_link_libraries(test_package jr_msgs::jr_msgs)

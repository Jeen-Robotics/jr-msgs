import os
from conan import ConanFile
from conan.tools.cmake import CMake, CMakeToolchain, CMakeDeps, cmake_layout
from conan.tools.files import collect_libs, copy


class JrMsgsConan(ConanFile):
    name = "jr_msgs"
    version = "1.0.0"
    description = "ROS message types as Protocol Buffer definitions for C++"
    topics = ("ros", "protobuf", "robotics", "messages")
    url = "https://github.com/jeen-robotics/jr-msgs"
    homepage = "https://github.com/jeen-robotics/jr-msgs"
    license = "Apache-2.0"
    author = "Jeen Robotics"

    settings = "os", "compiler", "build_type", "arch"
    options = {
        "shared": [True, False],
        "fPIC": [True, False],
    }
    default_options = {
        "shared": False,
        "fPIC": True,
    }

    def export_sources(self):
        copy(
            self,
            "*.proto",
            src=os.path.join(self.recipe_folder, ".."),
            dst=self.export_sources_folder,
        )
        copy(
            self,
            "CMakeLists.txt",
            src=os.path.join(self.recipe_folder, ".."),
            dst=self.export_sources_folder,
        )

    def layout(self):
        cmake_layout(self)

    def config_options(self):
        if self.settings.os == "Windows":
            del self.options.fPIC

    def configure(self):
        if self.options.shared:
            del self.options.fPIC

    def requirements(self):
        self.requires(
            "protobuf/3.21.12",
            transitive_headers=True,
            transitive_libs=True,
        )

    def build_requirements(self):
        self.build_requires("protobuf/3.21.12")

    def generate(self):
        tc = CMakeToolchain(self)
        tc.generate()

        deps = CMakeDeps(self)
        deps.generate()

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        cmake = CMake(self)
        cmake.install()

    def package_info(self):
        self.cpp_info.libs = collect_libs(self)
        self.cpp_info.requires = ["protobuf::protobuf"]
        self.cpp_info.defines = [
            "GOOGLE_PROTOBUF_NO_RTTI",
            "GOOGLE_PROTOBUF_NO_STATIC_INITIALIZER",
        ]

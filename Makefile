# Makefile for generating protobuf bindings from ROS message definitions

# Default target
all: python cpp java go

# Python bindings
python:
	@echo "Generating Python protobuf bindings..."
	protoc --python_out=. *.proto
	@echo "Python bindings generated in current directory"

# C++ bindings
cpp:
	@echo "Generating C++ protobuf bindings..."
	protoc --cpp_out=. *.proto
	@echo "C++ bindings generated in current directory"

# Java bindings
java:
	@echo "Generating Java protobuf bindings..."
	protoc --java_out=. *.proto
	@echo "Java bindings generated in current directory"

# Go bindings
go:
	@echo "Generating Go protobuf bindings..."
	protoc --go_out=. *.proto
	@echo "Go bindings generated in current directory"

# JavaScript/TypeScript bindings
js:
	@echo "Generating JavaScript protobuf bindings..."
	protoc --js_out=import_style=commonjs:. *.proto
	@echo "JavaScript bindings generated in current directory"

# Clean generated files
clean:
	@echo "Cleaning generated protobuf files..."
	find . -name "*.pb.go" -delete
	find . -name "*.pb.cc" -delete
	find . -name "*.pb.h" -delete
	find . -name "*_pb2.py" -delete
	find . -name "*_pb2.pyc" -delete
	find . -name "*.java" -not -name "*.proto" -delete
	find . -name "*.js" -not -name "*.proto" -delete
	@echo "Generated files cleaned"

# Validate protobuf files
validate:
	@echo "Validating protobuf files..."
	protoc --proto_path=. --descriptor_set_out=/dev/null *.proto
	@echo "All protobuf files are valid"

# Help
help:
	@echo "Available targets:"
	@echo "  all     - Generate all language bindings"
	@echo "  python  - Generate Python bindings"
	@echo "  cpp     - Generate C++ bindings"
	@echo "  java    - Generate Java bindings"
	@echo "  go      - Generate Go bindings"
	@echo "  js      - Generate JavaScript bindings"
	@echo "  clean   - Remove all generated files"
	@echo "  validate- Validate protobuf files"
	@echo "  help    - Show this help message"

.PHONY: all python cpp java go js clean validate help

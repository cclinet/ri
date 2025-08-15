cmake_minimum_required(VERSION 3.15.0)
project(
  ri
  VERSION 0.1.0
  LANGUAGES C CXX)

set(DEV_MODULE Development)
set(Python_FIND_VIRTUALENV FIRST)
find_package(
  Python 3.14
  COMPONENTS Interpreter ${DEV_MODULE}
  REQUIRED)

execute_process(
  COMMAND "${Python_EXECUTABLE}" -m nanobind --cmake_dir
  OUTPUT_STRIP_TRAILING_WHITESPACE
  OUTPUT_VARIABLE nanobind_ROOT)
find_package(nanobind CONFIG REQUIRED)

message(STATUS "Python_INCLUDE_DIRS = ${Python_INCLUDE_DIRS}")
message(STATUS "Python_LIBRARIES = ${Python_LIBRARIES}")

nanobind_add_module(ri FREE_THREADED ri.cpp)
target_link_libraries(ri PRIVATE Python::Python)

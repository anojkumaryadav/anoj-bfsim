execute_process(COMMAND "/home/anoj/catkin_ws/build/cob_robots/cob_default_robot_behavior/catkin_generated/python_distutils_install.sh" RESULT_VARIABLE res)

if(NOT res EQUAL 0)
  message(FATAL_ERROR "execute_process(/home/anoj/catkin_ws/build/cob_robots/cob_default_robot_behavior/catkin_generated/python_distutils_install.sh) returned error code ")
endif()

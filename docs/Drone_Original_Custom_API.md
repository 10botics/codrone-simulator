### Original Drone API Supported
Link to Original API: https://docs.robolink.com/docs/CoDroneEDU/Python/Function-Documentation
- pair()
- land() (**Note:** When the drone is grabbing an object, the land function will be ignored)
- takeoff()
- avoid_wall()
- detect_wall()
- hover()
- move()
- reset_move()
- set_pitch()
- set_roll()
- set_throttle()
- set_yaw()
- turn_left()
- turn_right()
- go()
- move_forward()
- move_backward()
- move_left()
- move_right()
- drone_LED_off()
- set_drone_LED()
- drone_buzzer()
- start_drone_buzzer()
- end_drone_buzzer()
- get_bottom_range()
- get_front_range()

## Custom Drone Simulator API
Link to Github Custom API Package: https://github.com/10botics/codrone-simulator-sdk-python

### Extra Drone API
- grab()
  - The drone will grab up an arbitrary grabbable object within the grab range of the drone. The current range of the drone is a 1.1m height capsule with 0.3m radius, with the upper spherical center of the capsule as the center of the drone. **Note:** that only one arbitrary object will be grabbed if there are multiple grabbable objects within range. Also, if the drone already grabbed a grabbable object, this command will be ignored.

- release()
  - The drone will release the grabbed object if the drone has grabbed one. The released object will be placed on the drone position with height equal zero(y = 0). If there is no grabbed object, this command will be ignored. **Note:** that this command needs to be run before running the land command as the drone with grabbed object will not be able to land.

- reset_position_and_rotation()
  - The drone will be teleported to the initial position and rotation. The initial position and rotation is the position and rotation of the drone when the drone simulator is opened. **Note:** This Command will not reset the Timer or the score. Only Reset the Drone Position

- send_message(message):
  - The Drone will send out a message to the console. The message is the inputted string message. The message will only be shown in the console of the drone simulator, not the python console.

### Extra API
- teleport_to(x, y, z)
  - The x, y and z form the coordinate of the position that the drone will teleport to. It is a y-up left-handed coordinate system. The drone will directly teleport to the inputted position drone after the execution of this line. **Note:** that there are boundaries set for the teleport range.

- teleport_by(x, y, z)
  - The x, y, and z form the offset translation vector that the drone will move towards. It uses a y-up left-handed coordinate system. The drone will directly teleport by the specified offset after executing this command. **Note:** that there are boundaries set for the teleport range.

- teleport_yaw_to(yaw)
  - The yaw is the rotation angle that the drone will rotate to. Positive yaw value is clockwise rotation while negative yaw value is anti-clockwise rotation. The unit of the yaw value is in degrees. The forward direction(positive z-axis) yaw angle is 0. The drone will directly rotate toward with the input rotation after the execution of the line.

- teleport_yaw_by(yaw)
  - The yaw is the rotation angle offset that the drone will rotate toward. Positive yaw value is clockwise rotation while negative yaw value is anti-clockwise rotation. The unit of the yaw value is in degrees. The drone will directly rotate toward the input offset angle with the input rotation after the execution of the line.

- set_restart_pos(x, z)
  - The x and z form the coordinate of the position that the drone will be teleported to after next restart function is executed. **Note:** that there are boundaries set for the restart range.

- set_restart_yaw(yaw)
  - The yaw is the rotation angle that the drone will rotate to after next restart function is executed. Positive yaw value is clockwise rotation while negative yaw value is anti-clockwise rotation. The unit of the yaw value is in degrees. The forward direction(positive z-axis) yaw angle is 0.



### return to [README.md](/README.md)

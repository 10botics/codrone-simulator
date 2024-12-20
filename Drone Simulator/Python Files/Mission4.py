from codrone_simulator import Drone

# Initialize and pair with the drone
drone = Drone()
drone.pair()

# Mission 4 task execution
drone.takeoff()

# Example movement
drone.go(-50, 0, 0, 0, 3)  # Move backward
drone.turn_left(45)  # Turn left by 45 degrees
drone.go(0, 50, 0, 10, 5.6)  # Move forward diagonally

drone.land()

# Close connection to the drone
drone.close()

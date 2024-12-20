from codrone_simulator import Drone

# Initialize and pair with the drone
drone = Drone()
drone.pair()

# Mission 2 task execution
drone.takeoff()

# Example movement, grabbing, and releasing an object
drone.grab()  # Grab an object within range
drone.go(0, 50, 0, 30, 1)  # Move forward
drone.release()  # Release the grabbed object

drone.land()

# Close connection to the drone
drone.close()
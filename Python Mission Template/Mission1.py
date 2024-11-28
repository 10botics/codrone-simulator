from codrone_simulator import Drone

# Initialize and pair with the drone
drone = Drone()
drone.pair()

# Mission 1 task execution
drone.takeoff()

# Example movement and data retrieval (customize as needed for the mission)
front_range = drone.get_front_range()  # Get front range data
print("Front range:", front_range)

bottom_range = drone.get_bottom_range()  # Get bottom range data
print("Bottom range:", bottom_range)

# Send a message to the drone simulator console
drone.send_message(bottom_range)

drone.land()

# Close connection to the drone
drone.close()
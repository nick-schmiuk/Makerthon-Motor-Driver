import distanceHandler

distance = distanceHandler.Distance()

while True:
    print(f"Senor 1: {distance.getAvoidance(0, 2.5)}")
    print(f"Senor 2: {distance.getAvoidance(1, 2.5)}")
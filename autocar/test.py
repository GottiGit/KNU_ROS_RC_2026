from pop import Pilot

car = Pilot.AutoCar()

car.forward()
car.backward()
time.sleep()
car.stop()

value = car.getGyro()
print(value)

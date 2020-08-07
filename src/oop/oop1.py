# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class

# ALL VEHICLES
# --> Vehicle is the base class:
class Vehicle:
    pass

# ALL GROUNDED VEHICLES
# GroundVehicle inherits from Vehicle
class GroundVehicle(Vehicle):
    pass

# Car inherits from GroundVehicle
class Car(GroundVehicle):
    pass

# Motorcycle also inherits from GroundVehicle
class Motorcycle(GroundVehicle):
    pass

# ALL AIRBORNE VEHICLES
# FlightVehicle inherits from Vehicle
class FlightVehicle(Vehicle):
    pass

# Starship inherits from FlightVehicle
class Starship(FlightVehicle):
    pass

# Airplane also inherits from FlightVehicle
class Airplane(FlightVehicle):
    pass

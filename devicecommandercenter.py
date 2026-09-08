from abc import ABC, abstractmethod


# Step 2: Abstract class
class SmartDevice(ABC):

    def show_device(self):
        print("This is a smart device.")

    # Step 3: Abstract method
    @abstractmethod
    def turn_on(self):
        pass


# Step 4: Subclasses
class SmartLight(SmartDevice):

    def turn_on(self):
        print("The smart light is now ON.")


class SmartFan(SmartDevice):

    def turn_on(self):
        print("The smart fan is now ON.")


class SmartSpeaker(SmartDevice):

    def turn_on(self):
        print("The smart speaker is now ON.")


# Step 5: Create objects
light = SmartLight()
fan = SmartFan()
speaker = SmartSpeaker()

light.show_device()
light.turn_on()

fan.show_device()
fan.turn_on()

speaker.show_device()
speaker.turn_on()


# Step 6: Polymorphism without inheritance
class SecurityCamera:

    def check_status(self):
        print("Security camera is working.")


class DoorLock:

    def check_status(self):
        print("Door lock is secure.")


# Step 7: Shared interface
devices = [SecurityCamera(), DoorLock()]

for device in devices:
    device.check_status()
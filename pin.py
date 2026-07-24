class Account:
    def __init__(self, owner, pin):
        self.owner = owner          # Public attribute
        self.__pin = pin            # Private attribute

    # Show whether a PIN exists
    def show_pin_status(self):
        if self.__pin:
            print("PIN is set.")
        else:
            print("No PIN set.")

    # Check if the entered PIN is correct
    def check_pin(self, entered_pin):
        if entered_pin == self.__pin:
            print("Correct PIN!")
        else:
            print("Incorrect PIN.")

    # Setter method
    def set_pin(self, new_pin):
        if len(new_pin) == 4 and new_pin.isdigit():
            self.__pin = new_pin
            print("PIN updated successfully.")
        else:
            print("Error: PIN must be exactly 4 digits.")

    # String method
    def __str__(self):
        return f"Account Owner: {self.owner}"


# Step 6: Create object
my_account = Account("Alice", "1234")

# Print object
print(my_account)

# Show PIN status
my_account.show_pin_status()

# Check PIN
my_account.check_pin("1234")
my_account.check_pin("9999")

# Step 7: Try changing the private PIN directly
my_account.__pin = "9999"

print("\nAfter trying to change __pin directly:")
my_account.check_pin("9999")   # Should fail
my_account.check_pin("1234")   # Should still work

# Step 8: Change PIN safely using setter
my_account.set_pin("9999")

print("\nAfter using setter:")
my_account.check_pin("9999")

# Step 9: Test invalid PINs
my_account.set_pin("99")
my_account.set_pin("abcd")
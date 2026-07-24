class DailyMessage:
    def __init__(self):
        self.message = ""

    def get_message(self):
        self.message = input("Enter a message: ")

    def print_message(self):
        print("Message in uppercase:", self.message.upper())


class HelperSession:
    def __init__(self):
        print("Helper session started.")

    def __del__(self):
        print("Helper session ended.")


def create_session():
    session = HelperSession()
    return session


class PairFinder:
    def find_pair(self, numbers, target):
        seen = {}

        for i, num in enumerate(numbers):
            needed = target - num

            if needed in seen:
                print("Pair found at indices:", seen[needed], "and", i)
                return

            seen[num] = i

        print("No pair found.")


# Main Program

# Step 3
daily_text = DailyMessage()
daily_text.get_message()
daily_text.print_message()

# Step 5
session = create_session()

# Step 8
numbers = [10, 20, 30, 40, 50, 60, 70]

target = int(input("Enter the target sum: "))

finder = PairFinder()
finder.find_pair(numbers, target)

# Delete the HelperSession object
del session
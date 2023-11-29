class Person:
    def __init__(self, name, age, address):
        self._name = name
        self._age = age
        self._address = address

    # Getter and setter for name
    def get_name(self):
        return self._name

    def set_name(self, new_name):
        self._name = new_name

    # Getter and setter for age
    def get_age(self):
        return self._age

    def set_age(self, new_age):
        self._age = new_age

    # Getter and setter for address
    def get_address(self):
        return self._address

    def set_address(self, new_address):
        self._address = new_address

# Example usage:
# Create a Person object
person = Person(name="Abdul BAsit", age=21, address="zyx")

# Access attributes using getter methods
print("Name:", person.get_name())
print("Age:", person.get_age())
print("Address:", person.get_address())

# Modify attributes using setter methods
person.set_name("Abdul Basit Hammad")
person.set_age(22)
person.set_address("xyz")

# Verify the changes
print("Updated Name:", person.get_name())
print("Updated Age:", person.get_age())
print("Updated Address:", person.get_address())

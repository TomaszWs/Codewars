# ATM machines allow 4 or 6 digit PIN codes and PIN codes cannot contain anything but exactly 4 digits or exactly 6 digits.

# If the function is passed a valid PIN string, return true, else return false.
# Examples (Input --> Output)

# "1234"   -->  true
# "12345"  -->  false
# "a234"   -->  false

# My solution 

# def validate_pin(pin):
#     if pin.isdigit():
#         if len(pin) == 4 or len(pin) == 6: return True
#         else: return False
#     else: return False

# pin = "1234"
# pin2 = "12345"
# pin3 = "a234"
# pin4 = '111111'
# print(validate_pin(pin4))

# Best practices

def validate_pin(pin):
    return len(pin) in (4, 6) and pin.isdigit()

def validate_pin(pin):
    return len(pin) in [4, 6] and pin.isdigit()

import random

def generate_otp(length=6):
    return "".join(str(random.randint(0, 9)) for _ in range(length))

otp = generate_otp()
print(f"Your 6-digit OTP is: {otp}")
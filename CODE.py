import random
def generate_password():
  letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
  password = ""
  for i in range(8):
    password += random.choice(letters)
  return password
print(generate_password())

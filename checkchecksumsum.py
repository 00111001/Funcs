import hashlib
def calculate_checksum(filename):
    with open(filename, 'rb') as file:
        return hashlib.sha256(file.read()).hexdigest().upper()

print(calculate_checksum('NotifyThread.png'))
import sys,hashlib

pwd sys.argv[1]
message_digest= hashlib.sha1()
message_digest.update(bytes(pwd, encoding='utf-8'))
to_check = message_digest.hexdigest().upper()

leaked = False
with open('sha1_hashes.txt') as file:
    for line in file:
        if to_check in line:
            print(f"Dein Passwort wurde {line.split(':')[1].strip()} mal geleaked ")
            leaked = True
            break
        if not leaked:
            print("Not leaked yet")
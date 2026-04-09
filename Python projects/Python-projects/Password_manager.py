from cryptography.fernet import Fernet
import os
import hashlib


def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

def load_key():
    return open("key.key", "rb").read()

if not os.path.exists("key.key"):
    write_key()

key = load_key()
fer = Fernet(key)


def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def create_master_password():
    pwd = input("Create a master password: ")
    with open("master.txt", "w") as f:
        f.write(hash_password(pwd))

def verify_master_password():
    if not os.path.exists("master.txt"):
        create_master_password()

    pwd = input("Enter master password: ")
    with open("master.txt", "r") as f:
        stored_pwd = f.read()

    if hash_password(pwd) == stored_pwd:
        return True
    else:
        print("❌ Wrong password!")
        return False


if not verify_master_password():
    exit()


def add():
    name = input("Account Name: ")
    pwd = input("Password: ")

    with open("password.txt", "a") as f:
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")

    print("✅ Password added successfully!")

def view():
    if not os.path.exists("password.txt"):
        print("⚠️ No passwords stored yet.")
        return

    with open("password.txt", "r") as f:
        for line in f.readlines():
            data = line.rstrip()
            if "|" in data:
                user, passw = data.split("|")
                try:
                    decrypted = fer.decrypt(passw.encode()).decode()
                    print(f"User: {user} | Password: {decrypted}")
                except:
                    print(f"User: {user} | Password: [Decryption Failed]")


while True:
    print("\n--- Password Manager ---")
    mode = input("Choose: add / view / quit: ").lower()

    if mode == "quit":
        print("👋 Exiting...")
        break
    elif mode == "add":
        add()
    elif mode == "view":
        view()
    else:
        print("❌ Invalid option.")


def add():
    name = input("Account name: ")
    pwd = input("Password: ")

    with open("password.txt", "a") as f:
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")


while True:
    mode = input(
        "Add or view passwords (view/add), press q to quit: ").lower()

    if mode == "q":
        break
    elif mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode")
   
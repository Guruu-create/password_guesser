correct_password = "secret123"
attempts = 0
while attempts < 3:
    guess = input("Enter password: ") 

    if guess == correct_password:
        print("Access Granted!")
        break
    else:
        print("Access Denied!")
        attempts = attempts + 1

if attempts == 3:
    print("Locked out!")
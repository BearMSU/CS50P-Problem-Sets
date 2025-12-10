import random

while True:
    try:
        level = int(input("Level: "))
        if level > 0:
            break
        else:
            raise Exception
    except ValueError:
        pass
    except NameError:
        pass
    except:
        pass

n = random.randint(1, level)
guess = 0

while guess != n:
    guess = input("Guess: ")
    if guess.isnumeric():
        guess = int(guess)
    else:
        continue
    if guess > n:
        print("Too large!")
    elif guess < n:
        print("Too small!")
    else:
        print("Just right!")

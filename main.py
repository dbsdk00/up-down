import random

answer = random.randint(1, 150)

prediction = int(input())

while prediction != answer:
    if prediction < answer:
        print("UP!")

    elif prediction > answer:
        print("DOWN!")

    prediction = int(input())

print("SUCCESS!")
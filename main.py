import random

answer = random.randint(1, 100)

prediction = int(input())

while prediction != answer:
    if prediction < answer:
        print("up")

    elif prediction > answer:
        print("down")

    prediction = int(input())

print("success")
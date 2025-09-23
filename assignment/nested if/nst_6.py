# TODO 6. Check if a student has passed, then check if they scored distinction (>=75). 

print("Entered score is must in 1 to 100")

score = int(input("Enter your mark : "))

if 0 <= score <= 100:
    if score > 30:
        if score >= 75:
            print("You are awesome")
        else:
            print("your score is not greater than 75.")
    else:
        print("You failed ! try again")
else:
    print("Unvalid mark. again enter mark")
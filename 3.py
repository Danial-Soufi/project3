total = 0.0
count = 0

print("Enter numbers to calculate the average. Press Enter without typing to stop:")

while True:
    try:
        value = input("Enter a number: ")
        if value == "":  
            break
        total += float(value) 
        count += 1
    except ValueError:
        print("Please enter a valid number.")  

if count > 0:
    print(f"Average is {total / count:.2f}")  
else:
    print("No numbers were entered.")7

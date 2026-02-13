# Ricardo Alvear
# Assignment: #1

# Assigns a string datatype to a variable named 'gym_member'
gym_member = "Alex Alliton"

# Assigns a double datatype to a variable named 'preferred_weight_kg'
preferred_weight_kg = 20.5

# Assigns an integer datatype to a variable named 'highest_reps'
highest_reps = 25

# Assigns a boolean datatype to a variable named 'membership_active'
membership_active = True

# Creates a dictionary that assigns a tuple datatype to a variable named 'workout_stats'
workout_stats = {
    "alex": (30, 45, 20),
    "jamie": (60, 10, 50),
    "taylor": (10, 20, 30)
}

# Loop through the dictionary and saves the sum of each friend's workout times
total_workout = {}
for key, value in workout_stats.items():
    total = sum(value)
    total_workout.update({f"{key}_Total": total})


workout_list = [
    workout_stats["alex"],
    workout_stats["jamie"],
    workout_stats["taylor"]
]

# Slice for yoga and running (first two columns) for ALL friends
yoga_running_list = []
weightlift_list = []
all_friends = workout_list[0:3]

# Slice for weightlifting (third column) for the LAST TWO friends
for yoga_running in all_friends:
    first_two_values = yoga_running[0:2]
    yoga_running_list.append(first_two_values)

last_two_friends = workout_list[1:3]
for weightlifting in last_two_friends:
    last_values = weightlifting[2:3]
    weightlift_list.append(last_values)



i = 0
for value in workout_list:
    if sum(value) >= 120:
        if i == 0:
            name = "Alex"
        elif i == 1:
            name = "Jamie"
        else:
            name = "Taylor"

        y_r = yoga_running_list[i]
        wl = weightlift_list[i - 1][0]
        print(f"Great job staying active {name}!")
        print(f'"{name}": "Yoga and running {y_r} and weightlifting ({wl})"')
    i += 1

# Ask for the name of a friend, turns the input into lowercase, and checks if the key is the same as the input
userInput = input("Enter the name of a friend: ").lower()
for key, value in workout_stats.items():
    if key == userInput:
        print(f"{key}'s workout for yoga is {value[0]}, running is {value[1]}, and weightlifting is {value[2]}. The total workout time is {sum(value)} minutes.")
        break
    else:
        print(f"Friend {userInput} not found in the records.")
        break

# Gets the highest workout time
highest = 0
highest_name = ""
for key, value in workout_stats.items():
    if sum(value) > highest:
        highest = sum(value)
        highest_name = key
print(f"The friend with the highest total workout time is {highest_name} with {highest} minutes.")

# Gets the lowest workout time
lowest = sum(workout_stats["alex"])
lowest_name = ""
for key, value in workout_stats.items():
        if sum(value) < lowest:
            lowest = sum(value)
            lowest_name = key
print(f"The friend with the lowest total workout time is {lowest_name} with {lowest} minutes.")
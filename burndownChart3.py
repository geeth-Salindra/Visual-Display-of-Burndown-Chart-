import matplotlib.pyplot as plt


# Define the number of days in the sprint and the starting effort
num_days = 10  # Number of days in the sprint
starting_effort=300
input_actual_burndown = [starting_effort, 280, 250, 210, 170, 160, 130, 100, 80, 40, 2] #input_actual_burndown = [300, 280, 250,...]


days = list(range(num_days + 1))
ideal_burndown = [starting_effort - (starting_effort / num_days) * day for day in days]
actual_burndown = input_actual_burndown # The purpose of this line is to get all the inputs in same place

# Plotting the burndown chart
plt.figure(figsize=(10, 6)) #size (he width is set to 10 inches, and the height is set to 6 inches.)
plt.plot(days, ideal_burndown, label='Ideal Burndown', linestyle='--', color='blue')
plt.plot(days, actual_burndown, label='Actual Burndown', marker='o', color='red')

# Adding labels and title
plt.xlabel('Day')
plt.ylabel('Remaining Effort (hrs)')
plt.title('Burndown Chart')
plt.xticks(days)
plt.legend()
plt.grid(True)
plt.show()

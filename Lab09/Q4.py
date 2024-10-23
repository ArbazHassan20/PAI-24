import matplotlib.pyplot as plt

# Sample data: list of student ages
ages = [18, 22, 21, 25, 29, 31, 34, 36, 40, 28,
        22, 25, 30, 19, 20, 33, 26, 29, 38, 41]

# Define age groups
age_groups = ['18-25', '26-30', '31-35', '36 and above']
group_counts = [0] * len(age_groups)

# Count the number of students in each age group
for age in ages:
    if 18 <= age <= 25:
        group_counts[0] += 1
    elif 26 <= age <= 30:
        group_counts[1] += 1
    elif 31 <= age <= 35:
        group_counts[2] += 1
    elif age >= 36:
        group_counts[3] += 1

# Create a pie chart
plt.figure(figsize=(8, 8))
plt.pie(group_counts, labels=age_groups, autopct='%1.1f%%', startangle=140, colors=plt.cm.Paired.colors)
plt.title('Distribution of Student Ages')

# Show the plot
plt.show()

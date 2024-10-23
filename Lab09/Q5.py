import matplotlib.pyplot as plt

# Sample data: gender distribution
genders = ['Male', 'Female']
counts = [35, 20]  # Number of male and female students

# Create a pie chart
plt.figure(figsize=(8, 8))
plt.pie(counts, labels=genders, autopct='%1.1f%%', startangle=140, colors=['skyblue', 'lightcoral'])
plt.title('Gender Distribution Among Students')

# Show the plot
plt.show()

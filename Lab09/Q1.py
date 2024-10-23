import matplotlib.pyplot as plt
import numpy as np

# Sample data for 20 students' heights (in cm)
students = ['Student ' + str(i) for i in range(1, 21)]
heights = [150, 160, 165, 170, 155, 180, 175, 158, 162, 167,
           159, 172, 169, 174, 168, 161, 176, 164, 171, 177]

# Bar Chart
plt.figure(figsize=(12, 6))

# Bar colors
colors = plt.cm.viridis(np.linspace(0, 1, len(heights)))

plt.subplot(1, 2, 1)
plt.bar(students, heights, color=colors)
plt.title('Student Heights (Bar Chart)')
plt.xlabel('Students')
plt.ylabel('Height (cm)')
plt.xticks(rotation=50)
plt.tight_layout()

# Pie Chart
plt.subplot(1, 2, 2)
plt.pie(heights, labels=students, autopct='%1.1f%%', colors=colors)
plt.title('Student Heights (Pie Chart)')
plt.tight_layout()

# Show both charts
plt.show()

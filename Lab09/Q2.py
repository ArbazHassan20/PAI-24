import matplotlib.pyplot as plt

# Sample data: list of cities and their populations
cities = ['New York', 'Los Angeles', 'Islamabad', 'Hyderabad', 'Peshawar',
          'Rawalpindi', 'Sukkhar', 'Multan', 'Delhi', 'Abu Duabi']
populations = [8419600, 3980400, 2716000, 2328000, 1690000,
               1584200, 1547200, 1423800, 1340000, 1027000]

# Create a horizontal bar graph
plt.figure(figsize=(10, 6))
plt.barh(cities, populations, color='skyblue')
plt.title('Population of Cities')
plt.xlabel('Population')
plt.ylabel('Cities')
plt.tight_layout()

# Show the plot
plt.show()

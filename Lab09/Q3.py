import matplotlib.pyplot as plt

# Sample data: list of ice cream flavors and scoops sold
flavors = ['Vanilla', 'Chocolate', 'Strawberry', 'Mint', 'Cookies & Cream',
           'Rocky Road', 'Pistachio', 'Mango']
scoops_sold = [150, 200, 120, 80, 90, 60, 50, 70]

# Create a pie chart
plt.figure(figsize=(8, 8))
plt.pie(scoops_sold, labels=flavors, autopct='%1.1f%%', startangle=140, colors=plt.cm.Paired.colors)
plt.title('Ice Cream Sales Distribution')

# Show the plot
plt.show()

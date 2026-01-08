In this project, I worked on the Eco-Ride Urban Mobility System based on the use cases given in the PDF.

First, I created a basic Python program that displays a welcome message when the application starts. Then, I designed the system using Object Oriented Programming concepts. I created a base Vehicle class and extended it into ElectricCar and ElectricScooter using inheritance.

I used encapsulation to protect vehicle data like battery percentage and status, and accessed them through methods. I applied abstraction to define common behaviors and polymorphism so that the same method behaves differently for different vehicle types.

To manage vehicles across different locations, I used a dictionary where each hub name is mapped to a list of vehicles. I ensured data integrity by preventing duplicate vehicle IDs.

I implemented searching and sorting features to find vehicles based on battery level, hub location, model name, and fare. I also added fleet analytics to count vehicles by their current status.

For data persistence, I implemented file handling. I used CSV to save and load fleet data so that information is not lost when the program stops. I also implemented JSON integration to store complex nested hub–vehicle relationships and handle serialization of custom objects.

Both CSV and JSON files are automatically created by the program, and data is loaded back into the system on startup.

Overall, this project helped me understand how OOP concepts, data structures, algorithms, and file handling work together in a real-world Python application.
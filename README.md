# Overbond Coding Assesment Solution

# How to Execute Application

To execute the solution, first install matplotlib and numpy using pip in a terminal or console. In a linux terminal this would be
'sudo apt install pip' followed by 'pip install matplotlib' and finally 'pip install numpy'.

Following this run main.py in the directory and the scatter plot of the provided data file should be displayed.

# Technologies and Tools Used

For this solution, Python3 was used to write the functions that perform the parsing of data and creation of any and all data structures used
to create the scatter plot. A python dictionary was used to store the records of data from the raw file and as a source for the scatter plot.

Python was primarily used due to the ease of syntax usage and the ease in manipulating string object files. The dictionary data structure in python
is also another reason as it is a hash table like structure that allows for fast data access of key, value paired data.

Matplotlib and numpy were used for the plot creation as they allow for the ease of creating plots from data objects in Python files such as
the python dictionary. Matplotlib 
also makes it easy to create different types of graphs like scatter and bar graphs with colored points.

# Algorithm
The algorithm for the solution essentially parses the data file, and then stores values for Issuance date, CleanBid, CleanAsk and Last Price, using the identification string prefix tags. Once these values are identified and stored in a dictionary, two lists, one containing all issuance dates as the x-axis points and one with all the numerical values as the y-axis points are created and used to produce a scatter plot with the aid of built in scatter plot creation functions in Matplotlib. 

# Tradeoffs and Additional development
The primary tradeoff of using Python3 for this solution would be the lack of graph design complexity for making the scatter plot in that it took me more time to set up the scatter plot construction than it would have had I used another programming language or tool. Were I given additional time I would like to have done more elaborate testing as I feel like due to the amount of time taken in working on how to produce the graph from the python code, I was unable to test my code as thoroughly as I wanted to.

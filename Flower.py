#Ben Holmes
#September 19, 2023
#IT1025
#Module 12 Task 2

#This code creates a class called Flower, defines methods grow() and bloom(),
# and has a main function to create flower objects from the Flower class and calls to 
# their methods.
class Flower:
    #Constructor method, sets the name attribute for the object
    def __init__(self, name):
        self.name = name
	
    #Method, grow() with a reference to self to grow that instance of the flower object
    def grow(self):
        print("The " +self.name + " is growing.")
	
    #Method, bloom() with a referece to self to bloom that instance of the flower object
    def bloom(self):
        print("The " + self.name + " is blooming.")

def main():
    flower1 = Flower("Rose") #Instantiate a flower object called flower1 with the attribute name "Rose"
    flower1.grow() #Call the grow method of flower1
    flower1.bloom() #Call the bloom method of flower1
    flower2 = Flower("Daisy") #Instantiate a flower object called flower2 with the attribute name "Daisy"
    flower2.grow() #Call the grow method of flower2
    flower2.bloom() #Call the bloom method of flower2
    #New code for Module 12 Task 2
    flower3 = Flower("Rhodedendron") #Instantiate a flower object called flower3 with the attribute name "Rhodedendron"
    flower3.grow() #Call the grow method of flower3
    flower3.bloom() #Call the bloom method of flower3
    

if __name__ == "__main__": #Entry point for the main() function
  main()
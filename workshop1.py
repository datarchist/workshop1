print('hello world')

#A function
def my_func(x):
    return x*x

#A for loop with an if statement
for i in range(5):
    print(my_func(i))
    if(my_func(i) == 4):
        print("2 squared found and the answer is 4")

#A class denoting an object of type Garden
class Garden:
    def __init__(self, name, plants):
        self.name = name
        self.plants = plants

    #Getter function for name variable    
    def get_name(self):
        return self.name
        
    #Setter function for name variable    
    def set_new_name(self, new_name):
        self.name = new_name
    
    def water_garden(self):
        for index in range(len(self.plants)):
            plant = self.plants[index]
            if(plant.water_needed() > 0):
                plant.water_plant()
                print(plant.kind + " in plot " + str(index) + " needs " + str(plant.water_needed()) + " more gallons of water today!")
            else:
                print("No need to water! " + plant.kind + " in plot " + str(index) + " well watered")
    
    def check_if_each_flower_is_blooming(self):
        for index in range(len(self.plants)):
            plant = self.plants[index]
            if(plant.kind == "Flower"):
                print(plant.kind + " in plot " + str(index) + " is " + ("in bloom." if plant.check_if_flower_is_blooming() else "not in bloom."))

class Plant:
    #Water level measured in gallons
    def __init__(self, type_plant, life = "1 year", cycle = "1 week", ampd = 10, amt = 0):
        self.kind = type_plant
        self.lifespan = life
        self.grow_cycle = cycle
        self.amount_water_needed_per_day = ampd
        self.amount_watered_today = amt
    
    #call this function to water your plant
    def water_plant(self):
        self.amount_watered_today += 1
    
    #call this function to check the amount of water still needed today
    def water_needed(self):
        return self.amount_water_needed_per_day - self.amount_watered_today
        
class Tree(Plant):
    def __init__(self, tree_type, height, num_fruits, l= "1 year", c= "1 week", ampd = 10, amt = 0):
        Plant.__init__(self, type_plant = "Tree", life = l, cycle = c, ampd = ampd, amt = amt)
        self.tree_type = tree_type
        self.height = height
        self.num_fruits = num_fruits
    
    #Reduce number of fruit by 1
    def pick_fruit(self):
        self.num_fruits -= 1
        
    #Set number of fruits to new fruit count, this is a function called a setter
    def recount_fruit(self, new_fruits_count):
        self.num_fruits = new_fruits_count
    
    #This is a function called a "getter"
    def get_tree_type(self):
        return self.tree_type

#Import code written by python open source so you can use it for free (for more advanced users, try to go over this code in future courses)
import datetime
class Flower(Plant):
        def __init__(self, flower_type, color_leaves, bloom_season, l= "1 year", c= "1 week", ampd = 10, amt = 0):
            Plant.__init__(self, type_plant = "Flower", life = l, cycle = c, ampd = ampd, amt = amt)
            self.flower_type = flower_type
            self.leaf_color = color_leaves
            self.bloom_season_start = bloom_season[0]
            self.bloom_season_end = bloom_season[1]
        
        def check_if_flower_is_blooming(self):
            start = datetime.datetime.strptime(self.bloom_season_start, "%d-%m-%Y")
            end = datetime.datetime.strptime(self.bloom_season_end, "%d-%m-%Y")
            now = datetime.datetime.now()
            if(start <= now <= end):
                return True
            else:
                return False

#Instances of the classes written above           
plant1 = Plant("Bush") 
plant2 = Plant("Shrub", 2, ampd = 4) 
tree1 = Tree(ampd= 3, tree_type = "Spruce", height = "10 Feet", num_fruits = 0) 
tree2 = Tree(ampd = 7, tree_type = "Orange", height = "5 Feet", num_fruits = 10) 
tree3 = Tree(tree_type = "Concord Grape", height = "6 Feet", num_fruits = 100)
flower1 = Flower(flower_type = "Lily", color_leaves="white", bloom_season=["01-06-2022", "31-08-2022"])
flower2 = Flower(ampd = 3, flower_type = "Rose", color_leaves="Red", bloom_season=["22-06-2022", "22-09-2022"])
flower3 = Flower(flower_type = "Rose", color_leaves="Red", bloom_season=["31-07-2022", "31-08-2022"])
my_garden = Garden("Datarden", [plant1, plant2, tree1, tree2, tree3, flower1, flower2, flower3])

print(my_garden.get_name())
my_garden.set_new_name("The " + my_garden.get_name())
print(my_garden.get_name())

for watering_round in range(11):
    #\n in a string means "new line character", it is just for spacing
    print("\nBeginning watering round " + str(watering_round))
    my_garden.water_garden()
    print("Done with watering round " + str(watering_round) + "\n")
print("Yay! Finished watering all my plants today!\n\nChecking if flowers are blooming:\n")
my_garden.check_if_each_flower_is_blooming()

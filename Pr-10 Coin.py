"""
Make your Coins


Here we make our coins with different characteristics like weight,
value , colour, diameter, thickness, number of edges,
Then we add functionality of that coin such as tossing a coin
or after some use of particular coin the colour and value get changed.

"""

import random 

class Coin:
    def __init__ (self, rare = False, face = "Head", clean = True, **info):

        for key, values in info.items():
            setattr(self, key, values)
            
        
        self.is_rare = rare
        self.face = face
        self.is_clean = clean

        if self.is_rare :
            self.value = self.original_value * 1.25
        else :
            self.value = self.original_value

        if self.is_clean :
            self.colour = self.clean_colour
        else:
            self.colour = self.rusty_colour

    def rust(self):
        self.colour = self.rusty_colour
    
    def clean(self):
        self.colour = sel.clean_colour
    
    def __del__(self):
        print("Coin Spent!")

    def flip(self):
        head_option = ["Head", "Tail"]
        choice = random.choice(head_option)
        self.face = choice

    def __str__(self):
        if self.original_value >= 1:
            return " Rs.{} coin ".format(int(self.original_value))

        
class Tangent(Coin):
    def __init__(self):
        data={
            "original_value" : 100.00,
            "clean_colour" : "Gold",
            "rusty_colour" : "Greenish",
            "diameter" : 100.00,#mm
            "thickness" : 5.00,#mm
            "weight" : 10.00,#g
            "num_edges" : 1
            }
        super().__init__(**data)
        
class Rupee(Coin):
    def __init__(self):
        data={
            "original_value" : 1.00,
            "clean_colour" : "Silver",
            "rusty_colour" : None,
            "diameter" : 20.00,#mm 
            "thickness" : 1.45,#mm
            "weight" : 6.00,#g
            "num_edges" : 1
            }
        super().__init__(**data)
        
        def rust(self):
            self.colour = self.clean_colour
        def clean(self):
            self.colour = self.clean_colour
        
class Alfa(Coin):
    def __init__(self):
        data={
            "original_value" : 10.00,
            "clean_colour" : "Bronze",
            "rusty_colour" : "Brownish",
            "diameter" : 40.00,#mm
            "thickness" : 2.45,#mm 
            "weight" : 7.00,#g
            "num_edges" : 1
            }
        super().__init__(**data)    

class Beta(Coin):
    def __init__(self):
        data={
            "original_value" : 20.00,
            "clean_colour" : "Platinum",
            "rusty_colour" : None,
            "diameter" :50.00,#mm 
            "thickness" : 3.45,#mm 
            "weight" : 8.00,#g
            "num_edges" : 1
            }
        super().__init__(**data)
        
        def rust(self):
            self.colour = self.clean_colour
        def clean(self):
            self.colour = self.clean_colour

class Gamma(Coin):
    def __init__(self):
        data={
            "original_value" : 30.00,
            "clean_colour" : "Blue",
            "rusty_colour" : None,
            "diameter" : 60.00,#mm 
            "thickness" : 4.45,#mm 
            "weight" : 9.00,#g
            "num_edges" : 1
            }
        super().__init__(**data)


coins=[Rupee(), Alfa(), Beta(), Gamma(), Tangent()]

for coin in coins :
    arguments =[coin, coin.colour, coin.value, coin.diameter, coin.thickness, coin.num_edges, coin.weight]
    string = "{}- Colour:{}, Value:{}, Diameter:{}mm, Thickness:{}mm, Number of Edges:{}, Mass:{}g".format(*arguments)
    print(string)
        

    
        
    
        
    
        
    

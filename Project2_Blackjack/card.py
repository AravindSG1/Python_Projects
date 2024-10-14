

"""Creates the card objects that is every kind of card in the deck"""
class Cards():
    def __init__(self):
        pass

    #setters
    def set_name(self, name):
        self.name = name

    def set_suit(self, suit):
        self.suit = suit
    
    def set_rank(self, rank):
        if(rank>10):
            self.rank = 10
        
        else:
            self.rank = rank
                    
    #getters
    def get_name_of_card(self):
        print(f"{self.name} of {self.suit}")
    
    def get_value(self):
        return self.rank
    
    def get_name(self):
        return self.name
        
class chips():
    def __init__(self,chip_value):
        self.chip_value = chip_value

    #setters
    def set_chip_value(self, chip_value):
        self.chip_value = chip_value
    
    def set_change_chip_value(self, chip_value):
        self.chip_value+=chip_value
    

    #getters
    def get_chip_value(self):
        return self.chip_value
        



''' Simulation eines Ampelsystem '''

#Class Definition

class Ampel(object):
    """ Ampel () """
    def __init__(self):
        """constructor"""
        self.zustand = 'rot'
    
    def setZustand(self, z):
        """ set_zusatnd """
        self.zustand = z

    def schalten(self):
        """ schalten """
        if self.zustand == 'rot':
            self.zustand = 'rotgelb'
        elif self.zustand == 'rotgelb':
            self.zustand = 'gruen'
        elif self.zustand == 'gruen':
            self.zustand = 'gelb'
        elif self.zustand == 'gelb':
            self.zustand = 'rot'
       
        
    def getLampen(self):
        """ getLampen """
        if self.zustand == 'rot':
            return (True, False, False)
        elif self.zustand == 'rotgelb':
            return (True, True, False)
        elif self.zustand == 'gruen':
            return (False, False, True)
        elif self.zustand == 'gelb':
            return (False, True, False)
       
    
### Test ###

a1 = Ampel()            
print "Start:", a1.getLampen()  

a1.schalten()
print"1", a1.getLampen()	# nach 1 mal umschalten, rotgelb

a1.schalten()
print "2", a1.getLampen()	# nach 2 mal umschalten, gruen	 	

a1.schalten()
print "3", a1.getLampen()	# nach 3 mal umschalten, gelb  

a1.schalten()
print "4", a1.getLampen()	# nach 4 mal umschalten, rot

    
                

from sys import exit
from random import randint 
#import pocket


class Scene (object):

    def enter(self):
        print "This scene is not yet configured. Subclass it and implement enter()"
        exit(1)


class Make_a_dice (Scene):
        
    def enter(self):
        print "Now you can make a dice."
        d=int(raw_input('dice:'))
        
        if d==1:
            return 'card1'
        elif d==2:
            return 'card2'
        elif d==3:
            return 'card3'
        elif d==4:
            return 'card4'
        elif d==5:
            return 'card5'
        elif d==6:
            return 'card6'
        else:
            print "Invalid input."
            print "Please make a dice again."
            return 'make_a_dice'
               

class End (Scene):
    
    def enter (self):
        global balance
        print "Game over!"
        print "You got %d dollars in your pocket." %balance
        
        exit(1)
        
                
class GetCash (Scene):

    def enter (self):
        print "Cong! You got 500 dollars cash."
        print "Put them in your pocket."
         
        delta=500
        global balance
        global ctr
        current_balance=PocketBalance()
        balance=current_balance.calculate(balance, delta)
        ctr=current_balance.count(ctr)
        
        print "You have used %d chance(s) for dicing." %ctr
        print "There are (5-%d) left." % ctr
        
        if balance>0:
            print "Now you got %d dollars in your pocket." % balance
        else:
            print "Now you are in debt %d dollars." % balance
        
        return 'make_a_dice'
     
        
class LoseCash (Scene):

    def enter (self):
        print "Bad news! You will lose 400 dollars cash."
        print "Please pay it now."
        
        delta=-400
        global balance
        global ctr
        current_balance=PocketBalance()
        balance=current_balance.calculate(balance, delta)
        ctr=current_balance.count(ctr)
        
        print "You have used %d chance(s) for dicing." %ctr
        print "There are (5-%d) left." % ctr
        
        if balance>0:
            print "Now you got %d dollars in your pocket." % balance
        else:
            print "Now you are in debt %d dollars." % balance
        
        return 'make_a_dice'
     
        
class GetGold (Scene):

    def enter (self):
        print "Cong! You got 1 kg gold."
        print "You can take a ticket valuing 680 dollars, which is the same value to 1 kg gold."
        
        delta=680
        global balance
        global ctr
        current_balance=PocketBalance()
        balance=current_balance.calculate(balance, delta)
        ctr=current_balance.count(ctr)
        
        print "You have used %d chance(s) for dicing." %ctr
        print "There are (5-%d) left." % ctr
        
        if balance>0:
            print "Now you got %d dollars in your pocket." % balance
        else:
            print "Now you are in debt %d dollars." % balance
        
        return 'make_a_dice'
        
        
class GetHouse (Scene):

    def enter (self):
        print "Cong! You got a house."
        print "You can take a ticket valuing 1100 dollars, which is the same value to a house."
        
        delta=1100
        global balance
        global ctr
        current_balance=PocketBalance()
        balance=current_balance.calculate(balance, delta)
        ctr=current_balance.count(ctr)
        
        print "You have used %d chance(s) for dicing." %ctr
        print "There are (5-%d) left." % ctr
        
        if balance>0:
            print "Now you got %d dollars in your pocket." % balance
        else:
            print "Now you are in debt %d dollars." % balance
        
        return 'make_a_dice'
        
        
class LoseHouse (Scene):

    def enter (self):
        print "Bad news! You'r gonna lose your house."
        print "You can pay 1100 dollars."
        
        delta=-1100
        global balance
        global ctr
        current_balance=PocketBalance()
        balance=current_balance.calculate(balance, delta)
        ctr=current_balance.count(ctr)
        
        print "You have used %d chance(s) for dicing." %ctr
        print "There are (5-%d) left." % ctr
        
        if balance>0:
            print "Now you got %d dollars in your pocket." % balance
        else:
            print "Now you are in debt %d dollars." % balance
        
        return 'make_a_dice'
        

class DoItAgain (Scene):
    
    def enter (self):
        print "Opps....You got nothing this time and have a chance to make a dice again."
        
        delta=0
        global balance
        global ctr
        current_balance=PocketBalance()
        balance=current_balance.calculate(balance, delta)
        ctr=current_balance.count(ctr)
        
        return 'make_a_dice'
    

    
class Engine (object):
    
    def __init__(self, scene_map):
        self.scene_map=scene_map
        
    def play (self):
        current_scene=self.scene_map.opening_scene()
        
        while True:
            print "\n----------"
            next_scene_name=current_scene.enter()
            current_scene=self.scene_map.next_scene(next_scene_name)
     
class Map (object):

    scenes={'make_a_dice': Make_a_dice(),
            'card1': GetCash(),
            'card2': LoseCash(),
            'card3': GetGold(),
            'card4': GetHouse(),
            'card5': LoseHouse(),
            'card6': DoItAgain()
           } 
   
    def __init__(self, start_scene):
        self.start_scene=start_scene
        
    def next_scene (self, scene_name):
        return Map.scenes.get(scene_name)
       
    def opening_scene (self):
        return self.next_scene(self.start_scene)


class PocketBalance (object):

    def calculate (self, balance, delta):
        
        balance=balance+delta
        return balance 
            
    def count (self, ctr):
        if ctr<4:
            ctr=ctr+1
            return ctr
        else: 
            ending=End()
            ending.enter()
            

def main():
	print "Welcome to the Fortune Adventure Game."
	print "In this game you have 5 times to make a dice."
	print "You can find a card depending on the dice number."
	print "You will earn or lose wealth according to the content of the card."
	print "After 5 times, the game will check your pocket"
    
	balance=0
	counter=0
  
	a_map=Map('make_a_dice')
	a_game=Engine(a_map)
	a_game.play()   
 

 
if __name__ == "__main__":
	main()           
              
              

    

class Card():
  """ Represtents a standard playing Card"""
  suit_names = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
  rank_names = [None, 'Ace', '2', '3', '4', '5', '6', '7','8', '9', '10', 'Jack', 'Queen', 'King']
  def __init__(self,suit=0,rank=2):
    self.suit=suit
    self.rank=rank
    
  def __str__(self):
    return '%s of %s'%(Card.rank_names[self.rank],Card.suit_names[self.suit])
    
  def __cmp__(self,other):
    t1=self.suit,self.rank
    t2=other.suit,other.rank
    return cmp(t1,t2)

class Deck():
  """Represents a Group of standard 52 cards"""
  def __init__(self):
    self.cards=[]
    for suit in range(4):
      for rank in range(1,14):
        self.cards.append(Card(suit,rank))
        
  def __str__(self):
    res=[]
    for card in self.cards:
      res.append(str(card))
    return '\n'.join(res)
    
obj=Deck()
print obj          

### Testing task 1:

# Carry out static testing on the code below.
# Comment on any errors that you see below.

Note that we are only looking for errors here.

**Not** any issues with, i.e.: 
Thinking that methods should be renamed or should be class level, or using string interpolation etc. 

These aren't errors but rather standards that vary from developer to developer. 

Only comment on errors that would stop the tests running.

```python

class CardGame:
  # Missing the def __init__ initialisation section.  Without this, we cannot make instances of the class.

  def check_for_ace(self, card):
    if card.value = 1:
      # need to have two '=' signs to check card.value is equal to 1.
      return True
    else
    # else needs a colon after it
      return False
   

  dif highest_card(self, card1 card2):
  # 'dif' should be 'def' to define a function.  Also, need ',' between 'card1' and 'card2'
  if card1.value > card2.value:
    return card
    # should specify 'card1'
  else:
    return card2
  


def cards_total(self, cards):
# The line above needs to be indented in order to be a method of the class
  total
  # total needs an assigned value, e.g. total = 0
  for card in cards:
    total += card.value
    # return is in the for loop so will end the program after the first card.  Indentation should be removed so that the total is returned after looping through all of the cards
    return "You have a total of" + total
    # total needs to be converted to string.  Need a space after 'of'
  
```

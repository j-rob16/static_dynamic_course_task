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

# card.value = 1 needs to be a double '=' => card.value == 1:
# if statement needs a colon after 'else' in order to run
  def check_for_ace(self, card):
    if card.value = 1:
      return True
    else
      return False
   
# methods need to be declared with 'def'. 'dif' will stop the code from running
# the card1 & card2 parameters need to be comma separated
# the if statement needs to be indented in order to run
# 'card' is not a parameter passed to this method
  dif highest_card(self, card1 card2):
  if card1.value > card2.value:
    return card
  else:
    return card2
  
# cards_total method is outside of the scope of the class. Needs to be indented to the right
# total variable needs to be defined in order to become a variable
# return statement is indented too far to the right. Will return a string for every card in cards.
# total needs to be changed to a string in order to concatenate
def cards_total(self, cards):
  total
  for card in cards:
    total += card.value
    return "You have a total of" + total
  
```

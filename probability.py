import random

def roll_dice(n):
  drawn=[]
  #Put the prediction in a list
  for i in range(n):
    roll=random.randint(1,6)
    drawn.append(roll)
  return drawn


def prob(expected_roll, num_dice_rolled, num_experiments):
  m=0
  r=0
  for i in range(num_experiments):
    #Call the roll_dice function to roll the dice 
    another_roll=roll_dice(num_dice_rolled)
    #Call the contains_draws funcion to compare the rolls
    if contains_draws(expected_roll, another_roll):
      r=r+1
      if r==1:
        if i > 0:
          print("It took " + str(i) + " rolls to have your elements")
        else:
          print("The first roll was your expected roll")
      m += 1

  txt=str(m) + " over " + str(num_experiments) + " or " + str(m/num_experiments) + "%"
  return txt
  
#compare the list of expected draw with the actual draw  
def contains_draws(exptected_draw, actual_draw):
  for b in exptected_draw:
    if b in actual_draw:
      actual_draw.remove(b)
    else:
      return False
  return True

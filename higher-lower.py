from art import logo, vs
from game_data import data
import random
from replit import clear

def contestantProfile():
  """
  the profile for the contestants
  """
  
  return list((random.choice(data)).values())
  
def result(compare_followers, against_followers, guess):
  """
  check who has more followers
  """
  count = 0
  if guess == "a":
    if compare_followers > against_followers:
      print("correct")
      return "correct"
      clear()
       
    else:
      return "wrong"
      
  elif guess == "b":
    if against_followers > compare_followers:
      print("correct")
      return "correct"
      clear()
        
    else:
      return "wrong"
   
def higherLower():
  """
  the gain of higherLower fn
  """
  count = 0
  print(logo)
  
  profile_a = contestantProfile()
  print(f"compare A: {profile_a[0]}, a {profile_a[2]}, from {profile_a[3]}")
  #print(profile_a[1])
  profile_a_followers = profile_a[1]

  guessRight = True
  while guessRight:
    
    print(vs)
    
    profile_b = contestantProfile()
    print(f"Against B: {profile_b[0]}, a {profile_b[2]}, from {profile_b[3]}")
    #print(profile_b[1])
    profile_b_followers = profile_b[1]
    
    guess = input("Who has more followers? Type A or B :").lower()
     
    rightAnswer = result(profile_a_followers, profile_b_followers, guess)
    
    if rightAnswer == "correct":
      
      clear()
      print(logo)
      count += 1
      print("You're right! Current score:",count)
      
      profile_a = profile_b
      print(f"compare A: {profile_a[0]}, a {profile_a[2]}, from {profile_a[3]}")
      #print(profile_a[1])
      profile_a_followers = profile_a[1]

    elif rightAnswer == "wrong":
      clear()
      print("Sorry, that's wrong. Final score:",count)
      guessRight = False
      
higherLower()
  



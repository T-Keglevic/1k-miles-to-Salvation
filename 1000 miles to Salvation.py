#import resources, clear console
import random

from os import system, name
def clear():
   if name == 'nt':
    _ = system('cls')
   else:
    _ = system('clear')
clear()


#initial variables
miles_left = 1000
fuel = random.randint(90, 160)
parts = random.randint(7, 14)
health = random.randint(90, 101)
show_sign = 1
conditions_met = True
won = 0

#game phases: encounter, repair, drive
def encounter():
  global fuel
  global health
  global parts
  global conditions_met
  print("You have encountered bandits.\n")
  answer = input("Will you (O)utrun them, (F)ire at them, or (R)am into them?\n ")
  if answer.lower() == "o":
    print("\nEngine screaming, you take to the highway and outdrive the bandits.\n")
    fuel = fuel - random.randint(1, 21)
    health = health - random.randint(1, 7)
    if fuel <= 0:
      conditions_met = False
  elif answer.lower() == "f":
    print("\nFiring your weapons, you create a fountain of blood and fuel out of the bandits' vehicles.\n")
    salvaged_parts = random.randint(1, 7)
    parts += salvaged_parts
    health = health - random.randint(1, 7)
    if health <= 0:
      conditions_met = False
    print(f"\nYou salvage {salvaged_parts} parts from the wrecks, and your car has sustained some damage.")
  elif answer.lower() == "r":
    print("\nIn a tactical decision or by wild berserking, you use dust as cover and ram a bandit's car off the road, leaving behind a smoldering wreck.\n")
    salvaged_fuel = random.randint(1, 101)
    fuel += salvaged_fuel 
    health = health - random.randint(1, 7)
    if health <= 0:
      conditions_met = False
    print(f"\nYou salvage {salvaged_fuel} fuel from the wrecks, and your car has sustained some damage.")
  else:
    lost_fuel = random.randint(10, 51)
    fuel -= lost_fuel
    if fuel <= 0:
      conditions_met = False
    lost_parts = random.randint(2, 11)
    if parts > 0:
      parts -= lost_parts
    health = health - random.randint(3, 18)
    if health <= 0:
      conditions_met = False
    print(f"\nYou missed your intended action. You outpace the pursuit on canyon roads, but have lost {parts} parts, {fuel} fuel, and have sustained some damage.\n")

def repair():
  global health
  global parts
  global conditions_met
  repair = 100 - health
  if parts < repair:
    health += parts
    parts = 0
  else:
    parts -= repair
    health += repair
  if fuel <= 0:
    conditions_met = False
  print(f"You repair your car with {parts} parts. The car is {health}% operational.\n")

def drive():
  global fuel
  global miles_left
  global show_sign
  miles_left_old = miles_left
  miles_left -= random.randint(1, 200)
  miles_left_new = miles_left
  fuel = int(fuel - ((miles_left_old-miles_left_new)/8))
  if miles_left > 0:
    print(f"You have {fuel} fuel, and {parts} parts. There are {miles_left} miles left to Salvation.")
  if miles_left < 300:
    if show_sign == 1:
      print(f"You pass a road sign: Welcome to Salvation, {miles_left} miles ahead. Population 665.")
      show_sign = 0


#end conditions
def win():
  global conditions_met
  global won
  print("You have traveled 1000 miles to Salvation. Thank you for playing. Kibertekt 2023.")
  conditions_met = False
  won = 1

def lose():
  print(f"You are stopped. Salvation still lies {miles_left} miles beyond your reach.")
  restart = input("Drive again (y/n)? ")
  if restart.lower() == "y":
    game_start()
  else:
    print("Thank you for playing 1000 miles to Salvation. Kibertekt 2023.")


#game start
def game_start():
  print("The desert your Purgatory\nThe Car your Redemption\nA cold night behind\nAnd a thousand miles to Salvation.\n\n\n")
  print(f"You have {parts} parts, and {fuel} fuel. The engine is singing words of power. Press Enter to open the throttle.\n")
  input()
  while miles_left > 0:
    encounter()
    repair()
    drive()
  else:
    win()


#main loop
while conditions_met == True:
  game_start()
else:
  if won != 1:
    lose()
  else:
    input("Cool the engine down.")
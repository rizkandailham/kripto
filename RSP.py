import random
from time import sleep

class rock_paper_scissor:
  def computer(self):
    turn=["ROCK","PAPER","SCISSOR"]
    return ''.join(random.sample(turn,1))

  def player(self):
    f=input("Show me your guess player:")
    if f=="1":
      turn="ROCK"
    if f=="2":
      turn = "PAPER"
    if f=="3":
      turn = "SCISSOR"
    return turn

  def versus(self,computer,player):
    win="nothing"
    if computer == player:
      win="Draw"
    if computer=="ROCK" and player == "SCISSOR":
      win = "Computer"
    if computer == "ROCK" and player == "PAPER":
      win = "Player"
    if computer == "SCISSOR" and player == "PAPER":
      win = "Computer"
    if computer == "SCISSOR" and player == "ROCK":
      win = "Player"
    if computer == "PAPER" and player == "ROCK":
      win = "Computer"
    if computer == "PAPER" and player == "SCISSOR":
      win = "Player"
    return win

  def gas():
    attempt=True
    playing=rock_paper_scissor()
    print("Welcome Challenger fight the monster and claim your victory!")
    print("1. For ROCK")
    print("2. For PAPER")
    print("3. For SCISSOR")
    while attempt:
         print("Silahkan tunggu sebentar sedang membuat arena baru")
         sleep(5)
         result=playing.versus(playing.computer(),playing.player())
         if result == 'Player':
                 print("Player Win Congratulations")
                 print("here is your flag: the_hero_never_cry_but_a_man_need_to_talk")
                 attempt=False
         if result == 'Computer':
                 print("Demon Lord has winning the game!")
                 print("Your spirit has inherit for the next challenger.")
         if result == "Draw":
                print("Time for next round!")

if __name__ == "__main__":
    rock_paper_scissor.gas()

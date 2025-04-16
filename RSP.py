import random


class rock_paper_scissor:
  def computer(self):
    turn=["ROCK","PAPER","SCISSOR"]
    return random.sample(turn,1)

  def player(self):
    f=input()
    if f=="1":
      turn="ROCK"
    if f=="2":
      turn = "PAPER"
    if f=="3":
      turn = "SCISSOR"
    return turn

  def versus(self,computer,player):
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

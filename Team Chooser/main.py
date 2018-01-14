from random import choice

players = []
file = open('players.txt', 'r')
players = file.read().splitlines()
print(players)

teamA = []
teamB = []

while len(players) > 0:
  playerA = choice(players)
  print(playerA)
  teamA.append(playerA)
  players.remove(playerA)
  print('Players left:', players)
  
  if players == []:
    break
  
  playerB = choice(players)
  print(playerB)
  teamB.append(playerB)
  players.remove(playerB)
  print('Player left:', players)
  
print('Team A:', teamA)
print('Team B', teamB)


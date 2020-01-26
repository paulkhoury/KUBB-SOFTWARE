import csv
import time
import pandas as pd
from datetime import datetime

print("Kubb League\nЛига Кубба\nLigue de Queb\n")

while True:

    time.sleep(0.1) 
    print("Options:")
    time.sleep(0.1) 
    print("1. View Stats & Standings")
    time.sleep(0.1) 
    print("2. Add/Edit Scores")
    time.sleep(0.1) 
    print("3. Create a New Kubber Profile")
    time.sleep(0.1) 
    print("(type in the number of your option and press enter)")

    direct = input("\n>>> ")

    if direct == "1":

      #with open("master.csv") as csvfile:
        #readCSV = csv.reader(csvfile, delimiter=",")
        #for row in readCSV:
          #print(row)
      print("Top 9 players are Varsity. In case of tie, number of wins will serve as tie-breaker")
      masterpandas = pd.read_csv('master.csv')
      print(masterpandas)

    elif direct == "2":
      
      print("\nFor your convenience, here is a list of existing named and registered kubbers:\n**********\n",open("players.txt", "r").read(),"\n**********")
      name = (input("\nWhich player's points/attempts/wins do you wish to update?\n(type names exactly as shown on above list)\n>>> "))
      player_file = (name+".txt")

      points_to_add = int(input("\nEnter the quantitative value that you wish to add to the current POINTS.(Negative to remove, 0 to skip) \n>>> "))
      attempts_to_add = int(input("\nEnter the quantitative value that you wish to add to the current ATTEMPTS.(Negative to remove, 0 to skip) \n>>> "))
      wins_to_add = int(input("\nEnter the quantitative value that you wish to add to the current WINS.(Negative to remove, 0 to skip) \n>>> "))

      player = open(player_file)
      contents = player.read()
      contents = contents.split("\n")

      init_points = int(contents[1])
      new_points = init_points + points_to_add

      init_attempts = int(contents[2])
      new_attempts = init_attempts + attempts_to_add

      init_wins = int(contents[3])
      new_wins = init_wins + wins_to_add

      contents[1] = str(new_points)
      contents[2] = str(new_attempts)
      contents[3] = str(new_wins)
      contents[4] = str(float(new_points)/float(new_attempts))

      print("\n",datetime.now(),"\nSuccessfully added",str(points_to_add),"point(s),",str(attempts_to_add),"attempt(s), and",str(wins_to_add),"win(s) to",name,"\n")
      receipt = (datetime.now(),"Successfully added",str(points_to_add),"point(s),",str(attempts_to_add),"attempt(s), and",str(wins_to_add),"win(s) to",name)

      record = open("receipt.txt","a")
      record.write(str(receipt))
      record.write("\n")
      record.close()

      open(player_file, "w").close()

      file = open(player_file,"w")
      file.write("\n".join(contents)) 
      file.close() 

      print("ACTION COMPLETED.")

      cleanSlateMaster = open("master.csv","w")
      cleanSlateMaster.write("Name,Points,Attempts,Wins,Accuracy")
      cleanSlateMaster.write("\n")
      cleanSlateMaster.close()

      listOfPlayers = open("players.txt")
      splitListOfPlayers = listOfPlayers.read().split("\n")
      for i in splitListOfPlayers:
        individual = open(i+".txt") 
        statsInList = individual.read().split("\n")
        statsInList = ",".join(statsInList)

        rewriteMaster = open("master.csv","a")
        rewriteMaster.write(str(statsInList))
        rewriteMaster.write("\n")
        rewriteMaster.close()
      #to be condensed!

      #with open('master.csv', 'w', newline='') as file:
        #writer = csv.writer(file)
        #writer.writerow(["Player", "Points", "Attempts","Wins"])
        #writer.writerow(open("player1.txt").read().split("\n"))
        #writer.writerow(open("player2.txt").read().split("\n"))
        #writer.writerow(open("player3.txt").read().split("\n"))


        array = []

        with open('master.csv') as csvDataFile:
            csvReader = csv.reader(csvDataFile)
            for row in csvReader:
                array.append(row)

        def sortFifth(val): 
            return val[4]  
          
        array.sort(key = sortFifth, reverse = True)   

        open('master.csv', 'w').close()
        reorderMaster = open("master.csv","a")
        for item in array:
          reorderMaster.write(",".join(item))
          reorderMaster.write("\n")
        reorderMaster.close()

    elif direct == "3":
      player_list = open("players.txt")
      kubbers = player_list.read().split("\n")
      print("\nFor your convenience, here is a list of existing named and registered kubbers:\n**********\n",open("players.txt", "r").read(),"\n**********")
      new_player = input("What is the name of the Kubber you would like to add?\n>>> ").lower()
      new_player_file = (new_player+".txt")
      f = open("players.txt", "a")
      f.write("\n")
      f.write(new_player)
      f.close()
      new_file = open(new_player_file,"a+")
      #new_file.close
      #new_file = open(new_player_file, "a")
      new_file.write(new_player)
      new_file.write("\n0\n0\n0\n0")
      new_file.close()
      print("ACTION COMPLETED.")

      cleanSlateMaster = open("master.csv","w")
      cleanSlateMaster.write("Name,Points,Attempts,Wins,Accuracy")
      cleanSlateMaster.write("\n")
      cleanSlateMaster.close()

      listOfPlayers = open("players.txt")
      splitListOfPlayers = listOfPlayers.read().split("\n")
      for i in splitListOfPlayers:
        individual = open(i+".txt") 
        statsInList = individual.read().split("\n")
        statsInList = ",".join(statsInList)

        rewriteMaster = open("master.csv","a")
        rewriteMaster.write(str(statsInList))
        rewriteMaster.write("\n")
        rewriteMaster.close()

    #sam mekhael feature
    else:
      print("1,2,or 3 retard")
          
    while True:
        answer = input('\nContinue using Kubb Software? (y/n):\n>>> ').lower()
        if answer in ('y', 'n'):
            break
        print ('Invalid input.')
    if answer == 'y':
        print("\n")
        continue
    else:
        print ('\nGoodbye')
        break
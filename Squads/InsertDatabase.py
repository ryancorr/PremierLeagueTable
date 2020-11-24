import psycopg2
import re


def insertGames(c,file):
	gameNum = 1
	curdate = ''
	teams = {'Leicester City' : 1, 'Tottenham Hotspur' : 2, 'Liverpool': 3, 'Southampton' : 4, 'Chelsea' : 5, 'Aston Villa' : 6,
	'Everton': 7, 'Crystal Palace' : 8, 'Wolverhampton Wanderers' : 9, 'Manchester City' : 10, 'Arsenal' : 11, 'West Ham United' : 12,
	'Newcastle United' : 13, 'Manchester United' : 14, 'Leeds United' : 15, 'Brighton and Hove Albion': 16, 'Fulham' : 17, 'West Bromwich Albion' : 18,
	'Burnley' : 19, 'Sheffield United' : 20}

	for line in file:
		if line.startswith("#"):
			curLine = line.split()
			curLine[0] = curLine[0][1:]
			curdate = '2020-' + curLine[1] + '-' + curLine[0]
		else:
			curLine = line.split(" v ")
			curLine = [curLine[0], curLine[1].rstrip(" \n")]
			tone = ['' + curLine[0] + ''][0]
			ttwo = ['' + curLine[1] + ''][0]
			oneId = teams.get(tone)
			twoId = teams.get(ttwo)
			c.execute("INSERT INTO table_game (gamedate,teamone_id, teamtwo_id) VALUES (%s,%s,%s)" ,(curdate,oneId,twoId))
			#c.execute("INSERT INTO table_game_teams (game_id, team_id) VALUES (%s,%s)" ,(gameNum,oneId))
			#c.execute("INSERT INTO table_game_teams (game_id, team_id) VALUES (%s,%s)" ,(gameNum,twoId))
			gameNum += 1
			
	con.commit()				
	con.close()


def insertPlayers(c,file,teamId):
	for line in file:
		curLine = line.split("\t")
		if curLine[-1] == '\n':
			curLine.pop(-1)
		curLine[-1] = curLine[-1].rstrip('\n')
		curLine[-1] = curLine[-1].rstrip(' ')
		curLine[2] = curLine[2][:-4]
		#c.execute("INSERT INTO table_player (name, number, position, nation, club_id) VALUES (%s,%s,%s,%s,%s)" ,(curLine[3],curLine[0],curLine[1],curLine[2],teamId))

	con.commit()				
	con.close()

def insertPic(c,file,teamId):
	for line in file:
		curLine = line.split()
		link = curLine[-1]
		picLink = link.replace("110x140", "250x250")
		num = curLine[0]
		c.execute("UPDATE table_player SET picture = (%s) WHERE club_id = (%s) AND number = (%s)" , (picLink, teamId, num))

	con.commit()				
	con.close()

#connect to postres db
con = psycopg2.connect(host = 'localhost', database = "premtable", user = "postgres", password = "xxxxxxx", port = "5432")

#cursor
c= con.cursor()


file = open("games.txt", "r", encoding='utf8')
#insertPic(c,file,1)
insertGames(c,file)















'''
Creating Table
c.execute("""CREATE TABLE PremTable (
			name text,
			played integer,
			won integer,
			drawn integer,
			lost integer,
			points integer
		)""")

#Insert all the clubs into the table

c.execute("INSERT INTO PremTable VALUES ('Leicester City',8,6,0,2,18)")
c.execute("INSERT INTO PremTable VALUES ('Tottenham Hotspur',8,5,2,1,17)")
c.execute("INSERT INTO PremTable VALUES ('Liverpool',8,5,2,1,17)")
c.execute("INSERT INTO PremTable VALUES ('Southamption',8,5,1,2,16)")
c.execute("INSERT INTO PremTable VALUES ('Chelsea',8,4,3,1,15)")
c.execute("INSERT INTO PremTable VALUES ('Aston Villa',7,5,0,2,15)")
c.execute("INSERT INTO PremTable VALUES ('Everton',8,4,1,3,13)")
c.execute("INSERT INTO PremTable VALUES ('Crystal Palace', 8,4,1,3,13)")
c.execute("INSERT INTO PremTable VALUES ('Wolverhamption Wanderers',8,4,1,3,13)")
c.execute("INSERT INTO PremTable VALUES ('Manchester City',7,3,3,1,12)")
c.execute("INSERT INTO PremTable VALUES ('Arsenal',8,4,0,4,12)")
c.execute("INSERT INTO PremTable VALUES ('West Ham Utd',8,3,2,3,11)")
c.execute("INSERT INTO PremTable VALUES ('Newcastle Utd',8,3,2,3,11)")
c.execute("INSERT INTO PremTable VALUES ('Manchester Utd', 7,3,1,3,10)")
c.execute("INSERT INTO PremTable VALUES ('Leeds Utd',8,3,1,4,10)")
c.execute("INSERT INTO PremTable VALUES ('Brighton and Hove Albion',8,1,3,4,10)")
c.execute("INSERT INTO PremTable VALUES ('Fulham',8,1,1,6,4)")
c.execute("INSERT INTO PremTable VALUES ('West Bromwich Albion',8,0,3,5,3)")
c.execute("INSERT INTO PremTable VALUES ('Burnley',7,0,2,5,2)")
c.execute("INSERT INTO PremTable VALUES ('Sheffield Utd',8,0,1,7,1)")
'''











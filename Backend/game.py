from coord import Coord
from piece import Piece

class Game:
	def __init__(self):
		self.board = [[Piece() for x in range(8)] for y in range(8)]
		pieces = ["rook", "knight", "bishop", "queen", "king", "bishop", "knight", "rook"]
		currId = 0
		for i in range(8):
			self.board[0][i] = Piece(pieces[i], 1, currId, 0)
			currId+=1
		for i in range(8):
			self.board[1][i] = Piece("pawn", 1, currId, 0)
			currId+=1
		for i in range(8):
			self.board[6][i] = Piece("pawn", 0, currId, 0)
			currId+=1
		for i in range(8):
			self.board[7][i] = Piece(pieces[i], 0, currId, 0)
			currId+=1
		self.kings = [None,None]
		for c in [Coord(x,y) for x in range(8) for y in range(8)]:
			if self.getSquare(c).name == "king":
				self.kings[self.getSquare(c).team] = c
		
		self.turnCount = 0
	
	def getPossibleMoves(self, c:Coord):
		if(c.isValid() == False):
			return -1
		p = self.getSquare(c)
		enemyTeam = 0 if p.team==1 else 1
		if p.name == "knight":
			deltas = [
				Coord(1,2),Coord(2,1),
				Coord(-1,2),Coord(-2,1),
				Coord(1,-2),Coord(2,-1),
				Coord(-1,-2),Coord(-2,-1),
			]
			out = []
			for delta in deltas:
				temp = c+delta
				if(temp.isValid() and self.getSquare(temp).team != p.team):
					out.append(temp)
			return out
		elif p.name == "king":
			deltas = [
				Coord(-1,0),Coord(-1,-1),
				Coord(0,-1),Coord(1,-1),
				Coord(1,0),Coord(1,1),
				Coord(0,1),Coord(-1,1)
			]
			out = []
			for delta in deltas:
				temp = c+delta
				if(temp.isValid() and self.getSquare(temp).team != p.team):
					out.append(temp)
			return out
		elif p.name == "rook":
			deltas = [
				Coord(-1,0),Coord(1,0),
				Coord(0,1),Coord(0,-1)
			]
			out = []
			for delta in deltas:
				temp = c+delta
				while (temp.isValid() and self.getSquare(temp).team != p.team):
					if(self.getSquare(temp).team == enemyTeam):
						out.append(temp)
						break
					out.append(temp)
					temp = temp+delta
			return out
		elif p.name == "bishop":
			deltas = [
				Coord(-1,1),Coord(-1,-1),
				Coord(1,1),Coord(1,-1)
			]
			out = []
			for delta in deltas:
				temp = c+delta
				while (temp.isValid() and self.getSquare(temp).team != p.team):
					if(self.getSquare(temp).team == enemyTeam):
						out.append(temp)
						break
					out.append(temp)
					temp = temp+delta
			return out
		elif p.name == "queen":
			deltas = [
				Coord(-1,0),Coord(1,0),
				Coord(0,1),Coord(0,-1),
				Coord(-1,1),Coord(-1,-1),
				Coord(1,1),Coord(1,-1)
			]
			out = []
			for delta in deltas:
				temp = c+delta
				while (temp.isValid() and self.getSquare(temp).team != p.team):
					if(self.getSquare(temp).team == enemyTeam):
						out.append(temp)
						break
					out.append(temp)
					temp = temp+delta
			return out
		elif p.name == "pawn":
			out = []

			forwards = Coord(0,1)
			if(p.team == 0):
				forwards = Coord(0,-1)
			if(self.getSquare(c+forwards).team == -1):
				out.append(c+forwards)
				if(p.timeMoved == 0 and self.getSquare(c+forwards+forwards).team == -1): 
					out.append(c+forwards+forwards)
			
			#capturing
			deltas = [Coord(-1, 0)+forwards, Coord(1, 0)+forwards]
			for delta in deltas:
				t = c+delta
				# print("Coord:",t)
				# print("Square:",self.getSquare(t))
				# print("Team:",self.getSquare(t).team)
				if t.isValid() and self.getSquare(t).team == enemyTeam:
					out.append(t)
			"""Add en passant if extra time"""
			return out
	
	def updateKingPos(self):
		for c in [Coord(x,y) for x in range(8) for y in range(8)]:
			if self.getSquare(c).name == "king":
				self.kings[self.getSquare(c).team] = c

	def kingInCheck(self, team:int):
		enemy = 1 if team==0 else 0
		self.updateKingPos()
		for tempC in [Coord(x,y) for x in range(8) for y in range(8)]:
			if self.getSquare(tempC).team == enemy:
				if(self.kings[enemy] in self.getPossibleMoves(tempC)):
					print(" > ",self.getSquare(tempC))
					return True
		return False

	def checkValid(self, c:Coord, to:Coord):
		if(c == to):
			return False
		team = self.getSquare(c).team
		enemy = 1 if team == 0 else 0
		oldRef = self.getSquare(to)
		oldPiece = Piece(oldRef.name, oldRef.team, oldRef.id, oldRef.timeMoved)
		self.movePiece(c, to)
		if(self.getSquare(to).name == "king" or self.getSquare(c).name == "king"):
			self.updateKingPos()
		
		out = self.kingInCheck(enemy)
		
		self.movePiece(to, c)
		self.setSquare(to, oldPiece)
		# if(out == True):
			# self.debugPrint()
		return out
	
	# def checkValid(self, c:Coord, to:Coord):
	# 	if(c == to):
	# 		return False
	# 	team = self.getSquare(c).team
	# 	enemy = 1 if team == 0 else 0
	# 	oldRef = self.getSquare(to)
	# 	oldPiece = Piece(oldRef.name, oldRef.team, oldRef.id, oldRef.timeMoved)
	# 	self.movePiece(c, to)
	# 	if(self.getSquare(to).name == "king" or self.getSquare(c).name == "king"):
	# 		self.updateKingPos()
		
	# 	out = True
	# 	for tempC in [Coord(x,y) for x in range(8) for y in range(8)]:
	# 		if(self.getSquare(tempC).team == enemy):
	# 			if(self.kings[team] in self.getPossibleMoves(tempC)):
	# 				out = False
	# 				break
	# 	self.movePiece(to, c)
	# 	self.setSquare(to, oldPiece)
	# 	# if(out == True):
	# 		# self.debugPrint()
	# 	return out
	
	
	def isCheckMate(self, team):
		for tempC in [Coord(x,y) for x in range(8) for y in range(8)]:
			if(self.getSquare(tempC).team == team):
				if(len(self.getValidMoves(tempC))>0):
					print(self.getSquare(tempC))
					print(tempC,"can move to",[str(v) for v in self.getValidMoves(tempC)])
					return False
		return True
	

	def getValidMoves(self, c:Coord):
		possible = self.getPossibleMoves(c)
		# print([str(x) for x in possible])
		out = []
		for move in possible:
			# print("Move:",move)
			if(self.checkValid(c, move)):
				# self.debugPrint()
				out.append(move)
		return out

	def movePiece(self, fromC:Coord, toC:Coord):
		# print("Moving from:",fromC)
		# print("Moving to  :",toC)
		if self.getSquare(fromC).name == "king":
			self.updateKingPos()
		elif self.getSquare(toC).name == "king":
			self.updateKingPos()
		self.setSquare(toC, self.getSquare(fromC))
		self.setSquare(fromC, Piece())

	def getSquare(self, c:Coord):
		if(c.isValid() == False):
			raise Exception("Invalid get, out of bounds: Tried to get at "+str(c))
		return self.board[c.y][c.x]
	
	def setSquare(self, c:Coord, p:Piece):
		if(c.isValid() == False):
			raise Exception("Invalid set, out of bounds: Tried to get at "+str(c))
		self.board[c.y][c.x] = Piece(p.name, p.team, p.id, p.timeMoved)

	def debugPrint(self):
		for row in self.board:
			for val in row:
				if(val.team!=-1):
					print(val.name[0],end="")
				else:
					print(" ",end="")
			print()
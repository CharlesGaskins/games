# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 11:44:30 2019

@author: Charles
"""

#this is to make an automated game of tictactoe that a person can play against
#their computer

#name spaces of board

import random

#spaces = ['top-L', 'top-M', 'top-R',
#          'mid-L', 'mid-M', 'mid-R',
#          'low-L', 'low-M', 'low-R']
##
###assign 
#board = {spaces[0]: ' ', spaces[1]: ' ', spaces[3]: ' ',
#            spaces[3]: ' ', spaces[4]: ' ', spaces[5]: ' ',
#            spaces[6]: ' ', spaces[7]: ' ', spaces[8]: ' '}
#board layout
def printBoard(board):
# "board" is a list of 10 strings representing the board (ignore index 0)
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')

#user picking which letter they want to be
def inputLetterChoice():
    letter = ''
    while not (letter == 'X' or letter == 'O'):
        print('first pick X or 0')
        letter = input().upper()
        
#computer is the letter the user doesn't choose
    if letter == 'X':
        return ['X', 'O']
    else:
        return ['0', 'X']
    
#random pick of who goes first
def goesFirst():
    if random.randint(0,1) == 0:
        return 'computer'
    else:
        return 'player'
    
#allows player to make a move
def makeMove(board, letter, move):
    board[move] = letter 

#winning combos   
def winningMoves(board, letter):
    return (
    (board[7] == letter and board[8] == letter and board[9] == letter) or 
    (board[4] == letter and board[5] == letter and board[6] == letter) or 
    (board[1] == letter and board[2] == letter and board[3] == letter) or 
    (board[7] == letter and board[4] == letter and board[1] == letter) or 
    (board[8] == letter and board[5] == letter and board[2] == letter) or 
    (board[9] == letter and board[6] == letter and board[3] == letter) or 
    (board[7] == letter and board[5] == letter and board[3] == letter) or 
    (board[9] == letter and board[5] == letter and board[1] == letter)) 

#make copy of board
def getBoardCopy(board):
    dupeBoard = []
    
    for b in board:
        dupeBoard.append(b)
    return dupeBoard
    

#returns as TRUE if space is available
def freeSpace(board, move):
    return board[move] == ' '

#let player choose their move
def playerMove(board):
    move = ' ' 
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not freeSpace(board, int(move)):
        print("What's your move big shot? (1-9)")
        move = input()
    return int(move)

#makes sure move is valid or not
def chooseMoveFromList(board, movesList):
    possibleMoves = []
    for i in movesList:
        if freeSpace(board, i):
            possibleMoves.append(i)
    if len(possibleMoves) != 0:
            return random.choice(possibleMoves)
    else:
            return None
        
#computer's moves
def computerMove(board, computerLetter):
    if computerLetter == 'X':
        playerLetter = 'O'
    else:
        playerLetter = 'X'
        
#AI algorythm
    for c in range(1,10):
        copy = getBoardCopy(board)
        if freeSpace(copy, c):
            makeMove(copy, computerLetter, c)
            if winningMoves(copy, computerLetter):
                return c
     #if possible, block move       
    for c in range(1,10):
        copy = getBoardCopy(board)
        if freeSpace(copy, c):
            makeMove(copy, playerLetter, c)
            if winningMoves(copy, playerLetter):
                return c
            
    #going for the corners
    move = chooseMoveFromList(board, [1,3,7,9])
    if move != None:
        return move
    
    #go for the center
    if freeSpace(board, 5):
        return 5
    
    #make a move on the sides
    return chooseMoveFromList(board, [2,4,6,8])

#if board is full
def noMovesLeft(board):
    for i in range(1,10):
        if freeSpace(board, i):
            return False
        return True
    
def playAgain():
    print('Do you want another piece of this? (yes/no)')
    return input().lower().startswith('y')

    
print('WELCOME TO HELL!!!')



while True:
    theBoard = [' '] * 10
    playerLetter, computerLetter = inputLetterChoice()
    turn =goesFirst()
    print(turn + ' will go first.')
    gameIsPlaying = True
    
    while gameIsPlaying:
        if turn == 'player':
            printBoard(theBoard)
            move = playerMove(theBoard)
            makeMove(theBoard, playerLetter, move)
        
            if winningMoves(theBoard, playerLetter):
                printBoard(theBoard)
                print('Way to go nerd!')
                gameIsPlaying = False
            
            else:
                if noMovesLeft(theBoard):
                    printBoard(theBoard)
                    print('Tie')
                    break
                else:
                    turn = 'compter'
                
        else:
            move = computerMove(theBoard, computerLetter)
            makeMove(theBoard, computerLetter, move)
            
            if winningMoves(theBoard, computerLetter):
                printBoard(theBoard)
                print('You lost like a bitch')
                gameIsPlaying = False
                break
            else:
                if noMovesLeft(theBoard):
                    printBoard(theBoard)
                    print('Tie')
                    break
                else:
                    turn = 'player'
                
    if not playAgain():
        break
                
                
            
        
        
        
        


    



    
    

    

        
    
        
    
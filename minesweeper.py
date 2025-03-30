# complete matrix, with bombs and numbers
# empty matrix
# revealing matrix
# check bomb function, empty matrix function, reveal matrix function

# problems: 

import random
import numpy as np
import copy
NUM_BOMBS=10

def main():
    print("Minesweeper\n")
    global NUM_BOMBS
    bombs=0
    #sept="|"
    grid_game=[]
    mod_grid=[]
    for _ in range(1, 11):
        grid_game.append([0 for _ in range(1, 11)])  
        mod_grid.append([" " for _ in range(1, 11)])    
    #print(np.matrix(grid_game))
    #print()    
    while bombs < NUM_BOMBS:
        bombs+=1
        bomb_row=random.randint(0, 9)
        bomb_col=random.randint(0, 9)
        grid_game[bomb_row][bomb_col] = "*"
    print(np.matrix(mod_grid))  
    list_reveal=[]
    fin_grid=copy.deepcopy(mod_grid) 
    game(mod_grid, grid_game, list_reveal)      
    while not(nested_lists_equal(mod_grid, full_grid(grid_game, None, fin_grid, list_reveal))):
        game(mod_grid, grid_game, list_reveal)      
    else:
        print("You win!")
        exit()    
    #print(f"{i}, {sept}, ")       

def nested_lists_equal(list1, list2):
    return np.all(list1 == list2)
            
def game(mod_grid, grid_game, list_reveal):
    while True:
        inp=input("Pick a row, col (row/col): ")
        if all(c==" " for c in inp):
            continue
        if inp[0].isdigit() and int(inp[0]) in range(10) and inp[1] =="/" and inp[2].isdigit() and int(inp[2]) in range(10):
            global row, col
            row=int(inp[0])
            col=int(inp[2])
            break
        else:
            continue    
    check_bomb(row, col, mod_grid, grid_game, list_reveal)

def check_bomb(row, col, mod_grid, grid_game, list_reveal):
      if grid_game[row][col]=="*":
          print("You lose")
          print(full_grid(grid_game, mod_grid, None, list_reveal))
          exit()
      elif grid_game[row][col]==0:
          reveal(grid_game, mod_grid, row, col, list_reveal)
          print("y")
          print(np.matrix(mod_grid))
      else:
          print("Already taken!")
          game()                                                              

def reveal(grid_game, mod_grid, r, c, list_reveal):      
    if [r, c] in list_reveal:
        return
    if grid_game[r][c]=="*":
        mod_grid[r][c] = "*"
        if r != 0 and c != 0:
            if grid_game[r-1][c-1] !="*":
                grid_game[r-1][c-1] +=1
                mod_grid[r-1][c-1] = grid_game[r-1][c-1]        
        if r != 0:    
            if grid_game[r-1][c] !="*":
                grid_game[r-1][c] +=1       
                mod_grid[r-1][c] = grid_game[r-1][c]                              
        if r != 0 and c != 9:    
            if grid_game[r-1][c+1] !="*":
                grid_game[r-1][c+1] +=1         
                mod_grid[r-1][c+1] = grid_game[r-1][c+1]
        if c != 0:    
            if grid_game[r][c-1] !="*":
                grid_game[r][c-1] +=1           
                mod_grid[r][c-1] = grid_game[r][c-1]
        if c != 9:    =
            if grid_game[r][c+1] !="*":
                grid_game[r][c+1] +=1    
                mod_grid[r][c+1] = grid_game[r][c+1]     
        if r != 9 and c != 0:    
            if grid_game[r+1][c-1] !="*":
                grid_game[r+1][c-1] +=1       
                mod_grid[r+1][c-1] = grid_game[r+1][c-1]    
        if r != 9:    
            if grid_game[r+1][c] !="*":
                grid_game[r+1][c] +=1      
                mod_grid[r+1][c] = grid_game[r+1][c]
        if r != 9 and c != 9:
            if grid_game[r+1][c+1] !="*":
                grid_game[r+1][c+1] +=1         
                mod_grid[r+1][c+1] = grid_game[r+1][c+1]    
    
    if grid_game[r][c]==0:
        if r != 0 and c != 0:
            if grid_game[r-1][c-1] =="*":
                grid_game[r][c] +=1
        if r != 0:    
            if grid_game[r-1][c] =="*":
                grid_game[r][c] +=1
        if r != 0 and c != 9:                                         
            if grid_game[r-1][c+1] =="*":
                grid_game[r][c] +=1
        if c != 0:             
            if grid_game[r][c-1] =="*":
                grid_game[r][c] +=1
        if c != 9:               
            if grid_game[r][c+1] =="*":
                grid_game[r][c] +=1
        if r != 9 and c != 0:             
            if grid_game[r+1][c-1] =="*":
                grid_game[r][c] +=1  
        if r != 9:             
            if grid_game[r+1][c] =="*":
                grid_game[r][c] +=1
        if r != 9 and c != 9:          
            if grid_game[r+1][c+1] =="*":
                grid_game[r][c] +=1               
    mod_grid[r][c]=grid_game[r][c]
    #print(grid_game[r][c], r, c)
    list_reveal.append([r, c])   
                                                                                                                                                                                                 
    if grid_game[r][c]==0:
        if r !=9:
           reveal(grid_game, mod_grid, r+1, c, list_reveal)
        if r != 0:                                                                                                                            
           reveal(grid_game, mod_grid, r-1, c, list_reveal)                  
        if c !=9:
           reveal(grid_game, mod_grid, r, c+1, list_reveal)                                                  
        if c !=0:
           reveal(grid_game, mod_grid, r, c-1, list_reveal)            
        if r !=0 and c !=0:
           reveal(grid_game, mod_grid, r-1, c-1, list_reveal)   
        if r !=0 and c !=9:
           reveal(grid_game, mod_grid, r-1, c+1, list_reveal)                                                                                                                                                                                   
        if r !=9 and c !=0:
           reveal(grid_game, mod_grid, r+1, c-1, list_reveal)  
        if r !=9 and c != 9:
           reveal(grid_game, mod_grid, r+1, c+1, list_reveal)                                                                                                                                                                                             
                                                                                                                                                                                                                                                                                                             
def full_grid(grid_game, mod_grid, fin_grid, list_reveal):
    global row, col, NUM_BOMBS
    for r in range(len(grid_game)):
          for c in range(len(grid_game[r])):
               if grid_game[r][c]=="*":
                   NUM_BOMBS -=1
                   if mod_grid== None:
                       reveal(grid_game, fin_grid, row, col, list_reveal)
                       fin_grid[r][c]=" "
                       continue
                   elif fin_grid == None:
                       reveal(grid_game, mod_grid, row, col, list_reveal)
                       continue        
          if NUM_BOMBS==0:
                    break                     
    if mod_grid == None:
        return np.matrix(fin_grid)  
    elif fin_grid == None:
        return np.matrix(mod_grid)                                 
main()      
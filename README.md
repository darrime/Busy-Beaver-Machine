# Busy Beaver machine

## A python code for simulating busy beaver game

### Input

- Input data following markdown table format

  |     | A   | B   | C   |
  | --- | --- | --- | --- |
  | 0   | 1RB | 0RC | 1LC |
  | 1   | 1RH | 1RB | 1LA |

### Output

- Output result is saved in .txt file  
   1 : [(0)]  
   2 : [1 (0)]  
   3 : [1 0 (0)]  
   4 : [1 (0) 1]  
   5 : [(1) 1 1]  
   6 : [(0) 1 1 1]  
   7 : [1 (1) 1 1]  
   8 : [1 1 (1) 1]  
   9 : [1 1 1 (1)]  
   10 : [1 1 1 1 (0)]  
   11 : [1 1 1 1 0 (0)]  
   12 : [1 1 1 1 (0) 1]  
   13 : [1 1 1 (1) 1 1]  
   14 : [1 1 (1) 1 1 1]

Additionally, main.c file is a same busy beaver machine that [written by prof. Brailsford](http://www.eprg.org/computerphile/busy-beaver.c).  
(But exactly, it works in different way than my code.)

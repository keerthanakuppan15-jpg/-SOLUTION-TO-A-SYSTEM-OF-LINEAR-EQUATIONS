# -SOLUTION-TO-A-SYSTEM-OF-LINEAR-EQUATIONS
## Aim:
To write a python program to find a solution to a system of linear equations.
## Equipment’s required:
1. 	Hardware – PCs
2. 	Anaconda – Python 3.7 Installation / Moodle-Code Runner
## Algorithm:
### Step 1: 
Import the numpy module to use the built-in functions for calculation
### Step 2: 
Prepare the lists from each linear equations and assign in np.array()
### Step 3: 
Using the np.linalg.solve(), we can find the solutions.
### Step 4: 
End the program
## Program:
```
#Program to find the solution for the given linear equations.
#Developed by:keerthana k
#RegisterNumber:212225230137
import numpy as np

matrixA= np.array([[1,-3],[3,1]])

B= np.array([0,10])
result= np.linalg.solve(matrixA,B)

print(result)
```

## Output:
<img width="1300" height="595" alt="image" src="https://github.com/user-attachments/assets/0f585e5b-f3f4-466e-aff4-b154fe90a107" />

## Result: 
Thus the solutions for the linear equations are successfully solved using python program


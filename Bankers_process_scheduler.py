# Banker's Algorithm
import numpy as np

# main variables 
n = 5 # Number of processes
m = 4 # Number of resources
file = "inp3.txt"

# Takes input form text files
def input_from_file(file):
    with open(file) as f:
        data = f.readlines()
        full_data = []
        
        # changes the input to a list of lists of ints 
        for i in range(len(data)):
            full_data.append(list(map(int, data[i].split())))
          
        # creating Matrix
        claim = [[],[],[],[],[]]
        allocation = [[],[],[],[],[]]
        available = []

        # seprates the input into the claim matrix, allocation matrix, and available resources by the blank lists
        for i in range(len(full_data)):
            if i == 0:
                claim[i] = full_data[i]
            elif i == 1:
                claim[i] = full_data[i]
            elif i == 2:
                claim[i] = full_data[i]
            elif i == 3:
                claim[i] = full_data[i]
            elif i == 4:
                claim[i] = full_data[i]
            elif i == 6:
                allocation[0] = full_data[i]
            elif i == 7:
                allocation[1] = full_data[i]
            elif i == 8:
                allocation[2] = full_data[i]
            elif i == 9:
                allocation[3] = full_data[i]
            elif i == 10:
                allocation[4] = full_data[i]
            elif i == 12:
                available = full_data[i]

    # converting from lists of lists to arrays
    Claim = np.array(claim)
    Allocation = np.array(allocation)
    Available = np.array(available)
    av = np.array(available)
    return Claim, Allocation, Available, av


# Banker's Algorithm
"""
    Takes in Claim Matrix, Allocation Matrix, Available Resources, av and returns Safe Sequence if it exists
"""
def bankers(Claim, Allocation, Available, av):

    # setup 
    Final = [0]*n
    ans = [0]*n
    ind = 0
    
    for k in range(n):
        Final[k] = 0
    
    Need = [[ 0 for i in range(m)]for i in range(n)]
    for i in range(n):
        for j in range(m):
            Need[i][j] = Claim[i][j] - Allocation[i][j]

    # Banker's Algorithm
    y = 0
    for k in range(5):
        for i in range(n):
            if (Final[i] == 0):
                flag = 0
                for j in range(m):
                    if (Need[i][j] > Available[j]):
                        flag = 1
                        break
                     
                if (flag == 0):
                    ans[ind] = i
                    ind += 1
                    for y in range(m):
                        Available[y] += Allocation[i][y]
                    Final[i] = 1

    # printing Run Sequence  
    z = 0
    for i in ans:
        print("Available    " + str(av[0]) + "    " + str(av[1]) + "    " + str(av[2]) + "    " + str(av[3]))
        print("P" + str(i) + " runs      " + str(Allocation[i][0]) + "    " + str(Allocation[i][1]) + "    " + str(Allocation[i][2]) + "    " + str(Allocation[i][3]))
        for z in range(m):
            av[z] += Allocation[i][z]
        
    for i in range(n):
        if (Final[i] == 0):
            return "Not Safe :("

    seq = "Yes, the initial state is a safe state. Safe sequence is: "   
    #print(len(ans)) 
    for i in range(n):
        seq += "P"
        seq += str(ans[i])
        if i != n-1:
            seq += ", "
        else:
            seq += "."
    return seq

# print Matrix
def printMatrix(Claim, Allocation, Available):
    
    need = np.subtract(Claim, Allocation)


    print("Showing input from file: " + file)
    print("Claim                       Allocation                  C - A")
    print("")
    print("    A    B    C    D           A    B    C    D            A    B    C    D")
    print("P0  " + str(Claim[0][0]) + "    " + str(Claim[0][1]) + "    " + str(Claim[0][2]) + "    " + str(Claim[0][3]) + "       P0  " + str(Allocation[0][0]) + "    " + str(Allocation[0][1]) + "    " + str(Allocation[0][2]) + "    " + str(Allocation[0][3]) + "        P0  " + str(need[0][0]) + "    " + str(need[0][1]) + "    " + str(need[0][2]) + "    " + str(need[0][3]))
    print("P1  " + str(Claim[1][0]) + "    " + str(Claim[1][1]) + "    " + str(Claim[1][2]) + "    " + str(Claim[1][3]) + "       P1  " + str(Allocation[1][0]) + "    " + str(Allocation[1][1]) + "    " + str(Allocation[1][2]) + "    " + str(Allocation[1][3]) + "        P1  " + str(need[1][0]) + "    " + str(need[1][1]) + "    " + str(need[1][2]) + "    " + str(need[1][3]))
    print("P2  " + str(Claim[2][0]) + "    " + str(Claim[2][1]) + "    " + str(Claim[2][2]) + "    " + str(Claim[2][3]) + "       P2  " + str(Allocation[2][0]) + "    " + str(Allocation[2][1]) + "    " + str(Allocation[2][2]) + "    " + str(Allocation[2][3]) + "        P2  " + str(need[2][0]) + "    " + str(need[2][1]) + "    " + str(need[2][2]) + "    " + str(need[2][3]))
    print("P3  " + str(Claim[3][0]) + "    " + str(Claim[3][1]) + "    " + str(Claim[3][2]) + "    " + str(Claim[3][3]) + "       P3  " + str(Allocation[3][0]) + "    " + str(Allocation[3][1]) + "    " + str(Allocation[3][2]) + "    " + str(Allocation[3][3]) + "        P3  " + str(need[3][0]) + "    " + str(need[3][1]) + "    " + str(need[3][2]) + "    " + str(need[3][3]))
    print("P4  " + str(Claim[4][0]) + "    " + str(Claim[4][1]) + "    " + str(Claim[4][2]) + "    " + str(Claim[4][3]) + "       P4  " + str(Allocation[4][0]) + "    " + str(Allocation[4][1]) + "    " + str(Allocation[4][2]) + "    " + str(Allocation[4][3]) + "        P4  " + str(need[4][0]) + "    " + str(need[4][1]) + "    " + str(need[4][2]) + "    " + str(need[4][3]))

    print("")
    print("Available")
    print("A    B    C    D")
    print("" + str(Available[0]) + "    " + str(Available[1]) + "    " + str(Available[2]) + "    " + str(Available[3]))
    print("")


# Main
def main():
    
    # get Claim, Allocation, and Available from file
    matrix = input_from_file(file)

    # printMatrix(matrix[0], matrix[1], matrix[2])
    printMatrix(matrix[0], matrix[1], matrix[2])
    
    # pass in the matrix to the bankers algorithm then print the output
    print(bankers(matrix[0], matrix[1], matrix[2], matrix[3]))
    
if __name__ == "__main__":
  main()
  

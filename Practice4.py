print("Hello April ready for the marathon")

names =  ['Ashish','Gagan',None,'Vidya']

for name in names:
    if name is None:
        print("Found a missing name")
        break
else:
    print("All names are available")


# 1. Find the Runner-Up Score!Task: Given a list of scores, find the 
# second-highest score. You must handle 
# duplicate values, as the highest score may appear more than once.
# Logic: Use a set to remove duplicates, then sort the remaining unique values.python

def get_runner_up(arr):
    # set() removes duplicates; sorted() returns a new sorted list
    unique_scores = sorted(list(set(arr)))
    # Index -2 gets the second to last element (the runner-up)
    return unique_scores[-2]

# Example usage
scores = [2, 3, 6, 6,3,5,8,7]
print(get_runner_up(scores)) 

def get_third_winner(arr):
    unique_score = sorted(list(set(arr)))
    return unique_score[-3]

score =[100,103,88,29,100]
print(get_third_winner(score))



# 2. List ComprehensionsTask: Generate a list of all possible coordinates \
# ((i, j, k)\) on a 3D grid where the sum \(i + j + k\) is not equal to a 
# target \(n\).Logic: Use a single-line nested loop to filter data, a common 
# pattern for cleaning datasets.

def filter_coordinates(x, y, z, n):
    # Generates [i, j, k] such that i+j+k != n
    return [[i, j, k] for i in range(x + 1) 
                      for j in range(y + 1) 
                      for k in range(z + 1) 
                      if (i + j + k) != n]

# Example: Grid up to 1,1,1 where sum is not 2
print(filter_coordinates(1, 1, 1, 2))
# Output: [[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]

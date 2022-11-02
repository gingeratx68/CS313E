import math, sys
def towerOfHanoi(n, from_rod, to_rod, aux_rod1, aux_rod2, count):
    k=round(n-(math.sqrt(2*n+1))+1)
    if (n == 0):
        return
    if (n == 1):
        return
    else:
        towerOfHanoi((2*(n - k)-1), from_rod, aux_rod1, aux_rod2, to_rod, count+1)
        towerOfHanoi((2*(n - k)-1), aux_rod1, to_rod, from_rod, aux_rod2, count+1)
def num_moves (n):
    towerOfHanoi(n, 'A', 'D', 'B', 'C', 0)
def main():
  # read number of disks and print number of moves
    num_moves(3)

if __name__ == "__main__":
    main()

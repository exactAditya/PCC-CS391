// n queens problem solved using backtracking approach
#include <stdio.h>
#define N 4

// board[n] stores column and index represents rows as every row can only contain queen at one column only
int board[N];

void printQ(){
  for (int row = 0; row < N; row++){
    for (int col = 0; col < N; col++){
      if (col == board[row]) printf("Q");
      else printf("#");
    }
    printf("\n");
  }
  printf("\n");
}

// place queen at their board
void place_queen(int board[], int r){
  // base case: queen piece is placed in each row of board
  if (r == N){
    printQ();
  }
  else {// try placing in each column of row r
    for (int j = 0; j < N; j++){
      int legal = 1;
      // check if non attacking position
      for (int i = 0; i < r; i++){
        if (board[i] == j || board[i] == j+r-i || board[i] == j-r+i){
          legal = 0;
          break;
        }
      }
      if (legal){
        board[r] = j;
        // recursive case: when piece in row r is place then place in the next row
        place_queen(board, r+1);
      }
    }
  }
}
int main(){
  place_queen(board, 0);
  return 0;
}

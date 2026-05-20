// n queens problem solved using backtracking approach
#include <stdio.h>
#include <stdlib.h>
#define N 4

// board[n] stores column and index represents rows as every row can only contain queen at one column only
int board[N];

// check if queens if placed in same column or diagonals
// returns 1 when non attacking cell else 0
int is_safe(int current_row, int current_col, int board[]){
  // checking all the previous rows with current row if they have same column or diagonals
  for (int prev_row = 0; prev_row < current_row; prev_row++){
    // same column checking
    if (board[prev_row] == current_col) return 0;
    // same diagonals check
    if (abs(current_row-prev_row) == abs(current_col- board[prev_row])) return 0; 
  }
  return 1;
}

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
  // check placement for each column of row r
  for (int col = 0; col < N; col++){
    // if non attacking positon then place the queen
    if (is_safe(r, col, board)) {
      board[r] = col;
    // terminating case: row index == max no of rows
    if (r == N-1) {
      printQ();
    }
    else
      place_queen(board, r+1);
    }
  }
}

int main(){
  place_queen(board, 0);
  return 0;
}

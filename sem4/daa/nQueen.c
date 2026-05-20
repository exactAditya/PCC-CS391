// n queens problem solved using ... approach
#include <stdio.h>
#define N 8

// board[n] stores column and index represents rows as every row can only contain queen at one column only
int board[N];

// check if queens if placed in same column or diagonals
// returns 1 when non attacking cell else 0
int is_safe(int current_row, int current_col, int board[]){
  // checking all the previous rows with current row if they have same column or diagonals
  for (int prev_row = 0; prev_row < current_row; prev_row++){
    // same column checking
    if (board[prev_row] == board[current_row]) return 0;
    // same diagonals check
    if (abs(current_row-prev_row) == abs(current_col- board[prev_row])) return 0; 
  }
  return 1;
}

int 
int main(){
  return 0;
}

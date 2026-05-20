// n queens problem solved using ... approach
#include <stdio.h>
#define N 4

// board[n] stores column and index represents rows as every row can only contain queen at one column only
int board[N];

// check if queens if placed in same column or diagonals
// returns 1 when non attacking cell else 0
// int is_safe(int current_row, int current_col, int board[]){
//   // checking all the previous rows with current row if they have same column or diagonals
//   for (int prev_row = 0; prev_row < current_row; prev_row++){
//     // same column checking
//     if (board[prev_row] == board[current_row]) return 0;
//     // same diagonals check
//     if (abs(current_row-prev_row) == abs(current_col- board[prev_row])) return 0; 
//   }
//   return 1;
// }

void printQ(){
  for (int i = 0; i < N; i++){
    if (board[i] >= 0)
    printf("row %d col %d\n",i, board[i]);
  }
}
void clearBoard(int board[], int start, int end){
  for (int row = start; row < end; row++) board[row] = -1; 
}
// place queen at their board
void place_queen(int board[], int r){

  if (r == N){
    printQ();
  }
  else {
    for (int j = 0; j < N; j++){
      int legal = 1;
      for (int i = 0; i < r; i++){
        if (board[i] == j || board[i] == j+r-i || board[i] == j-r+i){
          legal = 0;
        }
      }
      if (legal){
        board[r] = j;
        place_queen(board, r+1);
      }
    }
  }
  // // go through each row of the board
  // for (int row = 0; row < N; row++){
  //   // try placing queen in each column
  //   for (int col = 0; col < N; col++){
  //     if (is_safe(row, col, board)){
  //       board[row] = col;
  //       break;
  //     }      
  //   }
  // }    
}
int main(){
  place_queen(board, 0);
  return 0;
}

#include <stdio.h>
#include <string.h>
#define MAX(x,y) ((x) > (y) ? (x) : (y))

int lcs(char* str, char* str2){
  int longest = 0;
  // 2d table for storing fuction calls results
  int dp[strlen(str)+1][strlen(str2)+1];
  memset(dp, 0, sizeof(dp));
  for (int i = 0; i < strlen(str)+1; i++){
    for (int j = 0; j < strlen(str2)+1; j++){
      if (i == 0 || j == 0)
        dp[i][j] = 0;
      else if (str[i] == str2[j])
        dp[i][j] = 1 + dp[i-1][j-1];
      else
        dp[i][j] = MAX(dp[i-1][j], dp[i][j-1]);
      longest = MAX(longest, dp[i][j]);
    }
  }
  return longest;
}

int main(){
  char* str = "money";
  char* str2 = "monkey";

  printf("Longest common subsequence length: %d ",lcs(str, str2));
  return 0;
}

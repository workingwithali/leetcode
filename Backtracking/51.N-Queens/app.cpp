#include <iostream>
#include <vector>
using namespace std;
class Solution{
    public:
        bool issafe(vector<string> &board, int row, int col, int n)
        {

            for (int j = 0; j < n; j++)
            {
                if (board[j][col] == 'Q')
                {
                    return false;
                }
            }
            for (int i = row, j = col; i >= 0 && j >= 0; i--, j--)
            {
                if (board[i][j] == 'Q')
                {
                    return false;
                }
            }
            for (int i = row - 1, j = col + 1; i >= 0 && j < n; i--, j++)
            {
                if (board[i][j] == 'Q')
                {
                    return false;
                }
            }
            return true;
        }
        void queen(vector<int> &board,int row,int n, vector<vector<int>> &ans){
            if (row== n){
                ans.push_back(board);
                return;
            }
            for (int j=0;j<n;j++){
                if(issafe(board,row,j,ans)){
                    board[row][j] = 'Q';
                    queen(board,row+1,n,ans);
                    board[row][j] = '.';

                }
            }
        }
            vector<vector<int>> solveNQueens(int n)
        {
            vector<int> board(n,string(n,'.'));
            vector<vector<int>>ans;
            return ans;
        }
}
int main(){
    return 0;
}
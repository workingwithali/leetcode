#include <iostream>
#include <vector>
using namespace std;
class Solution{
    public:
        void queen(vector<int> &board,int row,int n, vector<vector<int>> &ans){
            if (row== n){
                ans.push_back(board);
                return;
            }
            for (int j=0;j<n;j++){
                if(issafe(board,row,j,ans)){
                    board[row][j] = 'Q'
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
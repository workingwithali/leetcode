#include<iosrtream>
#include<vector>
using namespace std;
class Solution{
    public:
    int row col;
    boot helper(vector<vector<int>> board, string word, int r ,int c , int i){
        if (i== word.size()){
            return true;
        }
        if (r<0||c<0||r>=row||c>=col||board[r][c]!=word[i]||board[r][c]=='#'){
            return false;
        }
        board[r][c] = '#';
        bool res = helper(board, word, r - 1, c, i + 1) || helper(board, word, r + 1, c, i + 1) || helper(board, word, r , c-1, i + 1) || helper(board, word, r , c+1, i + 1) ;
        board[r][c] = word[i];
        return res;
    }
}
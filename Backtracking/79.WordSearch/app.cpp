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
    }
}
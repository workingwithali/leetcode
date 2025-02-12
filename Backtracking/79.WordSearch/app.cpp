#include<iostream>
#include<vector>
using namespace std;
class Solution{
    public:
    	int row;
		int col;
    	bool helper(vector<vector<string>> board, string word, int r ,int c , int i){
        	if (i== word.size()){
            	return true;
        	}
        	if (r<0||c<0||r>=row||c>=col||board[r][c] != word[i]||board[r][c]=='#'){
           		return false;
        	}
        	board[r][c] = '#';
        	bool res = helper(board, word, r - 1, c, i + 1) || helper(board, word, r + 1, c, i + 1) || helper(board, word, r , c-1, i + 1) || helper(board, word, r , c+1, i + 1) ;
        	board[r][c] = word[i];
        	return res;
    	}
    	bool exit(vector<vector<string>>board, string word){
        row = board.size();
        col = board[0].size();
        for(int r = 0 ;r<row; r++ ){
            for (int c = 0; c<col; c++){
                if( helper(board, word, r, c, 0)){
                    return true;
                }
            }
        }
        return false;
    }
};
int main(){
    Solution s;
    board = [ [ "A", "B", "C", "E" ], [ "S", "F", "C", "S" ], [ "A", "D", "E", "E" ] ];
    word = "ABCCED";
    cout<< s.exit(board, word);
    return 0;
}
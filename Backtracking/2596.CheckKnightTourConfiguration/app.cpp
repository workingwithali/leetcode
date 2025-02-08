#include<iostream>
#include<vector>
using namespace std;
class Solution{
    public:
        isvaild(vector<vector<int>>grid,int r, int c ,int n,int expval){
            if (r < 0|| c < 0|| r >=n || c>= || grid[r][c]!= expval){
                return false;
            }
            if (expval == n*n-1){
                return true;
            }
            bool ans2 = isvaild(grid, r - 1, c + 2, n, expval + 1);
            bool ans1 = isvaild(grid, r - 2, c + 1, n, expval + 1);
            bool ans3 = isvaild(grid, r + 1, c + 2, n, expval + 1);
            bool ans4 = isvaild(grid, r + 2, c - 1, n, expval + 1);
            bool ans5 = isvaild(grid, r + 2, c + 1, n, expval + 1);
            bool ans6 = isvaild(grid, r - 1, c - 2, n, expval + 1);
            bool ans7 = isvaild(grid, r + 1, c - 2, n, expval + 1);
            bool ans8 = isvaild(grid, r - 2, c - 1, n, expval + 1);
            return ans1 || ans2 || ans3 || ans4 || ans5 || ans6 || ans7 || ans8;
        }
        checkgrid(vector<vector<int>> grid){
            return isvaild(grid, 0 ,0 ,gird.size(),0);
        }

}


int main(){
    Solution s;
    vector<vector<int> grid = [ [ 0, 11, 16, 5, 20 ], [ 17, 4, 19, 10, 15 ], [ 12, 1, 8, 21, 6 ], [ 3, 18, 23, 14, 9 ], [ 24, 13, 2, 7, 22 ] ]
    s.checkgrid(grid);

    return 0;
}
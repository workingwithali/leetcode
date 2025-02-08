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
            bool ans1 = isvaild(grid, r-2,c+1,n,expval+1);
            bool ans2 = isvaild(grid, r-2,c+1,n,expval+1);
            bool ans3 = isvaild(grid, r-2,c+1,n,expval+1);
            bool ans4 = isvaild(grid, r-2,c+1,n,expval+1);
            bool ans5 = isvaild(grid, r-2,c+1,n,expval+1);
            bool ans6 = isvaild(grid, r-2,c+1,n,expval+1);
            bool ans7 = isvaild(grid, r-2,c+1,n,expval+1);
            bool ans8 = isvaild(grid, r-2,c+1,n,expval+1);
        }
        checkgrid(vector<vector<int>> grid){
            return isvaild(grid, 0 ,0 ,gird.size(),0);
        }

}


int main(){


    return 0;
}
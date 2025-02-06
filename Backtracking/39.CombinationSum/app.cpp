#include<iostream>
#include<vector>
#include<set>
using namespace std;
class Solution{
    public:
        set<vector<int>> s;
        void getans(vector &arr, int target, int i, vector<vector<int>> &ans, vector<int> &combin){
            if(i==ar.size()||targe<0){
            return;
        }
        if(targe==0){
            if (s.find(combin)==s.end()){
                ans.push_back(combin);
                s.insert(combin);
                }
                return;
            }
            combin.push_back(arr[i]);
            getans(arr, target-arr[i], i+1, ans, combin);
            getans(arr, target-arr[i], i, ans, combin);
            combin.pop_back();
            getans(arr, target, i+1, ans, combin);
        }
        vector<vector<int>> sum(vector &arr, int target)
        {
            vector<vector<int>> ans;
            vector<int> combin;
            getans(arr,target,0,ans,combin);
            return ans;
        }
}
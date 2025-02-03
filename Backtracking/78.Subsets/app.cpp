#include <iostream>
#include <vector>
using namespace std;
void subset(vector<int> &arr, vector<int> &ans,int i,vector<vector<int>>& allsubset){
    if (i== arr.size()){
        
        allsubset.push_back(ans);
        return;
    }
    ans.push_back(arr[i]);
    subset(arr,ans,i+1,allsubset);
    ans.pop_back();
    subset(arr,ans,i+1,allsubset);
}
void printSubsets(const vector<vector<int>>& allsubset) {
    for (const auto& subset : allsubset) {
        cout << "{ ";
        for (int num : subset) {
            cout << num << " ";
        }
        cout << "}\n";
    }
}

    int main()
{
    vector<vector<int>> allsubset;
    vector<int> arr = {1,2,3};
    vector<int> ans ;
    subset(arr,ans,0,allsubset);
    printSubsets(allsubset);

    return 0;
}
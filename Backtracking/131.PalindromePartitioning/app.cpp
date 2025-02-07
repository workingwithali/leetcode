#include<iostream>
#include<vector>
using namespace std;
class Solution{
    public:
    bool ispalin(stirng s){
        string s2 = s;
        reverse(s2.begin(),s2.end());
        return s2 == s;
    }
    void getpalin(string s, ector<string> &partitions, vector < vector<string> &ans){
        if(s.size()==0){
            ans.push_back(partitions)
            return;
        }
        for(int i = 0; i< s.size(); i++){
            sting part = s.substr(0,i+1);
            if (ispalin(part)){
                partitions.push_back(part);
                getpalin(s.substr(i+1),partitions,ans);
                partitions.pop_back();
            }
        }
    }
        vector<vector<string>> palindorme(string s)
    {
        vector<string> partitions;
        vector<vector<string> ans;
        getpalin(s,partitions,ans);
        return ans;
    }
}
int main(){

}
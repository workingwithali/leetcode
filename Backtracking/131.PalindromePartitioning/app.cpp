#include<iostream>
#include<vector>
using namespace std;
class Solution{
    public:
    bool ispalin(stirng s){
        string s2 = s;
        reverse(s2.begin(),s2.end());
    }
    vector<vector<string>> palindorme(string s){
        vector<string> partitions;
        vector<vector<string> ans;
        getpalin(s,partitions,ans);
        return ans;
    }
}
int main(){

}
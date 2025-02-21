#include<iostream>
#include<vector>
using namespace std;
class Solution{
	public:
		int element(vector<int>arr){
			int n=arr.size();
			for(int val:arr){
				int feq =0;
				for(int ele:arr){
					if(ele==val){
						feq++;
					}
				}
				if(feq>n/2)return val;
			}
		}
};
int main(){
	vector<int>arr ={2,2,1,1,1,2,2};
	Solution sol;
	int ans=sol.element(arr);
	cout<<ans;
	
}
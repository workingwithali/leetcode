#include <iostream>
#include <vector>
using namespace std;
class Solution{
	public:
		int search(vector<int>&arr,int tar,int s, int e){
			if (s <= e){
				int mid = (s+e)/2;
				if (arr[mid] == tar) return mid;
				else if (arr[mid]<tar){
					return search(arr , tar,mid+1,e);
				}else{
					return search(arr,tar,s,mid-1);
				}
			}
			return -1;
		}
};



int main(){
	vector<int> nums = {0,3,5,9,12};
	int target = 9;
	Solution s;
	cout <<s.search(nums,target,0,nums.size()-1);
	
	return 0;
}
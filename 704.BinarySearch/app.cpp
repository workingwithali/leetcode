#include <iostream>
#include <vector>
using namespace;
class Solution{
	public:
		int search(vector<int>arr,int tar,int s, int e){
			if (s <= e){
				int mid = (s+e)/2;
				if (arr[mid] == tar) return mid;
				else if (arr[mid]<tar){
					return search(arr , tar,mid+1,e);
				}else{
					return search(arr,tar,s,mid-1);
				}
				return -1;
			}
		}
};



int main(){
	
	return 0;
}
#include<iostream>
#include<vector>
using namespace std

class Solution{
public:
    vector<vector<int>> result;

    void backtrack(int current, int n, int k, vector<int> &combination)
    {
        // Base case: If we have picked k elements
        if (combination.size() == k)
        {
            result.push_back(combination);
            return;
        }

        // Base case: If current number exceeds n
        if (current > n)
            return;

        // Include current number
        combination.push_back(current);
        backtrack(current + 1, n, k, combination);

        // Exclude current number (backtrack)
        combination.pop_back();
        backtrack(current + 1, n, k, combination);
    }

    vector<vector<int>> combine(int n, int k)
    {
        vector<int> combination;
        backtrack(1, n, k, combination);
        return result;
    }
}













int main()
{
    int n, k;
    cout << "Enter n and k: ";
    cin >> n >> k;

    Solution sol;
    vector<vector<int>> combinations = sol.combine(n, k);

    cout << "Combinations:\n";
    for (auto &combo : combinations)
    {
        cout << "[ ";
        for (int num : combo)
            cout << num << " ";
        cout << "]\n";
    }

    return 0;
}
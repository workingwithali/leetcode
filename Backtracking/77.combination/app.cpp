#include<iostream>
#include<vector>
using namespace std















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
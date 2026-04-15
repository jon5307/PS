#include <iostream>
#include <unordered_set>
#include <string>
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(0);

    int n, m, c;
    cin >> n;
    unordered_set<int> set;
    for (int i = 0; i < n; i++)
    {
        cin >> c;
        set.insert(c);
    }
    cin >> m;
    string result;
    for (int i = 0; i < m; i++)
    {
        cin >> c;
        if (set.find(c) != set.end())
            result += "1 ";
        else
            result += "0 ";
    }
    cout << result;
    return 0;
}

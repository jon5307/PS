#include <iostream>
#include <set>
using namespace std;

struct Descending
{
    bool operator()(const string &a, const string &b) const
    {
        return a > b;
    }
};

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    int n;
    string name, status;
    set<string, Descending> people;
    cin >> n;
    for (int i = 0; i < n; i++)
    {
        cin >> name >> status;
        if (status.compare("enter") == 0)
        {
            people.insert(name);
        }
        else
        {
            people.erase(name);
        }
    }
    for (const string &n : people)
    {
        cout << n << "\n";
    }
    return 0;
}

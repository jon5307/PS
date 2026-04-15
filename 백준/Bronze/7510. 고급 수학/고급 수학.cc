#include <iostream>
#include <algorithm>
using namespace std;

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int n;
    cin >> n;

    for (int i = 1; i <= n; i++)
    {
        int a, b, c;
        cin >> a >> b >> c;
        int sides[3] = {a, b, c};
        sort(sides, sides + 3);
        cout << "Scenario #" << i << ":\n";
        if (sides[0] * sides[0] + sides[1] * sides[1] == sides[2] * sides[2])
        {
            cout << "yes\n";
        }
        else
        {
            cout << "no\n";
        }
        if (i != n)
        {
            cout << "\n";
        }
    }

    return 0;
}

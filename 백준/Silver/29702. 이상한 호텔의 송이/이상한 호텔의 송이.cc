#include <iostream>
#include <iomanip>
#include <cmath>
using namespace std;

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    int t, floor;
    unsigned long long n, room;
    cin >> t;
    for (int i = 0; i < t; i++)
    {
        cin >> n;
        floor = log2(n) + 1;
        room = n - (1ULL << (floor - 1));
        while (floor > 0)
        {
            cout << floor << setw(18) << setfill('0') << room + 1 << "\n";
            room /= 2;
            floor--;
        }
    }
    return 0;
}

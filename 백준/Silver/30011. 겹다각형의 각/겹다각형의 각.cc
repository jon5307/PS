#include <iostream>
using namespace std;

int main()
{
    int n, i;
    long long score;
    cin >> n;
    int an[n];
    for (i = 0; i < n; i++)
        cin >> an[i];
    score = 180 * (an[0] - 2);
    for (i = 1; i < n; i++)
        score += 180 * an[i];
    cout << score << endl;
    return 0;
}

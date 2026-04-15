#include <iostream>
using namespace std;

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    string x,y;
    int a,b;
    cin >> x >> y;
    a = abs(x[0]-y[0]);
    b = abs(x[1]-y[1]);
    cout << min(a,b) << " "<< max(a,b) << "\n";
    return 0;
}

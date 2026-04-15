#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    string s;
    cin >> s;
    vector<int> num(10);
    int sixnine = 0;
    for (char c : s) {
        if (c == '6' || c == '9') {
            sixnine++;
        } else {
            num[c-'0']++;
        }
    }
    cout << max(*max_element(num.begin(),num.end()),(sixnine-1)/2+1);
    return 0;

}

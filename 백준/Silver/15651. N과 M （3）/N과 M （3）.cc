#include <iostream>
#include <vector>
using namespace std;

int n, m;

void gen_seq(int dept, vector<short> &arr)
{
    if (dept == m)
    {
        for (short num : arr)
        {
            cout << num << " ";
        }
        cout << "\n";
        return;
    }
    for (int i = 1; i <= n; i++)
    {
        arr[dept] = i;
        gen_seq(dept + 1, arr);
    }
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(0);

    cin >> n >> m;
    vector<short> arr(m);
    gen_seq(0, arr);
    return 0;
}

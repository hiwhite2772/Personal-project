#include <bits/stdc++.h>
using namespace std;
void solve()
{
    int m, n, p;
    cin >> m >> n >> p;

    vector<vector<int>> arr_a(m, vector<int>(n));
    for (int i = 0; i < m; i++)
    {
        for (int j = 0; j < n; j++)
        {
            cin >> arr_a[i][j];
        }
    }

    vector<vector<int>> arr_b(n, vector<int>(p));
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < p; j++)
        {
            cin >> arr_b[i][j];
        }
    }

    vector<vector<int>> arr_c(m, vector<int>(p));
    for (int i = 0; i < m; i++)
    {
        for (int j = 0; j < p; j++)
        {
            arr_c[i][j] = 0;
            for (int k = 0; k < n; k++) {
                arr_c[i][j] += arr_a[i][k] * arr_b[k][j];
            }
        }
    }

    for (int i = 0; i < m; i++)
    {
        for (int j = 0; j < p; j++) {
            cout << arr_c[i][j] << " ";
        }
        cout << "\n";
    }
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    solve();
    return 0;
}
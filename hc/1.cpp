#include <bits/stdc++.h>
using namespace std;
#define LL long long
#define vi vector<int>
#define srt(a) sort(a.begin(), a.end());
#define se second
#define fi first
#define pb push_back
#define all(x) (x).begin(), (x).end()
#define forn(i, n) for (int i = 0; i < (int)(n); ++i)
#define for1(i, n) for (int i = 1; i <= (int)(n); ++i)

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);
    cout.precision(10);
    cout << fixed;
    int t;
    cin >> t;
    for1(tt, t)
    {
        cout << "Case #" << tt << ": ";
        LL n, m;
        LL k, a, b;
        vector<pair<int, int>> pp;
        cin >> n >> m >> k;
        cin >> a >> b;
        forn(i, k)
        {
            int o, s;
            cin >> o >> s;
            pp.push_back(make_pair(o, s));
        }
        if (k == 1)
        {
            cout << "N\n";
            continue;
        }
        else
        {
            int a1 = abs(pp[0].fi - pp[1].fi) % 2;
            int a2 = abs(pp[0].se - pp[1].se) % 2;
            if (a1 != a2)
            {
                cout << "N\n";
                continue;
            }
            bool x = 1;
            int cc = 0;
            for (auto c : pp)
            {
                a1 = abs(c.fi - a);
                a2 = abs(c.se - b);
                if ((a1 == 1 && a2 == 0) || (a1 == 0 && a2 == 1))
                {
                    cc++;
                    continue;
                }
                a1 = abs(c.fi - a) % 2;
                a2 = abs(c.se - b) % 2;
                if ((a1 == 1 && a2 == 0) || (a1 == 0 && a2 == 1))
                {
                    cout << "N\n";
                    x = 0;
                    break;
                }
            }
            if (cc == 2)
            {
                cout << "N\n";
                continue;
            }
            if (x == 0)
                continue;
            cout << "Y\n";
        }
    }
    return 0;
}
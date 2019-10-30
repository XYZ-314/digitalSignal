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
int uf[500005];
int par(int x)
{
    return uf[x] < 0 ? x : uf[x] = par(uf[x]);
}
void join(int x, int y)
{
    x = par(x);
    y = par(y);
    if (x == y)
        return;
    if (uf[x] > uf[y])
    {
        swap(x, y);
    }
    uf[x] += uf[y];
    uf[y] = x;
}

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
        map<int, int> mm;
        cout << "Case #" << tt << ": ";
        int n, m;
        cin >> n >> m;
        forn(i, n)
        {
            uf[i] = -1;
        }
        forn(i, m)
        {
            int l, r;
            cin >> l >> r;
            l--, r--;
            while (l < r)
            {
                join(l, r);
                l++;
                r--;
            }
        }
        set<pair<LL, LL>> s;
        forn(i, n)
        {
            if (uf[i] < 0)
            {
                s.insert(make_pair(-1 * uf[i], i));
            }
        }
        vector<pair<LL, LL>> vv;
        for (auto i : s)
        {
            vv.pb(i);
        }
        int c0 = 0;
        cout << "\n*** ";
        int cl = 0, cr = vv.size() - 1;
        for (auto i : s)
        {
            cout << i.fi << " ";
            int a = abs(c0 + i.fi);
            int b = abs(c0 - i.fi);
            if (a > b)
            {
                c0 = c0 - i.fi;
                mm[i.se] = 0;
            }
            else
            {
                c0 = c0 + i.fi;
                mm[i.se] = 1;
            }
        }

        int cc0 = 0, cc1 = 0;
        forn(i, n)
        {
            cout << mm[par(i)];
            if (mm[par(i)] == 0)
                cc0++;
            else
                cc1++;
        }

        cout << endl;
        cout << "*** " << abs(cc0 - cc1) << endl;
    }
    return 0;
}
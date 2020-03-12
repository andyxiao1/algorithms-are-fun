#include <bits/stdc++.h>
using namespace std;
int main() {
    #ifndef ONLINE_JUDGE
    freopen("in", "r", stdin);
    freopen("out", "w", stdout);
    #endif
    long long n; cin >> n;
    long long a[n], b[n];
    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }
    for (int i = 0; i < n; i++) {
        cin >> b[i];
    }
    long long g[n];
    for (int i = 0; i < n; i++) {
        g[i] = a[i] - b[i];
    }
    long long cnt = 0;
    sort(g, g + n);
    for (int i = 1; i < n; i++) {
        // if greater than -g[i] then the pair is good
        // should only look left to avoid double counting
        if (g[i] > 0) {
            auto smallest = upper_bound(g, g + n, -1 * g[i]) - g;
            cnt += (long long) i - smallest;
        }
    }
    cout << cnt << "\n";
    return 0;
}
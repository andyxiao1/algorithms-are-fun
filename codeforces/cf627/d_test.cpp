#include <bits/stdc++.h>
using namespace std;
int main() {
    #ifndef ONLINE_JUDGE
    freopen("in", "r", stdin);
    freopen("out", "w", stdout);
    #endif
    int n; cin >> n;
    int a[n], b[n];
    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }
    for (int i = 0; i < n; i++) {
        cin >> b[i];
    }
    int g[n];
    for (int i = 0; i < n; i++) {
        g[i] = a[i] - b[i];
    }
    int cnt = 0;

    for (int i = 0; i < n; i++) {
        for (int j = i + 1; j < n; j++) {
            if (g[j] + g[i] > 0) {
                cnt++;
            }
        }
    }
    cout << cnt << "\n";
    return 0;
}
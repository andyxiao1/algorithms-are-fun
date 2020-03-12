#include <bits/stdc++.h>
using namespace std;
int main() {
    #ifndef ONLINE_JUDGE
    freopen("in", "r", stdin);
    freopen("out", "w", stdout);
    #endif
    int t; cin >> t;
    for (int p = 0; p < t; p++) {
        int n; cin >> n;
        int arr[n];
        for (int k = 0; k < n; k++) {
            cin >> arr[k];
        }

        unordered_map<int, int> m; // maps int to first time it appeared
        bool passed = true;
        // need to check if there are 2 equal nums more than 1 apart from each other

        for (int i = 0; i < n; i++) {
            if (m.count(arr[i])) {
                if (i - m[arr[i]] > 1) {
                    cout << "YES\n";
                    passed = false;
                    break;
                }
            } else {
                m[arr[i]] = i;
            }
        }
        if (passed) {
            cout << "NO\n";
        }
    }
    return 0;
}
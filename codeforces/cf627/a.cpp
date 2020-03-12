#include <bits/stdc++.h>
using namespace std;
int main() {
    #ifndef ONLINE_JUDGE
    freopen("in", "r", stdin);
    freopen("out", "w", stdout);
    #endif

    int t; cin >> t;
    for (int i = 0; i < t; i++) {
        int n; cin >> n;
        int arr[n];
        for (int k = 0; k < n; k++) {
            cin >> arr[k];
        }
        bool isEven = true;
        bool passed = true;
        if (arr[0] % 2 == 1) {
            isEven = false;
        }
        for (int k = 0; k < n; k++) {
            if ((arr[k] % 2 == 0) != isEven) {
                cout << "NO\n";
                passed = false;
                break;
            }
        }
        if (passed) {
            cout << "YES\n";
        }
    }
    return 0;
}
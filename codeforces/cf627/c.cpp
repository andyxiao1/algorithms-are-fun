#include <bits/stdc++.h>
using namespace std;
int main() {
    #ifndef ONLINE_JUDGE
    freopen("in", "r", stdin);
    freopen("out", "w", stdout);
    #endif
    int t; cin >> t;
    for (int p = 0; p < t; p++) {
        string s; cin >> s;
        // want to find max distance between r's
        s = "R" + s + "R";
        int i = 1, d = -1, curr = 0;
        while (i < s.length()) {
            curr++;
            if (s[i] == 'R') {
                d = max(d, curr);
                curr = 0;
            }
            i++;
        }
        if (d == -1) {
            cout << (s.length() - 1) << "\n";
        } else {
            cout << d << "\n";
        }
    }
    return 0;
}
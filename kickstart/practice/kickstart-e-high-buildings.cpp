#include <iostream>
using namespace std;

void solve() {
    int n, a, b, c;
    cin >> n; cin >> a; cin >> b; cin >> c;

    if (a + b - c > n || c > a || c > b || (a == 1 && b == 1 && n > 1)) {
        cout << "IMPOSSIBLE" << endl;
        return;
    }

    // increasing seq
    for (int i = n - a + c; i < n; i++) {
        cout << i << " ";
    }

    if (a == 1) {
        cout << n << " ";
        for (int i = 0; i < n - (a + b - c); i++) {
            cout << 1 << " ";
        }
    } else if (b == 1) {
        for (int i = 0; i < n - (a + b - c); i++) {
            cout << 1 << " ";
        }
        cout << n << " ";
    } else {
        for (int i = 0; i < c; i++) {
            if (i == c - 1) {
                for (int i = 0; i < n - (a + b - c); i++) {
                    cout << 1 << " ";
                }
            }
            cout << n << " ";
        }
    }
    
    // decreasing seq
    for (int i = n - 1; i > n - (b - c + 1); i--) {
        cout << i << " ";
    }
    cout << endl;
}

int main() {
    int t; cin >> t;
    for (int i = 1; i <= t; i++) {
        cout << "Case #" << i << ": ";
        solve();
    }
}
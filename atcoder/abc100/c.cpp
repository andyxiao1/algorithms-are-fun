#include <bits/stdc++.h>
using namespace std;
int main() {
    int x, n, cnt = 0;
    cin >> n;
    for (int i = 0; i < n; i++) {
        cin >> x;
        while (x % 2 == 0 && x > 1) {
            x /= 2;
            cnt++;
        }
    }
    cout << cnt << "\n";
    return 0;
}

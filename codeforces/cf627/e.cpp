#include <bits/stdc++.h>
using namespace std;
int main() {
    #ifndef ONLINE_JUDGE
    freopen("in", "r", stdin);
    freopen("out", "w", stdout);
    #endif
    int n, h, l, r;
    cin >> n >> h >> l >> r;
    int a[n];
    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }

    // dp approach
    // h * n matrix
    // rows = hours
    // col = day

    int dp[h][n];
    for (int i = 0; i < h; i++) {
        dp[i][n - 1] = (l <= i && i <= r) ? 1 : 0;
    }

    // dp[row][col] = if u were to sleep on the col^th day at row time
    for (int col = n - 2; col >= 0; col--) {
        for (int row = 0; row < h; row++) {
            dp[row][col] = (l <= row && row <= r) ? 1 : 0;
            dp[row][col] += max(dp[(row + a[col + 1]) % h][col + 1], dp[(row + a[col + 1] - 1) % h][col + 1]);
        }
    }
    cout << max(dp[a[0]][0], dp[a[0] - 1][0]);

    return 0;
}
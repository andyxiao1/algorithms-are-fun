#include <iostream>
using namespace std;

int main() {    
    int t; cin >> t;
    for (int i = 1; i <= t; i++) {
        int n; cin >> n;
        int arr[n];
        for (int j = 0; j < n; j++) {
            cin >> arr[j];
        }
        int diff[n - 1];
        for (int j = 0; j < n - 1; j++) {
            diff[j] = arr[j + 1] - arr[j];
        }
        int ans = 1;
        for (int j = 0, k = 0; j < n - 1; j = k) {
            for (k = j; k < n - 1 && diff[k] == diff[j]; k++) {
                ans = max(ans, k - j + 2);
            }
        }
        cout << "Case #" << i << ": " << ans << endl;
    }
}
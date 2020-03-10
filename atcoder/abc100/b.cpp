#include <bits/stdc++.h>
using namespace std;
int main() {
    int D, N;
    cin >> D >> N;
    int S = 1;
    for (int i = 0; i < D; i++) {
        S *= 100;
    }
    if (N < 100) {
        cout << N * S << "\n";
    } else {
        cout << 101 * S << "\n";
    }
    return 0;
}
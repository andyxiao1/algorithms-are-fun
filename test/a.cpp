#include <bits/stdc++.h>
using namespace std;
int main() {
    int x;
    vector<int> v;
    int a = 56;
    while (cin >> x) {
        v.push_back(x);
    }
    sort(v.rbegin(), v.rend());
    for (int i : v) {
        cout << i << "\n" << a;
    }
    return 0;
}

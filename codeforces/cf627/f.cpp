#include <bits/stdc++.h>
using namespace std;
int main() {
    #ifndef ONLINE_JUDGE
    freopen("in", "r", stdin);
    freopen("out", "w", stdout);
    #endif
    int n; cin >> n;
    int c[n], res[n];
    int u, v;
    vector<vector<int>> g(n);
    for (int i = 0; i < n; i++) {
        cin >> c[i];
    }
    for (int i = 0; i < n - 1; i++) {
        cin >> u >> v;
        u--; v--;
        g[u].push_back(v);
        g[v].push_back(u);
    }
    for (int vtx = 0; vtx < n; vtx++) {
        stack<int> s;
        s.push(vtx);
        bool seen[n];
        seen[vtx] = true;
        int diff = 0;
        while (!s.empty()) {
            int src = s.top();
            s.pop();
            diff += (c[src] == 1) ? 1 : -1;
            for (auto p : g[src]) {
                if (!seen[p]) {
                    s.push(g[src][p]);
                    seen[p] = true;
                }
            }
        }
        res[vtx] = diff;
    }
    for (int vtx = 0; vtx < n; vtx++) {
        int max_v = res[vtx];
        for (auto p : g[vtx]) {
            max_v = max(res[p], max_v);
        }
        cout << max_v << " ";
    }
    cout << "\n";
    return 0;
}
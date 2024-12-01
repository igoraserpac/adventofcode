#include <bits/stdc++.h>
using namespace std;

#define ll long long
#define FOR(i,m,n) for(int i = m; i < n; i++)
#define pv(x) for(auto i: x) cout << i << ' '; cout << endl;

int main(){
    vector<ll> v1, v2;
    map<ll,ll> m2;
    ll a, b;
    while(cin >> a >> b){
        v1.push_back(a);
        v2.push_back(b);
        m2[b]++;
    }
    ll total = 0;
    sort(v1.begin(), v1.end());
    sort(v2.begin(), v2.end());
    FOR(i,0,v1.size()){
        total += abs(v1[i] - v2[i]);
    }
    cout << "p1: " << total << endl;

    int conf = 0;
    for(auto i: v1){
        conf += i * m2[i];
    }
    cout << "p2: " << conf << endl;

    
    return 0;
}
#include <bits/stdc++.h>
using namespace std;
int main(void){
    int n, k;
    cin >> n >> k;
    vector<int> H(n);
    for(int i=0;i<n;i++) cin >> H[i];
    const int inf = 1e9;
    vector<int> dp(n+1, inf);
    dp[1] = 0;

    for(int i=1;i<=n;i++){
        for(int j=1;j<=k && i<n-j+1;j++){
            dp[i+j] = min(dp[i]+abs(H[i-1]-H[i+j-1]), dp[i+j]);
            // cout<<i<<j<<endl;
        }
    }

    cout << dp[n] << endl;
    return 0;
}
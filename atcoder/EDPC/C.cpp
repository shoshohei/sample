#include <bits/stdc++.h>
using namespace std;

int main(void){
    int n;
    cin >> n;
    vector<int> A(n), B(n), C(n);
    for(int i=0;i<n;i++) cin >> A[i] >> B[i] >> C[i];
    vector<vector<int>> dp(n, vector<int>(3,0));
    dp[0][0] = A[0];
    dp[0][1] = B[0];
    dp[0][2] = C[0];
    for(int i=1;i<n;i++){
        dp[i][0] = max(dp[i-1][1]+A[i], dp[i-1][2]+A[i]);
        dp[i][1] = max(dp[i-1][0]+B[i], dp[i-1][2]+B[i]);
        dp[i][2] = max(dp[i-1][0]+C[i], dp[i-1][1]+C[i]);
    }

    cout << max(dp[n-1][0], max(dp[n-1][1], dp[n-1][2])) << endl;
}
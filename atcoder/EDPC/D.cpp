#include <bits/stdc++.h>
#include <vector>
using namespace std;
int main(void){
    long long n, weight;
    cin >> n >> weight;
    vector<long long> W(n), V(n);
    for(int i=0;i<n;i++) cin >> W[i] >> V[i];
    vector<vector<long long>> dp(n, vector<long long>(weight+1, 0));

    for(int i=0;i<n;i++){
        for(int w=1;w<=weight;w++){
            if(i==0){
                dp[i][w] = (W[i]<=w) ? V[i]:0;
            }
            else{
                dp[i][w] = (W[i]>w) ? dp[i-1][w] : max(dp[i-1][w-W[i]]+V[i], dp[i-1][w]); 
            }
        }
    }
    long long total_max = 0;
    for(int i=0;i<dp.size();i++){
        long long val = 0;
        for(int j=0;j<dp[0].size();j++){
            val = max(val, dp[i][j]);
        }
        total_max = max(total_max, val);
    }
    cout << total_max << endl;
    return 0;
}
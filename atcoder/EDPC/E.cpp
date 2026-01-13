#include <bits/stdc++.h>
#include <vector>
using namespace std;
int main(void){
    long long n, weight;
    cin >> n >> weight;
    vector<long long> W(n), V(n);
    for(int i=0;i<n;i++) cin >> W[i] >> V[i];
    vector<vector<long long>> dp(n, vector<long long>(weight+1, 0));
    

}
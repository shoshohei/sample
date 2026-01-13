#include<bits/stdc++.h>
using namespace std;

int main(){
	int n,q;
	cin >> n >> q;
	deque<pair<int,int>>d;
	for(int i=1;i<=n;i++)d.push_back({i,0});

    for(int i=0;i<q;q++){
        int t;
        cin>>t;
        if (t==1){
            char c;
            cin>>c;
            auto[x,y]=d[0];
            if(c=='R')d.push_front({x+1, y});
            if(c=='L')d.push_front({x-1, y});
            if(c=='D')d.push_front({x, y-1});
            if(c=='U')d.push_front({x, y+1});
            d.pop_back();
        }
        else{
            int x ;
            cin>>x;
            x--;
            cout<<d[x].first<<' '<<d[x].second<<endl;
        }
    }
}
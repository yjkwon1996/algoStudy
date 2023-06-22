#include <string>
#include <vector>
#include <iostream>
#include <map>
#include <algorithm>

using namespace std;

// 무게별 개수 내림차순 정렬
bool comp(int &a, int &b) {
    return a>b;
}

// k개의 귤을 골라 상자 하나에 담는데, 크기별로 분류했을 때 서로 다른 종류의 수를 최소화하기

int solution(int k, vector<int> tangerine) {
    int answer = 0;
    vector<int> cnt(10000001);
    
    for (int i=0; i<tangerine.size(); i++) {
        cnt[tangerine[i]] += 1;
    }
    
    // for (int i=0; i<tangerine.size(); i++) {
    //     cout << i << " " << cnt[i] << endl;
    // }
    
    sort(cnt.begin(), cnt.end(), comp);
    
    int idx = 0;
    while (k>0) { // idx 무게가 cnt[idx]개만큼 있으므로, 빼서 쓰면 됨
        k -= cnt[idx];
        idx += 1;
        answer += 1;
    }
    
    return answer;
}
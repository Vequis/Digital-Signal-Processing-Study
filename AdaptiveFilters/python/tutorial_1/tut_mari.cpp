#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {

    vector<int> v;

    int x;
    while(cin >> x) {
        if (x == -1) break;
        v.push_back(x);
    }

    int k;
    cin >> k;
    
    sort(v.begin(), v.end());

    for (int i = 0; i < k; i++) {
        cout << v[i] << " ";
    }
    cout << endl;
}
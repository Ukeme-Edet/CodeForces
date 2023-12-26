#include <bits/stdc++.h>

int main()
{
	using namespace std;
	ios::sync_with_stdio(0);
	cin.tie(0);
	string s;
	cin >> s;
	set<char> st(s.begin(), s.end());
	st.size() % 2 ? cout << "IGNORE HIM!\n" : cout << "CHAT WITH HER!\n";
}

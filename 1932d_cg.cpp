/**
 * @file 1932d_cg.cpp
 * @author Ukeme Edet (ukemeedet2207@gmail.com)
 * @brief The solution to the problem Card Game(https://codeforces.com/contest/1932/problem/D)
 * @version 0.1
 * @date 2024-04-03
 *
 * @copyright Copyright (c) 2024
 *
 */

#include <bits/stdc++.h>

using namespace std;

/**
 * @brief The main function
 *
 * @return int
 */
int main(void)
{
	ios::sync_with_stdio(0);
	cin.tie(0);
	short t, n, non_trump_remainder_count, i;
	char trump_suit;
	vector<string> normal_deck, trump_cards;
	map<char, short> suit_count;
	string card;

	cin >> t;
next:
	while (t--)
	{
		cin >> n >> trump_suit;
		normal_deck.clear();
		trump_cards.clear();
		suit_count.clear();
		non_trump_remainder_count = 0;
		for (i = 0; i < n * 2; i++)
		{
			cin >> card;
			suit_count[card[1]]++;
			card[1] != trump_suit ? normal_deck.push_back(card) : trump_cards.push_back(card);
		}
		for (auto &suit : suit_count)
			non_trump_remainder_count += suit.first != trump_suit ? suit.second % 2 : 0;
		if (non_trump_remainder_count > suit_count[trump_suit])
		{
			cout << "IMPOSSIBLE\n";
			goto next;
		}
		sort(trump_cards.begin(), trump_cards.end());
		sort(normal_deck.begin(), normal_deck.end(), [](const string &a, const string &b)
			 { return a[1] < b[1] || (a[1] == b[1] && a[0] < b[0]); });
		for (i = 0; i < normal_deck.size();)
		{
			if (i < normal_deck.size() - 1 && normal_deck[i][1] == normal_deck[i + 1][1])
			{
				cout << normal_deck[i] << " " << normal_deck[i + 1] << '\n';
				i += 2;
			}
			else
			{
				cout << normal_deck[i] << " " << trump_cards.back() << '\n';
				trump_cards.pop_back();
				i++;
			}
		}
		for (i = 0; i < trump_cards.size(); i += 2)
			cout << trump_cards[i] << " " << trump_cards[i + 1] << '\n';
	}
	return (EXIT_SUCCESS);
}
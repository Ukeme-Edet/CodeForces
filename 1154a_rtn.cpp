/**
 * @file 1154a_rtn.cpp
 * @author Ukeme Edet (ukemeedet2207@gmail.com)
 * @brief This is the solution to codeforces problem 1154A
 * @version 0.1
 * @date 2024-01-29
 *
 * @copyright Copyright (c) 2024
 *
 */
#include <bits/stdc++.h>

using namespace std;

/**
 * @brief main function
 *
 * @return int
 */
int main(void)
{
	ios::sync_with_stdio(0);
	cin.tie(0);
	int board[4];

	cin >> board[0] >> board[1] >> board[2] >> board[3];
	sort(board, board + 4);
	cout << board[0] + board[1] - board[3] << " " << board[0] + board[2] - board[3] << " " << board[1] + board[2] - board[3] << '\n';
	return (EXIT_SUCCESS);
}

#include <iostream>
#include <vector>
#include <string>

using namespace std;

void displayBoard(const vector<vector<char>>& board) {
    for (const auto& row : board) {
        for (size_t i = 0; i < row.size(); ++i) {
            cout << " " << row[i];
            if (i < row.size() - 1) cout << " |";
        }
        cout << endl;
        if (&row != &board.back()) {
            for (size_t i = 0; i < row.size(); ++i) {
                cout << "---";
                if (i < row.size() - 1) cout << "+";
            }
            cout << endl;
        }
    }
    cout << endl;
}

bool checkWin(const vector<vector<char>>& board, char player, int winCondition) {
    int n = board.size();
    for (int i = 0; i < n; ++i) {
        int rowCount = 0, colCount = 0;
        for (int j = 0; j < n; ++j) {
            rowCount += (board[i][j] == player);
            colCount += (board[j][i] == player);
        }
        if (rowCount >= winCondition || colCount >= winCondition) return true;
    }
    for (int i = 0; i <= n - winCondition; ++i) {
        int mainDiag = 0, antiDiag = 0;
        for (int j = 0; j < winCondition; ++j) {
            mainDiag += (board[i + j][i + j] == player);
            antiDiag += (board[i + j][n - 1 - i - j] == player);
        }
        if (mainDiag == winCondition || antiDiag == winCondition) return true;
    }
    return false;
}

bool checkDraw(const vector<vector<char>>& board) {
    for (const auto& row : board) {
        for (char cell : row) {
            if (cell == ' ') return false;
        }
    }
    return true;
}

void playTicTacToe(int boardSize = 3, int winCondition = 3) {
    vector<vector<char>> board(boardSize, vector<char>(boardSize, ' '));
    char currentPlayer = 'X';
    int playerXWins = 0, playerOWins = 0, draws = 0;
    while (true) {
        displayBoard(board);
        cout << "Player " << currentPlayer << ", enter your move (row and column numbers, 1-" << boardSize << "): ";
        int row, col;
        cin >> row >> col;
        if (row < 1 || row > boardSize || col < 1 || col > boardSize || board[row - 1][col - 1] != ' ') {
            cout << "Invalid move. Try again." << endl;
            continue;
        }
        board[row - 1][col - 1] = currentPlayer;
        if (checkWin(board, currentPlayer, winCondition)) {
            displayBoard(board);
            cout << "Player " << currentPlayer << " wins!" << endl;
            if (currentPlayer == 'X') ++playerXWins;
            else ++playerOWins;
            break;
        } else if (checkDraw(board)) {
            displayBoard(board);
            cout << "The game is a draw!" << endl;
            ++draws;
            break;
        }
        currentPlayer = (currentPlayer == 'X') ? 'O' : 'X';
    }
    cout << "Current Stats: Player X Wins: " << playerXWins << ", Player O Wins: " << playerOWins << ", Draws: " << draws << endl;
    cout << "Play again? (y/n): ";
    char choice;
    cin >> choice;
    if (choice == 'y' || choice == 'Y') playTicTacToe(boardSize, winCondition);
}

int main() {
    cout << "Welcome to Enhanced Tic-Tac-Toe!" << endl;
    cout << "Enter the board size (default is 3): ";
    int boardSize;
    cin >> boardSize;
    if (boardSize < 3) boardSize = 3;
    cout << "Enter the win condition (default is 3 in a row): ";
    int winCondition;
    cin >> winCondition;
    if (winCondition < 3 || winCondition > boardSize) winCondition = 3;
    playTicTacToe(boardSize, winCondition);
    return 0;
}


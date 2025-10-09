# 🎮 Tic-Tac-Toe Game in Python

This is a **two-player Tic-Tac-Toe game** built in Python.

## Overview
- Two players take turns — one plays as **“X”**, the other as **“O”**.  
- They place their marks on a **3×3 grid**.  
- The goal is to get **three marks in a row**: horizontally, vertically or diagonally.  
- If all spaces are filled and no one wins, the game ends in a **draw**.

## How It Works
1. The game initializes a board with positions **1–9** to show available spots.  
2. The current board is displayed in a **3×3 layout** after each move.  
3. The program checks if the **board is full** to determine a draw. 
4. Players can **choose their markers** (X or O) before the game begins.
5. The game **validates each move**, ensuring it’s a number from 1–9 and that the position isn’t already taken.
6. After each move, the board is **updated** and **displayed** immediately.
7. The game detects **winning combinations** (rows, columns, diagonals) and declares the winner.
8. If no winner is found and the board is full, it declares a **draw**.
9. After the game ends, players can choose to **play again** without restarting the program.

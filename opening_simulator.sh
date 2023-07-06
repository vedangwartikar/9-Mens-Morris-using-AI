#!/bin/bash
echo 'xxxxxxxxxxxxxxxxxxxxx' > board1.txt

if [ "$1" == "-i" ]; then
    python3 MiniMaxOpeningImproved.py board1.txt board2.txt 2 --print_board
    python3 MiniMaxOpeningBlack.py board2.txt board2.txt 2 --print_board
    python3 MiniMaxOpeningImproved.py board2.txt board2.txt 2 --print_board
    python3 MiniMaxOpeningBlack.py board2.txt board2.txt 2 --print_board
    python3 MiniMaxOpeningImproved.py board2.txt board2.txt 2 --print_board
    python3 MiniMaxOpeningBlack.py board2.txt board2.txt 2 --print_board
    python3 MiniMaxOpeningImproved.py board2.txt board2.txt 2 --print_board
    python3 MiniMaxOpeningBlack.py board2.txt board2.txt 2 --print_board
    python3 MiniMaxOpeningImproved.py board2.txt board2.txt 2 --print_board
    python3 MiniMaxOpeningBlack.py board2.txt board2.txt 2 --print_board
    python3 MiniMaxOpeningImproved.py board2.txt board2.txt 2 --print_board
    python3 MiniMaxOpeningBlack.py board2.txt board2.txt 2 --print_board
    python3 MiniMaxOpeningImproved.py board2.txt board2.txt 2 --print_board
    python3 MiniMaxOpeningBlack.py board2.txt board2.txt 2 --print_board
    python3 MiniMaxOpeningImproved.py board2.txt board2.txt 2 --print_board
    python3 MiniMaxOpeningBlack.py board2.txt board2.txt 2 --print_board
else
    python3 MiniMaxOpening.py board1.txt board2.txt 2 --print_board
    python3 MiniMaxOpeningBlack.py board2.txt board2.txt 2 --print_board
    python3 MiniMaxOpening.py board2.txt board2.txt 2 --print_board
    python3 MiniMaxOpeningBlack.py board2.txt board2.txt 2 --print_board
    python3 MiniMaxOpening.py board2.txt board2.txt 2 --print_board
    python3 MiniMaxOpeningBlack.py board2.txt board2.txt 2 --print_board
    python3 MiniMaxOpening.py board2.txt board2.txt 2 --print_board
    python3 MiniMaxOpeningBlack.py board2.txt board2.txt 2 --print_board
    python3 MiniMaxOpening.py board2.txt board2.txt 2 --print_board
    python3 MiniMaxOpeningBlack.py board2.txt board2.txt 2 --print_board
    python3 MiniMaxOpening.py board2.txt board2.txt 2 --print_board
    python3 MiniMaxOpeningBlack.py board2.txt board2.txt 2 --print_board
    python3 MiniMaxOpening.py board2.txt board2.txt 2 --print_board
    python3 MiniMaxOpeningBlack.py board2.txt board2.txt 2 --print_board
    python3 MiniMaxOpening.py board2.txt board2.txt 2 --print_board
    python3 MiniMaxOpeningBlack.py board2.txt board2.txt 2 --print_board
fi
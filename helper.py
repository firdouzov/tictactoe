import numpy as np
import random
import pickle
import os

def create_board():
    return [' ' for _ in range(9)]

def print_board(board):
    print("\nCurrent Tic Tac Toe Board:")
    print(f" {board[0] or 1} | {board[1] or 2} | {board[2] or 3} ")
    print("---+---+---")
    print(f" {board[3] or 4} | {board[4] or 5} | {board[5] or 6} ")
    print("---+---+---")
    print(f" {board[6] or 7} | {board[7] or 8} | {board[8] or 9} ")

def get_available_moves(board):
    return [i for i in range(9) if board[i] == ' ']

def check_win(board, player):
    win_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]  # Diagonals
    ]
    
    for combo in win_combinations:
        if all(board[i] == player for i in combo):
            return True
    return False

def check_draw(board):
    return ' ' not in board

def choose_action(board, q_table, epsilon):
    available_moves = get_available_moves(board)
    
    # Exploration
    if random.uniform(0, 1) < epsilon:
        return random.choice(available_moves)

    board_key = tuple(board)
    best_value = float('-inf')
    best_moves = []
    
    for move in available_moves:
        q_value = q_table.get((board_key, move), 0)
        if q_value > best_value:
            best_value = q_value
            best_moves = [move]
        elif q_value == best_value:
            best_moves.append(move)
    
    return random.choice(best_moves)

def update_q_table(q_table, state, action, reward, next_state, done, 
                   learning_rate=0.1, discount_factor=0.9):
    state_key = tuple(state)
    next_state_key = tuple(next_state)
    
    current_q = q_table.get((state_key, action), 0)
    
    if done:
        future_max_q = 0
    else:
        available_next_moves = get_available_moves(next_state)
        future_max_q = max([q_table.get((next_state_key, next_action), 0) 
                             for next_action in available_next_moves])
    
    new_q = current_q + learning_rate * (reward + discount_factor * future_max_q - current_q)
    q_table[(state_key, action)] = new_q
    
    return q_table

def save_q_table(q_table, filename="q_table.pkl"):
    with open(filename, 'wb') as file:
        pickle.dump(q_table, file)

def load_q_table(filename="q_table.pkl"):
    if os.path.exists(filename):
        with open(filename, 'rb') as file:
            return pickle.load(file)
    return {}

def play_adaptive_game(q_table, epsilon=0.1):
    board = create_board()
    current_player = 'X'
    game_history = []
    done = False
    
    while not done:
        # AI's turn (X player)
        available_moves = get_available_moves(board)
        action = choose_action(board, q_table, epsilon)
        
        # Store current state for learning
        previous_board = board.copy()
        
        board[action] = current_player
        game_history.append((previous_board, action))
        
        print(f"\nAI plays at position: {action + 1}")
        print_board(board)
        
        # Check game state
        if check_win(board, current_player):
            # Reward for winning
            for prev_board, prev_action in game_history:
                q_table = update_q_table(q_table, prev_board, prev_action, 10, board, True)
            print("AI wins!")
            break
        elif check_draw(board):
            # Neutral reward for draw
            for prev_board, prev_action in game_history:
                q_table = update_q_table(q_table, prev_board, prev_action, 5, board, True)
            print("It's a draw!")
            break
        
        # Human's turn
        while True:
            try:
                move_input = input("Enter your move (1-9): ")
                move = int(move_input) - 1
                
                if move not in available_moves:
                    print("Invalid move. Try again.")
                    continue
                
                board[move] = 'O'
                break
            except (ValueError, IndexError):
                print("Invalid input. Use a number between 1-9.")
        
        if check_win(board, 'O'):
            # Penalty for losing
            for prev_board, prev_action in game_history:
                q_table = update_q_table(q_table, prev_board, prev_action, -10, board, True)
            print_board(board)
            print("You win!")
            break
        elif check_draw(board):
            # Neutral reward for draw
            for prev_board, prev_action in game_history:
                q_table = update_q_table(q_table, prev_board, prev_action, 5, board, True)
            print_board(board)
            print("It's a draw!")
            break
        
        current_player = 'X'
    
    print_board(board)
    return q_table
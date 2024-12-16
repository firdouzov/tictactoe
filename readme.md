# Tic Tac Toe with Q-Learning

This project is a Tic Tac Toe game powered by a Q-learning algorithm. The AI improves its gameplay with each match by learning from wins, losses, and draws. It uses a Q-table to store knowledge, allowing it to play more strategically over time.

---

## Features

- **Q-learning AI**: The AI uses reinforcement learning to improve its gameplay dynamically.
- **Persistent Learning**: The Q-table is saved after every game and loaded at the start of the program, ensuring the AI retains its knowledge across sessions.
- **Interactive Gameplay**: You can play against the AI while it learns from your moves.

---

## How It Works

1. **Q-table**: The Q-table stores the AI's learned values for state-action pairs.
2. **Reinforcement Learning**:
   - **Reward**: The AI is rewarded for winning (+10), penalized for losing (-10), and given a neutral reward for a draw (+5).
   - **Learning**: After every move, the Q-table is updated using the Q-learning formula.
3. **Exploration vs. Exploitation**:
   - The AI chooses a random move (`exploration`) or the best-known move from the Q-table (`exploitation`), depending on the `epsilon` value.
4. **Persistence**:
   - The Q-table is saved to a file (`q_table.pkl`) after each game.
   - It is loaded at the start of the program, allowing the AI to resume learning from its previous state.

---

## Installation

### Prerequisites
- Python 3.6 or higher

### Steps
1. Clone this repository or download the script file.
   ```bash
   git clone <repository_url>
   ```
2. Navigate to the project directory.
   ```bash
   cd tic-tac-toe-qlearning
   ```
3. Run the script.
   ```bash
   python tic_tac_toe.py
   ```

---

## Usage

### Playing the Game
1. Run the script:
   ```bash
   python tic_tac_toe.py
   ```
2. Follow the prompts to make your moves. Enter a number between 1-9 to select a position on the board.
3. The AI will play its turn and display the updated board.
4. Continue playing until someone wins or the game ends in a draw.
5. After the game, you can choose to play again or exit.

### Q-Table Persistence
- The Q-table is saved to a file named `q_table.pkl` after every game.
- If the file exists, it is loaded when the program starts. This ensures that the AI retains its knowledge across sessions.

---

## File Structure

```
.
├── tic_tac_toe.py       # Main script for the game
├── q_table.pkl          # (Generated) Q-table file for persistent learning
└── README.md            # This documentation file
```

---

## Customization

### Adjust AI Parameters
- **Learning Rate (`learning_rate`)**: Adjust how quickly the AI learns from new information (default: 0.1).
- **Discount Factor (`discount_factor`)**: Set how much the AI values future rewards (default: 0.9).
- **Exploration Rate (`epsilon`)**: Control the balance between exploration and exploitation (default: 0.1).

### Modifying Rewards
- You can customize the rewards for different outcomes (win, loss, draw) in the `update_q_table` function.

---

## Known Limitations

- The AI only improves its gameplay when it plays as `X` (the first player). Enhancing it to play optimally as `O` would require additional logic.
- For very long sessions, the Q-table file size may grow significantly.

---

## Future Enhancements

- Add functionality for the AI to play as `O` (second player).
- Optimize the Q-table storage for large datasets.
- Implement a graphical user interface (GUI).

---

## License

This project is licensed under the MIT License. You are free to use, modify, and distribute it.

---

## Acknowledgments

- Inspired by the fundamentals of Q-learning in reinforcement learning.
- Special thanks to the Python community for the tools and resources used in this project.


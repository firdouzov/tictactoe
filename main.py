from helper import *
def main():
    # Load Q-table from file
    q_table = load_q_table()
    
    print("AI is ready to play and learn!")
    
    while True:
        q_table = play_adaptive_game(q_table)
        
        save_q_table(q_table)
        
        play_again = input("\nPlay again? (y/n): ").lower()
        if play_again != 'y':
            break
    
    print("Thanks for playing!")

if __name__ == "__main__":
    main()

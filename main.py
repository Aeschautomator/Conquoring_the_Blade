# Import necessary scripts
from scripts.bot_behavior import run_bot
from scripts.reporting import generate_report
from scripts.data_collection import capture_game_data
from models.ai_model import load_trained_model

def main():
    # Step 1: Load AI model
    print("Loading AI model...")
    model = load_trained_model('models/trained_model.pkl')
    
    # Step 2: Start data collection (key logs, screenshots)
    print("Starting data collection...")
    capture_game_data()

    # Step 3: Run the bot and play the game
    print("Starting bot...")
    run_bot(model)

    # Step 4: Generate a performance report after the battle
    print("Generating performance report...")
    generate_report()

    print("Bot execution completed. Check the performance report in /data/performance_report.txt")

if __name__ == "__main__":
    main()

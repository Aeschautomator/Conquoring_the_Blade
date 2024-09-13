Game AI Bot Project
This project is an AI-powered bot designed to play a non-turn-based strategy game where the player controls a hero and a unit. The bot is tasked with moving the hero, commanding the unit, and defeating enemies in the most efficient way possible while minimizing losses. The bot uses machine learning to make strategic decisions and logs gameplay data for performance analysis.

Project Features
Hero and Unit Control: The bot simulates key presses to control a hero and a unit in real-time.
AI-Driven Decisions: An AI model predicts actions based on the current game state, including movement, attacks, and unit commands.
Gameplay Data Logging: The bot logs key presses, screenshots, and battle statistics for analysis.
Performance Reports: After each battle, a performance report is generated, providing insights into the bot’s efficiency.
Extensible Architecture: The project is designed to be modular and expandable, allowing for future improvements (e.g., reinforcement learning).


game_bot_project/
│
├── data/                       # Stores gameplay data, key logs, and performance reports
│   ├── screenshots/            # Folder for screenshots during gameplay
│   ├── key_log.txt             # Logs all key presses
│   ├── battle_stats.json       # Stores battle statistics
│   └── performance_report.txt  # Performance summary of each battle
│
├── models/                     # AI model and training data
│   ├── ai_model.py             # AI model code
│   ├── trained_model.pkl       # Trained model file
│   └── training_data.csv       # Training dataset
│
├── scripts/                    # Main scripts for controlling the bot and training the AI
│   ├── bot_behavior.py         # Main bot logic for controlling hero and unit
│   ├── key_pressing.py         # Handles key press simulation
│   ├── reporting.py            # Generates performance reports
│   ├── data_collection.py      # Captures and logs key presses and screenshots
│   └── training_loop.py        # Training loop for the AI model
│
├── requirements.txt            # List of dependencies
├── README.md                   # Project documentation
└── main.py                     # Main entry point to run the bot

How to Set Up the Project
1. Clone the Repository
bash
Copy code
git clone https://github.com/yourusername/game_bot_project.git
cd game_bot_project
2. Install Dependencies
Make sure you have Python 3.8+ installed. Install the required Python libraries by running:

bash
Copy code
pip install -r requirements.txt
3. Configure the Game Environment
Ensure the game you want the bot to play is running in a windowed mode.
The bot will simulate key presses, so it should be focused on the game window during execution.
4. Run the Bot
To run the bot and start controlling the hero and unit, use:

bash
Copy code
python main.py
The bot will begin to simulate key presses and control the game based on the AI's decisions.

5. Check Performance Reports
After each battle, the bot generates a performance report. You can find the reports in:

bash
Copy code
/data/performance_report.txt


How It Works
1. Bot Behavior (bot_behavior.py)
The core logic for the bot is housed in bot_behavior.py. The bot moves the hero using the W, A, S, D keys and commands the unit to follow or attack using the C and V keys, respectively.

The bot's behavior is determined by the AI model in ai_model.py. The model processes the game state and predicts the next action for the bot, such as moving, retreating, or commanding the unit to attack.

2. Key Press Simulation (key_pressing.py)
This script handles all simulated key presses using the pyautogui library. It allows the bot to send commands to the game as if a human player is pressing the keys.

3. Data Logging and Collection (data_collection.py)
To improve the AI model and analyze gameplay, the bot logs key presses, battle statistics, and captures screenshots at regular intervals. These logs are saved in the data/ folder for analysis.

4. AI Model (ai_model.py)
The AI model is trained to predict the best action in each game state. You can train or fine-tune the model using gameplay data stored in training_data.csv. The model is serialized as trained_model.pkl and loaded during gameplay.

Training the AI
To train the AI model using your gameplay data, run the training_loop.py script:

bash
Copy code
python scripts/training_loop.py
This script will load the gameplay data (training_data.csv), train a new model, and save it as trained_model.pkl. The bot will use this model to make more informed decisions during gameplay.

Future Improvements
The project is designed to be extensible, and you can add the following features:

Reinforcement Learning: Implement reinforcement learning algorithms like Q-learning to allow the bot to learn from experience.
Multi-agent Control: Expand the bot's ability to control multiple units or handle more complex strategies.
Advanced Reporting: Improve the reporting system to include more detailed analytics, charts, and performance metrics.
UI Integration: Integrate a graphical user interface (GUI) for easier bot configuration and real-time performance monitoring.


THIS PROJECT HAS BEEN SHELVED AS THE GAME USES EASY ANTI CHEAT AND WOULD LIKELY DETECT THE BOT
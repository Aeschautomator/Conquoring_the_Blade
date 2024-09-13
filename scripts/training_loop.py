# Example function for triggering actions based on AI model predictions
def ai_controlled_bot(model, game_state):
    action = model.predict(game_state)  # Get action from AI model

    if action == 'move_forward':
        press_key('w', duration=2)

    elif action == 'move_backward':
        press_key('s', duration=1.5)

    elif action == 'attack':
        press_key('v')

    elif action == 'follow':
        press_key('c')

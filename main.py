import random
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

class RPSApp(App):
    def build(self):
        # The choices for the game
        self.choices = ['Rock', 'Paper', 'Scissors']
        # Layout to organize the elements on the screen
        layout = BoxLayout(orientation='vertical')

        # Label to display the result of the game
        self.result_label = Label(text="Choose Rock, Paper, or Scissors")
        layout.add_widget(self.result_label)

        # Layout to hold the buttons
        button_layout = BoxLayout(orientation='horizontal')

        # Create buttons for each choice (Rock, Paper, Scissors)
        for choice in self.choices:
            btn = Button(text=choice, on_press=self.on_choice)
            button_layout.add_widget(btn)

        layout.add_widget(button_layout)
        return layout

    def on_choice(self, instance):
        user_choice = instance.text
        computer_choice = random.choice(self.choices)
        result = self.get_winner(user_choice, computer_choice)
        # Update the label to show the game result
        self.result_label.text = f"Your choice: {user_choice}\nComputer's choice: {computer_choice}\n{result}"

    def get_winner(self, user, computer):
        if user == computer:
            return "It's a tie!"
        elif (user == 'Rock' and computer == 'Scissors') or \
             (user == 'Paper' and computer == 'Rock') or \
             (user == 'Scissors' and computer == 'Paper'):
            return "You win!"
        else:
            return "Computer wins!"

if __name__ == "__main__":
    RPSApp().run()

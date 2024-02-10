from taipy.gui import Gui

# Define the submit action
def submit_action(state):
    # Placeholder for the action to be taken when the submit button is pressed.
    # You might want to send the file to the VM here.
    # For demonstration, we'll just print the file path.
    print(f"File submitted: {state.file_selector}")

# Create a GUI object
gui = Gui()

# Define the GUI layout
gui.add_page(name="Soccer-Futures", page=
"""
# Soccer Futures

Please upload an MP4 file related to soccer futures and click submit.

<|file_selector|id=file_selector|multiple=True|extensions=.csv,.xlsx,.mp4|>

<|button|label=Submit|on_action=submit_action|>
""")

# Run the application
if __name__ == "__main__":
    gui.run()

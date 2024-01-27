# Import the tkinter module and give it the alias 'tk'
import tkinter as tk

# Create the main application window
app_window = tk.Tk()
app_window.title("Python Calculator")

# Create an Entry widget for the display
result_display = tk.Entry(app_window, width=20, font=("Arial", 20))
result_display.grid(row=0, column=0, columnspan=4, ipadx=46, ipady=40)

# Define button labels
button_labels = [
    "7",
    "8",
    "9",
    "/",  # Row 1
    "4",
    "5",
    "6",
    "*",  # Row 2
    "1",
    "2",
    "3",
    "-",  # Row 3
    "0",
    ".",
    "=",
    "+",  # Row 4
]

# Create buttons and place them in a grid
row, col = 1, 0
calculator_buttons = []
for label in button_labels:
    # Create a button with specified label, width, height, and font
    button = tk.Button(app_window, text=label, width=5, height=2, font=("Arial", 16))
    # Place the button in a grid with specified padding
    button.grid(row=row, column=col, padx=5, pady=5)
    # Add the button to the list of calculator_buttons
    calculator_buttons.append(button)
    # Move to the next column, reset to the first column if needed
    col += 1
    if col > 3:
        col = 0
        row += 1


# Function to handle button clicks
def on_button_click(event):
    # Get the current text in the display
    current_text = result_display.get()

    # Get the label of the button that was clicked
    clicked_button = event.widget
    button_text = clicked_button["text"]

    if button_text == "=":
        try:
            # Evaluate the expression and display the result
            result = eval(current_text)
            result_display.delete(0, tk.END)
            result_display.insert(tk.END, str(result))
        except:
            # Handle errors (e.g., division by zero)
            result_display.delete(0, tk.END)
            result_display.insert(tk.END, "Error")
    else:
        # Append the button's text to the current display text
        result_display.insert(tk.END, button_text)


# Function to clear the display
def clear_display():
    result_display.delete(0, tk.END)


# Bind the on_button_click function to the calculator buttons
for button in calculator_buttons:
    button.bind("<Button-1>", on_button_click)

# Create a clear button and bind the clear_display function
clear_button = tk.Button(
    app_window, text="C", width=5, height=2, font=("Arial", 16), command=clear_display
)
clear_button.grid(row=5, column=0, columnspan=4, padx=5, pady=5)

# Start the tkinter event loop
app_window.mainloop()

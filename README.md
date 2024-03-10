# TechnoHacks_Internship_Task_3

ALGORITHM:

Function Definitions:
button_click(item): Appends the clicked button's text to the expression and updates the display.
button_equal(): Evaluates the final expression and displays the result.
button_clear(): Clears the expression and updates the display.

Initialize Tkinter:
Create the main window with title, size, and background color.
Create a StringVar to store the input expression and initialize it to an empty string.

Create Entry Widget:
Create an Entry widget to display the input expression.
Set the font, border width, background color, and alignment.

Create Buttons:
Define the layout of the calculator buttons (digits, operators, and special buttons).
Create each button with the specified text, font, padding, background color, and command (linked to the button_click function).

Place Buttons:
Use grid layout to place the buttons on the main window, following the specified layout.

Create Equal and Clear Buttons:
Create additional buttons for equal (=) and clear (C) functionalities.
Set the background color, font, padding, and command (linked to button_equal and button_clear functions).

Run the Tkinter Event Loop:
Start the Tkinter event loop to handle user interactions and update the display accordingly.

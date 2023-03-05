// Provides standard library functions for memory allocation, 
// process control, and other utility functions
#include <stdlib.h>
// Provides access to the terminal I/O interface
#include <termios.h>
// Provides access to the UNIX operating system API
// (read and write operations, file operations, system calls etc.)
#include <unistd.h>


// Define a struct to store the original terminal attributes.
struct termios orig_termios;


// Function to restore the terminal to its original state.
void disableRawMode() {
    // sets the terminal attributes with the original settings in the orig_termios struct
    tcsetattr(STDIN_FILENO, TCSAFLUSH, &orig_termios);
}


// Function to enable raw mode on the terminal.
void enableRawMode() {
    // Get the current attributes of the terminal and store them in the orig_termios struct.
    tcgetattr(STDIN_FILENO, &orig_termios);
    
    // Call the disableRawMode() function when the program exits.
    atexit(disableRawMode);

    // Create a new termios struct with the original attributes.
    struct termios raw = orig_termios;

    // Turn off the ECHO flag in the raw struct. ECHO causes characters typed on the terminal to be echoed
    // (printed) to the terminal, which is not desirable in raw mode.
    raw.c_lflag &= ~(ECHO);

    // Set the terminal attributes with the new settings in the raw struct.
    tcsetattr(STDIN_FILENO, TCSAFLUSH, &raw);
}


// The main function of the program.
int main() {
    // Enable raw mode on the terminal.
    enableRawMode();

    // Define a char variable to store input from the user.
    char ch;

    // Read characters from the terminal one at a time until the character 'q' is entered.
    while (read(STDIN_FILENO, &ch, 1) == 1 && ch != 'q');
    
    // Return 0 to indicate successful completion of the program.
    return 0;
}
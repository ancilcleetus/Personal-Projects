// provides functions to control terminal I/O
#include <termios.h>
// provides access to the UNIX operating system API
#include <unistd.h>

void enableRawMode() {
    // struct containing information about terminal attributes and modes
    struct termios raw;

    // get the current attributes of the terminal
    tcgetattr(STDIN_FILENO, &raw);

    // turns off the ECHO flag in the raw struct
    // ECHO flag causes characters typed on the terminal to be echoed (printed)
    // to the terminal, which is not desirable in raw mode
    raw.c_lflag &= ~(ECHO);

    // sets the terminal attributes with the new settings in the raw struct
    tcsetattr(STDIN_FILENO, TCSAFLUSH, &raw);
}

int main() {
    enableRawMode();

    char ch;
    // reads characters from the terminal one at a time until the character 'q' is entered
    while (read(STDIN_FILENO, &ch, 1) == 1 && ch != 'q');
    
    return 0;
}
# passwordcrack

This program attempts to crack any password given to it. Your password isn't necessarily good if it wasn't cracked by this program, the program suffers from poor memory management due in part to using Python as a language and otherwise due to code quality.

## Usage

1. Run `main.py`
2. Follow the text prompts.
    - If you choose not to edit the settings, default settings will be chosen.

### Fork and change my program for your use

- Please familiarize yourself with the terms of the [GPL-3.0](LICENSE.md) GNU General Public License before forking this project.

- To change the max allowed length edit the `MAX_LENGTH` variable in the program directly. Beware, even at a low number the chances of the program being killed due to lack of memory is high.

- Don't try to modify this program to hack websites or computers. Even if it's for educational purposes, if you are smart enough to retarget the password input to a password field elsewhere, you are smart enough to write an exponentially better algorithm.

## License

This project is licensed under the [GPL-3.0](LICENSE.md)
GNU General Public License - see the [LICENSE.md](LICENSE.md) file for
details.

# AoE2DE_AIBuilder
A python executable remake of the Forgotten Empires AoE2 AI Builder that creates AoE2DE-compatible AI files. These files are intended for campaigns, as they only have basic build and attack instructions. (Requires Python 2.7.x or Python 3.x to run.)

This program will create the ".ai" and ".per" files that are used for custom AI in AoE2. Place them in your install path's AI folder to allow the AI to appear in the Scenario Editor. In addition, be sure to include the additional library ".per" files in your AI folder to handle common behaviors.

The original FE version of this tool, with the ability to scale units built by difficulty and to allow the AI to cheat, can be found here: http://www.forgottenempires.net/aibuilder/

(Original FE tool and original version of the library files created by Jan1302.)

Known Potential Issues:
- "Fortifications" upgrade toggle does nothing; all of its upgrades are under "University" in the library file.
- The AI Name entry does not check to see if the entered name is a valid filename.
- The program was designed to be run with Python 2.7.x. Some attempt to make it compatible with Python 3.x and later has been made, but this has not been tested.

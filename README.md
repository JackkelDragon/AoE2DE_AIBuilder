# AoE2DE_AIBuilder
A python executable remake of the Forgotten Empires AoE2 AI Builder that creates AoE2DE-compatible AI files. These files are intended for campaigns, as they only have basic build and attack instructions. (Requires Python 3.9.x or higher to run.)

This program will create the ".ai" and ".per" files that are used for custom AI in AoE2. Place them in your install path's AI folder to allow the AI to appear in the Scenario Editor. In addition, be sure to include the additional library ".per" files in your AI folder to handle common behaviors.

The original FE version of this tool, with the ability to scale units built by difficulty and to allow the AI to cheat, can be found here: http://www.forgottenempires.net/aibuilder/

(Original FE tool and original version of the library files created by Jan1302.)

Known Potential Issues:
- The AI Name entry does not check to see if the entered name is a valid filename.

v2 Update (December 2022) Notes:
- Some bugs relating to unit counts should now be fixed.
- Added limited support for training units based on editor IDs.
- Aging up should now work properly.
- If the number of military scouts is set to zero, the AI should no longer do any scouting.
- Added the option to allow the AI to cheat for specific resources.
- Minor visual tweaks and fixes.
- NOTE: JSON saves made with older versions of the program may no longer work! (New fields have been added to the current version.)

# AoE2DE_AIBuilder
A python executable remake of the Forgotten Empires AoE2 AI Builder that creates AoE2DE-compatible AI files. These files are intended for campaigns, as they only have basic build and attack instructions.

This program will create the ".ai" and ".per" files that are used for custom AI in AoE2. Place them in your install path's AI folder to allow the AI to appear in the Scenario Editor. In addition, be sure to [library ai and immobile].

The original FE version of this tool, with the ability to scale units built by difficulty and to allow the AI to cheat, can be found here: http://www.forgottenempires.net/aibuilder/

Known Potential Issues:
- "Fortifications" upgrade toggle does nothing; all of its upgrades are under "University" in the library file.
- The AI Name entry does not check to see if the entered name is a valid filename.

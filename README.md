# Tower Defense Game

## Project Overview
This is a tower defense game where players defend a marshmallow protagonist by placing towers along a path to stop waves of enemies. The game features various tower types (e.g., Cannon, Freeze, Laser), each with unique abilities and characteristics. Players can save their progress and resume from where they left off.

**Key Features:**
- Multiple tower types with different abilities
- Various enemy waves with increasing difficulty
- Save and load functionality to save progress
- Customizable game maps and environments

---

## Setup Instructions

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/Eytral/Marshmallow-Tower-Defense-Official.git
   cd Marshmallow-Tower-Defense-Official
   ```

2. **Install Dependencies:**

   - **Python Version**: Python 3.x (Recommended: Python 3.7+)
   - `pygame`: A library used for game development
   - `pytest`: A library used for testing

   You can install all necessary dependencies by running the following command:

   ```bash
   pip install -r requirements.txt
   ```

---

3. **Run the Game:**

   After setting up, simply run the `main.py` file to start the game:

   ```bash
   python main.py
   ```

---

## Usage Guide

- **Main Menu:**
  - Start a new game
  - Access settings for game options (difficulty)
  - Exit the game

- **Gameplay:**
  - Place towers on available spots on the map to defend against enemies (spawning on red tile) from reaching the end (green tile).
  - Each wave of enemies will increase in difficulty as the game progresses.
  - Collect resources by defeating enemies to upgrade or build new towers.
  - Manage your resources (money, lives) effectively until the final wave to win!
- **Demonstration:**
   - https://www.youtube.com/watch?v=iEzwoqcZnvc
---

## Requirements Reference

1. **Grid-Based Map/Coordinate System**:
   - **Requirement**: A grid-based map system that uses coordinates to define positions for both enemies and towers.
   - **Implementation**: The game uses a 2D array to represent the grid map, with each grid cell containing a number indicating whether it is passable or an obstacle. This system defines the map and ensures that both enemies and towers (and empty spaces) are placed at specific coordinates. Towers are stored in a dictionary with their coordinates as keys, allowing easy selection of towers based on grid coordinates, and decoupling the grid/map and towers.

2. **Different Enemy Types with Unique Designs, Health, Number, and Mechanics**:
   - **Requirement**: Different enemy types, each with unique characteristics like health, number, and mechanics (e.g., resistance to certain towers).
   - **Implementation**: The game features multiple enemy types, each with unique properties such as health, movement speed, and resistance to specific tower types. These mechanics are handled by the enemy subclasses that define these attributes.
      - **Examples**:
         - **Cracker Enemy**: 
            - **Attributes**: The cracker enemy has defense, reducing damage taken from all towers. 
            - **Mechanics**: It is resistant to damage from the bird flamethrower tower, and it can break, occuring after its health is less than half, increasing its movement speed but reducing its defense, meaning it takes additional damage from towers; the bomb tower immediately breaks the cracker ignoring the health requirement, making it a specific, effective counter to that enemy. 
         - **Chocolate Enemies**:
            - **Attributes**: The white chocolate enemy has a uniquely fast movement speed, but low health to compensate, while the dark chocolate is a well rounded tough enemy, with decent defense, speed and health.
            - **Mechanics**: Both of the chocolate variants will melt if damaged by the bird flamethrower tower, reducing their speed, and defense in the case of the dark chocolate enemy. 
         - **Smore Enemy**: 
            - **Attributes**: The smore is a boss enemy with alot of health, but slow speed.
            - **Mechanics**: Upon death, it splits into its components; 2 cracker enemies, a dark chocolate enemy, and a marshmallow enemy.

3. **Wave-Based Enemy Spawning System, Progressively Increasing in Difficulty**:
   - **Requirement**: A wave-based enemy spawning system that increases in difficulty over time.
   - **Implementation**: Enemies spawn in waves, and the difficulty increases over time. This is achieved by a wave manager that controls the number, type, and frequency of enemy spawns, with later waves featuring stronger and more enemies (determined by preset data; the enemy spawns ramp up in linear increments, starting at a preset default value).

4. **Enemy Spawning and Pathfinding Mechanisms**:
   - **Requirement**: A mechanism to spawn enemies and guide them through a path from start to end using pathfinding.
   - **Implementation**: Enemies are spawned at predefined points (marked on 2D array) and follow a path to the goal using a basic pathfinding algorithm. The map grid system defines these paths, and enemies are guided from the start to the end, along the predetermined path on the grid (2D array). The enemies themselves are stored in a list (1D array).

5. **Different Tower Types with Unique Designs, Range, Damage, Attack Patterns/Types**:
   - **Requirement**: Different tower types with unique attributes like range, damage, and attack patterns/types.
   - **Implementation**: The game features multiple tower types, each with different attributes such as attack range, damage, damage type and unique attack patterns. These attributes are defined within each tower subclass.
      - **Examples**:
         - **Bird Flamethrower Tower**: 
            - **Attributes**: Has a low range, but infinite pierce and fast attack speed, firing a constant stream of fire. 
            - **Mechanics**: The projectiles it fires don't die on impact, rather they move a set distance before dying, mimicking a sort of melee attack.
            Its specific damage type (fire) is handled differently by chocolate and cracker enemies, (as previously described - 'melts' chocolate, less effective on crackers).
         - **Bomb Tower**: 
            - **Attributes**: Has splash damage, dealing a fraction of its total damage to all enemies within a splash tile radius of the initial enemy hit.
            - **Mechanics**: As previously described, the bomb has a specific effect on cracker enemies ('cracks' them - sends them their broken state, where speed attribute is increased but defense attribute is decreased)

6. **Resource Management System for Purchasing and Upgrading Towers**:
   - **Requirement**: A resource management system that enables players to purchase and upgrade towers.
   - **Implementation**: Players manage resources (money) to purchase and upgrade towers. The resource system is tied to the number and type of enemies defeated, and players need to balance their spending to optimize defense against increasingly difficult waves.

7. **Save System**:
   - **Requirement**: A system to save progress, including level completion, scores, and settings.
   - **Not Implemented**: A save system was initially planned to save player progress, level completion, scores, and settings. However, due to skill and time limitations, this feature has not been implemented at this stage of development. This means players must start a new game each time they play, without the ability to continue from a previous session.

---


## Credits & Acknowledgements

- **Developer**: [Jason Gregory](https://github.com/Eytral)
- **Special Thanks to**:
  - **[ChatGPT](https://chatgpt.com/) ([OpenAI](https://openai.com))**: Helped with development issues and debugging
  - **[Bloons Tower Defense 6](https://ninjakiwi.com/Games/Mobile/Bloons-TD-6.html) ([Ninja Kiwi](https://ninjakiwi.com/))**: Main inspiration for game mechanics/design
  - **[Pygame library](https://www.pygame.org)**: Tool for 2D game development in Python.
  - **[Craftpix](https://craftpix.net/product/obstacle-game-asset-pack/?num=1&count=1588&sq=19%20obstacles%20game&pos=0)**: Tower and projectile Sprites
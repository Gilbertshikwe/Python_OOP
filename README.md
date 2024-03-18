# Eating Competition Code

This repository contains the code for an eating competition. The code is organized into three main files, each serving a specific purpose.

## participant.py

This file defines the `Participant` class, which represents a participant in the eating competition. Each participant has attributes for their name, number of chicken wings eaten, number of hamburgers eaten, and number of hotdogs eaten. The file also calculates the participant's score based on the points assigned to each food item (5 points for chicken wings, 3 points for hamburgers, and 2 points for hotdogs).

## competition.py

This file defines the `Competition` class, which represents the eating competition itself. It initializes with a list of participants, creating `Participant` instances based on the provided data. The class sorts the participants based on their scores and names, producing a scoreboard. It also provides a method to access the scoreboard.

## main.py

This file contains example usage of the `Competition` class. It creates instances of the `Competition` class with different sets of participants and prints the scoreboard for each competition example.

Each file encapsulates related functionality, following the principles of modular programming and separation of concerns. This structure makes the code easier to understand, maintain, and extend. 

Please refer to the individual files for more detailed information.

### Usage
- Clone the repository: git clone <repository-url>
- Install dependencies: pip install -r requirements.txt
- Run `main.py` to test the functionality.
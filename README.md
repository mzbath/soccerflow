# soccerflow
Mini-project to collect data, store data in database, and visualise data to practice using sqlite and python.

## Data source
The data used are collected from the open source StatsBomb data using ```statsbombpy``` API.

## Database
A single match was selected for simplicity and multiple relations created:
- teams: containing the unique team id and their name
- players: containing the player id, player name, team id (i.e., a foreign key), position, jersey number.

## Visualisation
Data visualisation created using ```plotly``` to display passes on the pitch and players who performed most effective passes.

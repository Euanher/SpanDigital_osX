import os
import platform
from collections import defaultdict
from typing import List, Tuple, Dict 

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FONT_SIZE = 32
LOGO_SIZE = (50, 50)
ASSETS_FOLDER = "./assets"  # Path to the folder containing team logos

def grab_some_coffee():
    print("Grabbing some coffee...")

def grab_some_champagne():
    print("Grabbing some champagne...")

def format_output(rankings):
    """
    Format the rankings into a human-readable string.

    Args:
        rankings: List of tuples containing (rank, team, points).

    Returns:
        A formatted string representing the rankings.
    """
    lines = []
    for rank, team, points in rankings:
        point_label = "pt" if points == 1 else "pts"
        lines.append(f"{rank}. {team}, {points} {point_label}")
    return "\n".join(lines)

def parse_input(input_lines: List[str]) -> List[Tuple[str, int, str, int]]:
    """
    Parse match results from input lines.

    Args:
        input_lines: List of strings representing match results.

    Returns:
        A list of tuples containing team1, score1, team2, score2.
    """
    results = []
    for line in input_lines:
        parts = line.split(", ")
        team1, score1 = parts[0].rsplit(" ", 1)
        team2, score2 = parts[1].rsplit(" ", 1)
        results.append((team1, int(score1), team2, int(score2)))
    return results

def calculate_points(results: List[Tuple[str, int, str, int]], all_teams: set) -> Dict[str, int]:
    """
    Calculate points for each team based on match results.

    Args:
        results: List of match results with team names and scores.
        all_teams: A set of all teams, which ensures even teams that don't score points are included.

    Returns:
        A dictionary mapping team names to their points.
    """
    points = defaultdict(int)
    for team1, score1, team2, score2 in results:
        # Ensure both teams are in the all_teams set even if they score 0 points
        all_teams.add(team1)
        all_teams.add(team2)

        if score1 > score2:
            points[team1] += 3
        elif score1 < score2:
            points[team2] += 3
        else:
            points[team1] += 1
            points[team2] += 1

    # Ensure teams with 0 points are added to the dictionary
    for team in all_teams:
        if team not in points:
            points[team] = 0

    return points

def rank_teams(points: Dict[str, int]) -> List[Tuple[int, str, int]]:
    """
    Rank teams based on points, sorted by descending points and team name.

    Args:
        points: Dictionary mapping team names to points.

    Returns:
        A list of tuples (rank, team name, points).
    """
    # Sort by points descending and then by team name ascending
    sorted_teams = sorted(points.items(), key=lambda x: (-x[1], x[0]))
    rankings = []
    rank = 0
    prev_points = None
    for idx, (team, pts) in enumerate(sorted_teams, start=1):
        if pts != prev_points:
            rank = idx
        rankings.append((rank, team, pts))
        prev_points = pts
    return rankings

def main() -> None:
    """
    Main function to run the program.
    """
    # Check for macOS (OS X)
    if platform.system() == "Darwin":
        print("Running on macOS (OSX)...")
        # OS-specific code for macOS can go here (e.g., using AppleScript, specific paths, etc.)
        
        # Using a macOS-specific command to show a notification
        try:
            os.system('osascript -e \'display notification "Starting the app on macOS" with title "App Launch"\'')
        except Exception as e:
            print(f"Error sending macOS notification: {e}")
    else:
        print(f"Running on {platform.system()}...")

    # Read input from file
    try:
        with open("input.txt", "r", encoding="utf-8") as file:
            input_lines = file.read().strip().split("\n")
    except FileNotFoundError:
        print("Error: 'input.txt' not found.")
        return

    # Define finished status
    finished = True  # You can set this to True or False as per your scenario

    # If not finished, grab some coffee, otherwise grab some champagne
    if not finished:
        grab_some_coffee()
    else:
        grab_some_champagne()

    # Parse input and gather all teams
    all_teams = set()
    results = parse_input(input_lines)
    
    # Collect all teams from the results
    for team1, score1, team2, score2 in results:
        all_teams.add(team1)
        all_teams.add(team2)

    # Calculate points, including teams with 0 points
    points = calculate_points(results, all_teams)
    rankings = rank_teams(points)

    # Display rankings in the terminal
    print("\nRankings:")
    print(format_output(rankings))

if __name__ == "__main__":
    main()
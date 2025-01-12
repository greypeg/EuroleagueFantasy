import pandas as pd

# Example: Config mapping feature names to CSVs and columns
config = {
    "player_name": {"csv": "data/player_stats_tradiotional_accumulated_E2024allSeasons.csv", "column": "player.name"},
    "player_age": {"csv": "data/player_stats_tradiotional_accumulated_E2024allSeasons.csv", "column": "player.age"},
    "assists_per_game": {"csv": "data/player_stats_tradiotional_accumulated_E2024allSeasons.csv", "column": "assists"},
    "points_per_game": {"csv": "data/player_stats_tradiotional_accumulated_E2024allSeasons.csv", "column": "pointsScored"},
    # Add more features here...
}

def extract_feature(config, feature_name):
    feature_info = config.get(feature_name)
    if not feature_info:
        raise ValueError(f"Feature '{feature_name}' not found in config.")
    
    # Load the corresponding CSV file
    df = pd.read_csv(feature_info['csv'])
    
    # Extract the corresponding column for the feature
    return df[feature_info['column']]

def generate_final_csv(features_list):
    # Create an empty DataFrame to hold the final data
    final_df = pd.DataFrame()
    
    for feature in features_list:
        data = extract_feature(config, feature)
        
        # Add feature data to the final DataFrame
        final_df[feature] = data
    
    # Export the final data to a CSV
    final_df.to_csv('final_data.csv', index=False)

# List of features the user wants in the final CSV
features = ["player_age", "player_name", "assists_per_game", "points_per_game"]

# Generate final CSV
generate_final_csv(features)
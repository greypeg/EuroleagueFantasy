import pandas as pd
from euroleague_api.boxscore_data import BoxScoreData
from euroleague_api.game_stats import GameStats
from euroleague_api.play_by_play_data import PlayByPlay
from euroleague_api.player_stats import PlayerStats
from euroleague_api.shot_data import ShotData
from euroleague_api.standings import Standings
from euroleague_api.team_stats import TeamStats

season_start=2019
season_end = 2024
roundid = 20
competition_code = "E"

#Generate Shot data current season and multiple
# shotdata = ShotData()

# shot_data_current_round = shotdata.get_game_shot_data(season_end, roundid)

# shot_data_season = shotdata.get_game_shot_data_single_season(season_end)

# shot_data_season.to_csv(
#     f"data/shotData/shot_data_{competition_code}{season_end}.csv", index=False)

# df2 = shotdata.get_game_shot_data_multiple_seasons(season_start, season_end)
# df2.to_csv(
#     f"data/shotData/shot_data_{competition_code}{season_start}-{season_end}.csv", index=False)

#Generate Boxscores
# boxscore = BoxScoreData(competition_code)

# boxscore_multiple_seasons = boxscore.get_player_boxscore_stats_multiple_seasons(season_start, season_end)
# boxscore_multiple_seasons.to_csv(
#     f"data/boxscores/boxscore_multiple_seasons_{competition_code}{season_start}-{season_end}.csv", index=False)

# team_bxs_df = boxscore.get_game_boxscore_quarter_data_single_season(season_end)
# team_bxs_df.to_csv(
#     f"data/boxscores/team_boxscore_stats_{competition_code}{season_end}.csv", index=False)

# player_bxs_df = boxscore.get_player_boxscore_stats_single_season(season_end)
# player_bxs_df.to_csv(
#     f"data/boxscores/player_boxscore_stats_{competition_code}{season_end}.csv", index=False)

#Generate GameStats
gamestats = GameStats(competition_code)
game_reports_df = gamestats.get_game_reports_range_seasons(start_season=season_start, end_season=season_end)
# game_stats_df = gamestats.get_game_stats(season_end)
game_comparison_stats_df = gamestats.get_game_teams_comparison_range_seasons(start_season=season_start, end_season=season_end)

game_reports_df.to_csv(
    f"data/game-stats/game_report_{competition_code}{season_start}-{season_end}.csv", index=False)
# game_stats_df.to_csv(
#     f"data/game-stats/game_stats_{competition_code}{season_end}.csv", index=False)
game_comparison_stats_df.to_csv(
    f"data/game-stats/game_pregame_teams_comparison_{competition_code}{season_start}-{season_end}.csv", index=False)

#Generate round standings
# standings = Standings(competition_code)
# standings_df = standings.get_standings(season=season, round_number=5)
# standings_df.to_csv(
#     f"/data/standings/standings_{competition_code}{season}_{roundid}.csv", index=False)

#Generate play by play
playbyplay = PlayByPlay(competition_code)

pbp_df = playbyplay.get_game_play_by_play_data_multiple_seasons(start_season=season_start, end_season=season_end)
pbp_df.to_csv(
    f"data/play-by-play/game_play_by_play_{competition_code}{season_start}-{season_end}.csv", index=False)

# pbp_df = playbyplay.get_pbp_data_with_lineups(season_end, gamecode, validate=True)
# pbp_df.to_csv(
#     f"/data/play-by-play/game_play_by_play_with_lineups{competition_code}-G{gamecode}{season_end}.csv", index=False)

#Generate TeamStats
teamstats = TeamStats(competition_code)

team_stats_opponentsAdvanced_df = teamstats.get_team_stats_range_seasons(
    endpoint="opponentsAdvanced", start_season=season_start, end_season=season_end, phase_type_code=None, statistic_mode="PerGame")
team_stats_opponentsAdvanced_df.to_csv(
     f"data/team-stats/team_stats_opponentsAdvanced_per_game_{competition_code}{season_start}-{season_end}.csv", index=False)

team_stats_traditional_df = teamstats.get_team_stats_range_seasons(
    endpoint="traditional", start_season=season_start, end_season=season_end, phase_type_code=None, statistic_mode="PerGame")
team_stats_traditional_df.to_csv(
     f"data/team-stats/team_stats_traditional_per_game_{competition_code}{season_start}-{season_end}.csv", index=False)

team_stats_opponentsTraditional_df = teamstats.get_team_stats_range_seasons(
    endpoint="opponentsTraditional", start_season=season_start, end_season=season_end, phase_type_code=None, statistic_mode="PerGame")
team_stats_opponentsTraditional_df.to_csv(
     f"data/team-stats/team_stats_opponentsTraditional_per_game_{competition_code}{season_start}-{season_end}.csv", index=False)

team_stats_advanced_df = teamstats.get_team_stats_range_seasons(
    endpoint="advanced", start_season=season_start, end_season=season_end, phase_type_code=None, statistic_mode="PerGame")
team_stats_advanced_df.to_csv(
     f"data/team-stats/team_stats_advanced_per_game_{competition_code}{season_start}-{season_end}.csv", index=False)

#Generate all different CSVs with player stats from a range of seasons
playerstats = PlayerStats(competition_code)

traditional_stats = playerstats.get_player_stats_range_seasons(endpoint="traditional", start_season=season_start,end_season=season_end)
traditional_stats.to_csv(
    f"data/player-stats/player_traditional_stats_pergame_{competition_code}{season_start}-{season_end}.csv", index=False)

advanced_stats = playerstats.get_player_stats_range_seasons(endpoint="advanced", start_season=season_start,end_season=season_end)
advanced_stats.to_csv(
    f"data/player-stats/player_advanced_stats_pergame_{competition_code}{season_start}-{season_end}.csv", index=False)

misc_stats = playerstats.get_player_stats_range_seasons(endpoint="misc", start_season=season_start,end_season=season_end)
misc_stats.to_csv(
    f"data/player-stats/player_misc_stats_pergame_{competition_code}{season_start}-{season_end}.csv", index=False)

scoring_stats = playerstats.get_player_stats_range_seasons(endpoint="scoring", start_season=season_start,end_season=season_end)
scoring_stats.to_csv(
    f"data/player-stats/player_scoring_stats_pergame_{competition_code}{season_start}-{season_end}.csv", index=False)
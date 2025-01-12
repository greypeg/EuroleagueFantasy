import pandas as pd
from euroleague_api.boxscore_data import BoxScoreData
from euroleague_api.game_stats import GameStats
from euroleague_api.play_by_play_data import PlayByPlay
from euroleague_api.player_stats import PlayerStats
from euroleague_api.shot_data import ShotData
from euroleague_api.standings import Standings
from euroleague_api.team_stats import TeamStats


season = 2024
roundid = 20
competition_code = "E"
# shotdata = ShotData()
# df = shotdata.get_game_shot_data(season, roundid)

# shot_data_df = shotdata.get_game_shot_data_single_season(season)
# shot_data_df.to_csv(
#     f"shot_data_{competition_code}{season}.csv", index=False)

# df2 = shotdata.get_game_shot_data_multiple_seasons(2022, season)


# boxscore = BoxScoreData(competition_code)
# team_bxs_df = boxscore.get_game_boxscore_quarter_data_single_season(season)
# player_bxs_df = boxscore.get_player_boxscore_stats_single_season(season)
# player_bxs_df.to_csv(
#     f"player_boxscore_stats_{competition_code}{season}.csv", index=False)

# team_bxs_df.to_csv(
#     f"team_boxscore_stats_{competition_code}{season}.csv", index=False)
# gamestats = GameStats(competition_code)
# game_reports_df = gamestats.get_game_reports_single_season(season)
# game_stats_df = gamestats.get_game_stats_single_season(season)
# game_comparison_stats_df = gamestats.get_game_teams_comparison_single_season(season)

# game_reports_df.to_csv(
#     f"game_report_{competition_code}{season}.csv", index=False)
# game_stats_df.to_csv(
#     f"game_stats_{competition_code}{season}.csv", index=False)
# game_comparison_stats_df.to_csv(
#     f"game_pregame_teams_comparison_{competition_code}{season}.csv", index=False)
# standings = Standings(competition_code)
# standings_df = standings.get_standings(season=season, round_number=5)
# standings_df.to_csv(
#     f"standings_{competition_code}{season}_{roundid}.csv", index=False)
# playbyplay = PlayByPlay(competition_code)
# pbp_df = playbyplay.get_game_play_by_play_data_single_season(season)
# pbp_df.to_csv(
#     f"game_play_by_play_{competition_code}{season}.csv", index=False)

# teamstats = TeamStats(competition_code)
# team_stats_df = teamstats.get_team_stats_single_season(
#     endpoint="advanced", season=season, phase_type_code=None, statistic_mode="PerGame")

# team_stats_df.to_csv(
#     f"team_stats_advanced_per_game_{competition_code}{season}.csv", index=False)

playerstats = PlayerStats(competition_code)

player_stats_df_perGame = playerstats.get_player_stats_all_seasons(

    endpoint="advanced", phase_type_code=None, statistic_mode="Accumulated")

# player_stats_df_accumulated = playerstats.get_player_stats_all_seasons(

#     endpoint="advanced", phase_type_code=None, statistic_mode="Accumulated")

# player_stats_df_per100Possesions = playerstats.get_player_stats_all_seasons(

#     endpoint="advanced", phase_type_code=None, statistic_mode="Per100Possesions")    

# player_stats_df_accumulated.to_csv(
#     f"player_stats_advanced_accumulated_{competition_code}'allSeasons.csv", index=False)

# player_stats_df_per100Possesions.to_csv(
#     f"player_stats_advanced_per100possesions_{competition_code}{season}allSeasons.csv", index=False)

player_stats_df_perGame.to_csv(
    f"player_stats_advanced_accumulated_{competition_code}{season}allSeasons.csv", index=False)
from soccer.teams.models import seasons_with_stats_by_team

def prime_cache():
    """
    A list of functions to use to prime the cache
    so that a random user doesn't have to sit around waiting for them.
    """
    # Turn this into something that you register a frequency for...
    # Run periodically
    seasons_with_stats_by_team()

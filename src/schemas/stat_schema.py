from main import ma


class StatSchema(ma.Schema):
    class Meta:
        fields = ["stats_id", "games_played", "goals",
                  "position", "avg_disposals", "avg_tackles", "avg_marks", "player_id"]


# a single stat schema
stat_schema = StatSchema()
# multiple stats schema
stats_schema = StatSchema(many=True)

from flask import Blueprint
from main import db
from models.clubs import Club
from models.coaches import Coach
from models.doctors import Doctor
from models.players import Player
from models.stats import Stat
from datetime import date


db_commands = Blueprint("db", __name__)


@db_commands.cli.command('create')
def create_db():
    # Tell SQLAlchemy to create all tables for all AFL models in the physical DB
    db.create_all()
    print('Tables created')


@db_commands.cli.command('drop')
def drop_db():
    # Tell SQLAlchemy to drop all tables
    db.drop_all()
    print('Tables dropped')


@db_commands.cli.command('seed')
def seed_db():
    # Create a new Club entry (in memory)
    club1 = Club(
        club_name="Western Bulldogs",
        city_located="Melbourne",
        year_established=1877
    )
    # Add the new club to the current transaction (in memory)
    db.session.add(club1)

    # Create a new Coach entry (in memory)
    coach1 = Coach(
        c_first_name="Luke",
        c_last_name="Beveridge",
        coach_type="Head Coach",
        years_coached=8,
        club_id=1
    )
    # Add the new coach to the current transaction (in memory)
    db.session.add(coach1)

    # Create a new Doctor entry (in memory)
    doctor1 = Doctor(
        d_first_name="Gary",
        d_last_name="Zimmerman",
        years_served=26,
        club_id=1
    )
    # Add the new Doctor to the current transaction (in memory)
    db.session.add(doctor1)

    # Create a new Player entry (in memory)
    player1 = Player(
        p_first_name="Marcus",
        p_last_name="Bontempelli",
        p_dob=date(day=24, month=11, year=1995),
        p_salary=900000,
        club_id=1
    )
    # Add the new Player to the current transaction (in memory)
    db.session.add(player1)

    # Create a new Stat entry (in memory)
    stat1 = Stat(
        games_played=191,
        goals=178,
        position="Midfielder",
        avg_disposals=25,
        avg_tackles=4,
        avg_marks=7,
        player_id=1
    )
    # Add the new Player to the current transaction (in memory)
    db.session.add(stat1)

    # Commit the transaction to the physical DB
    db.session.commit()

    print('Table seeded')

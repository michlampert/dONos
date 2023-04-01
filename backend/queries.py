from sqlalchemy.sql import text

from setup import app, db


def get_company_id(name: str):
    results = db.session.execute(
        text('select CompanyID from Company where Name = :name'), 
        {'name': name}
    ).fetchone()

    return results[0]

def get_leaderboard(company: str):
    results = db.session.execute(
        text('select LeaderboardID from Leaderboard where CompanyID = :company'), 
        {'company': company}
    ).fetchone()

    return results[0]

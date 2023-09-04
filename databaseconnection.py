import sqlite3
from functools import lru_cache

from GroovyRevived.song import Song


class DatabaseConnection:
    filename: str = "database.db"

    @lru_cache(maxsize=0)
    def get_connection(self):
        return sqlite3.connect(self.filename)

    def add_song_to_db(self, song: Song, user: str):
        with self.get_connection() as conn:
            conn.execute(
                """
                INSERT INTO GroovyHistory(title,user,count)
                VALUES ( ?, ?, ?)
                ON CONFLICT(title,user) DO UPDATE SET count=count+1
                """
                ,
                (song.title, user, 1)
            )

    def show_top_songs(self):
        with self.get_connection() as conn:
            return conn.execute(
                """
                SELECT title, SUM(count) AS count
                FROM GroovyHistory
                GROUP BY title
                ORDER BY count DESC
                LIMIT 10
                """
            )

    def show_top_users(self):
        with self.get_connection() as conn:
            return conn.execute(
                """
                SELECT user, SUM(count) AS count
                FROM GroovyHistory
                GROUP BY user
                ORDER BY count DESC
                LIMIT 10
                """
            )

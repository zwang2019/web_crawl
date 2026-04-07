from pathlib import Path
import sqlite3

PROJECT_ROOT = Path(__file__).resolve().parent.parent
DB_PATH = PROJECT_ROOT / "data" / "storage.db"
SQL_PATH = PROJECT_ROOT / "SQLs" / "sqlite_init.sql"

print(f"SQL_PATH: {SQL_PATH}")
print(f"DB_PATH: {DB_PATH}")


def init_sqlite() -> None:
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)

    with sqlite3.connect(DB_PATH) as conn:
        conn.execute("PRAGMA foreign_keys = ON;")
        conn.execute("PRAGMA busy_timeout = 5000;")

        sql = SQL_PATH.read_text(encoding="utf-8")
        conn.executescript(sql)
        conn.commit()

    print(f"SQLite initialized successfully: {DB_PATH}")


if __name__ == "__main__":
    init_sqlite()
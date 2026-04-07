--
PRAGMA foreign_keys = ON;
PRAGMA journal_mode = WAL;
PRAGMA synchronous = NORMAL;
PRAGMA temp_store = MEMORY;
PRAGMA busy_timeout = 5000;

CREATE TABLE IF NOT EXISTS ops_schema_migrations (
    version      TEXT PRIMARY KEY,
    applied_at   TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS suning_books (
    id            INTEGER PRIMARY KEY,
    book_name     TEXT NOT NULL,
    book_price    REAL NOT NULL,
    book_shop     TEXT NOT NULL,
    created_at    TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(book_name, book_shop)
);


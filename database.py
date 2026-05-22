"""
database.py — SQLite setup and all query helpers.

"""

import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).parent / "db" / "translations.db"


def get_connection() -> sqlite3.Connection:
    """Return a connection with row_factory so rows behave like dicts."""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db() -> None:
    """Create tables if they don't exist yet. Safe to call on every startup."""
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    conn = get_connection()
    cur = conn.cursor()

    cur.executescript("""
        CREATE TABLE IF NOT EXISTS translations (
            translation_id          INTEGER PRIMARY KEY AUTOINCREMENT,
            german_text             TEXT    NOT NULL UNIQUE,
            audio_path              TEXT,
            created_at              DATETIME DEFAULT CURRENT_TIMESTAMP
        );
    """)

    conn.commit()
    conn.close()


# ── Translation CRUD ──────────────────────────────────────────────────────────────────

def insert_translation(german_text: str, audio_path: str) -> int:
    """Insert a new translation row. Returns the new translation id."""
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO translations (german_text, audio_path) VALUES (?, ?)",
        (german_text, audio_path),
    )
    translation_id = cur.lastrowid
    conn.commit()
    conn.close()
    return translation_id


def get_all_translations() -> list[dict]:
    conn = get_connection()
    rows = conn.execute("SELECT * FROM translations ORDER BY created_at DESC").fetchall()
    conn.close()
    return [dict(r) for r in rows]


def get_translation(translation_id: int) -> dict | None:
    conn = get_connection()
    row = conn.execute("SELECT * FROM translations WHERE translation_id = ?", (translation_id,)).fetchone()
    conn.close()
    return dict(row) if row else None


def delete_translation(translation_id: int) -> bool:
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM translations    WHERE translation_id       = ?", (translation_id,))
    deleted = cur.rowcount > 0
    conn.commit()
    conn.close()
    return deleted

from sqlalchemy import text
from sqlalchemy.orm import Session


def check_connection(session: Session) -> dict:
    try:
        session.execute(text("SELECT 1"))
        return {
            "Status": "Success",
            "Detail": "Connection to database is successful",
            "Host": session.bind.url.host,
            "Database": session.bind.url.database,
            "Query": session.bind.url.query,
        }
    except Exception as e:
        return {
            "Status": "Failed",
            "Detail": str(e),
        }
    finally:
        session.close()

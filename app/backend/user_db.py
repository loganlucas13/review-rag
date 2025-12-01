from typing import List
from psycopg2.extensions import cursor
from postgres_login import login
from querylog_db import remove_user_querylogs


# Create 'User' table in database (if it doesn't exist)
# Returns True if successful, False otherwise
def setup_user_db(cursor: cursor) -> bool:
    try:
        create_user_table_query = """
            CREATE TABLE IF NOT EXISTS "User" (
                id SERIAL PRIMARY KEY,
                name VARCHAR(50) NOT NULL,
                email VARCHAR(100) NOT NULL UNIQUE,
                role VARCHAR(7) NOT NULL CHECK(role IN ('EndUser', 'Admin', 'Curator')),
                username VARCHAR(20) NOT NULL UNIQUE,
                password VARCHAR(255) NOT NULL,
                last_activity_timestamp TIMESTAMP DEFAULT (CURRENT_TIMESTAMP AT TIME ZONE 'America/Chicago')
            );
        """
        cursor.execute(create_user_table_query)
        return True
    except Exception as e:
        print(f"Error while creating User table: {e}")
        return False


# Add a user to the user database
def add_user(role: str, username: str, password: str, name: str, email: str) -> bool:
    try:
        add_user_query = """
            INSERT INTO "User" (role, username, password, name, email)
            VALUES (%s, %s, %s, %s, %s);
        """

        cursor = login()
        cursor.execute(add_user_query, (role, username, password, name, email))
        cursor.close()
        return True
    except Exception as e:
        print(f"Error while adding user: {e}")
        return False


# Remove a user from the user database
def remove_user(user_id: int) -> bool:
    try:
        get_role_query = """
            SELECT role
            FROM "User"
            WHERE id = %s;
        """

        remove_user_query = """
            DELETE FROM "User"
            WHERE id = %s;
        """

        cursor = login()
        cursor.execute(get_role_query, (user_id,))
        role = cursor.fetchone()[0]

        # remove all query logs if user is an EndUser
        if role == "EndUser":
            status = remove_user_querylogs(user_id)
            if not status:
                raise Exception("Error while removing user query logs.")

        cursor.execute(remove_user_query, (user_id,))
        cursor.close()
        return True
    except Exception as e:
        print(f"Error while deleting user: {e}")
        return False


# Log in user with 'username' and 'password'
def log_in_user(username: str, password: str) -> tuple[bool, int, str]:
    try:
        log_in_user_query = """
            SELECT id, role FROM "User"
            WHERE username = %s AND password = %s;
        """

        cursor = login()
        cursor.execute(log_in_user_query, (username, password))
        result = cursor.fetchone()
        cursor.close()

        if not result:
            return (False, -1, "")
        return True, result[0], result[1]
    except Exception as e:
        print(f"Error while logging in user: {e}")
        return False, -1, ""


# Gets all users from the 'User' table
def get_all_users() -> List[dict]:
    try:
        get_all_users_query = """
            SELECT id, name, email, role, username, password, last_activity_timestamp
            FROM "User"
            ORDER BY id;
        """

        cursor = login()
        cursor.execute(get_all_users_query)
        results = cursor.fetchall()
        cursor.close()

        users = []
        for result in results:
            users.append(
                {
                    "id": result[0],
                    "name": result[1],
                    "email": result[2],
                    "role": result[3],
                    "username": result[4],
                    "password": result[5],
                    "last_activity_timestamp": str(result[6]) if result[6] else None,
                }
            )
        return users
    except Exception as e:
        print(f"Error while logging in user: {e}")
        return []


# Updates the user with 'user_id' with new attributes (parameters)
def edit_user(user_id, role, username, password, name, email) -> bool:
    try:
        edit_user_query = """
        UPDATE "User"
        SET role = %s, username = %s, password = %s, name = %s, email = %s
        WHERE id = %s;
        """

        cursor = login()
        cursor.execute(
            edit_user_query, (role, username, password, name, email, user_id)
        )
        cursor.close()
        return True
    except Exception as e:
        print(f"Error while editing user: {e}")
        return False


# Updates the timestamp of a user to the current time
def update_user_timestamp(user_id: int) -> bool:
    try:
        update_timestamp_query = """
            UPDATE "User"
            SET last_activity_timestamp = NOW() AT TIME ZONE 'America/Chicago'
            WHERE id = %s;
        """

        cursor = login()
        cursor.execute(update_timestamp_query, (user_id,))
        cursor.close()
        return True
    except Exception as e:
        print(f"Error while updating user timestamp: {e}")
        return False

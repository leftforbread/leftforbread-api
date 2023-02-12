import logging
import os
import random
import time
from argparse import ArgumentParser, RawTextHelpFormatter

from datetime import date

import psycopg
from psycopg.errors import SerializationFailure, Error
from psycopg.rows import namedtuple_row

DATABASE_URL="postgresql://jaycee:_JyGFbsyg9IvjclwMKOeNQ@older-mink-8935.7tt.cockroachlabs.cloud:26257/sec?sslmode=verify-full"

cur_user = " "

def create_accounts(conn, username, password):
    with conn.cursor() as cur:
        cur.execute(
            "INSERT INTO user_info (username, pass, health_tag, diet_tags) VALUES (%s, %s, ARRAY[], ARRAY[])", (username, password,))
        logging.debug("create_accounts(): status message: %s",
                      cur.statusmessage)


def delete_accounts(conn, username):
    with conn.cursor() as cur:
        cur.execute("DELETE FROM user_info WHERE username == %s", (username,))
        logging.debug("delete_accounts(): status message: %s",
                      cur.statusmessage)

def add_htag(conn, username, tag):
    with conn.cursor() as cur:
        cur.execute("UPDATE user_info SET health_tag = array_append(health_tag, %s) WHERE username = %s", (tag, username,))
    logging.debug("add_htag(): status message: %s",
                      cur.statusmessage)

def add_dtag(conn, username, tag):
    with conn.cursor() as cur:
        cur.execute("UPDATE user_info SET diet_tags = array_append(diet_tags, %s) WHERE username = %s", (tag, username,))
    logging.debug("add_dtag(): status message: %s",
                      cur.statusmessage)

def get_htag(conn, username):
    with conn.cursor() as cur:
        cur.execute("SELECT health_tag FROM user_info WHERE username = %s", (username,))
        return cur.fetchone()

def get_dtag(conn, username):
    with conn.cursor() as cur:
        cur.execute("SELECT diet_tags FROM user_info WHERE username = %s", (username,))
        return cur.fetchone()
    

def add_favorite(conn, username, recipie):
    with conn.cursor() as cur:
        cur.execute("INSERT INTO favorites (user, recipie_id) VALUES (%s, %s)", (username, recipie,))
    logging.debug("create_accounts(): status message: %s",
                      cur.statusmessage)

def remove_favorite(conn, username, recipie):
    with conn.cursor() as cur:
        cur.execute("DELETE FROM favorites WHERE username == %s AND recipie == %s", (username, recipie))

def create_plan(conn, recipies, user):
    with conn.cursor() as cur:
        cur.execute("INSERT INTO weekly_plans (b_1, b_2, b_3, b_4, b_5, b_6, b_7, l_1, l_2, l_3, l_4, l_5, l_6, l_7, d_1, d_2, d_3, d_4, d_5, d_6, d_7, user, date) VALUES (%d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d,, %s)", (recipies[0], recipies[1], recipies[2], recipies[3], recipies[4], recipies[5], recipies[6], recipies[7], recipies[8], recipies[9], recipies[10], recipies[11], recipies[12], recipies[13], recipies[14], recipies[15], recipies[16], recipies[17], recipies[18], recipies[19], recipies[20], user, date.today(),))
    logging.debug("create_accounts(): status message: %s",
                      cur.statusmessage)

def get_plan(conn, user):
    with conn.cursor() as cur:
        cur.execute("SELECT * FROM weekly_plans WHERE d = (SELECT MAX(d) FROM weekly_plans WHERE username = %s)", (user,))
        return cur.fetchall()

def get_favorites(conn, user):
    with conn.cursor() as cur:
        cur.execute("SELECT * FROM favorites WHERE username == %s", (user,))
        return cur.fetchall()

def login(conn, name, passw):
    with conn.cursor() as cur:
        cur.execute("SELECT username FROM user_info WHERE (username = %s AND pass = %s)", (name, passw,))
        ret = cur.fetchone()
        if ret == None:
            print("Login Failed")
        else:
            print("Login Success")
            return ret


def start():
    opt = parse_cmdline()
    logging.basicConfig(level=logging.DEBUG if opt.verbose else logging.INFO)
    db_url = "postgresql://jaycee:_JyGFbsyg9IvjclwMKOeNQ@older-mink-8935.7tt.cockroachlabs.cloud:26257/sec?sslmode=verify-full"
    conn = psycopg.connect(db_url, 
                            application_name="$ docs_simplecrud_psycopg3", 
                            row_factory=namedtuple_row)
    return conn




def main():
    conn = start()
    create_accounts(conn, "tester", "a")
    cur_user = login(conn, "tester", "a")
    print(cur_user)


def parse_cmdline():
    parser = ArgumentParser(description=__doc__,
                            formatter_class=RawTextHelpFormatter)

    parser.add_argument("-v", "--verbose",
                        action="store_true", help="print debug info")

    parser.add_argument(
        "dsn",
        default=os.environ.get("DATABASE_URL"),
        nargs="?",
        help="""\
database connection string\
 (default: value of the DATABASE_URL environment variable)
            """,
    )

    opt = parser.parse_args()
    if opt.dsn is None:
        parser.error("database connection string not set")
    return opt


if __name__ == "__main__":
    main()
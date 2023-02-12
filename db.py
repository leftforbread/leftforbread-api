import logging
import os
import random
import time
from argparse import ArgumentParser, RawTextHelpFormatter

from datetime import date

import psycopg
from psycopg.errors import SerializationFailure, Error
from psycopg.rows import namedtuple_row

DATABASE_URL="postgresql://jaycee:k6vLAmPNu_D6e9i5WE9TJg@older-mink-8935.7tt.cockroachlabs.cloud:26257/sec?sslmode=verify-full"


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
        return cur.execute("SELECT health_tag FROM user_info WHERE username = %s", (username,))

def get_dtag(conn, username):
    with conn.cursor() as cur:
        cur.execute("SELECT diet_tags FROM user_info WHERE username = %s", (username,))
        print(cur.fetchone())
    

def add_favorite(conn, username, recipie):
    with conn.cursor() as cur:
        cur.execute("INSERT INTO favorites (user, recipie_id) VALUES (%s, %s)", (username, recipie,))
    logging.debug("create_accounts(): status message: %s",
                      cur.statusmessage)

def create_plan(conn, recipies, user):
    with conn.cursor() as cur:
        cur.execute("INSERT INTO weekly_plans (b_1, b_2, b_3, b_4, b_5, b_6, b_7, l_1, l_2, l_3, l_4, l_5, l_6, l_7, d_1, d_2, d_3, d_4, d_5, d_6, d_7, user, date) VALUES (%d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d,, %s)", (recipies[0], recipies[1], recipies[2], recipies[3], recipies[4], recipies[5], recipies[6], recipies[7], recipies[8], recipies[9], recipies[10], recipies[11], recipies[12], recipies[13], recipies[14], recipies[15], recipies[16], recipies[17], recipies[18], recipies[19], recipies[20], user, date.today(),))
    logging.debug("create_accounts(): status message: %s",
                      cur.statusmessage)

#def get_plan(conn, user,)




def run_transaction(conn, op, max_retries=3):
    """
    Execute the operation *op(conn)* retrying serialization failure.

    If the database returns an error asking to retry the transaction, retry it
    *max_retries* times before giving up (and propagate it).
    """
    # leaving this block the transaction will commit or rollback
    # (if leaving with an exception)
    with conn.transaction():
        for retry in range(1, max_retries + 1):
            try:
                op(conn)

                # If we reach this point, we were able to commit, so we break
                # from the retry loop.
                return

            except SerializationFailure as e:
                # This is a retry error, so we roll back the current
                # transaction and sleep for a bit before retrying. The
                # sleep time increases for each failed transaction.
                logging.debug("got error: %s", e)
                conn.rollback()
                logging.debug("EXECUTE SERIALIZATION_FAILURE BRANCH")
                sleep_seconds = (2**retry) * 0.1 * (random.random() + 0.5)
                logging.debug("Sleeping %s seconds", sleep_seconds)
                time.sleep(sleep_seconds)

            except psycopg.Error as e:
                logging.debug("got error: %s", e)
                logging.debug("EXECUTE NON-SERIALIZATION_FAILURE BRANCH")
                raise e

        raise ValueError(
            f"transaction did not succeed after {max_retries} retries")


def main():
    opt = parse_cmdline()
    logging.basicConfig(level=logging.DEBUG if opt.verbose else logging.INFO)
    try:
        # Attempt to connect to cluster with connection string provided to
        # script. By default, this script uses the value saved to the
        # DATABASE_URL environment variable.
        # For information on supported connection string formats, see
        # https://www.cockroachlabs.com/docs/stable/connect-to-the-database.html.
        db_url = "postgresql://jaycee:k6vLAmPNu_D6e9i5WE9TJg@older-mink-8935.7tt.cockroachlabs.cloud:26257/sec?sslmode=verify-full"
        conn = psycopg.connect(db_url, 
                               application_name="$ docs_simplecrud_psycopg3", 
                               row_factory=namedtuple_row)
        #ids = create_accounts(conn)
        #create_accounts(conn, "test" , "123")
            
        #toId = ids.pop()
        #fromId = ids.pop()

        try:
            create_accounts(conn, "tester" , "123")
            add_dtag(conn, "tester", "a")
            get_dtag(conn, "tester")
            #run_transaction(conn, lambda conn:  create_accounts(conn, "test" , "123"))
        except ValueError as ve:
            # Below, we print the error and continue on so this example is easy to
            # run (and run, and run...).  In real code you should handle this error
            # and any others thrown by the database interaction.
            logging.debug("run_transaction(conn, op) failed: %s", ve)
            pass
        except psycopg.Error as e:
            logging.debug("got error: %s", e)
            raise e


    except Exception as e:
        logging.fatal("database connection failed")
        logging.fatal(e)
        return


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
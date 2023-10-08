from .connection import connection

def create_tables():
    try:
        with connection() as (cur, conn):
            sql = """
            create table if not exists file(
                id serial,
                filename varchar(15),
                id_proyect integer unique
            );
            """
            cur.execute(sql)
            conn.commit()

    except Exception as e:
        print(e)
import sqlite3


def insert_colors():
    with sqlite3.connect("animal.db") as conn:
        conn.cursor()
        querry = '''INSERT INTO color(color)
                    VALUES'''
        for color in ['orange', 'blue ', 'white', 'black', 'brown', 'brown ', 'seal', 'Breed Specific', 'blue',
                      'cream ', 'chocolate', 'orange ', 'silver', 'flame', 'cream', 'lynx', 'seal ', 'lilac', 'buff',
                      'blue cream', 'black ', 'silver lynx', 'gray', 'gray ', 'yellow', 'apricot', 'lynx ',
                      'chocolate ', 'silver ', 'lilac ', 'brown tiger', 'black tiger', 'tan', 'orange tiger', 'flame ',
                      'silver lynx ', 'sable', 'pink', 'brown merle', 'fawn']:
            querry += f"('{color}'),"
        querry = querry[:-1]
        conn.execute(querry)


def update_my_table_with_color1_id():
    with sqlite3.connect("animal.db") as conn:
        conn.row_factory = sqlite3.Row
        result = conn.execute('''SELECT *
                                FROM color c
                                ''').fetchall()

        for i in result:
            value = dict(i)

            conn.execute(f'''
                         UPDATE my_table
                         SET color1 = {value["id"]}
                         where color1 = '{value["color"]}'
                         ''')


def update_my_table_with_color2_id():
    with sqlite3.connect("animal.db") as conn:
        conn.row_factory = sqlite3.Row
        result = conn.execute('''SELECT *
                                FROM color c
                                ''').fetchall()

        for i in result:
            if i is None:
                continue
            else:
                value = dict(i)

                conn.execute(f'''
                             UPDATE my_table
                             SET color2 = {value["id"]}
                             where color2 = '{value["color"]}'
                            ''')


def insert_breeds():
    with sqlite3.connect("animal.db") as conn:
        conn.cursor()
        querry = '''INSERT INTO breeds(breed)
                    VALUES'''
        for breed in ['domestic shorthair', 'domestic mediumhair', 'siamese', 'russian blue', 'domestic longhair',
                      'manx', 'ragdoll', 'snowshoe/domestic shorthair', 'snowshoe', 'angora', 'himalayan',
                      'domestic longhair/persian', 'japanese bobtail', 'domestic longhair/rex',
                      'siamese/domestic shorthair', 'domestic mediumhair/siamese', 'maine coon', 'devon rex',
                      'balinese', 'american shorthair', 'british shorthair', 'angora/persian', 'munchkin shorthair',
                      'domestic shorthair/siamese', 'manx/domestic longhair', 'persian', 'cymric', 'tonkinese',
                      'siamese/angora', 'burmese', 'sphynx', 'domestic shorthair/domestic mediumhair', 'bengal',
                      'domestic longhair/russian blue', 'bombay', 'exotic shorthair',
                      'domestic shorthair/british shorthair', 'abyssinian', 'manx/domestic shorthair',
                      'norwegian forest cat', 'snowshoe/ragdoll', 'manx/siamese', 'turkish van', 'cornish rex',
                      'birman', 'american curl shorthair', 'siamese/japanese bobtail', 'havana brown',
                      'munchkin longhair', 'bengal/domestic shorthair', 'domestic shorthair/domestic shorthair',
                      'pixiebob shorthair', 'american wirehair', 'domestic mediumhair/maine coon',
                      'domestic shorthair/maine coon', 'scottish fold', 'oriental sh', 'chartreux', 'turkish angora',
                      'javanese', 'domestic shorthair/manx', 'domestic longhair/domestic longhair',
                      'domestic shorthair/abyssinian', 'ocicat', 'domestic mediumhair/manx']:
            querry += f"('{breed}'),"
        querry = querry[:-1]
        conn.execute(querry)


def update_my_table_with_breeds_id():
    with sqlite3.connect("animal.db") as conn:
        conn.row_factory = sqlite3.Row
        result = conn.execute('''SELECT *
                                FROM breeds
                                ''').fetchall()

        for i in result:
            if i is None:
                continue
            else:
                value = dict(i)

                conn.execute(f'''
                             UPDATE my_table
                             SET breed = {value["id"]}
                             where breed = '{value["breed"]}'
                            ''')


def create_tables_for_outcome():
    with sqlite3.connect('animal.db') as conn:
        conn.cursor()
        querry1 = '''CREATE TABLE outcome_type(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name VARCHAR(20)
                    )'''
        querry2 = '''CREATE TABLE outcome_subtype(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    type_id INTEGER,
                    name VARCHAR(20),
                    FOREIGN KEY (type_id) REFERENCES outcome_type(id)
                    )'''
        conn.execute(querry1)
        conn.execute(querry2)


def insert_outcome_type():
    with sqlite3.connect("animal.db") as conn:
        conn.cursor()
        querry = '''INSERT INTO outcome_type(name)
                    VALUES'''
        for name in ['Transfer', 'Adoption', 'Return to Owner', 'Died', 'Euthanasia', 'Missing', 'Disposal',
                     'Rto-Adopt', '']:
            querry += f"('{name}'),"
        querry = querry[:-1]
        conn.execute(querry)


def update_my_table_with_outcome_type():
    with sqlite3.connect("animal.db") as conn:
        conn.row_factory = sqlite3.Row
        result = conn.execute('''SELECT *
                                FROM outcome_type
                                ''').fetchall()

        for i in result:
            if i is None:
                continue
            else:
                value = dict(i)

                conn.execute(f'''
                             UPDATE my_table
                             SET outcome_type = {value["id"]}
                             where outcome_type = '{value["name"]}'
                            ''')


def insert_outcome_subtype():
    with sqlite3.connect("animal.db") as conn:
        conn.cursor()
        querry1 = '''INSERT INTO outcome_subtype(name)
                    VALUES'''
        for name in ['Partner', 'Undef', 'Offsite', 'SCRP', 'Foster', 'In Kennel', 'Suffering', 'Rabies Risk',
                     'Medical', 'At Vet', 'In Foster', 'Enroute', 'Aggressive', 'Barn', 'Snr', 'Possible Theft',
                     'In Surgery', 'Underage']:
            querry1 += f"('{name}'),"
        querry1 = querry1[:-1]
        conn.execute(querry1)


def update_type_id_in_subtype():
    with sqlite3.connect("animal.db") as conn:
        conn.row_factory = sqlite3.Row
        result = conn.execute('''SELECT outcome_type, outcome_subtype
                                        FROM my_table
                                        ''').fetchall()

        for i in result:
            if None in i:
                continue
            else:
                value = dict(i)

                conn.execute(f'''
                                 UPDATE outcome_subtype
                                 SET type_id = {value["outcome_type"]}
                                 where name = '{value["outcome_subtype"]}'
                                 ''')

# update_type_id_in_subtype()

# insert_outcome_subtype()

# update_my_table_with_outcome_type()

# insert_outcome_type()

# create_tables_for_outcome()

# update_my_table_with_breeds_id()

# insert_breeds()

# update_my_table_with_color2_id()

# update_my_table_with_color1_id()

# insert_colors()

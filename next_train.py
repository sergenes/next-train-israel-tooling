import sqlite3

conn = sqlite3.connect('nt.db')

rishon = 0
sheni = 1
shlishi = 2
revii = 3
chameshi = 4
shishi = 5
shabat = 6


def query_train_stops(train_id, day_of_week):
    cursor = conn.execute(f"""
        SELECT SH.*, ST.ZNAME, ST.ZNAMEHE, ST.ZNAMERU, ST.ZNAMEAR
            FROM ZTLSCHEDULE AS SH
            INNER JOIN ZTLSTATIONS AS ST ON SH.ZSTATIONID = ST.ZSTATIONID
        WHERE SH.ZTRAINNUMBER = {train_id}
        AND ZDAYOFWEEK = {day_of_week}
        ORDER BY SH.ZTIME ASC;
    """)

    print(" P :  Time  : Name")
    print("---:--------:---------------")
    for row in cursor:
        print(" " + str(row[3]) + " : " + row[11] + "  : " + str(row[14]))
    conn.close()


def query_time_table(station_id, day_of_week, hour, filter_direction=None):
    cursor = conn.execute(f"""
        SELECT SH.*, ST.ZNAME, ST.ZNAMEHE, ST.ZNAMERU, ST.ZNAMEAR
            FROM ZTLSCHEDULE AS SH
            INNER JOIN ZTLSTATIONS AS ST ON SH.ZDESTINATIONID = ST.ZSTATIONID
        WHERE SH.ZSTATIONID = {station_id}
        AND ZDESTINATIONID != {station_id}
        AND ZHOUR >= {hour}
        AND ZDAYOFWEEK = {day_of_week}
        ORDER BY SH.ZTIME ASC;
    """)

    print("Time  : P : Di : Train : Name")
    print("------:---:----:-------:-----------")
    for row in cursor:
        # print(row)
        direction = row[5]
        if direction == 0 and filter_direction != 0:
            print("\033[31m" + row[11] + " : " + str(row[3]) + " : NS :   " + str(row[2]) + " : " + row[14] + '\033[0m')
        elif direction == 2 and filter_direction != 2:
            print("\033[32m" + row[11] + " : " + str(row[3]) + " : WE :   " + str(row[2]) + " : " + row[14] + '\033[0m')
        elif direction == 3 and filter_direction != 3:
            print("\033[33m" + row[11] + " : " + str(row[3]) + " : EW :   " + str(row[2]) + " : " + row[14] + '\033[0m')
        elif direction == 1 and filter_direction != 1:
            print("\033[34m" + row[11] + " : " + str(row[3]) + " : SN :   " + str(row[2]) + " : " + row[14] + '\033[0m')
    conn.close()


def query_all_stations():
    cursor = conn.execute("SELECT * FROM 'ZTLSTATIONS'")
    for row in cursor:
        print(row)
    conn.close()


def main():
    query_all_stations()
    query_time_table('3100', chameshi, 9)
    query_train_stops(227, chameshi)


if __name__ == '__main__':
    main()
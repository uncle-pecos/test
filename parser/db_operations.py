from __future__ import print_function

import mysql.connector
from mysql.connector import errorcode

#def insert_to_table(table_name, build_number,avg_metric,min_metric,max_metric,conn,cursor):
def insert_to_table(table_name,build_number,conn,cursor,data_list, comment):
    #sql = "INSERT INTO  (build_number, avg_metric,min_metric, max_metric ) VALUES (%s, %s, %s, %s)"
    val = (build_number, data_list[0],data_list[1],data_list[2], data_list[3], data_list[4], data_list[5],
           data_list[6],data_list[7],data_list[8],data_list[9],data_list[10],data_list[11],data_list[12],
           data_list[13],data_list[14],data_list[15],data_list[16],data_list[17],data_list[18],data_list[19],data_list[20],
           data_list[21],data_list[22],data_list[23],data_list[24],data_list[25],data_list[26],data_list[27],data_list[28],
           data_list[29],data_list[30],data_list[31],data_list[32],data_list[33],data_list[34],data_list[35],comment)
    try:
        cursor.execute(f"""
        INSERT INTO {table_name} (build_number, invalidStats, fps_0_5,fps_6_10, fps_11_15, fps_16_20, 
                fps_21_25, fps_26_30, fps_31_35, fps_36_40, fps_41_45, fps_46_50,
                fps_51_55, fps_56_60, fps_gt_60, fpsDeviation, fpsMin5s, fpsMin5sFixTime,
                fpsMin2sFixTime, fpsMin2s, fpsMax, fpsAvg, fpsAvgAlt, availableVirtualMemory,
                peakVirtualMemoryUsage, graphicsDriverHeapMax, graphicsDriverHeapAvg, videoMemoryMax,
                videoMemoryAvg, scaleformHeapMax, scaleformHeapAvg, wwiseHeapMax, wwiseHeapAvg, genericMemoryHeapMax, genericMemoryHeapAvg,
                totalHeapMax, totalHeapAvg, comment)
        VALUES (%s, %s, %s, %s, %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s )""", val)


    except mysql.connector.Error as err:
        if err.errno == 1062:
            cursor.execute(f"""
                    UPDATE {table_name}
                    SET build_number = %s, invalidStats = %s, fps_0_5 = %s,fps_6_10 = %s, fps_11_15 = %s, fps_16_20 = %s, 
                fps_21_25 = %s, fps_26_30 = %s, fps_31_35 = %s, fps_36_40 = %s, fps_41_45 = %s, fps_46_50 = %s,
                fps_51_55 = %s, fps_56_60 = %s, fps_gt_60 = %s, fpsDeviation = %s, fpsMin5s = %s, fpsMin5sFixTime = %s,
                fpsMin2sFixTime = %s, fpsMin2s = %s, fpsMax = %s, fpsAvg = %s, fpsAvgAlt = %s, availableVirtualMemory = %s,
                peakVirtualMemoryUsage = %s, graphicsDriverHeapMax = %s, graphicsDriverHeapAvg = %s, videoMemoryMax = %s,
                videoMemoryAvg = %s, scaleformHeapMax = %s, scaleformHeapAvg = %s, wwiseHeapMax = %s, wwiseHeapAvg = %s, 
                genericMemoryHeapMax = %s, genericMemoryHeapAvg = %s,
                totalHeapMax = %s, totalHeapAvg = %s, comment = %s
                    WHERE build_number = {build_number}
                            """,val)
            conn.commit()
        else:
            #print("Error: ", err)
            print("Error: ", err)
    else:
        conn.commit()


def show_data(table_name,cursor):
    cursor.execute(f"SELECT * FROM {table_name}")
    results = cursor.fetchall()
    print(results)
    #conn.close()

def create_table(table_name,conn,cursor):
    table = {}
    table[table_name] = (
            "CREATE TABLE %s ("
            "  `build_number` int(11) NOT NULL,"
            "  `invalidStats` varchar(20) NOT NULL,"
            "  `fps_0_5` varchar(20) NOT NULL,"
            "  `fps_6_10` varchar(20) NOT NULL,"
            "  `fps_11_15` varchar(20) NOT NULL,"
            "  `fps_16_20` varchar(20) NOT NULL,"
            "  `fps_21_25` varchar(20) NOT NULL,"
            "  `fps_26_30` varchar(20) NOT NULL,"
            "  `fps_31_35` varchar(20) NOT NULL,"
            "  `fps_36_40` varchar(20) NOT NULL,"
            "  `fps_41_45` varchar(20) NOT NULL,"
            "  `fps_46_50` varchar(20) NOT NULL,"
            "  `fps_51_55` varchar(20) NOT NULL,"
            "  `fps_56_60` varchar(20) NOT NULL,"
            "  `fps_gt_60` varchar(20) NOT NULL,"
            "  `fpsDeviation` varchar(20) NOT NULL,"
            "  `fpsMin5s` varchar(20) NOT NULL,"
            "  `fpsMin5sFixTime` varchar(20) NOT NULL,"
            "  `fpsMin2sFixTime` varchar(20) NOT NULL,"
            "  `fpsMin2s` varchar(20) NOT NULL,"
            "  `fpsMax` varchar(20) NOT NULL,"
            "  `fpsAvg` varchar(20) NOT NULL,"
            "  `fpsAvgAlt` varchar(20) NOT NULL,"
            "  `availableVirtualMemory` varchar(20) NOT NULL,"
            "  `peakVirtualMemoryUsage` varchar(20) NOT NULL,"
            "  `graphicsDriverHeapMax` varchar(20) NOT NULL,"
            "  `graphicsDriverHeapAvg` varchar(20) NOT NULL,"
            "  `videoMemoryMax` varchar(20) NOT NULL,"
            "  `videoMemoryAvg` varchar(20) NOT NULL,"
            "  `scaleformHeapMax` varchar(20) NOT NULL,"
            "  `scaleformHeapAvg` varchar(20) NOT NULL,"
            "  `wwiseHeapMax` varchar(20) NOT NULL,"
            "  `wwiseHeapAvg` varchar(20) NOT NULL,"
            "  `genericMemoryHeapMax` varchar(20) NOT NULL,"
            "  `genericMemoryHeapAvg` varchar(20) NOT NULL,"
            "  `totalHeapMax` varchar(20) NOT NULL,"
            "  `totalHeapAvg` varchar(20) NOT NULL,"
            "  `comment` varchar(150),"
            "  PRIMARY KEY (`build_number`)"
            ") ENGINE=InnoDB" % (table_name)) 

    table_description = table[table_name]
    try:
        print("Creating table {}: ".format(table_name), end='')
        cursor.execute(table_description)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            print("already exists.")
        else:
            print(err.msg)
    else:
        print("OK")

    #cursor.close()
    #conn.close()


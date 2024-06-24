from database.DB_connect import DBConnect
from model.distretto import Distretto


class DAO():
    def __init__(self):
        pass

    @staticmethod
    def getAnni():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select distinct year(e.reported_date) as anno
from events e 
"""

        cursor.execute(query)

        for row in cursor:
            result.append(row["anno"])

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getNodi(anno):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select e.district_id as id, abs(e.geo_lon) as lon, abs(e.geo_lat) as lat
from events e 
where year(e.reported_date)=%s
group by e.district_id 
"""

        cursor.execute(query,(anno,))

        for row in cursor:
            result.append(Distretto(**row))

        cursor.close()
        conn.close()
        return result
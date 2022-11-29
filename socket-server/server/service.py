import pymysql


iot_db = pymysql.connect(
    user='root',
    passwd='1111',
    host='34.168.65.229',
    db='iot',
    charset='utf8'
)

db_client = iot_db.cursor(pymysql.cursors.DictCursor)


def get_class_data(_class, period, day_week):
    sql = "select a.code, a.class_name, a.grade, a.professor_name, a.score, a.type, \
    b.classroom, b.day_week, b.period from class_time b left join _class a on a.id = b.class_data_id \
    where b.classroom='{_class}' and b.period='{period}' and b.day_week='{day_week}';"\
        .format(_class= _class, period=period, day_week=day_week)

    db_client.execute(sql)
    return db_client.fetchall()
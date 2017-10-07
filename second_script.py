from Connection import Connection
from RipLib import User, Hotel, Booking

con = Connection("dbuser", "123", "rip_course_db")

with con:
    user = User(con, 'Петр', 'Петров')
    user.save()

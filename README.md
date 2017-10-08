# RFID-Secure-Application
RFID EM-18 Reader Module is interfaced with Arduino UNO . Python Windows Application is developed which connects both Serial Data and SQL Database and provide an UI.

Interfacing of EM-18 MODULE with ARDUINO UNO is illustrated in this [instructable](https://www.instructables.com/id/EM-18-RFID-Reader-Module-Interfaced-With-Arduino-U/).
This Repository includes the development of a Window-Based Application which has following features-

1. Take Serial Data from Arduino UNO. (or any other Microcontroller)
2. Database Connectivity. (For Analysis)
3. Email Capability. 
4. GUI Interface.

Aim of this project:- 

In this project, I am reading the RFID Tag Keys from Serial Data send by Arduino Uno. This serial data is checked with a build in a database table named "Members". This table contains <NAME, DESIGNATION, RFIDKEYS, PHOTONAME> of all the members of the department. If RFID (captured serially) is found in the database, Application will check whether the person has the authorization to enter the premises. If person's Designation is above some particular Designation in the hierarchy, then the only person is allowed to enter. The Valid person's photo with all information (except RFID KEY), time and date will be displayed on the GUI. This whole displayed information is also stored in a Database for FUTURE STATS. If the person is not VALID (or don't have authorization), Access is Denied for the person. If an intruder tries to crack the system by touching a fake RFID Tag, An Email will be sent to HEAD informing the same.


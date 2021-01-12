import MySQLdb
import os
from time import sleep
import time
import random

def main():
    cls()

    print(" Stephen Labs Inc.")
    print()
    print()

    for x in range (0,102):
        #b = " Loading " + str(x) + "% " + "✄" * x
        b = " Loading " + str(x) + "% " + "█" * x
        if x < 101:
            print (b, end="\r")
            sleep_time = float(random.uniform(0.00,1.0))
            if (sleep_time < 0.5):
                time.sleep(sleep_time)
        else:
            b = ""

    print()
    print()
    print()
    nonsense = input(str("Press enter to continue"))
    print("*" * 50)

    cls()
    menu = ""
    while (True):
        print(" Main Menu")
        print()
        print("| customers | barbers | appointments | ")
        print()
        print("Here are today's appointments:")
        print()
        display_appointment()
        print()
        menu = input(str(" ===> "))
        cls()
        if (menu == "customers"):
            while (menu == "customers"):
                cls()
                print("Customer Menu")
                print("| create | edit | delete | view | main |")
                print()

                cust_menu = input(str("===>"))

                if (cust_menu == "create"):
                    cls()
                    print("Create Customer")
                    name = input(str("Customer's name: "))
                    if (name != "cancel"):
                        phone = input(str("Customer's phone: "))
                        if (phone != "cancel"):
                            create_customer(name, phone)
                            input(str("Press enter to continue"))
                        else:
                            cls()
                    else:
                        cls()
                if (cust_menu == "edit"):
                    cls()
                    print("Edit Customer")
                    nonsense = input(str("Press enter to load customers"))
                    print()
                    display_customer()
                    print("Select a customer Id")
                    cust_id = input(str("===>"))
                    cls()
                    action = input(str("Enter an action: name, phone or p&n: \n ===> "))

                    if (cust_id != "cancel"):

                        if (action != "cancel"):
                            if (action == "name"):
                                updated_name = input(str("enter a new name: "))
                                cls()
                                edit_customer_name(updated_name, cust_id)

                            if (action == "phone"):
                                updated_phone = input(str("enter a new phone #: "))
                                cls()
                                edit_customer_phone(cust_id, updated_phone)

                            if (action == "p&n"):
                                updated_name = input(str("enter a new name: "))
                                updated_phone = input(str("enter a new phone #: "))
                                cls()
                                edit_customer_name_and_phone(updated_name, cust_id, updated_phone)
                            input(str("Press enter to continue"))
                        else:
                            cls()
                    else:
                        cls()

                if (cust_menu == "delete"):
                    while True:
                        cls()
                        print("Delete Customer")
                        print()
                        display_customer()
                        print("Select a customer Id")
                        cust_id = input(str("===>"))
                        if (cust_id != "cancel"):
                            delete_customer(cust_id)
                            repeat = input(str("delete another? y/n"))
                            if (repeat == "y"):
                                continue
                            else:
                                break
                        else:
                            cls()

                if (cust_menu == "view"):
                    cls()
                    print("View Customers")
                    nonsense = input(str("Press enter to load customers"))
                    print()
                    display_customer()
                    input(str("Press enter to continue"))
                    cls()

                if (cust_menu == "main"):
                    menu = "main"
                    cls()
        if (menu == "barbers"):
            while (menu == "barbers"):
                cls()
                print("Barber Menu")
                print("| create | edit | delete | view | main |")
                print()

                cust_menu = input(str("===>"))

                if (cust_menu == "create"):
                    cls()
                    print("Create Barber")
                    name = input(str("Barber's name: "))
                    if (name != "cancel"):
                        phone = input(str("Barber's phone: "))
                        if (phone != "cancel"):
                            create_barber(name, phone)
                            input(str("Press enter to continue"))
                        else:
                            cls()
                    else:
                        cls()
                if (cust_menu == "edit"):
                    cls()
                    print("Edit Barber")
                    nonsense = input(str("Press enter to load barbers"))
                    print()
                    display_barber()
                    print("Select a barber Id")
                    barb_id = input(str("===>"))
                    cls()
                    action = input(str("Enter an action: name, phone or p&n: \n ===> "))

                    if (barb_id != "cancel"):

                        if (action != "cancel"):
                            if (action == "name"):
                                updated_name = input(str("enter a new name: "))
                                cls()
                                edit_barber_name(updated_name, barb_id)

                            if (action == "phone"):
                                updated_phone = input(str("enter a new phone #: "))
                                cls()
                                edit_barber_phone(barb_id, updated_phone)

                            if (action == "p&n"):
                                updated_name = input(str("enter a new name: "))
                                updated_phone = input(str("enter a new phone #: "))
                                cls()
                                edit_barber_name_and_phone(updated_name, barb_id, updated_phone)
                            input(str("Press enter to continue"))
                        else:
                            cls()
                    else:
                        cls()

                if (cust_menu == "delete"):
                    while True:
                        cls()
                        print("Delete Barber")
                        print()
                        display_barber()
                        print("Select a barber Id")
                        barb_id = input(str("===>"))
                        if (barb_id != "cancel"):
                            delete_barber(barb_id)
                            repeat = input(str("delete another? y/n"))
                            if (repeat == "y"):
                                continue
                            else:
                                break
                        else:
                            cls()

                if (cust_menu == "view"):
                    cls()
                    print("View barbers")
                    nonsense = input(str("Press enter to load barbers"))
                    print()
                    display_barber()
                    input(str("Press enter to continue"))
                    cls()

                if (cust_menu == "main"):
                    menu = "main"
                    cls()

        if (menu == "appointments"):
            while (menu == "appointments"):
                cls()
                print("Appointment Menu")
                print("| create | delete | view | main |")
                print()

                cust_menu = input(str("===>"))
                cls()
                if (cust_menu == "create"):
                    cls()
                    print("Create Appointment")
                    print()

                    display_barber()
                    print("Select a barber Id")
                    barb_id = input(str("===>"))
                    cls()
                    if (barb_id != "cancel"):
                        display_customer()
                        print("Select a customer Id")
                        cust_id = input(str("===>"))
                        cls()
                        if (cust_id != "cancel"):
                            display_timeslot()
                            print("Select a time slot Id")
                            timeslot_id = input(str("===>"))
                            cls()
                            if (timeslot_id != "cancel"):

                                create_appointment(barb_id, cust_id, timeslot_id)
                                input(str("Press enter to continue"))
                            else:
                                cls()
                        else:
                            cls()
                    else:
                        cls()

                if (cust_menu == "delete"):
                    while True:
                        cls()
                        print("Delete Appointment")
                        print()
                        display_appointment()
                        print("Select a appointment Id")
                        app_id = input(str("===>"))
                        if (app_id != "cancel"):
                            #delete_barber(barb_id)
                            delete_appointment(app_id)
                            cls()
                            display_appointment()
                            repeat = input(str("delete another? y/n: "))
                            if (repeat == "y"):
                                continue
                            else:
                                break
                        else:
                            cls()

                if (cust_menu == "view"):
                    cls()
                    print("View Appointments")
                    nonsense = input(str("Press enter to load Appointments"))
                    print()
                    display_appointment()
                    input(str("Press enter to continue"))
                    cls()

                if (cust_menu == "main"):
                    menu = "main"
                    cls()

def create_customer(name = "", phone = ""):
    db = MySQLdb.connect (host="lawre223.mysql.pythonanywhere-services.com", # your host
            user="lawre223",
            passwd="PythonMySQL" ,
            db="lawre223$default")
    #cur = db.cursor()
    cur = db.cursor()
    query = "INSERT INTO customer (name, phone, active) values ('%s', '%s', 'y')" % (name, phone)
    cur.execute(query)
    results_query = "SELECT * FROM customer where name IN ('%s') and active = 'y'" % (name)
    cur.execute(results_query)

    print("Record successfully inserted")
    for row in cur.fetchall():
        print(" {: <5} {: <20} {: <20}".format(*row))
    db.commit()
    cur.close()
    db.close()
    print()

def display_customer():
    db = MySQLdb.connect (host="lawre223.mysql.pythonanywhere-services.com", # your host
            user="lawre223",
            passwd="PythonMySQL" ,
            db="lawre223$default")
    #cur = db.cursor()
    cur = db.cursor()
    results_query = "SELECT * FROM customer where active = 'y'"
    cur.execute(results_query)
    row_count = 0
    header = ["Id", "Name", "Phone"]
    print(" {: <5} {: <20} {: <20}".format(*header))
    for row in cur.fetchall():
        print(" {: <5} {: <20} {: <20}".format(*row))
        row_count = row_count + 1
    print()
    print("Rows returned: ", row_count)
    print()

    db.commit()
    cur.close()
    db.close()
    print()

def edit_customer_name(updated_name="", cust_id=""):
    db = MySQLdb.connect (host="lawre223.mysql.pythonanywhere-services.com", # your host
            user="lawre223",
            passwd="PythonMySQL" ,
            db="lawre223$default")
    cur = db.cursor()
    #update customer

    if (cust_id != "cancel"):
        query = "update customer set name = '%s' where custid in ('%s')" % (updated_name, cust_id)
        cur.execute(query)
        results_query = "SELECT * FROM customer where custid IN ('%s') and active = 'y'" % (cust_id)
        cur.execute(results_query)

        print("Record successfully updated")
        for row in cur.fetchall():
            print(" {: <5} {: <20} {: <20}".format(*row))
    else:
        print("edit cancelled")

    db.commit()
    cur.close()
    db.close()
    print()

def edit_customer_name_and_phone(updated_name="", cust_id="", updated_phone=""):
    db = MySQLdb.connect (host="lawre223.mysql.pythonanywhere-services.com", # your host
            user="lawre223",
            passwd="PythonMySQL" ,
            db="lawre223$default")
    cur = db.cursor()
    #update customer

    if (cust_id != "cancel"):
        query = "update customer set name = '%s' where custid in ('%s')" % (updated_name, cust_id)
        cur.execute(query)

        query = "update customer set phone = '%s' where custid in ('%s')" % (updated_phone, cust_id)
        cur.execute(query)

        results_query = "SELECT * FROM customer where custid IN ('%s') and active = 'y'" % (cust_id)
        cur.execute(results_query)

        print("Record successfully updated")
        for row in cur.fetchall():
            print(" {: <5} {: <20} {: <20}".format(*row))
    else:
        print("edit cancelled")

    db.commit()
    cur.close()
    db.close()
    print()

def edit_customer_phone(cust_id="", updated_phone=""):
    db = MySQLdb.connect (host="lawre223.mysql.pythonanywhere-services.com", # your host
            user="lawre223",
            passwd="PythonMySQL" ,
            db="lawre223$default")
    cur = db.cursor()
    #update customer

    if (cust_id != "cancel"):
        query = "update customer set phone = '%s' where custid in ('%s')" % (updated_phone, cust_id)
        cur.execute(query)
        results_query = "SELECT * FROM customer where custid IN ('%s') and active = 'y'" % (cust_id)
        cur.execute(results_query)

        print("Record successfully updated")
        for row in cur.fetchall():
            print(" {: <5} {: <20} {: <20}".format(*row))
    else:
        print("edit cancelled")

    db.commit()
    cur.close()
    db.close()
    print()

def delete_customer(cust_id):
    db = MySQLdb.connect (host="lawre223.mysql.pythonanywhere-services.com", # your host
            user="lawre223",
            passwd="PythonMySQL" ,
            db="lawre223$default")
    cur = db.cursor()
    if (cust_id != "cancel"):
      #delete customer
        query = "update customer set active = 'n' where custid in ('%s')" % (cust_id)
        cur.execute(query)
        results_query = "SELECT * FROM customer where custid IN ('%s') and active = 'y'" % (cust_id)
        cur.execute(results_query)

        print("Record successfully deleted")
    else:
        print("edit cancelled")

    db.commit()
    cur.close()
    db.close()
    print()

def create_barber(name = "", phone = ""):
    db = MySQLdb.connect (host="lawre223.mysql.pythonanywhere-services.com", # your host
            user="lawre223",
            passwd="PythonMySQL" ,
            db="lawre223$default")
    #cur = db.cursor()
    cur = db.cursor()
    query = "INSERT INTO barber (name, phone, active) values ('%s', '%s', 'y')" % (name, phone)
    cur.execute(query)
    results_query = "SELECT * FROM barber where name IN ('%s') and active = 'y'" % (name)
    cur.execute(results_query)

    print("Record successfully inserted")
    for row in cur.fetchall():
        print(" {: <5} {: <20} {: <20}".format(*row))
    db.commit()
    cur.close()
    db.close()
    print()

def display_barber():
    db = MySQLdb.connect (host="lawre223.mysql.pythonanywhere-services.com", # your host
            user="lawre223",
            passwd="PythonMySQL" ,
            db="lawre223$default")
    #cur = db.cursor()
    cur = db.cursor()
    results_query = "SELECT * FROM barber where active = 'y'"
    cur.execute(results_query)
    row_count = 0
    header = ["Id", "Name", "Phone"]
    print(" {: <5} {: <20} {: <20}".format(*header))
    for row in cur.fetchall():
        print(" {: <5} {: <20} {: <20}".format(*row))
        row_count = row_count + 1
    print()
    print("Rows returned: ", row_count)
    print()

    db.commit()
    cur.close()
    db.close()
    print()

def edit_barber_name(updated_name="", barb_id=""):
    db = MySQLdb.connect (host="lawre223.mysql.pythonanywhere-services.com", # your host
            user="lawre223",
            passwd="PythonMySQL" ,
            db="lawre223$default")
    cur = db.cursor()
    #update barber

    if (barb_id != "cancel"):
        query = "update barber set name = '%s' where barberid in ('%s')" % (updated_name, barb_id)
        cur.execute(query)
        results_query = "SELECT * FROM barber where barberid IN ('%s') and active = 'y'" % (barb_id)
        cur.execute(results_query)

        print("Record successfully updated")
        for row in cur.fetchall():
          print (row[1], "", row[2])
    else:
        print("edit cancelled")

    db.commit()
    cur.close()
    db.close()
    print()

def edit_barber_name_and_phone(updated_name="", barb_id="", updated_phone=""):
    db = MySQLdb.connect (host="lawre223.mysql.pythonanywhere-services.com", # your host
            user="lawre223",
            passwd="PythonMySQL" ,
            db="lawre223$default")
    cur = db.cursor()
    #update barber

    if (barb_id != "cancel"):
        query = "update barber set name = '%s' where barberid in ('%s')" % (updated_name, barb_id)
        cur.execute(query)

        query = "update barber set phone = '%s' where barberid in ('%s')" % (updated_phone, barb_id)
        cur.execute(query)

        results_query = "SELECT * FROM barber where barberid IN ('%s') and active = 'y'" % (barb_id)
        cur.execute(results_query)

        print("Record successfully updated")
        for row in cur.fetchall():
          print (row[1], "", row[2])
    else:
        print("edit cancelled")

    db.commit()
    cur.close()
    db.close()
    print()

def edit_barber_phone(barb_id="", updated_phone=""):
    db = MySQLdb.connect (host="lawre223.mysql.pythonanywhere-services.com", # your host
            user="lawre223",
            passwd="PythonMySQL" ,
            db="lawre223$default")
    cur = db.cursor()
    #update barber

    if (barb_id != "cancel"):
        query = "update barber set phone = '%s' where barberid in ('%s')" % (updated_phone, barb_id)
        cur.execute(query)
        results_query = "SELECT * FROM barber where barberid IN ('%s') and active = 'y'" % (barb_id)
        cur.execute(results_query)

        print("Record successfully updated")
        for row in cur.fetchall():
          print (row[1], "", row[2])
    else:
        print("edit cancelled")

    db.commit()
    cur.close()
    db.close()
    print()

def delete_barber(barb_id):
    db = MySQLdb.connect (host="lawre223.mysql.pythonanywhere-services.com", # your host
            user="lawre223",
            passwd="PythonMySQL" ,
            db="lawre223$default")
    cur = db.cursor()
    if (barb_id != "cancel"):
      #delete barber
        query = "update barber set active = 'n' where barberid in ('%s')" % (barb_id)
        cur.execute(query)
        results_query = "SELECT * FROM barber where barberid IN ('%s') and active = 'y'" % (barb_id)
        cur.execute(results_query)

        print("Record successfully deleted")
    else:
        print("delete cancelled")

    db.commit()
    cur.close()
    db.close()
    print()

def display_timeslot():
    db = MySQLdb.connect (host="lawre223.mysql.pythonanywhere-services.com", # your host
            user="lawre223",
            passwd="PythonMySQL" ,
            db="lawre223$default")
    #cur = db.cursor()
    cur = db.cursor()
    results_query = "SELECT * FROM timeslot where available  = 'y'"
    cur.execute(results_query)
    row_count = 0
    for row in cur.fetchall():
        print(" {: <5} {: <10}".format(*row), "", row[2])
        row_count = row_count + 1
    print()
    print("Rows returned: ", row_count)
    print()
    db.commit()
    cur.close()
    db.close()
    print()

def create_appointment(barber_id = "", cust_id = "", timeslot_id = ""):
    db = MySQLdb.connect (host="lawre223.mysql.pythonanywhere-services.com", # your host
            user="lawre223",
            passwd="PythonMySQL" ,
            db="lawre223$default")
    #cur = db.cursor()
    cur = db.cursor()
    query = "INSERT INTO appointment (barberid, custid, timeslotid, active) values ('%s', '%s', '%s', 'y')" % (barber_id, cust_id, timeslot_id)
    cur.execute(query)

    query = "update timeslot set available = 'n' where timeslotid in ('%s')" % (timeslot_id)
    cur.execute(query)

    print("Record successfully inserted")
    db.commit()
    cur.close()
    db.close()
    display_appointment()
    print()

def display_appointment():
    db = MySQLdb.connect (host="lawre223.mysql.pythonanywhere-services.com", # your host
            user="lawre223",
            passwd="PythonMySQL" ,
            db="lawre223$default")
    #cur = db.cursor()
    cur = db.cursor()
    results_query = "SELECT appointment.appointmentid, barber.name, customer.name, timeslot.hour, timeslot.date FROM (((appointment INNER JOIN barber ON appointment.barberid = barber.barberid) INNER JOIN customer ON appointment.barberid = customer.custid) INNER JOIN timeslot ON appointment.timeslotid = timeslot.timeslotid) WHERE appointment.active = 'y' order by timeslot.date, timeslot.hour asc;"
    cur.execute(results_query)
    row_count = 0

    header = ["Id", "Barber Name", "Customer Name", "Hour", "Date"]
    print(" {: <5} {: <20} {: <20} {: <10} {: >5}".format(*header))

    for row in cur.fetchall():
        print(" {: <5} {: <20} {: <20} {: <10}".format(*row), "", row[4])
        row_count = row_count + 1
    print()
    print("Rows returned: ", row_count)
    print()
    db.commit()
    cur.close()
    db.close()
    print()

def delete_appointment(app_id):
    db = MySQLdb.connect (host="lawre223.mysql.pythonanywhere-services.com", # your host
            user="lawre223",
            passwd="PythonMySQL" ,
            db="lawre223$default")
    cur = db.cursor()
    if (app_id != "cancel"):
      #delete customer
        query = "select timeslotid from appointment where appointmentid in ('%s')" % (app_id)
        cur.execute(query)
        print(cur.execute(query))

        for row in cur.fetchall():
          timeslot_id = str(row[0])
          print(timeslot_id)
          query = "update timeslot set available = 'y' where timeslotid in ('%s')" % (timeslot_id)
          cur.execute(query)

        query = "delete from appointment where appointmentid in ('%s')" % (app_id)
        cur.execute(query)

        print("Record successfully deleted")
    else:
        print("edit cancelled")

    db.commit()
    cur.close()
    db.close()
    print()

def cls():
    # now, to clear the screen
    os.system('cls' if os.name=='nt' else 'clear')
    print("*" * 110)
    print(" " * 47 + "Barber Shop Pro©")
    print("*" * 110)

while True:
    main()


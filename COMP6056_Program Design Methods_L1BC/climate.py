import csv
import json
import atexit
import matplotlib.pyplot as plt
import pathlib
import getpass
import datetime
from datetime import date
from time import strftime 


class Climate_Buddy:
    def __init__(self):
        self.username1 = ""
        self.start1 = ""
    
    def login(self, start):

        print("""\n
                    *******************************************
                        Welcome To The Climate Buddy v1.01 
                    *******************************************
                        Please use you credentials to login
                    -------------------------------------------""")
        status = False
        while status ==False:
            username = input("USERNAME >> _ _ ")
            password  = getpass.getpass()
            if username in start.users and (start.getUser(username).getpass()) == password:
                print("welcome user >> ", username)
                status = True
                self.username1 = username
                return username

            else:
                print("Invalid Login Credentials !!\nIf you dont have login credentials contact system adminstrator.")
    def loadjson(self): #this block of code is used load the json file that has user data
        filename = "/Users/ellispaxmapakama/Desktop/workspace/final project/climate.json"
        with open(filename, "r") as f:
            fill = json.load(f)
            get = Climate(fill["System"])

            for key, value in fill["users"].items():
                make = Users(value["fname"], value["password"], value["access"])
                make.set_access(value["access"])
                
                get.create_user(key, make)
            
            return get

    def savejson(self, start): #this block of code is used to save user data to the json file
        filename = "/Users/ellispaxmapakama/Desktop/workspace/final project/climate.json"  
        with open(filename,"w") as fp:
            fil = {}
            fil["System"] = start.System
            fil["users"] = {}
            for username, data in start.getall().items():
                fil["users"][username] = {
                    "fname": data.getuser(),
                    "password": data.getpass(),
                    "access": data.getAccess()
                }
            json.dump(fil, fp, indent = 4)

    def get_filepath(self):
        root = "/Users/ellispaxmapakama/Desktop/workspace/final project/csv/"
        print("Make Sure the  file is in the correct specified folder.\nIf you are not sure contact the system adminstrator for help!")
        name = str(input("Enter complete filename with extension >> "))
        Filename = pathlib.Path(root + name)
        if Filename.exists():
            return Filename
        else:
            print("The file that you are trying to mount does not exist!")
            self.main_menu(self.start1,self.username1)
    def extract(self):
        filename = self.get_filepath()
        date = []
        min_temps, max_temps, avg_temps = [],[],[]
        max_humidity, min_humidity, avg_humidity, cloud_cover = [],[],[],[]
        max_windspeed, min_windspeed, avg_windspeed, wind_gust = [],[],[],[]
        max_pressure, min_pressure, avg_pressure = [],[],[]
        visibility, sun_hours = [],[]
        precipitation = []


        with open(filename) as f:
            reader = csv.reader(f)
            header_row = next(reader)

            for row in reader:
                date.append(row[0])
                max_temps.append(float(row[1]))
                min_temps.append(float(row[2]))
                avg_temps.append(float(row[3]))

                max_humidity.append(float(row[4]))
                min_humidity.append(float(row[5]))
                avg_humidity.append(float(row[6]))
                cloud_cover.append(float(row[7]))
        
                max_windspeed.append(float(row[8]))
                min_windspeed.append(float(row[9]))
                avg_windspeed.append(float(row[10]))
                wind_gust.append(float(row[11]))

                max_pressure.append(float(row[12]))
                min_pressure.append(float(row[13]))
                avg_pressure.append(float(row[14]))

                visibility.append(float(row[15]))
                sun_hours.append(float(row[16]))
                precipitation.append(float(row[17]))

            
        def calc_annual_avgs():
            day_counter = 0
            rain_days = 0
            for item in date:
                day_counter += 1
            
            day = int(day_counter)
            
            for item in precipitation:
                if item > 0:
                    rain_days += 1


            maxtemp, mintemp, avgtemp = 0,0,0
            maxhumidity, minhumidity, avghumidity, cloudcover  = 0,0,0,0
            maxwindspeed, minwindspeed, avgwindspeed,windgust = 0,0,0,0
            maxpressure, minpressure, avgpressure = 0,0,0
            visibility_, sunhours = 0,0
            precp = 0
            
            maxtemp = (sum(max_temps))/day
            mintemp = (sum(min_temps))/day
            avgtemp = (sum(avg_temps))/day
            maxhumidity = (sum(max_humidity))/day
            minhumidity = (sum(min_humidity))/day
            avghumidity = (sum(avg_humidity))/day
            cloudcover = (sum(cloud_cover))/day
            maxwindspeed = (sum(max_windspeed))/day
            minwindspeed = (sum(min_windspeed))/day
            avgwindspeed = (sum(avg_windspeed))/day
            windgust = (sum(wind_gust))/day
            maxpressure = (sum(max_pressure))/day
            minpressure = (sum(min_pressure))/day
            avgpressure = (sum(avg_pressure))/day
            visibility_ = (sum(visibility))/day
            sunhours = (sum(sun_hours))
            precp = (sum(precipitation))/day

            return maxtemp,mintemp,avgtemp,maxhumidity,minhumidity,avghumidity,cloudcover,maxwindspeed,minwindspeed,avgwindspeed,windgust,maxpressure,minpressure,avgpressure,visibility_,sunhours,precp

            


        aa,ab,ac,ad,ae,af,ag,ah,ai,aj,ak,al,am,an,ao,ap,aq = calc_annual_avgs()
        month = input("Enter Month >> ")

        row = [str(month),str(round(aa, 2)),str(round(ab, 2)),str(round(ac, 2)),str(round(ad, 2)),str(round(ae, 2)),str(round(af, 2)),str(round(ag, 2)),str(round(ah, 2)),str(round(ai,2)),str(round(aj,2)),str(round(ak, 2)),str(round(al, 2)),str(round(am,2)),str(round(an,2)),str(round(ao, 2)),str(round(ap, 2)),str(round(aq, 2))]

        save = "/Users/ellispaxmapakama/Desktop/workspace/final project/csv/monthly_weather_2010.csv"
        with open(save, 'a') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerow(row)
            print("Data Has been saved in the Yearly Monthly Avarages CSV file ")
        csvFile.close()
        self.main_menu(self.start1,self.username1)
    def extract_yr(self):
        filename = self.get_filepath()
        date = []
        min_temps, max_temps, avg_temps = [],[],[]
        max_humidity, min_humidity, avg_humidity, cloud_cover = [],[],[],[]
        max_windspeed, min_windspeed, avg_windspeed, wind_gust = [],[],[],[]
        max_pressure, min_pressure, avg_pressure = [],[],[]
        visibility, sun_hours = [],[]
        precipitation = []


        with open(filename) as f:
            reader = csv.reader(f)
            header_row = next(reader)

            for row in reader:
                date.append(row[0])
                max_temps.append(float(row[1]))
                min_temps.append(float(row[2]))
                avg_temps.append(float(row[3]))

                max_humidity.append(float(row[4]))
                min_humidity.append(float(row[5]))
                avg_humidity.append(float(row[6]))
                cloud_cover.append(float(row[7]))
        
                max_windspeed.append(float(row[8]))
                min_windspeed.append(float(row[9]))
                avg_windspeed.append(float(row[10]))
                wind_gust.append(float(row[11]))

                max_pressure.append(float(row[12]))
                min_pressure.append(float(row[13]))
                avg_pressure.append(float(row[14]))

                visibility.append(float(row[15]))
                sun_hours.append(float(row[16]))
                precipitation.append(float(row[17]))

        

        def calc_avgs():
            counter = 0 #this will count number of months in the file
            rain_days = 0
            for item in date:
                counter += 1 #for every month in the list date counter is increamented by 1
            
            numMonths = int(counter) #changing counter to type int and assigned to numMonths
            
            for item in precipitation:
                if item > 0:
                    rain_days += 1


            maxtemp, mintemp, avgtemp = 0,0,0
            maxhumidity, minhumidity, avghumidity, cloudcover  = 0,0,0,0
            maxwindspeed, minwindspeed, avgwindspeed,windgust = 0,0,0,0
            maxpressure, minpressure, avgpressure = 0,0,0
            visibility_, sunhours = 0,0
            precp = 0
            
            #calculating average values
            maxtemp = (sum(max_temps))/numMonths
            mintemp = (sum(min_temps))/numMonths
            avgtemp = (sum(avg_temps))/numMonths
            maxhumidity = (sum(max_humidity))/numMonths
            minhumidity = (sum(min_humidity))/numMonths
            avghumidity = (sum(avg_humidity))/numMonths
            cloudcover = (sum(cloud_cover))/numMonths
            maxwindspeed = (sum(max_windspeed))/numMonths
            minwindspeed = (sum(min_windspeed))/numMonths
            avgwindspeed = (sum(avg_windspeed))/numMonths
            windgust = (sum(wind_gust))/numMonths
            maxpressure = (sum(max_pressure))/numMonths
            minpressure = (sum(min_pressure))/numMonths
            avgpressure = (sum(avg_pressure))/numMonths
            visibility_ = (sum(visibility))/numMonths
            sunhours = (sum(sun_hours))
            precp = (sum(precipitation))/numMonths

            return maxtemp,mintemp,avgtemp,maxhumidity,minhumidity,avghumidity,cloudcover,maxwindspeed,minwindspeed,avgwindspeed,windgust,maxpressure,minpressure,avgpressure,visibility_,sunhours,precp

            


        aa,ab,ac,ad,ae,af,ag,ah,ai,aj,ak,al,am,an,ao,ap,aq = calc_avgs() #values returned by the calc_avgs() function are assigned to these variables
        month = input("Enter Year >> ")

        #variable row has all values that are to be  appended into the new file, values rounded to 2 Dp
        row = [str(month),str(round(aa, 2)),str(round(ab, 2)),str(round(ac, 2)),str(round(ad, 2)),str(round(ae, 2)),str(round(af, 2)),str(round(ag, 2)),str(round(ah, 2)),str(round(ai,2)),str(round(aj, 2)),str(round(ak, 2)),str(round(al, 2)),str(round(am,2)),str(round(an,2)),str(round(ao, 2)),str(round(ap, 2)),str(round(aq, 2))]

        filename = "/Users/ellispaxmapakama/Desktop/workspace/final project/csv/yearly_weather.csv"
        with open(filename, 'a') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerow(row)
        csvFile.close()
        self.main_menu(self.start1,self.username1)
    def daily_data(self):
        filename = self.get_filepath()

        monthname = input("Enter name of month you will be working on >> ")
        year = input("Enter year >> ")
        date = []
        min_temps, max_temps, avg_temps = [],[],[]
        max_humidity, min_humidity, avg_humidity, cloud_cover = [],[],[],[]
        max_windspeed, min_windspeed, avg_windspeed, wind_gust = [],[],[],[]
        max_pressure, min_pressure, avg_pressure = [],[],[]
        visibility, sun_hours = [],[]
        precipitation = []

        with open(filename) as f:
            reader = csv.reader(f)
            header_row = next(reader)

            for row in reader:
                date.append(row[0])
                max_temps.append(float(row[1]))
                min_temps.append(float(row[2]))
                avg_temps.append(float(row[3]))

                max_humidity.append(float(row[4]))
                min_humidity.append(float(row[5]))
                avg_humidity.append(float(row[6]))
                cloud_cover.append(float(row[7]))
        
                max_windspeed.append(float(row[8]))
                min_windspeed.append(float(row[9]))
                avg_windspeed.append(float(row[10]))
                wind_gust.append(float(row[11]))

                max_pressure.append(float(row[12]))
                min_pressure.append(float(row[13]))
                avg_pressure.append(float(row[14]))

                visibility.append(float(row[15]))
                sun_hours.append(float(row[16]))
                precipitation.append(float(row[17]))

        def plot_pressure():
            maxpressure = max_pressure
            minpressure = min_pressure
            avgpressure = avg_pressure
            days = date
            dates = range(1, len(days + ['1']), 1)

            plt.plot(dates, maxpressure, label = 'Max Pressure')
            plt.plot(dates, minpressure, label = 'Min Pressure')
            plt.plot(dates, avgpressure, label = 'Average Pressure')
            plt.xticks(range(1, len(days + ['1']), 1))

            plt.axis([1,len(days), 20,30])
            plt.title(f'Max, Min & Average Pressure for {monthname} {year}')
            plt.ylabel('Pressure (Hg)')
            plt.xlabel('Day')
            plt.legend()
            plt.show()
        
        def plot_wind():
            max_wind = max_windspeed
            avg_wind = avg_windspeed
            gust = wind_gust
            days = date
            dates = range(1, len(days + ['1']), 1)

            plt.plot(dates, max_wind, label = 'Max Windsp')
            plt.plot(dates, avg_wind, label = 'Average Windsp')
            plt.plot(dates, gust, label = 'Wind Gust')
            plt.xticks(range(1, len(days + ['1']), 1))

            plt.axis([1,31,0,20])
            plt.title(f'Max, Average Windspeed & Wind Gust for {monthname} {year}')
            plt.ylabel('Speed (mph)')
            plt.xlabel('Day')
            plt.legend()
            plt.show()
        
        def plot_temps():
            temp_max = max_temps
            temp_min = min_temps
            temp_avg = avg_temps
            day = date
            dates = range(1, len(day + ['1']), 1)

            
            
            plt.plot(dates,temp_max, label = 'Max Temp')
            plt.plot(dates, temp_min, label = 'Min Temp')
            plt.plot(dates, temp_avg, label = 'Average Temp')
            plt.xticks(range(1, len(day + ['1']), 1))

            plt.axis([1, 31, 50, 95])
            plt.title(f'Min, Max & Average Temperatures for {monthname} {year}')
            plt.ylabel('Temperature(F)')
            plt.xlabel('Day')
            plt.legend()
            plt.show()
        plot_temps()
        plot_wind()
        plot_pressure()
        self.main_menu(self.start1,self.username1)
    def monthly_data(self):
        filename = self.get_filepath()
        year = input("Enter year >> ")
        date = []
        min_temps, max_temps, avg_temps = [],[],[]
        max_humidity, min_humidity, avg_humidity, cloud_cover = [],[],[],[]
        max_windspeed, min_windspeed, avg_windspeed, wind_gust = [],[],[],[]
        max_pressure, min_pressure, avg_pressure = [],[],[]
        visibility, sun_hours = [],[]
        precipitation = []


        with open(filename) as f:
            reader = csv.reader(f)
            header_row = next(reader)

            for row in reader:
                date.append(row[0])
                max_temps.append(float(row[1]))
                min_temps.append(float(row[2]))
                avg_temps.append(float(row[3]))

                max_humidity.append(float(row[4]))
                min_humidity.append(float(row[5]))
                avg_humidity.append(float(row[6]))
                cloud_cover.append(float(row[7]))
        
                max_windspeed.append(float(row[8]))
                min_windspeed.append(float(row[9]))
                avg_windspeed.append(float(row[10]))
                wind_gust.append(float(row[11]))

                max_pressure.append(float(row[12]))
                min_pressure.append(float(row[13]))
                avg_pressure.append(float(row[14]))

                visibility.append(float(row[15]))
                sun_hours.append(float(row[16]))
                precipitation.append(float(row[17]))
        def plot_pressure():
            maxpressure = max_pressure
            minpressure = min_pressure
            avgpressure = avg_pressure
            
            days = date
            
            C = len(date)
            B = list(range(1,C+1))
            plt.plot(B, maxpressure, label = 'Max Pressure')
            plt.plot(B, minpressure, label = 'Min Pressure')
            plt.plot(B, avgpressure, label = 'Average Pressure')
            plt.xticks(B, date)

            
            plt.title(f'Max, Min & Average Pressure for the year {year}')
            plt.ylabel('Pressure (Hg)')
            plt.xlabel('Month')
            plt.legend()
            plt.show()

        def plot_wind():
            max_wind = max_windspeed
            avg_wind = avg_windspeed
            gust = wind_gust
            
            days = date
            
            
            C = len(date)
            B = list(range(1,C+1))
            plt.plot(B, max_wind, label = 'Max Windsp')
            plt.plot(B, avg_wind, label = 'Average Windsp')
            plt.plot(B, gust, label = 'Wind Gust')
            plt.xticks(B, date)

            
            plt.title(f'Max, Average Windspeed & Wind Gust for year {year}')
            plt.ylabel('Speed (mph)')
            plt.xlabel('Month')
            plt.legend()
            plt.show()

        def plot_temps():
            temp_max = max_temps
            temp_min = min_temps
            temp_avg = avg_temps
        
            days = date
            

            
            C = len(date)
            B = list(range(1,C+1))
            plt.plot(B,temp_max, label = 'Max Temp')
            plt.plot(B, temp_min, label = 'Min Temp')
            plt.plot(B, temp_avg, label = 'Average Temp')
            plt.xticks(B, date)

            
            plt.title(f'Min, Max & Average Temperatures for year {year}')
            plt.ylabel('Temperature(F)')
            plt.xlabel('Month')
            plt.legend()
            plt.show()

        plot_temps()
        plot_wind()
        plot_pressure()
        self.main_menu(self.start1,self.username1)
    def year_data(self):
        filename = self.get_filepath()

        period = input("Enter Period >> ")
        date = []
        min_temps, max_temps, avg_temps = [],[],[]
        max_humidity, min_humidity, avg_humidity, cloud_cover = [],[],[],[]
        max_windspeed, min_windspeed, avg_windspeed, wind_gust = [],[],[],[]
        max_pressure, min_pressure, avg_pressure = [],[],[]
        visibility, sun_hours = [],[]
        precipitation = []


        with open(filename) as f:
            reader = csv.reader(f)
            header_row = next(reader)

            for row in reader:
                date.append(row[0])
                max_temps.append(float(row[1]))
                min_temps.append(float(row[2]))
                avg_temps.append(float(row[3]))

                max_humidity.append(float(row[4]))
                min_humidity.append(float(row[5]))
                avg_humidity.append(float(row[6]))
                cloud_cover.append(float(row[7]))
        
                max_windspeed.append(float(row[8]))
                min_windspeed.append(float(row[9]))
                avg_windspeed.append(float(row[10]))
                wind_gust.append(float(row[11]))

                max_pressure.append(float(row[12]))
                min_pressure.append(float(row[13]))
                avg_pressure.append(float(row[14]))

                visibility.append(float(row[15]))
                sun_hours.append(float(row[16]))
                precipitation.append(float(row[17]))
        def plot_pressure():
            maxpressure = max_pressure
            minpressure = min_pressure
            avgpressure = avg_pressure
            
            days = date
            
            C = len(date)
            B = list(range(1,C+1))
            plt.plot(B, maxpressure, label = 'Max Pressure')
            plt.plot(B, minpressure, label = 'Min Pressure')
            plt.plot(B, avgpressure, label = 'Average Pressure')
            plt.xticks(B, date)

            
            plt.title(f'Max, Min & Average Pressure for the year {period}')
            plt.ylabel('Pressure (Hg)')
            plt.xlabel('Month')
            plt.legend()
            plt.show()

        def plot_wind():
            max_wind = max_windspeed
            avg_wind = avg_windspeed
            gust = wind_gust
            
            days = date
            
            
            C = len(date)
            B = list(range(1,C+1))
            plt.plot(B, max_wind, label = 'Max Windsp')
            plt.plot(B, avg_wind, label = 'Average Windsp')
            plt.plot(B, gust, label = 'Wind Gust')
            plt.xticks(B, date)

            
            plt.title(f'Max, Average Windspeed & Wind Gust for year {period}')
            plt.ylabel('Speed (mph)')
            plt.xlabel('Month')
            plt.legend()
            plt.show()

        def plot_temps():
            temp_max = max_temps
            temp_min = min_temps
            temp_avg = avg_temps
        
            days = date
            

            
            C = len(date)
            B = list(range(1,C+1))
            plt.plot(B,temp_max, label = 'Max Temp')
            plt.plot(B, temp_min, label = 'Min Temp')
            plt.plot(B, temp_avg, label = 'Average Temp')
            plt.xticks(B, date)

            
            plt.title(f'Min, Max & Average Temperatures for year {period}')
            plt.ylabel('Temperature(F)')
            plt.xlabel('Month')
            plt.legend()
            plt.show()

        plot_temps()
        plot_wind()
        plot_pressure()
        self.main_menu(self.start1,self.username1)
    def main_menu(self, start, username): #this block contains the two main menus to be used by the  users


        self.start1 = start

        def visuals():
            print("""\n
                        *********************************
                            DATA VISUALISATIONS
                        *********************************
                                [1] USE DAILY DATA
                                [2] USE MONTHLY DATA
                                [3] USE YEARLY DATA

                                [R] RETURN TO MENU
                        ---------------------------------
                    """)
    
        def admin_menu():   #this menu is only visible to the adminstrator who has more priviledges than the ordinary user
            today = date.today()

            d1 = today.strftime("%b-%d-%Y")
            t1 = strftime('%H:%M:%S %p')

            print()
            print("""\n
                        *********************************
                          """, d1," | ", t1, """
                                CLIMATE BUDDY v1.01
                        *********************************
                                CHOOSE OPERATION 
                        *********************************
                                [1] ADD USER
                                [2] DELETE USER
                                [3] GET USERS
                                [4] EXTRACT FROM DAILY >> MONTHLY
                                [5] EXTRACT FROM MONTHLY >> YEARLY
                                [6] VISUALISATION AND ANALYSIS

                                [Q] QUIT

                        ---------------------------------   
                            logged in as >> """, start.getUser(username).getAccess(), """
                            """)
            userInput = input(" >>>>> ")    #used to get user choice

            if (userInput == "1"):
                name = input("Enter Full Name >> ")
                usern = input("Enter prefered username >> ")
                password = getpass.getpass()
                re_enter = getpass.getpass()
                access = input("Enter Access level >> ")

                if (password == re_enter):
                    acc = access
                    setter = Users(name, password, access)
                    setter.set_access(acc)
                    start.create_user(usern, setter)
                    print("User has been created.\nPlease keep your login credentials safe!")
                    admin_menu()
                else:
                    print("Passwords did not match !\nMake sure you have all the details and try again.")
                    admin_menu()

            elif (userInput == "2"):
                name = input("Enter Username >> ")
                if name in start.users:
                    print("Are you sure you want to delete user >>", name," from the system?")
                    ans = input("Yes (Y) or No (N) >> ")
                    if ans.upper() == "Y":
                        start.remove(name)
                        print("Record has been deleted!!")
                        admin_menu()
                    else:
                        print("Operation Aborted !!")
                        admin_menu()        
                else:
                    print("The user you want to delete does not exist!")
                    admin_menu()
            elif (userInput == "3"):
                userName = input("Enter Username >> ")
                if userName in start.users:
                    get = start.getUser(userName)
                    print("---------------------------------------------")
                    print("Full Name: ", get.getuser())
                    print("Username: ", userName)
                    print("Password: ", get.getpass())
                    print("Access Level: ", get.getAccess())
                    print("----------------------------------------------")
                    admin_menu()
                else:
                    print("User Not in the Database!")
                    admin_menu()
            elif (userInput == "4"):
                self.extract()

            elif (userInput == "5"):
                self.extract_yr()
            elif (userInput == "6"):
                visuals()
                inpt = input(" >> ")
                if inpt == "1":
                    self.daily_data()
                elif(inpt == "2"):
                    self.monthly_data()
                elif(inpt == "3"):
                    self.year_data()
                elif(inpt.upper() == "R"):
                    print("Are you sure you want to return to Main Menu ?")
                    qsn = input("Yes(Y) or No (N) >> ")
                    if qsn.upper() == "Y":
                        admin_menu()
                    else:
                        visuals()
                else:
                    print("Invalid Input!")
                    visuals()
            elif(userInput.upper() == "Q"):
                print("Are you sure you want to exit?")
                exitans = input("Yes (Y) or No (N) >> ")
                if (exitans.upper() == "Y"):
                    print("Thank you for using Climate Buddy v1.01.\nMake sure to check for updates!")
                    self.savejson(start)
                    exit()
                else:
                    print("Exit Procedure Aborted!")
                    admin_menu()
            else:
                print("Invalid Input !!")
                self.main_menu(self.start1,self.username1)

        def user_menu():    #this menu is for the ordinary users
            print("""\n
                        *********************************
                                CLIMATE BUDDY v1.01
                        *********************************
                                CHOOSE OPERATION 
                        *********************************
                                [1] EXTRACT DAILY >> MONTHLY
                                [2] EXTRACT MONTHLY >> YEARLY
                                [3] VISUALISATION & ANALYSIS

                                [Q] QUIT

                        ---------------------------------   
                            logged in as >> """,start.getUser(username).getAccess(),"""
                            """)
            userAns = input(" >>>> ")       #used to get user choice
            if (userAns == "1"):
                self.extract()

            elif(userAns == "2"):
                self.extract_yr()
            elif(userAns == "3"):
                visuals()
                usrAns = input(" >> ")
                if usrAns == "1":
                    self.daily_data()
                elif usrAns == "2":
                    self.monthly_data()
                elif usrAns == "3":
                    self.year_data()
                elif usrAns.upper() == "R":
                    print("Are you sure you want to return to main menu?")
                    ans = input("Yes (Y) or No (N) >> ")
                    if ans.upper() ==  "Y":
                        user_menu()
                    else:
                        print("Return Aborted!!")
                        visuals()
                else:
                    print("Invalid Input")
                    visuals()
            elif(userAns.upper() == "Q"):
                print("Are you sure you want to exit?")
                exitans = input("Yes (Y) or No (N) >> ")
                if (exitans.upper() == "Y"):
                    print("Thank you for using Climate Buddy v1.01.\nMake sure to check for updates soon!")
                    
                    exit()
                else:
                    print("Exit Procedure Aborted!")
                    user_menu()
            else:
                print("Invalid Input !!")
                self.main_menu(self.start1,self.username1)

        if start.getUser(username).getAccess() == "admin":  #validation check which differentiates ordinary user from admin user
            admin_menu()
        elif start.getUser(username).getAccess() == "user":
            user_menu()
    

class Climate:
    users = {}
    def __init__(self, name):
        self.System = name

    def create_user(self, username, user):
        self.users[username] = user
    
    def remove(self, username):
        if username in self.users:
            del self.users[username]

    def getUser(self, username):
        return self.users[username]

    def getall(self):
        return self.users
class Users:
    def __init__ (self, username, password, access):
        
        self.username = username
        self.password = password
        self.access = access
 

    def getuser(self):
        return self.username
    
    def getpass(self):
        return self.password

    def set_access(self, x):
        self.level = x

    def getAccess(self):
        return self.access

def run():
    Climate_obj = Climate_Buddy()

    
    start = Climate_obj.loadjson()
    username = Climate_obj.login(start)
  
    Climate_obj.main_menu(start, username)
   

run()




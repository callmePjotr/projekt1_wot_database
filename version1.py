# imports für die GUI
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import Screen, ScreenManager
from screen_nav import screen_helper, ErrorMsg
from kivymd.uix.textfield import MDTextField
from kivymd.uix.button import MDRectangleFlatButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from kivymd.uix.menu import MDDropdownMenu
from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button
from kivymd.uix.label import MDLabel

# imports für Cassandra
import cassandra
from cassandra.cluster import Cluster
from cassandra.policies import DCAwareRoundRobinPolicy
from cassandra.auth import PlainTextAuthProvider
import uuid
import re
import os
from pathlib import Path
import atexit
import webbrowser
import time


wichtig = ""
# verbinden mit dem Cluster, momentan funktioniert nur localhost
clstr=Cluster(['127.0.0.1'], port=9042)
clstr = Cluster()
session = clstr.connect("wot_database")


Window.size = (900, 650)


class MenuScreen(Screen):
    pass


class showDataScreen(Screen):
    dialog = None
    def get_value1(self, value):
        f = open("temp1.txt", "a")
        f.write(value)
        f.close()
        return value

    def get_value2(self, value):
        f = open("temp2.txt", "a")
        f.write(value)
        f.close()
        return value

    def get_value3(self, value):
        f = open("temp3.txt", "a")
        f.write(value)
        f.close()
        return value

    def get_value4(self, value):
        f = open("temp4.txt", "a")
        f.write(value)
        f.close()
        return value

    def fire(self):

        if not self.dialog:
            self.dialog = MDDialog(
                text="We are missing some files here, please try again",
                buttons=[
                    MDFlatButton(
                        text="CANCEL",
                        on_press=lambda _: ui()
                    )
                ],
            )

        path_to_file1 = 'temp1.txt'
        path1 = Path(path_to_file1)
        path_to_file2 = 'temp2.txt'
        path2 = Path(path_to_file2)
        path_to_file3 = 'temp3.txt'
        path3 = Path(path_to_file3)
        path_to_file4 = 'temp4.txt'
        path4 = Path(path_to_file4)



        if path1.is_file():
            f = open("temp1.txt", "r")
            tank_class = f.read()
            print(tank_class)
            f.close()
        else:
            self.dialog.open()
        if path2.is_file():
            f = open("temp2.txt", "r")
            nation = f.read()
            print(nation)
            f.close()
        else:
            self.dialog.open()
        if path3.is_file():
            f = open("temp3.txt", "r")
            tier = f.read()
            print(tier)
            f.close()
        else:
            self.dialog.open()
        if path4.is_file():
            f = open("temp4.txt", "r")
            tank = f.read()
            print(tier)
            f.close()
        else:
            self.dialog.open()


        def ui():
            #self.parent.current = "insertDataScreen"
            self.dialog.dismiss()

        t_class = ["light",
                   "medium",
                   "heavy",
                   "td",
                   "arty"]

        if (tank_class == 'light'):
            class_switch2 = t_class[0]
            table_select = "full_tank_list_{}".format(class_switch2)
        elif (tank_class == 'medium'):
            class_switch2 = t_class[1]
            table_select = "full_tank_list_{}".format(class_switch2)
        elif (tank_class == 'heavy'):
            class_switch2 = t_class[2]
            table_select = "full_tank_list_{}".format(class_switch2)
        elif (tank_class == 'td'):
            class_switch2 = t_class[3]
            table_select = "full_tank_list_{}".format(class_switch2)
        elif (tank_class == 'arty'):
            class_switch2 = t_class[4]
            table_select = "full_tank_list_{}".format(class_switch2)
        else:
            print(f"{tank_class} is not an valid input")
            print("Error occurs when clicking on list items twice")
            os.remove("temp1.txt")
            os.remove("temp2.txt")
            os.remove("temp3.txt")
            os.remove("temp4.txt")
            raise SystemExit

        new_tank0 = tank.replace(" ", "_")
        new_tank1 = new_tank0.lower()

        prepare_select1 = "funkg_{}".format(new_tank1)
        prepare_select2 = "kanone_{}".format(new_tank1)
        prepare_select3 = "ketten_{}".format(new_tank1)
        prepare_select4 = "motor_{}".format(new_tank1)
        prepare_select5 = "turm_{}".format(new_tank1)

        os.remove("temp1.txt")
        os.remove("temp2.txt")
        os.remove("temp3.txt")
        os.remove("temp4.txt")

        print(table_select)

        #hier einmal der Klassen-Tablleneintrag
        tonk1 = []
        tonk2 = []
        tonk3 = []
        tonk4 = []

        rows = session.execute("SELECT * FROM {} WHERE nation='{}' AND tier={}".format(table_select,nation,int(tier)))
        f = open("results.txt", "a")
        for row in rows:
            tonk1.append(row.nation)
            tonk2.append(row.tier)
            tonk3.append(row.id)
            tonk4.append(row.name)
            print(row.nation, row.tier, row.id, row.name)
            f.write("Nation   |  Tier  |  ID                                     |  Name")
            f.write("\n")
            f.write("-------------------------------------------------------------------------")
            f.write("\n")
            f.write(row.nation)
            f.write("  |   ")
            f.write(str(row.tier))
            f.write("   |  ")
            f.write(str(row.id))
            f.write("   |  ")
            f.write(row.name)
            f.write("\n")
            f.write("\n")
            f.write("\n")

        print("done")

        print("Funkgerät--------------------------------------------------------------")
        f.write("Funkgeraet--------------------------------------------------------------")
        f.write("\n")
        f.write("stat                     |  ID                                      |  value")
        f.write("\n")
        f.write("-------------------------------------------------------------------------")
        f.write("\n")

        rows = session.execute("SELECT * FROM {}".format(prepare_select1))
        #print(rows.stat)
        stats_funkg1 = []
        stats_funkg2 = []
        stats_kanone1 = []
        stats_kanone2 = []
        stats_ketten1 = []
        stats_ketten2 = []
        stats_motor1 = []
        stats_motor2= []
        stats_turm1 = []
        stats_turm2 = []
        for row in rows:
            funkg_id = row[1]
            funkg_val = row[2]
            #print(test)
            stats_funkg1.append(row.id)
            stats_funkg2.append(row.value)
            print(row.stat, row.id, row.value)
            f.write(row.stat)
            f.write("                   |   ")
            f.write(str(row.id))
            f.write("   |  ")
            f.write(row.value)

            f.write("\n")
            f.write("\n")

        print("Kanone--------------------------------------------------------------")
        f.write("Kanone--------------------------------------------------------------")
        f.write("\n")
        f.write("stat                     |  ID                                      |  value")
        f.write("\n")
        f.write("-------------------------------------------------------------------------")
        f.write("\n")

        rows = session.execute("SELECT * FROM {}".format(prepare_select2))
        for row in rows:
            stats_kanone1.append(row.id)
            stats_kanone2.append(row.value)
            print(row.stat, row.id, row.value)
            f.write(row.stat)
            f.write("                   |   ")
            f.write(str(row.id))
            f.write("   |  ")
            f.write(row.value)

            f.write("\n")
            f.write("\n")

        print("Ketten--------------------------------------------------------------")
        f.write("Ketten--------------------------------------------------------------")
        f.write("\n")
        f.write("stat                     |  ID                                      |  value")
        f.write("\n")
        f.write("-------------------------------------------------------------------------")
        f.write("\n")

        rows = session.execute("SELECT * FROM {}".format(prepare_select3))
        for row in rows:
            stats_ketten1.append(row.id)
            stats_ketten2.append(row.value)
            print(row.stat, row.id, row.value)
            f.write(row.stat)
            f.write("                   |   ")
            f.write(str(row.id))
            f.write("   |  ")
            f.write(row.value)

            f.write("\n")
            f.write("\n")

        print("Motor--------------------------------------------------------------")
        f.write("Motor--------------------------------------------------------------")
        f.write("\n")
        f.write("stat                     |  ID                                      |  value")
        f.write("\n")
        f.write("-------------------------------------------------------------------------")
        f.write("\n")

        rows = session.execute("SELECT * FROM {}".format(prepare_select4))
        for row in rows:
            stats_motor1.append(row.id)
            stats_motor2.append(row.value)
            print(row.stat, row.id, row.value)
            f.write(row.stat)
            f.write("                   |   ")
            f.write(str(row.id))
            f.write("   |  ")
            f.write(row.value)

            f.write("\n")
            f.write("\n")

        print("Turm--------------------------------------------------------------")
        f.write("Turm--------------------------------------------------------------")
        f.write("\n")
        f.write("stat                     |  ID                                      |  value")
        f.write("\n")
        f.write("-------------------------------------------------------------------------")
        f.write("\n")

        rows = session.execute("SELECT * FROM {}".format(prepare_select5))
        for row in rows:
            stats_turm1.append(row.id)
            stats_turm2.append(row.value)
            print(row.stat, row.id, row.value)
            f.write(row.stat)
            f.write("                   |   ")
            f.write(str(row.id))
            f.write("   |  ")
            f.write(row.value)

            f.write("\n")
            f.write("\n")


        print(stats_ketten1[0])
        print(stats_funkg2[2])



        html_content = f"<html> <head> <link rel='stylesheet' href='style.css'> </head> <h1> Your selected vehicle is: {tank}  <body> " \
                       f"<video autoplay muted loop id='myVideo'><source src='wot.mp4' type='video/mp4'></video> " \
                       f"<script> var video = document.getElementByID('myVideo'); video.play(); </script>" \
                       f"<h2> Panzer </h2><table class='styled-table'><thead><tr><th>Nation</th><th>Tier</th><th>ID</th><th>Name</th></tr></thead><tbody><tr><td>{tonk1[0]}</td><td>{tonk2[0]}</td><td>{tonk3[0]}</td><td>{tonk4[0]}</td></tr><!-- and so on... --></tbody></table></body> </html>" \
                       f"<h2> Turm </h2><table class='styled-table'><thead><tr><th>Stat</th><th>ID</th><th>Value</th></tr></thead><tbody><tr><td>view range (m)</td><td>{stats_turm1[0]}</td><td>{stats_turm2[0]}</td></tr><tr class='active-row'><td>health</td><td>{stats_turm1[1]}</td><td>{stats_turm2[1]}</td></tr><tr><td>weight (kg)</td><td>{stats_turm1[2]}</td><td>{stats_turm2[2]}</td></tr><tr class='active-row'><td>armor (f/s/r in mm)</td><td>{stats_turm1[3]}</td><td>{stats_turm2[3]}</td></tr><tr><td>rotation speed (deg/sec)</td><td>{stats_turm1[4]}</td><td>{stats_turm2[4]}</td></tr><!-- and so on... --></tbody></table>" \
                       f"<h2> Motor </h2><table class='styled-table'><thead><tr><th>Stat</th><th>ID</th><th>Value</th></tr></thead><tbody><tr><td>power(hp)</td><td>{stats_motor1[0]}</td><td>{stats_motor2[0]}</td></tr><tr class='active-row'><td>model</td><td>{stats_motor1[1]}</td><td>{stats_motor2[1]}</td></tr><tr><td>fire chance (%)</td><td>{stats_motor1[2]}</td><td>{stats_motor2[2]}</td></tr><tr class='active-row'><td>weight (kg)</td><td>{stats_motor1[3]}</td><td>{stats_motor2[3]}</td></tr><!-- and so on... --></tbody></table></body> </html>" \
                       f"<h2> Ketten </h2><table class='styled-table'><thead><tr><th>Stat</th><th>ID</th><th>Value</th></tr></thead><tbody><tr><td>max load (kg)</td><td>{stats_ketten1[0]}</td><td>{stats_ketten2[0]}</td></tr><tr class='active-row'><td>traverse speed (deg/sec)</td><td>{stats_ketten1[1]}</td><td>{stats_ketten2[1]}</td></tr><!-- and so on... --></tbody></table>" \
                       f"<h2> Kanone </h2><table class='styled-table'><thead><tr><th>Stat</th><th>ID</th><th>Value</th></tr></thead><tbody><tr><td>dispersion (at 100m)</td><td>{stats_kanone1[0]}</td><td>{stats_kanone2[0]}</td></tr><tr class='active-row'><td>aim time (sec)</td><td>{stats_kanone1[1]}</td><td>{stats_kanone2[1]}</td></tr><tr><td>weight (kg)</td><td>{stats_kanone1[2]}</td><td>{stats_kanone2[2]}</td></tr><tr class='active-row'><td>damage</td><td>{stats_kanone1[3]}</td><td>{stats_kanone2[3]}</td></tr><tr><td>rate of fire (rnds/min)</td><td>{stats_kanone1[4]}</td><td>{stats_kanone2[4]}</td></tr><tr><td>penetration (mm)</td><td>{stats_kanone1[5]}</td><td>{stats_kanone2[5]}</td></tr><!-- and so on... --></tbody></table>" \
                       f"<h2> Funkgerät </h2><table class='styled-table'><thead><tr><th>Stat</th><th>ID</th><th>Value</th></tr></thead><tbody><tr><td>model</td><td>{stats_funkg1[0]}</td><td>{stats_funkg2[0]}</td></tr><tr class='active-row'><td>range (m)</td><td>{stats_funkg1[1]}</td><td>{stats_funkg2[1]}</td></tr><tr><td>weight (kg)</td><td>{stats_funkg1[2]}</td><td>{stats_funkg2[2]}</td></tr><!-- and so on... --></tbody></table>"

        with open("index.html", "w") as html_file:
            html_file.write(html_content)
            print("Succesfully created")

        time.sleep(2)
        webbrowser.open_new_tab("index.html")

        #os.startfile("results.txt")
        #os.remove("results.txt")








    pass


class insertDataScreen(Screen):
    dialog = None
    nation = lambda text_item: text_item
    print(nation)

    def show_alert_dialog(self):
        if not self.dialog:
            self.dialog = MDDialog(
                title="Share your Tanks with others",
                text="This feature is not implemented yet.",
                buttons=[
                    MDFlatButton(
                        text="CANCEL",  on_release=self.close_dialog
                    ),
                ],
            )

        self.dialog.open()


    # Click Cancel Button
    def close_dialog(self, obj):
        # Close alert box
        self.dialog.dismiss()

    def get_value(self, value):
        # print(value)
        f = open("temp.txt", "a")
        f.write(value)
        f.close()
        return value

    def insertData(self):
        dialog = None
        self.t_nation = self.ids.nation.text
        # self.t_class = self.ids.t_class.text
        self.t_tier = self.ids.tier.text
        self.tank = self.ids.name.text
        self.test = self.ids
        print(wichtig)

        # File aus get_value() öffnen und lesen
        f = open("tanks.txt", "a")
        f.write(self.tank)
        f.write("\n")
        f.close()

        try:
            with open("temp.txt", "r") as f:
                tank_class = f.read()
                print(tank_class)
                f.close()
                os.remove("temp.txt")
        except FileNotFoundError:
            print("File not found")
            self.show_alert_dialog()
            raise SystemExit


            if not self.dialog:
                self.dialog = MDDialog(
                    text="These Text fields are required",
                    buttons=[
                        MDFlatButton(
                            text="CANCEL",
                            on_press=lambda _: ui()
                        )
                    ],
                )
                self.dialog.open()




        if (not self.tank or not self.t_nation or not self.t_tier):
            print("All Fields need to be set")
            raise SystemExit
        else:
            self.parent.current = "insertDataScreen2"

        def ui():
            self.parent.current = "insertDataScreen"
            self.dialog.dismiss()

        try:  # kivy stürzt ab, wenn nur ein Feld ausgefüllt ist anstatt das Dialogfenster zu öffnen
            int(self.t_tier)
        except ValueError:
            print("Parse to float did not work")

        #print(self.t_nation, type(int(self.t_tier)), self.tank)  # scheinbar funktioniert das dann doch
        new_tank = self.tank.replace(" ", "_")

        # insert in full_tank_list_
        class_switch = 1
        t_class = ["light",
                   "medium",
                   "heavy",
                   "td",
                   "arty"]

        if (tank_class == 'light'):
            class_switch2 = t_class[0]
            table_select = "full_tank_list_{}".format(class_switch2)
        elif (tank_class == 'medium'):
            class_switch2 = t_class[1]
            table_select = "full_tank_list_{}".format(class_switch2)
        elif (tank_class == 'heavy'):
            class_switch2 = t_class[2]
            table_select = "full_tank_list_{}".format(class_switch2)
        elif (tank_class == 'td'):
            class_switch2 = t_class[3]
            table_select = "full_tank_list_{}".format(class_switch2)
        elif (tank_class == 'arty'):
            class_switch2 = t_class[4]
            table_select = "full_tank_list_{}".format(class_switch2)
        else:
            print(f"{tank_class} is not an valid input")
            print("Error occurs when clicking on list items twice")
            raise SystemExit

        print(table_select)

        new_tank = self.tank.replace(" ", "_")

        insert2 = session.prepare(
            "INSERT INTO {} (nation, tier, id, name) VALUES (?, ?, ?, ?) IF NOT EXISTS".format(table_select))
        session.execute(insert2, [self.t_nation, int(self.t_tier), uuid.uuid1(), self.tank])

        turret_table = "turm_{}".format(new_tank)
        engine_table = "motor_{}".format(new_tank)
        tracks_table = "ketten_{}".format(new_tank)
        gun_table = "kanone_{}".format(new_tank)
        radio_table = "funkg_{}".format(new_tank)

        try:

            with open("turret_table.txt", "a") as f:
                f.write(turret_table)
                f.close()

            with open("engine_table.txt", "a") as f:
                f.write(engine_table)
                f.close()

            with open("tracks_table.txt", "a") as f:
                f.write(tracks_table)
                f.close()

            with open("gun_table.txt", "a") as f:
                f.write(gun_table)
                f.close()

            with open("radio_table.txt", "a") as f:
                f.write(radio_table)
                f.close()

        except FileNotFoundError:
            print("File not found")
            raise SystemExit


        session.execute(
            "CREATE TABLE {}(stat text, id timeuuid, value text, PRIMARY KEY(stat, id)) WITH CLUSTERING ORDER BY(id asc);".format(
                turret_table))
        session.execute(
            "CREATE TABLE {}(stat text, id timeuuid, value text, PRIMARY KEY(stat, id)) WITH CLUSTERING ORDER BY(id asc);".format(
                engine_table))
        session.execute(
            "CREATE TABLE {}(stat text, id timeuuid, value text, PRIMARY KEY(stat, id)) WITH CLUSTERING ORDER BY(id asc);".format(
                tracks_table))
        session.execute(
            "CREATE TABLE {}(stat text, id timeuuid, value text, PRIMARY KEY(stat, id)) WITH CLUSTERING ORDER BY(id asc);".format(
                gun_table))
        session.execute(
            "CREATE TABLE {}(stat text, id timeuuid, value text, PRIMARY KEY(stat, id)) WITH CLUSTERING ORDER BY(id asc);".format(
                radio_table))

        print("Done with Creating the tables for {}. :)".format(new_tank))

    def insertion(self):
        print("Hello from Insertion")
        print(self.t_nation)
        self.t_class
        self.t_tier
        self.tank
        self.test

    pass


class deleteDataScreen(Screen):

    def get_value5(self, value):
        f = open("temp5.txt", "a")
        f.write(value)
        f.close()
        return value

    def delete(self):
        try:
            with open("temp5.txt", "r") as f:
                tank = f.read()
                f.close()
                print(tank)
                os.remove("temp5.txt")
        except FileNotFoundError:
            print("File not found")
            raise SystemExit

        new_tank0 = tank.replace(" ", "_")
        new_tank1 = new_tank0.lower()

        prepare_select1 = "funkg_{}".format(new_tank1)
        prepare_select2 = "kanone_{}".format(new_tank1)
        prepare_select3 = "ketten_{}".format(new_tank1)
        prepare_select4 = "motor_{}".format(new_tank1)
        prepare_select5 = "turm_{}".format(new_tank1)

        session.execute("DROP TABLE {} IF EXISTS".format(prepare_select1))
        session.execute("DROP TABLE {} IF EXISTS".format(prepare_select2))
        session.execute("DROP TABLE {} IF EXISTS".format(prepare_select3))
        session.execute("DROP TABLE {} IF EXISTS".format(prepare_select4))
        session.execute("DROP TABLE {} IF EXISTS".format(prepare_select5))


        print(f"Succesfully deleted Tables for {tank}!")


    pass


class insertDataScreen2(Screen):
    def insertData2(self):
        t_armor = self.ids.t_armor.text
        t_rotation_speed = self.ids.t_rotation_speed.text
        t_view_range = self.ids.t_view_range.text
        t_health = self.ids.t_health.text
        t_weight = self.ids.t_weight.text
        e_model = self.ids.e_model.text
        e_power = self.ids.e_power.text
        e_fire_chance = self.ids.e_fire_chance.text
        e_weight = self.ids.e_weight.text
        tr_traverse = self.ids.tr_traverse.text
        tr_max_load = self.ids.tr_max_load.text
        g_rof = self.ids.g_rof.text
        g_penetration = self.ids.g_penetration.text
        g_damage = self.ids.g_damage.text
        g_dispersion = self.ids.g_dispersion.text
        g_aim_time = self.ids.g_aim_time.text
        g_weight = self.ids.g_weight.text

        try:

            with open("turret_table.txt", "r") as f:
                turret_table = f.read()
                f.close()
                os.remove("turret_table.txt")

            with open("engine_table.txt", "r") as f:
                engine_table = f.read()
                f.close()
                os.remove("engine_table.txt")

            with open("tracks_table.txt", "r") as f:
                tracks_table = f.read()
                f.close()
                os.remove("tracks_table.txt")

            with open("gun_table.txt", "r") as f:
                gun_table = f.read()
                f.close()
                os.remove("gun_table.txt")

        except FileNotFoundError:
            print("File not found")
            raise SystemExit




        # Turm-------------------------------------------

        insert_turret_armor = session.prepare(
            "INSERT INTO {} (stat, id, value) VALUES (?, ?, ?) IF NOT EXISTS".format(turret_table))
        insert_turret_rotation = session.prepare(
            "INSERT INTO {} (stat, id, value) VALUES (?, ?, ?) IF NOT EXISTS".format(turret_table))
        insert_turret_view_range = session.prepare(
            "INSERT INTO {} (stat, id, value) VALUES (?, ?, ?) IF NOT EXISTS".format(turret_table))
        insert_turret_health = session.prepare(
            "INSERT INTO {} (stat, id, value) VALUES (?, ?, ?) IF NOT EXISTS".format(turret_table))
        insert_turret_weight = session.prepare(
            "INSERT INTO {} (stat, id, value) VALUES (?, ?, ?) IF NOT EXISTS".format(turret_table))

        session.execute(insert_turret_armor, ['armor (f/s/r in mm)', uuid.uuid1(), t_armor])
        session.execute(insert_turret_rotation, ['rotation speed (deg/sec)', uuid.uuid1(), t_rotation_speed])
        session.execute(insert_turret_view_range, ['view range (m)', uuid.uuid1(), t_view_range])
        session.execute(insert_turret_health, ['health', uuid.uuid1(), t_health])
        session.execute(insert_turret_weight, ['weight (kg)', uuid.uuid1(), t_weight])

        # Motor-------------------------------------------

        insert_engine_model = session.prepare(
            "INSERT INTO {} (stat, id, value) VALUES (?, ?, ?) IF NOT EXISTS".format(engine_table))
        insert_engine_power = session.prepare(
            "INSERT INTO {} (stat, id, value) VALUES (?, ?, ?) IF NOT EXISTS".format(engine_table))
        insert_engine_fire = session.prepare(
            "INSERT INTO {} (stat, id, value) VALUES (?, ?, ?) IF NOT EXISTS".format(engine_table))
        insert_engine_weight = session.prepare(
            "INSERT INTO {} (stat, id, value) VALUES (?, ?, ?) IF NOT EXISTS".format(engine_table))

        session.execute(insert_engine_model, ['model', uuid.uuid1(), e_model])
        session.execute(insert_engine_power, ['power (hp)', uuid.uuid1(), e_power])
        session.execute(insert_engine_fire, ['fire chance (percent)', uuid.uuid1(), e_fire_chance])
        session.execute(insert_engine_weight, ['weight (kg)', uuid.uuid1(), e_weight])

        # Ketten-------------------------------------------

        insert_tracks_traverse = session.prepare(
            "INSERT INTO {} (stat, id, value) VALUES (?, ?, ?) IF NOT EXISTS".format(tracks_table))
        insert_tracks_max_load = session.prepare(
            "INSERT INTO {} (stat, id, value) VALUES (?, ?, ?) IF NOT EXISTS".format(tracks_table))

        session.execute(insert_tracks_traverse, ['traverse (deg / sec)', uuid.uuid1(), tr_traverse])
        session.execute(insert_tracks_max_load, ['max load (kg)', uuid.uuid1(), tr_max_load])

        # Kanone--------------------------------------------

        insert_gun_rof = session.prepare(
            "INSERT INTO {} (stat, id, value) VALUES (?, ?, ?) IF NOT EXISTS".format(gun_table))
        insert_gun_pen = session.prepare(
            "INSERT INTO {} (stat, id, value) VALUES (?, ?, ?) IF NOT EXISTS".format(gun_table))
        insert_gun_dmg = session.prepare(
            "INSERT INTO {} (stat, id, value) VALUES (?, ?, ?) IF NOT EXISTS".format(gun_table))
        insert_gun_dispersion = session.prepare(
            "INSERT INTO {} (stat, id, value) VALUES (?, ?, ?) IF NOT EXISTS".format(gun_table))
        insert_gun_aim_time = session.prepare(
            "INSERT INTO {} (stat, id, value) VALUES (?, ?, ?) IF NOT EXISTS".format(gun_table))
        insert_gun_weight = session.prepare(
            "INSERT INTO {} (stat, id, value) VALUES (?, ?, ?) IF NOT EXISTS".format(gun_table))

        session.execute(insert_gun_rof, ['rate of fire (rnds/min)', uuid.uuid1(), g_rof])
        session.execute(insert_gun_pen, ['penetration (mm)', uuid.uuid1(), g_penetration])
        session.execute(insert_gun_dmg, ['damage', uuid.uuid1(), g_damage])
        session.execute(insert_gun_dispersion, ['dispersion (at 100m)', uuid.uuid1(), g_dispersion])
        session.execute(insert_gun_aim_time, ['aim time (sec)', uuid.uuid1(), g_aim_time])
        session.execute(insert_gun_weight, ['weight (kg)', uuid.uuid1(), g_weight])

    pass


class insertDataScreen3(Screen):
    def insertData3(self):
        rd_model = self.ids.rd_model.text
        rd_range = self.ids.rd_range.text
        rd_weight = self.ids.rd_weight.text

        try:
            with open("radio_table.txt", "r") as f:
                radio_table = f.read()
                f.close()
                os.remove("radio_table.txt")
        except FileNotFoundError:
            print("File not found")
            raise SystemExit

        # Funkgerät------------------------------------------

        insert_radio_model = session.prepare(
            "INSERT INTO {} (stat, id, value) VALUES (?, ?, ?) IF NOT EXISTS".format(radio_table))
        insert_radio_range = session.prepare(
            "INSERT INTO {} (stat, id, value) VALUES (?, ?, ?) IF NOT EXISTS".format(radio_table))
        insert_radio_weight = session.prepare(
            "INSERT INTO {} (stat, id, value) VALUES (?, ?, ?) IF NOT EXISTS".format(radio_table))

        session.execute(insert_radio_model, ['model', uuid.uuid1(), rd_model])
        session.execute(insert_radio_range, ['range (m)', uuid.uuid1(), rd_range])
        session.execute(insert_radio_weight, ['weight (kg)', uuid.uuid1(), rd_weight])

    pass

class MyGoalsScreen (Screen):
    def on_enter(self):
        file= open("results.txt" , "r")
        load_file = ""
        for line in file:
            load_file = load_file + line
        file.close()
        self.ids.mylabel.text = load_file

sn = ScreenManager()
sn.add_widget(MenuScreen(name='menu'))
sn.add_widget(showDataScreen(name='showDataScreen'))
sn.add_widget(insertDataScreen(name='showDataScreen'))
sn.add_widget(deleteDataScreen(name='deleteDataScreen'))
sn.add_widget(insertDataScreen2(name='insertDataScreen2'))
sn.add_widget(insertDataScreen3(name='insertDataScreen3'))
sn.add_widget(MyGoalsScreen(name='MyGoalsScreen'))

class MyApp(MDApp):
    # nation = 'class_variable'
    dialog = None
    '''
    def build(self):
        self.theme_cls.primary_palette = 'Red'
        screen = Screen()
        self.username = Builder.load_string(screen_helper)
        screen.add_widget(self.username)
        return screen
'''

    def __init__(self, **kwargs):

        screen = Screen()
        super().__init__(**kwargs)
        self.screen = Builder.load_string(screen_helper)
        self.current = "insertDataScreen"
        n_items = ['china', 'czech', 'france', 'germany', 'italy', 'japan', 'poland', 'sweden', 'uk', 'usa', 'ussr']
        t_class = ["light", "medium", "heavy", "td", "arty"]
        tier = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]

        tank_list = []
        with open("tanks.txt","r") as f:
            for line in f:
                tank_list.append(line.rstrip("\n"))

        print(tank_list)





        menu_items = [
            {
                "text": f"{i}",
                "viewclass": "OneLineListItem",
                "on_release": lambda x=f"{i}": self.menu_callback(x),
            } for i in t_class
        ]
        self.menu = MDDropdownMenu(
            #  caller=self.screen.ids.button,
            items=menu_items,
            width_mult=2,
           # multiselect = false,
          #  touch_multiselect = false,
        )

        menu_items = [
            {
                "text": f"{i}",
                "viewclass": "OneLineListItem",
                "on_release": lambda x=f"{i}": self.menu_callback1(x),
            } for i in t_class
        ]
        self.menu1 = MDDropdownMenu(
            #  caller=self.screen.ids.button,
            items=menu_items,
            width_mult=2,
        )


        menu_items = [
            {
                "text": f"{i}",
                "viewclass": "OneLineListItem",
                "on_release": lambda x=f"{i}": self.menu_callback2(x),
            } for i in n_items
        ]
        self.menu2 = MDDropdownMenu(
            #  caller=self.screen.ids.button,
            items=menu_items,
            width_mult=2,
        )

        menu_items = [
            {
                "text": f"{i}",
                "viewclass": "OneLineListItem",
                "on_release": lambda x=f"{i}": self.menu_callback3(x),
            } for i in tier
        ]
        self.menu3 = MDDropdownMenu(
            #  caller=self.screen.ids.button,
            items=menu_items,
            width_mult=2,
        )
        #Hier einmal alle Panzer anzeigen
        menu_items = [
            {
                "text": f"{i}",
                "viewclass": "OneLineListItem",
                "on_release": lambda x=f"{i}": self.menu_callback4(x),
            } for i in tank_list
        ]
        self.menu4 = MDDropdownMenu(
            #  caller=self.screen.ids.button,
            items=menu_items,
            width_mult=2,
        )

        menu_items = [
            {
                "text": f"{i}",
                "viewclass": "OneLineListItem",
                "on_release": lambda x=f"{i}": self.menu_callback5(x),
            } for i in tank_list
        ]
        self.menu5 = MDDropdownMenu(
            #  caller=self.screen.ids.button,
            items=menu_items,
            width_mult=2,
        )



    nation = lambda text_item: text_item

    def menu_callback(self, text_item):
        # print(text_item)
        wichtig = text_item
        obj = insertDataScreen()
        obj.get_value(text_item)
        # obj.nation(text_item)
        # return lambda text_item : print(text_item) (text_item)
        # return text_item

    def menu_callback1(self, text_item):
        obj = showDataScreen()
        obj.get_value1(text_item)
        #klasse = text_item



    def menu_callback2(self, text_item):
        obj = showDataScreen()
        obj.get_value2(text_item)
        #nation = text_item


    def menu_callback3(self, text_item):
        obj = showDataScreen()
        obj.get_value3(text_item)
        #stufe = text_item

    def menu_callback4(self, text_item):
        obj = showDataScreen()
        obj.get_value4(text_item)

    def menu_callback5(self, text_item):
        obj = deleteDataScreen()
        obj.get_value5(text_item)

    def launch_menu(self, my_caller):
        self.menu.caller = my_caller
        self.menu.open()

    def launch_menu1(self, my_caller):
        self.menu1.caller = my_caller
        self.menu1.open()

    def launch_menu2(self, my_caller):
        self.menu2.caller = my_caller
        self.menu2.open()

    def launch_menu3(self, my_caller):
        self.menu3.caller = my_caller
        self.menu3.open()

    def launch_menu4(self, my_caller):
        self.menu4.caller = my_caller
        self.menu4.open()

    def launch_menu5(self, my_caller):
        self.menu5.caller = my_caller
        self.menu5.open()

    def build(self):
        self.theme_cls.primary_palette = 'Red'
        return self.screen

    def show_alert_dialog(self):
        if not self.dialog:
            self.dialog = MDDialog(
                title="Share your Tanks with others",
                text="This feature is not implemented yet.",
                buttons=[
                    MDFlatButton(
                        text="CANCEL", text_color=self.theme_cls.primary_color, on_release=self.close_dialog
                    ),
                ],
            )

        self.dialog.open()

    # Click Cancel Button
    def close_dialog(self, obj):
        # Close alert box
        self.dialog.dismiss()


class Bullet(Widget):
    def bullet_fly(self):
        img = Image(source='wot.png', size_hint_y=None, height=dp(40), pos=(85, 200))
        App.get_running_app().root.add_widget(img)



def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

#kv = Builder.load_file(resource_path("screen_nav.py"))
#entfernet files, nach dem Schließen der App
@atexit.register
def goodbye():
    print('You are now leaving the Python sector.')
    try:
        os.remove("results.txt")
        os.remove("index.html")
    except FileNotFoundError:
        raise SystemExit


if __name__ == '__main__':
    MyApp().run()
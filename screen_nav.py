screen_helper = """
ScreenManager:
    MenuScreen:
    showDataScreen:
    insertDataScreen:
    deleteDataScreen:
    insertDataScreen2:
    insertDataScreen3:
    MyGoalsScreen:

<MenuScreen>:
    name: 'menu'
    MDScreen:
        MDNavigationLayout:
            ScreenManager:
                MDScreen:
                    BoxLayout:
                        orientation: 'vertical'
                        MDToolbar: 
                            title: 'Demo'
                            left_action_items : [["menu",lambda x: nav_drawer.set_state("open")]]
                            right_action_items : [["share",lambda x: app.show_alert_dialog()]]
                            elevation: 10
                        Widget:    

            MDNavigationDrawer:
                id: nav_drawer
                BoxLayout:
                    orientation: 'vertical'
                    spacing: '8dp'
                    padding: '8dp'

                    MDLabel:
                        text: '   WoT-Database     '
                        size_hint_y: None
                        height: self.texture_size[1]

                    MDLabel:
                        text: '     '
                        size_hint_y: None
                        height: self.texture_size[1]

                    ScrollView:
                        MDList:
                            MDRectangleFlatIconButton:
                                icon: 'chevron-right'
                                text: 'Daten anzeigen'
                                line_color: 0, 0, 0, 0
                                pos_hint: {"center_x": .5, "center_y": .5}
                                on_press: root.manager.current = 'showDataScreen'
                            MDRectangleFlatIconButton:
                                icon: 'chevron-right'
                                text: 'Daten hinzufügen'
                                line_color: 0, 0, 0, 0
                                pos_hint: {"center_x": .5, "center_y": .5}
                                on_press: root.manager.current = 'insertDataScreen'
                            MDRectangleFlatIconButton:
                                icon: 'chevron-right'
                                text: 'Daten Löschen'
                                line_color: 0, 0, 0, 0
                                pos_hint: {"center_x": .5, "center_y": .5}
                                on_press: root.manager.current = 'deleteDataScreen'


<showDataScreen>:
    name :'showDataScreen'
    MDScreen:
        MDNavigationLayout:
            ScreenManager:
                MDScreen:
                    BoxLayout:
                        orientation: 'vertical'
                        MDToolbar: 
                            title: 'Demo'


                        
                        BoxLayout:
                            orientation: 'horizontal'

                                
                            MDRaisedButton:
                                id: button1
                                text: "                Choose a Class                "
                                pos_hint: {"center_x": .5, "center_y": 0.97}       
                                on_release: app.launch_menu1(self)
                                
                                
                            MDRaisedButton:
                                id: button2
                                text: "                Choose a Nation                "
                                pos_hint: {"center_x": .5, "center_y": .97}            
                                on_release: app.launch_menu2(self)
                                
                            MDRaisedButton:
                                id: button3
                                text: "                Choose a Tier                "
                                pos_hint: {"center_x": .5, "center_y": .97}            
                                on_release: app.launch_menu3(self)
                                
                            MDRaisedButton:
                                id: button3
                                text: "                Choose a certain Tank                 "
                                pos_hint: {"center_x": .5, "center_y": .97}            
                                on_release: app.launch_menu4(self)

                                    
                        MDRaisedButton:
                            text: 'show'
                            line_color: 0, 0, 0, 0
                            pos_hint: {"center_x": 0.5, "center_y": 0.5} 
                            on_press: root.fire()
                            
                            
                        Widget:    
                            MDRectangleFlatIconButton:
                                icon: 'share'
                                text: 'Return to previous'
                                line_color: 0, 0, 0, 0
                                pos_hint: {'left': 1, 'bottom': 1}
                                on_press: root.manager.current = 'menu'

                                    

<insertDataScreen>:
    name :'insertDataScreen'
    MDScreen:
        MDNavigationLayout:
            ScreenManager:
                MDScreen:
                    BoxLayout:
                        orientation: 'vertical'
                        MDToolbar: 
                            title: 'Grobe Panzerdaten angeben und Tabellenauswahl'


                            elevation: 10
                        Widget:
                        MDRectangleFlatIconButton:
                            icon: 'share'
                            text: 'Return to previous'
                            line_color: 0, 0, 0, 0
                            pos_hint: {'left': 1, 'bottom': 1}
                            on_press: root.manager.current = 'menu'



    BoxLayout:
        orientation: 'vertical'
        MDTextField:
            id: nation
            hint_text: "Enter Nation"
            icon_right: "android"
            icon_right_color: app.theme_cls.primary_color
            pos_hint:{'center_x': 0.5, 'center_y': 0.2}
            size_hint_x:None
            width:300

        MDRaisedButton:
            id: button
            text: "Choose a Class"
            pos_hint: {"center_x": .5, "center_y": .5}            
            on_release: app.launch_menu(self)


        MDTextField:
            id: tier
            input_filter: 'int'
            hint_text: "Enter Tank Tier"
            helper_text: "Tank Tiers are from 1 to 10"
            helper_text_mode: "on_focus"
            icon_right: "android"
            icon_right_color: app.theme_cls.primary_color
            pos_hint:{'center_x': 0.5, 'center_y': 0.2}
            size_hint_x:None
            width:300
        MDTextField:
            hint_text: "Enter Tank ID"
            icon_right: "android"
            helper_text: "automatically generated"
            helper_text_mode: "on_focus"
            icon_right_color: app.theme_cls.primary_color
            pos_hint:{'center_x': 0.5, 'center_y': 0.2}
            size_hint_x:None
            width:300
        MDTextField:
            id: name
            hint_text: "Enter Tank Name"
            icon_right: "android"
            icon_right_color: app.theme_cls.primary_color
            pos_hint:{'center_x': 0.5, 'center_y': 0.2}
            size_hint_x:None
            width:300

        MDRectangleFlatIconButton:
            text: 'submit'
            pos_hint: {'center_x': 0.5, 'center_y': 0.2}
            on_press: root.insertData()





        MDLabel:
            text: '     '
            size_hint_y: None
            height: self.texture_size[1]

<deleteDataScreen>:
    name :'deleteDataScreen'
    Screen:
        MDNavigationLayout:
            ScreenManager:
                Screen:
                    BoxLayout:
                        orientation: 'vertical'
                        MDToolbar: 
                            title: 'Demo'

                            right_action_items : [["share",lambda x: app.navigation_search()]]
                            elevation: 10
                        Widget:
                        MDRectangleFlatIconButton:
                            icon: 'share'
                            text: 'Return to previous'
                            line_color: 0, 0, 0, 0
                            pos_hint: {'left': 1, 'bottom': 1}
                            on_press: root.manager.current = 'menu'

    MDRaisedButton:
        text: 'select a vehicle'
        line_color: 0, 0, 0, 0
        pos_hint: {"center_x": 0.5, "center_y": 0.8} 
        on_press: app.launch_menu5(self)
        
        
    MDRaisedButton:
        text: 'delete'
        line_color: 0, 0, 0, 0
        pos_hint: {"center_x": 0.5, "center_y": 0.5} 
        on_release: root.delete()

<insertDataScreen2>:
    name:'insertDataScreen2'
    Screen:
        MDNavigationLayout:
            ScreenManager:
                Screen:
                    BoxLayout:
                        orientation: 'vertical'
                        MDToolbar: 
                            title: 'Panzerdaten spezifizieren'

                            right_action_items : [["share",lambda x: app.navigation_search()]]
                            elevation: 10
                        Widget:
                        MDRectangleFlatIconButton:
                            icon: 'share'
                            text: 'Return to previous'
                            line_color: 0, 0, 0, 0
                            pos_hint: {'left': 1, 'bottom': 1}
                            on_press: root.manager.current = 'insertDataScreen'

    BoxLayout:
        orientation:'horizontal'

        BoxLayout:
            orientation: 'vertical'
            pos_hint:{'center_x': 0.5, 'center_y': 0.7}
            MDLabel:
                text: '             Turret: '
                size_hint_y: None
                height: self.texture_size[1]

            MDTextField:
                id: t_armor
                hint_text: "armor (f/s/r) in mm"
                icon_right: "android"
                icon_right_color: app.theme_cls.primary_color
                pos_hint:{'center_x': 0.5, 'center_y': 0.2}
                size_hint_x:None
                width:300
            MDTextField:
                id: t_rotation_speed
                hint_text: "rotation speed (deg/sec)"
                icon_right: "android"
                icon_right_color: app.theme_cls.primary_color
                pos_hint:{'center_x': 0.5, 'center_y': 0.2}
                size_hint_x:None
                width:300
            MDTextField:
                id: t_view_range
                hint_text: "view range (m)"
                icon_right: "android"
                icon_right_color: app.theme_cls.primary_color
                pos_hint:{'center_x': 0.5, 'center_y': 0.2}
                size_hint_x:None
                width:300
            MDTextField:
                id: t_health
                hint_text: "health"
                icon_right: "android"
                icon_right_color: app.theme_cls.primary_color
                pos_hint:{'center_x': 0.5, 'center_y': 0.2}
                size_hint_x:None
                width:300
            MDTextField:
                id: t_weight
                hint_text: "weight (kg)"
                icon_right: "android"
                icon_right_color: app.theme_cls.primary_color
                pos_hint:{'center_x': 0.5, 'center_y': 0.2}
                size_hint_x:None
                width:300

            MDLabel:
                text: '             Tracks:'
                pos_hint: {'center_x': 0.5, 'center_y': 0.2}
                size_hint_y: None
                height: self.texture_size[1]

            MDTextField:
                id: tr_traverse
                hint_text: "traverse speed (deg/sec)"
                icon_right: "android"
                icon_right_color: app.theme_cls.primary_color
                pos_hint:{'center_x': 0.5, 'center_y': 0.2}
                size_hint_x:None
                width:300
            MDTextField:
                id: tr_max_load
                hint_text: "max load (kg)"
                icon_right: "android"
                icon_right_color: app.theme_cls.primary_color
                pos_hint:{'center_x': 0.5, 'center_y': 0.2}
                size_hint_x:None
                width:300

            MDRectangleFlatIconButton:
                text: 'submit'
                pos_hint: {'center_x': 0.5, 'center_y': 0.2}
                on_press: root.insertData2()
                on_release: root.manager.current = 'insertDataScreen3'


        BoxLayout:
            orientation: 'vertical'
            pos_hint:{'center_x': 0.5, 'center_y': 0.51}
            MDLabel:
                text: '            Engine: '
                size_hint_y: None
                height: self.texture_size[1]

            MDTextField:
                id: e_model
                hint_text: "Engine Model"
                icon_right: "android"
                icon_right_color: app.theme_cls.primary_color
                pos_hint:{'center_x': 0.5, 'center_y': 0.2}
                size_hint_x:None
                width:300
            MDTextField:
                id: e_power
                hint_text: "power (hp)"
                icon_right: "android"
                icon_right_color: app.theme_cls.primary_color
                pos_hint:{'center_x': 0.5, 'center_y': 0.2}
                size_hint_x:None
                width:300
            MDTextField:
                id: e_fire_chance
                hint_text: "fire chance (in percent)"
                icon_right: "android"
                icon_right_color: app.theme_cls.primary_color
                pos_hint:{'center_x': 0.5, 'center_y': 0.2}
                size_hint_x:None
                width:300
            MDTextField:
                id: e_weight
                hint_text: "weight (kg)"
                icon_right: "android"
                icon_right_color: app.theme_cls.primary_color
                pos_hint:{'center_x': 0.5, 'center_y': 0.2}
                size_hint_x:None
                width:300



            MDLabel:
                text: '            Gun: '
                size_hint_y: None
                height: self.texture_size[1]

            MDTextField:
                id: g_rof
                hint_text: "rate of fire (rnds/min)"
                icon_right: "android"
                icon_right_color: app.theme_cls.primary_color
                pos_hint:{'center_x': 0.5, 'center_y': 0.2}
                size_hint_x:None
                width:300
            MDTextField:
                id: g_penetration
                hint_text: "penetration (mm)"
                icon_right: "android"
                icon_right_color: app.theme_cls.primary_color
                pos_hint:{'center_x': 0.5, 'center_y': 0.2}
                size_hint_x:None
                width:300
            MDTextField:
                id: g_damage
                hint_text: "damage"
                icon_right: "android"
                icon_right_color: app.theme_cls.primary_color
                pos_hint:{'center_x': 0.5, 'center_y': 0.2}
                size_hint_x:None
                width:300
            MDTextField:
                id: g_dispersion
                hint_text: "dispersion (at 100m)"
                icon_right: "android"
                icon_right_color: app.theme_cls.primary_color
                pos_hint:{'center_x': 0.5, 'center_y': 0.2}
                size_hint_x:None
                width:300
            MDTextField:
                id: g_aim_time
                hint_text: "aim time (sec)"
                icon_right: "android"
                icon_right_color: app.theme_cls.primary_color
                pos_hint:{'center_x': 0.5, 'center_y': 0.2}
                size_hint_x:None
                width:300

            MDTextField:
                id: g_weight
                hint_text: "weight (kg)"
                icon_right: "android"
                icon_right_color: app.theme_cls.primary_color
                pos_hint:{'center_x': 0.5, 'center_y': 0.2}
                size_hint_x:None
                width:300

<insertDataScreen3>:
    name : 'insertDataScreen3'
    Screen:
        MDNavigationLayout:
            ScreenManager:
                Screen:
                    BoxLayout:
                        orientation: 'vertical'
                        MDToolbar: 
                            title: 'Panzerdaten spezifizieren2'

                            right_action_items : [["share",lambda x: app.navigation_search()]]
                            elevation: 10
                        Widget:
                        MDRectangleFlatIconButton:
                            icon: 'share'
                            text: 'Return to previous'
                            line_color: 0, 0, 0, 0
                            pos_hint: {'left': 1, 'bottom': 1}
                            on_press: root.manager.current = 'insertDataScreen2'

        BoxLayout:
            orientation: 'vertical'
            pos_hint:{'center_x': 0.5, 'center_y': 0.8}
            MDLabel:
                text: '                                                                           Radio Device: '
                size_hint_y: None
                height: self.texture_size[1]
            MDTextField:
                id: rd_model
                hint_text: "model"
                icon_right: "android"
                icon_right_color: app.theme_cls.primary_color
                pos_hint:{'center_x': 0.5, 'center_y': 0.2}
                size_hint_x:None
                width:300
            MDTextField:
                id: rd_range
                hint_text: "range (m)"
                icon_right: "android"
                icon_right_color: app.theme_cls.primary_color
                pos_hint:{'center_x': 0.5, 'center_y': 0.2}
                size_hint_x:None
                width:300               
            MDTextField:
                id: rd_weight
                hint_text: "weight (kg)"
                icon_right: "android"
                icon_right_color: app.theme_cls.primary_color
                pos_hint:{'center_x': 0.5, 'center_y': 0.2}
                size_hint_x:None
                width:300

            MDRectangleFlatIconButton:
                text: 'submit'
                pos_hint: {'center_x': 0.5, 'center_y': 0.2}
                on_press: root.insertData3()
                on_release: root.manager.current = 'menu'


<MyGoalsScreen>:
    name: "MyGoalsScreen"  

    MDToolbar:
        title: "My Results"
        pos_hint: {"top": 1} 
   

    MDCard:
        orientation: "vertical"
        pos_hint:{ "center_x" :0.5, "center_y": 0.5} 
        size_hint: 0.8, 0.7
        padding: "8dp"

    MDLabel:
        id: mylabel
        halign: "center"
        font_size: (root.width**2 + root.height**2) / 13**4
        size_hint: 0.8, 0.1


"""

ErrorMsg = """

MDFloatLayout:

    MDFlatButton:
        text: "ALERT DIALOG"
        pos_hint: {'center_x': .5, 'center_y': .5}
        on_release: app.show_alert_dialog()




"""
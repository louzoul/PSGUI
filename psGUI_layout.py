# -*- coding: utf-8 -*-
"""
Created on Fri Jul 24 20:31:05 2020

@author: yuta
"""
import PySimpleGUI as sg

itm_marker = ["None",".",",","o","^"]
itm_linestyle = ["None","solid","dashed","dashdot","dotted"]

font_frame = {"font":("Helvetica",15)}
font_check = {"default":False, "font":("Helvetica",15)}
font_text = {"font":("Helvetica",15), "size":(7,1)}
font_output = {"font":("Helvetica",15), "size":(7,1)}


def f_layout(window):

    if window == "Main":

        frame_canvas = sg.Frame("Canvas", **font_frame, layout=[
                        [sg.Canvas(key="-CANVAS-")]])
        
        frame_mole = sg.Frame("Mole", **font_frame, layout=[
                        [sg.Checkbox("ALL Check", **font_check, enable_events=True, key="check_all")],
                        [sg.Output(**font_output, key="matrix")],
                        [sg.Checkbox("Data-X", **font_check, key="check_12CO2"),sg.InputText(default_text = "0", **font_text, key = "Data-X")],
                        [sg.Checkbox("Data-Y", **font_check, key="check_13CO2"),sg.InputText(default_text = "1", **font_text, key = "Data-Y")]])
        
        frame_label = sg.Frame("Label", **font_frame, layout=[
                [sg.Text("Label X", **font_frame),sg.InputText(default_text = "X-axis", **font_text, key = "labelx",)],
                [sg.Text("Label Y", **font_frame),sg.InputText(default_text = "Y-axis", **font_text, key = "labely",)]])
        
        frame_button = [sg.Frame("Button", **font_frame, layout=[
                    [sg.Button("Load",key="load"),
                    sg.Button("Draw",key="draw"),
                    sg.Button("Popup",key="popup"),
                    sg.Button("Clear",key="clr"),
                    sg.Button("Save",key="save"),
                    sg.Button("Exit",key="exit")]])]

        layout = [[frame_mole,frame_canvas],[frame_label],frame_button]

    elif window == "Plot":
        layout = [[sg.Text("Marker", **font_frame), sg.InputCombo(itm_marker, size=(10,len(itm_marker)), default_value="None", key="marker")],
        [sg.Text("Linestyle", **font_frame), sg.InputCombo(itm_linestyle, size=(10,len(itm_linestyle)), default_value="solid", key="linestyle")],
        [sg.Checkbox("ManualRange X", **font_check, key="rangex"),
         sg.Checkbox("ManualRange Y", **font_check, key="rangey")],
        [sg.Checkbox("LogScale X", **font_check, key="logx"),
         sg.Checkbox("LogScale Y", **font_check, key="logy")],
        [sg.Text("Xmin", **font_frame),sg.InputText(default_text = "0", **font_text, key = "xmin",),
         sg.Text("Xmax", **font_frame),sg.InputText(default_text = "10", **font_text, key = "xmax",)],
        [sg.Text("Ymin", **font_frame),sg.InputText(default_text = "-1.0", **font_text, key = "ymin",),
         sg.Text("Ymax", **font_frame),sg.InputText(default_text = "1.0", **font_text, key = "ymax",)]]
    
    return layout
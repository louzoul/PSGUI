# -*- coding: utf-8 -*-
"""
Created on Fri Jul 24 20:31:05 2020

@author: yuta
"""
import PySimpleGUI as sg

itm_marker = ["None",".",",","o","^"]
itm_linestyle = ["None","solid","dashed","dashdot","dotted"]

font_Frame = {"font":("Helvetica",16)}
font_Checkbox = {"default":False, "font":("Helvetica",14)}
font_InputText = {"font":("Helvetica",14), "size":(7,1)}
font_Text = {"font":("Helvetica",14),"justification":"left"}
font_Button = {"font":("Helvetica",14)}
font_Output = {"font":("Helvetica",14), "size":(8,2)}
font_InputCombo = {"font":("Helvetica",14)}
font_Input = {"font":("Helvetica",13)}

def f_layout(window):

    if window == "Main":
        layout = [
        [sg.Frame("LoadFile", **font_Frame, layout=[
            [sg.Input(**font_Input),sg.FileBrowse(**font_Button, key="loadfile")]])],
        [sg.Frame("Canvas", **font_Frame, layout=[
            [sg.Canvas(key="-CANVAS-")]])],
        [sg.Frame("SaveCanvas", **font_Frame, layout=[
            [sg.Input(**font_Input),sg.FileSaveAs(**font_Button, key="savefile"), sg.OK(**font_Button, key="save")]])],
        [sg.Frame("Button", **font_Frame, layout=[
            [sg.Button("Draw", **font_Button, key="draw"),
             sg.Button("Clear", **font_Button, key="clr"),
             sg.Button("Setting Data", **font_Button, key="win_prepro"),
             sg.Button("Setting Plot", **font_Button, key="win_plot"),
             sg.Button("Exit", **font_Button, key="exit")]])]]

    elif window == "Prepro":
        layout = [
        [sg.Text("Row", **font_Text), sg.Output(**font_Output, key="row"),
         sg.Text("Column", **font_Text), sg.Output(**font_Output, key="column")],
        [sg.Checkbox("The number of data points use as X-Axis", **font_Checkbox, key="datapoints")],
        [sg.Checkbox("Multiplot using the all data", **font_Checkbox, key="multiplot")],
        [sg.Text("Data-X", **font_Text), sg.InputText(default_text = "0", **font_InputText, key = "Data-X"),
         sg.Text("Data-Y", **font_Text), sg.InputText(default_text = "1", **font_InputText, key = "Data-Y")]]

    elif window == "Plot":
        layout = [
        [sg.Text("Marker", **font_Text), sg.InputCombo(itm_marker, **font_InputCombo, size=(10,len(itm_marker)), default_value="None", key="marker"),
         sg.Text("Linestyle", **font_Text), sg.InputCombo(itm_linestyle, **font_InputCombo, size=(10,len(itm_linestyle)), default_value="solid", key="linestyle")],
        [sg.Checkbox("LogScale X", **font_Checkbox, key="logx"),
         sg.Checkbox("LogScale Y", **font_Checkbox, key="logy")],
        [sg.Checkbox("ManualRange X", **font_Checkbox, key="rangex"),
         sg.Checkbox("ManualRange Y", **font_Checkbox, key="rangey")],
        [sg.Text("Xmin", **font_Text),sg.InputText(default_text = "0", **font_InputText, key = "xmin",),
         sg.Text("Xmax", **font_Text),sg.InputText(default_text = "10", **font_InputText, key = "xmax",)],
        [sg.Text("Ymin", **font_Text),sg.InputText(default_text = "-1.0", **font_InputText, key = "ymin",),
         sg.Text("Ymax", **font_Text),sg.InputText(default_text = "1.0", **font_InputText, key = "ymax",)],
        [sg.Checkbox("Legend", **font_Checkbox, key="legend")],
        [sg.Text("Label X", **font_Text),sg.InputText(default_text = "X-axis", **font_InputText, key = "labelx",),
         sg.Text("Label Y", **font_Text),sg.InputText(default_text = "Y-axis", **font_InputText, key = "labely",)]]
    
    return layout
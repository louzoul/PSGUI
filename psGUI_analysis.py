# -*- coding: utf-8 -*-
"""
Created on Fri Jul 24 20:31:05 2020

@author: yuta
"""

import matplotlib.pyplot as plt
import numpy as np
import PySimpleGUI as sg
import matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from psGUI_layout import *
matplotlib.use("TkAgg")

# ------------------------------- Beginning of Matplotlib helper code -----------------------

def draw_figure(canvas, figure):
    figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
    figure_canvas_agg.draw()
    figure_canvas_agg.get_tk_widget().pack(side="top", fill="both", expand=10)
    figure_canvas_agg.get_tk_widget().grid(column=1,row=0)
    return figure_canvas_agg

def set_plt(event):
    if sub_values["logx"] == True:
        ax.set_xscale("log")
    if sub_values["logy"] == True:
        ax.set_yscale("log")
    if sub_values["rangex"] == True:
        try:
            ax.set_xlim(float(sub_values["xmin"]),float(sub_values["xmax"]))
        except ValueError:
            sg.popup_error("Error : Please input a numerical values")
            return
    if sub_values["rangey"] == True:
        try:
            ax.set_ylim(float(sub_values["ymin"]),float(sub_values["ymax"]))
        except ValueError:
            sg.popup_error("Error : Please input a numerical values")
            return
    ax.set_xlabel(values["labelx"])
    ax.set_ylabel(values["labely"])
    # ax.legend(loc="best",ncol=2)
    ax.grid()

    try:
        ax.plot(prepro_data[:,0],prepro_data[:,1],marker=sub_values["marker"],linestyle=sub_values["linestyle"])
    except NameError:
        sg.popup_error("Error : Please load a datafile")
        return
    
    return

def prepro(event):
    prepro_data = np.stack([data[:,int(values["Data-X"])],data[:,int(values["Data-Y"])]],1)
    return prepro_data

def load_file(datafile):
    data = np.loadtxt(datafile)
    window["matrix"].Update(data.shape)
    return data

# ------------------------------- Beginning of GUI CODE -------------------------------

layout_main = f_layout("Main")
window = sg.Window("Main Window", layout_main, finalize=True, element_justification="center", font="Helvetica 18")

layout_plot = f_layout("Plot")
window_plot = sg.Window("Plot Window", layout_plot, finalize=True, element_justification="center", font="Helvetica 18")
window_plot_active = True

fig = matplotlib.figure.Figure(figsize=(6,4), dpi=100)
fig_canvas_agg = draw_figure(window["-CANVAS-"].TKCanvas, fig)
ax = fig.add_subplot(111)

# イベントループ
while True:

    event,values = window.read(timeout=10)
    
    if event == None or event == "exit":
        window_plot.close()
        break
    
    elif event == "load":
        try:
            datafile = sg.popup_get_file("Please select a datafile")
            data = load_file(datafile)
        except (OSError,ValueError,TypeError):
            sg.popup_error("Error : Please select a datafile")
            
    elif event == "draw":
        ax.cla()
        try:
            prepro_data = prepro(event)
        except (NameError):
            sg.popup_error("Error : Please select a datafile")
        try:           
            set_plt(event)
        except TypeError:
            sub_values=[]
        fig_canvas_agg.draw()
        
    elif not window_plot_active and event == "popup":
        window_plot_active = True
        layout_plot = f_layout("Plot")
        window_plot = sg.Window("Plot Window", layout_plot, finalize=True, element_justification="center", font="Helvetica 18")
        
    elif event == "save":
        try:
            file = sg.popup_get_file("Please select a savefile", save_as=True)
            fig_canvas_agg.print_png(file)
        except (FileNotFoundError,ValueError):
            sg.popup_error("Error : Please select a savefile")
            
    elif event == "clr":
        ax.cla()
        fig_canvas_agg.draw()
    
    if window_plot_active:
        sub_event,sub_values = window_plot.read(timeout=10)
        if sub_event == None:
            window_plot_active = False
            window_plot.close()
            
window.close()

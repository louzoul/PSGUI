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
    figure_canvas_agg.get_tk_widget().pack(side="top", fill="both", expand=True)
    figure_canvas_agg.get_tk_widget().grid(column=1,row=0)
    return figure_canvas_agg

def set_plt(event):
    if values_plot["logx"] == True:
        ax.set_xscale("log")
    if values_plot["logy"] == True:
        ax.set_yscale("log")
    if values_plot["rangex"] == True:
        try:
            ax.set_xlim(float(values_plot["xmin"]),float(values_plot["xmax"]))
        except ValueError:
            sg.popup_error("Error : Please input a numerical values")
            return
    if values_plot["rangey"] == True:
        try:
            ax.set_ylim(float(values_plot["ymin"]),float(values_plot["ymax"]))
        except ValueError:
            sg.popup_error("Error : Please input a numerical values")
            return
    ax.set_xlabel(values_plot["labelx"])
    ax.set_ylabel(values_plot["labely"])
    ax.grid()

    try:
        if values_prepro["multiplot"]:
            ax.plot(prepro_data[:,0],prepro_data[:,1:],marker=values_plot["marker"],linestyle=values_plot["linestyle"])
        else:
            ax.plot(prepro_data[:,0],prepro_data[:,1],marker=values_plot["marker"],linestyle=values_plot["linestyle"])            
    except NameError:
        sg.popup_error("Error : Please load a datafile")
        return

    if values_plot["legend"] == True:
        ax.legend(loc="best",ncol=2)
    
    return

def prepro(event):
    X = np.linspace(0,len(data),len(data))
    if values_prepro["datapoints"] and values_prepro["multiplot"]:
        prepro_data = np.vstack([X.T,np.delete(data,int(values_prepro["Data-X"]),1).T]).T
    elif not values_prepro["datapoints"] and values_prepro["multiplot"]:
        prepro_data = np.vstack([data[:,int(values_prepro["Data-X"])].T,np.delete(data,int(values_prepro["Data-X"]),1).T]).T
    elif values_prepro["datapoints"] and not values_prepro["multiplot"]:
        prepro_data = np.stack([X,data[:,int(values_prepro["Data-Y"])]],1)
    elif not values_prepro["datapoints"] and not values_prepro["multiplot"]:
        prepro_data = np.stack([data[:,int(values_prepro["Data-X"])],data[:,int(values_prepro["Data-Y"])]],1)
    return prepro_data

def load_file(datafile):
    data = np.loadtxt(datafile)
    window_prepro["row"].Update(int(data.size/len(data)))
    window_prepro["column"].Update(len(data))
    return data

# ------------------------------- Beginning of GUI CODE -------------------------------

style_window = {"finalize":True, "element_justification":"left", "font":"Helvetica 18"}

layout_main = f_layout("Main")
window = sg.Window("Main Window", layout_main, **style_window)

layout_plot = f_layout("Plot")
window_plot = sg.Window("Plot Window", layout_plot, **style_window)
window_plot_active = True

layout_prepro = f_layout("Prepro")
window_prepro = sg.Window("Preprocessing Window", layout_prepro, **style_window)
window_prepro_active = True

fig = matplotlib.figure.Figure(figsize=(6,4), dpi=100)
fig.subplots_adjust(bottom=0.2, right=0.9, top=0.9, left=0.2)
fig_canvas_agg = draw_figure(window["-CANVAS-"].TKCanvas, fig)
ax = fig.add_subplot(111)

# イベントループ
while True:

    event,values = window.read(timeout=100)

    if values["loadfile"]:
        datafile = values["loadfile"]
        data = load_file(datafile)
    
    if event == None or event == "exit":
        window_plot.close()
        window_prepro.close()
        break
            
    elif event == "draw":
        ax.cla()
        try:
            prepro_data = prepro(event)
        except (NameError):
            sg.popup_error("Error : Please select a datafile")
        try:           
            set_plt(event)
        except TypeError:
            values_plot=[]
        fig_canvas_agg.draw()
    elif event == "clr":
        ax.cla()
        fig_canvas_agg.draw()
    
        
    elif not window_plot_active and event == "win_plot":
        window_plot_active = True
        layout_plot = f_layout("Plot")
        window_plot = sg.Window("Plot Window", layout_plot, **style_window)
    elif not window_prepro_active and event == "win_prepro":
        layout_prepro = f_layout("Prepro")
        window_prepro = sg.Window("Preprocessing Window", layout_prepro, **style_window)
        window_prepro_active = True
        
    elif event == "save":
        try:
            fig_canvas_agg.print_png(values["savefile"])
        except (FileNotFoundError,ValueError):
            sg.popup_error("Error : Please select a savefile")
            
    if window_plot_active:
        event_plot,values_plot = window_plot.read(timeout=100)
        if event_plot == None:
            window_plot_active = False
            window_plot.close()
    if window_prepro_active:
        event_prepro,values_prepro = window_prepro.read(timeout=100)
        if event_prepro == None:
            window_prepro_active = False
            window_prepro.close()

window.close()

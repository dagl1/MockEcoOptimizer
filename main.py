import os
import numpy as np
import pandas as pd
from dash import Dash, dcc
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate
import dash_bootstrap_components as dbc
from dash import html
import plotly.graph_objects as go

find_total_reduction_percentage_dict = {
    "option_1": {
        "percentage_piek_usage": 1,
        "battery_capacity_ratio": 1 / 2000,
        "solar_panel_ratio": 1/4,
        "total_reduction_percentage": 0.97,
    },
    "option_2": {
        "percentage_piek_usage": 1,
        "battery_capacity_ratio": 1 / 2000,
        "solar_panel_ratio": 1/3,
        "total_reduction_percentage": 0.125,
    },
    "option_3": {
        "percentage_piek_usage": 1,
        "battery_capacity_ratio": 1 / 2000,
        "solar_panel_ratio": 1/2,
        "total_reduction_percentage": 0.18,
    },
    "option_4": {
        "percentage_piek_usage": 1,
        "battery_capacity_ratio": 1 / 2000,
        "solar_panel_ratio": 2/3,
        "total_reduction_percentage": 0.235,
    },
    "option_5": {
        "percentage_piek_usage": 1,
        "battery_capacity_ratio": 1 / 2000,
        "solar_panel_ratio": 3/4,
        "total_reduction_percentage": 0.26,
    },
    "option_6": {
        "percentage_piek_usage": 0.66,
        "battery_capacity_ratio": 1 / 2000,
        "solar_panel_ratio": 1/4,
        "total_reduction_percentage": 0.10,
    },
    "option_7": {
        "percentage_piek_usage": 0.66,
        "battery_capacity_ratio": 1 / 2000,
        "solar_panel_ratio": 1/3,
        "total_reduction_percentage": 0.14,
    },
    "option_8": {
        "percentage_piek_usage": 0.66,
        "battery_capacity_ratio": 1 / 2000,
        "solar_panel_ratio": 1/2,
        "total_reduction_percentage": 0.208,
    },
    "option_9": {
        "percentage_piek_usage": 0.66,
        "battery_capacity_ratio": 1 / 2000,
        "solar_panel_ratio": 2/3,
        "total_reduction_percentage": 0.272,
    },
    "option_10": {
        "percentage_piek_usage": 0.66,
        "battery_capacity_ratio": 1 / 2000,
        "solar_panel_ratio": 3/4,
        "total_reduction_percentage": 0.299,
    },
    "option_11": {
        "percentage_piek_usage": 0.33,
        "battery_capacity_ratio": 1 / 2000,
        "solar_panel_ratio": 1/4,
        "total_reduction_percentage": 0.103,
    },
    "option_12": {
        "percentage_piek_usage": 0.33,
        "battery_capacity_ratio": 1 / 2000,
        "solar_panel_ratio": 1/3,
        "total_reduction_percentage": 0.135,
    },
    "option_13": {
        "percentage_piek_usage": 0.33,
        "battery_capacity_ratio": 1 / 2000,
        "solar_panel_ratio": 1/2,
        "total_reduction_percentage": 0.197,
    },
    "option_14": {
        "percentage_piek_usage": 0.33,
        "battery_capacity_ratio": 1 / 2000,
        "solar_panel_ratio": 2/3,
        "total_reduction_percentage": 0.273,
    },
    "option_15": {
        "percentage_piek_usage": 0.33,
        "battery_capacity_ratio": 1 / 2000,
        "solar_panel_ratio": 3/4,
        "total_reduction_percentage": 0.301,
    },
    "option_16": {
        "percentage_piek_usage": 1,
        "battery_capacity_ratio": 1 / 1500,
        "solar_panel_ratio": 1/4,
        "total_reduction_percentage": 0.098,
    },
    "option_17": {
        "percentage_piek_usage": 1,
        "battery_capacity_ratio": 1 / 1500,
        "solar_panel_ratio": 1/3,
        "total_reduction_percentage": 0.129,
    },
    "option_18": {
        "percentage_piek_usage": 1,
        "battery_capacity_ratio": 1 / 1500,
        "solar_panel_ratio": 1/2,
        "total_reduction_percentage": 0.186,
    },
    "option_19": {
        "percentage_piek_usage": 1,
        "battery_capacity_ratio": 1 / 1500,
        "solar_panel_ratio": 2/3,
        "total_reduction_percentage": 0.241,
    },
    "option_20": {
        "percentage_piek_usage": 1,
        "battery_capacity_ratio": 1 / 1500,
        "solar_panel_ratio": 3/4,
        "total_reduction_percentage": 0.26,
    },
    "option_21": {
        "percentage_piek_usage": 0.66,
        "battery_capacity_ratio": 1 / 1500,
        "solar_panel_ratio": 1/4,
        "total_reduction_percentage": 0.106,
    },
    "option_22": {
        "percentage_piek_usage": 0.66,
        "battery_capacity_ratio": 1 / 1500,
        "solar_panel_ratio": 1/3,
        "total_reduction_percentage": 0.14,
    },
    "option_23": {
        "percentage_piek_usage": 0.66,
        "battery_capacity_ratio": 1 / 1500,
        "solar_panel_ratio": 1/2,
        "total_reduction_percentage": 0.208,
    },
    "option_24": {
        "percentage_piek_usage": 0.66,
        "battery_capacity_ratio": 1 / 1500,
        "solar_panel_ratio": 2/3,
        "total_reduction_percentage": 0.27,
    },
    "option_25": {
        "percentage_piek_usage": 0.66,
        "battery_capacity_ratio": 1 / 1500,
        "solar_panel_ratio": 3/4,
        "total_reduction_percentage": 0.303,
    },
    "option_26": {
        "percentage_piek_usage": 0.33,
        "battery_capacity_ratio": 1 / 1500,
        "solar_panel_ratio": 1/4,
        "total_reduction_percentage": 0.103,
    },
    "option_27": {
        "percentage_piek_usage": 0.33,
        "battery_capacity_ratio": 1 / 1500,
        "solar_panel_ratio": 1/3,
        "total_reduction_percentage": 0.135,
    },
    "option_28": {
        "percentage_piek_usage": 0.33,
        "battery_capacity_ratio": 1 / 1500,
        "solar_panel_ratio": 1/2,
        "total_reduction_percentage": 0.198,
    },
    "option_29": {
        "percentage_piek_usage": 0.33,
        "battery_capacity_ratio": 1 / 1500,
        "solar_panel_ratio": 2/3,
        "total_reduction_percentage": 0.257,
    },
    "option_30": {
        "percentage_piek_usage": 0.33,
        "battery_capacity_ratio": 1 / 1500,
        "solar_panel_ratio": 3/4,
        "total_reduction_percentage": 0.281,
    },
    "option_31": {
        "percentage_piek_usage": 1,
        "battery_capacity_ratio": 1 / 2000,
        "solar_panel_ratio": 1,
        "total_reduction_percentage": 0.337,
    },
    "option_32": {
        "percentage_piek_usage": 0.66,
        "battery_capacity_ratio": 1 / 2000,
        "solar_panel_ratio": 1,
        "total_reduction_percentage": 0.37,
    },
    "option_33": {
        "percentage_piek_usage": 0.33,
        "battery_capacity_ratio": 1 / 2000,
        "solar_panel_ratio": 1,
        "total_reduction_percentage": 0.333,
    },
    "option_34": {
        "percentage_piek_usage": 1,
        "battery_capacity_ratio": 1 / 1500,
        "solar_panel_ratio": 1,
        "total_reduction_percentage": 0.344,
    },
    "option_35": {
        "percentage_piek_usage": 0.66,
        "battery_capacity_ratio": 1 / 1500,
        "solar_panel_ratio": 1,
        "total_reduction_percentage": 0.38,
    },
    "option_36": {
        "percentage_piek_usage": 0.33,
        "battery_capacity_ratio": 1 / 1500,
        "solar_panel_ratio": 1,
        "total_reduction_percentage": 0.36,
    },
    "option_37": {
        "percentage_piek_usage": 1,
        "battery_capacity_ratio": 1 / 4000,
        "solar_panel_ratio": 1/4,
        "total_reduction_percentage": 0.09,
    },
    "option_38": {
        "percentage_piek_usage": 1,
        "battery_capacity_ratio": 1 / 4000,
        "solar_panel_ratio": 1/3,
        "total_reduction_percentage": 0.117,
    },
    "option_39": {
        "percentage_piek_usage": 1,
        "battery_capacity_ratio": 1 / 4000,
        "solar_panel_ratio": 1/2,
        "total_reduction_percentage": 0.171,
    },
    "option_40": {
        "percentage_piek_usage": 1,
        "battery_capacity_ratio": 1 / 4000,
        "solar_panel_ratio": 2/3,
        "total_reduction_percentage": 0.225,
    },
    "option_41": {
        "percentage_piek_usage": 1,
        "battery_capacity_ratio": 1 / 4000,
        "solar_panel_ratio": 3/4,
        "total_reduction_percentage": 0.25,
    },
    "option_42": {
        "percentage_piek_usage": 1,
        "battery_capacity_ratio": 1 / 4000,
        "solar_panel_ratio": 1,
        "total_reduction_percentage": 0.323,
    },
    "option_43": {
        "percentage_piek_usage": 0.66,
        "battery_capacity_ratio": 1 / 4000,
        "solar_panel_ratio": 1/4,
        "total_reduction_percentage": 0.106,
    },
    "option_44": {
        "percentage_piek_usage": 0.66,
        "battery_capacity_ratio": 1 / 4000,
        "solar_panel_ratio": 1/3,
        "total_reduction_percentage": 0.14,
    },
    "option_45": {
        "percentage_piek_usage": 0.66,
        "battery_capacity_ratio": 1 / 4000,
        "solar_panel_ratio": 1/2,
        "total_reduction_percentage": 0.206,
    },
    "option_46": {
        "percentage_piek_usage": 0.66,
        "battery_capacity_ratio": 1 / 4000,
        "solar_panel_ratio": 2/3,
        "total_reduction_percentage": 0.264,
    },
    "option_47": {
        "percentage_piek_usage": 0.66,
        "battery_capacity_ratio": 1 / 4000,
        "solar_panel_ratio": 3/4,
        "total_reduction_percentage": 0.288,
    },
    "option_48": {
        "percentage_piek_usage": 0.66,
        "battery_capacity_ratio": 1 / 4000,
        "solar_panel_ratio": 1,
        "total_reduction_percentage": 0.351,
    },
    "option_49": {
        "percentage_piek_usage": 0.33,
        "battery_capacity_ratio": 1 / 4000,
        "solar_panel_ratio": 1/4,
        "total_reduction_percentage": 0.103,
    },
    "option_50": {
        "percentage_piek_usage": 0.33,
        "battery_capacity_ratio": 1 / 4000,
        "solar_panel_ratio": 1/3,
        "total_reduction_percentage": 0.134,
    },
    "option_51": {
        "percentage_piek_usage": 0.33,
        "battery_capacity_ratio": 1 / 4000,
        "solar_panel_ratio": 1/2,
        "total_reduction_percentage": 0.188,
    },
    "option_52": {
        "percentage_piek_usage": 0.33,
        "battery_capacity_ratio": 1 / 4000,
        "solar_panel_ratio": 2/3,
        "total_reduction_percentage": 0.23,
    },
    "option_53": {
        "percentage_piek_usage": 0.33,
        "battery_capacity_ratio": 1 / 4000,
        "solar_panel_ratio": 3/4,
        "total_reduction_percentage": 0.25,
    },
    "option_54": {
        "percentage_piek_usage": 0.33,
        "battery_capacity_ratio": 1 / 4000,
        "solar_panel_ratio": 1,
        "total_reduction_percentage": 0.294,
    },

}


find_solar_panel_amount_dict = {
            "option_1":
                {
                "percentage_piek_usage": 1,
                "battery_capacity_ratio": 1/2000,
                "total_reduction_percentage": 30,
                "solar_panels_required": 0.87,
            },
            "option_2":
                {
                "percentage_piek_usage": 1,
                "battery_capacity_ratio": 1/2000,
                "total_reduction_percentage": 40,
                "solar_panels_required": 1.23,
            },
            "option_3":
                {
                "percentage_piek_usage": 1,
                "battery_capacity_ratio": 1/2000,
                "total_reduction_percentage": 50,
                "solar_panels_required": 1.67,
            },
            "option_4":
                {
                "percentage_piek_usage": 1,
                "battery_capacity_ratio": 1/2000,
                "total_reduction_percentage": 60,
                "solar_panels_required": 2.3,
            },
            "option_5":
                {
                "percentage_piek_usage": 1,
                "battery_capacity_ratio": 1/2000,
                "total_reduction_percentage": 70,
                "solar_panels_required": 3.3,
            },
            "option_6":
                {
                "percentage_piek_usage": 0.66,
                "battery_capacity_ratio": 1/2000,
                "total_reduction_percentage": 30,
                "solar_panels_required": 0.75,
            },
            "option_7":
                {
                "percentage_piek_usage": 0.66,
                "battery_capacity_ratio": 1/2000,
                "total_reduction_percentage": 40,
                "solar_panels_required": 1.1,
            },
            "option_8":
                {
                "percentage_piek_usage": 0.66,
                "battery_capacity_ratio": 1/2000,
                "total_reduction_percentage": 50,
                "solar_panels_required": 1.59,
            },
            "option_9":
                {
                "percentage_piek_usage": 0.66,
                "battery_capacity_ratio": 1/2000,
                "total_reduction_percentage": 60,
                "solar_panels_required": 2.42,
            },
            "option_10":
                {
                "percentage_piek_usage": 0.66,
                "battery_capacity_ratio": 1/2000,
                "total_reduction_percentage": 70,
                "solar_panels_required": 4.42,
            },
            "option_11":
                {
                "percentage_piek_usage": 0.33,
                "battery_capacity_ratio": 1/2000,
                "total_reduction_percentage": 30,
                "solar_panels_required": 0.86,
            },
            "option_12":
                {
                "percentage_piek_usage": 0.33,
                "battery_capacity_ratio": 1/2000,
                "total_reduction_percentage": 40,
                "solar_panels_required": 142,
            },
            "option_13":
                {
                "percentage_piek_usage": 0.33,
                "battery_capacity_ratio": 1/2000,
                "total_reduction_percentage": 50,
                "solar_panels_required": 2.59,
            },
            "option_14":
                {
                "percentage_piek_usage": 0.33,
                "battery_capacity_ratio": 1/2000,
                "total_reduction_percentage": 60,
                "solar_panels_required": 8.5,
            },
            "option_15":
                {
                "percentage_piek_usage": 0.33,
                "battery_capacity_ratio": 1/2000,
                "total_reduction_percentage": 70,
                "solar_panels_required": None,
            },
            "option_16":
            {
                "percentage_piek_usage": 1,
                "battery_capacity_ratio": 1 / 1500,
                "total_reduction_percentage": 30,
                "solar_panels_required": 0.86,
            },
            "option_17":
            {
                "percentage_piek_usage": 1,
                "battery_capacity_ratio": 1 / 1500,
                "total_reduction_percentage": 40,
                "solar_panels_required": 1.20,
            },
            "option_18":
            {
                "percentage_piek_usage": 1,
                "battery_capacity_ratio": 1 / 1500,
                "total_reduction_percentage": 50,
                "solar_panels_required": 1.61,
            },
            "option_19":
            {
                "percentage_piek_usage": 1,
                "battery_capacity_ratio": 1 / 1500,
                "total_reduction_percentage": 60,
                "solar_panels_required": 0,
            },
            "option_20":
            {
                "percentage_piek_usage": 1,
                "battery_capacity_ratio": 1 / 1500,
                "total_reduction_percentage": 70,
                "solar_panels_required": 2.16,
            },
            "option_21":
            {
                "percentage_piek_usage": 0.66,
                "battery_capacity_ratio": 1 / 1500,
                "total_reduction_percentage": 30,
                "solar_panels_required": 0.75,
            },
            "option_22":
            {
                "percentage_piek_usage": 0.66,
                "battery_capacity_ratio": 1 / 1500,
                "total_reduction_percentage": 40,
                "solar_panels_required": 1.06,
            },
            "option_23":
            {
                "percentage_piek_usage": 0.66,
                "battery_capacity_ratio": 1 / 1500,
                "total_reduction_percentage": 50,
                "solar_panels_required": 1.47,
            },
            "option_24":
            {
                "percentage_piek_usage": 0.66,
                "battery_capacity_ratio": 1 / 1500,
                "total_reduction_percentage": 60,
                "solar_panels_required": 2.1,
            },
            "option_25":
            {
                "percentage_piek_usage": 0.66,
                "battery_capacity_ratio": 1 / 1500,
                "total_reduction_percentage": 70,
                "solar_panels_required": 327,
            },
            "option_26":
            {
                "percentage_piek_usage": 0.33,
                "battery_capacity_ratio": 1 / 1500,
                "total_reduction_percentage": 30,
                "solar_panels_required": 0.81,
            },
            "option_27":
            {
                "percentage_piek_usage": 0.33,
                "battery_capacity_ratio": 1 / 1500,
                "total_reduction_percentage": 40,
                "solar_panels_required": 1.25,
            },
            "option_28":
            {
                "percentage_piek_usage": 0.33,
                "battery_capacity_ratio": 1 / 1500,
                "total_reduction_percentage": 50,
                "solar_panels_required": 2.01,
            },
            "option_29":
            {
                "percentage_piek_usage": 0.33,
                "battery_capacity_ratio": 1 / 1500,
                "total_reduction_percentage": 60,
                "solar_panels_required": 3.90,
            },
            "option_30":
            {
                "percentage_piek_usage": 0.33,
                "battery_capacity_ratio": 1 / 1500,
                "total_reduction_percentage": 70,
                "solar_panels_required": 37.01,
            },
            "option_31":
            {
                "percentage_piek_usage": 1,
                "battery_capacity_ratio": 1 / 2000,
                "total_reduction_percentage": 20,
                "solar_panels_required": 0.55,
            },
            "option_32":
            {
                "percentage_piek_usage": 0.66,
                "battery_capacity_ratio": 1 / 2000,
                "total_reduction_percentage": 20,
                "solar_panels_required": 0.48,
            },
            "option_33":
            {
                "percentage_piek_usage": 0.33,
                "battery_capacity_ratio": 1 / 2000,
                "total_reduction_percentage": 20,
                "solar_panels_required": 0.51,
            },
            "option_34":
            {
                "percentage_piek_usage": 1,
                "battery_capacity_ratio": 1 / 1500,
                "total_reduction_percentage": 20,
                "solar_panels_required": 0.55,
            },
            "option_35":
            {
                "percentage_piek_usage": 0.66,
                "battery_capacity_ratio": 1 / 1500,
                "total_reduction_percentage": 20,
                "solar_panels_required": 0.48,
            },
            "option_36":
            {
                "percentage_piek_usage": 0.33,
                "battery_capacity_ratio": 1 / 1500,
                "total_reduction_percentage": 20,
                "solar_panels_required": 0.51,
            },


            "option_37":
            {
                "percentage_piek_usage": 1,
                "battery_capacity_ratio": 1 / 4000,
                "total_reduction_percentage": 20,
                "solar_panels_required": 0.6,
            },
            "option_38":
            {
                "percentage_piek_usage": 1,
                "battery_capacity_ratio": 1 / 4000,
                "total_reduction_percentage": 30,
                "solar_panels_required": 0.92,
            },
            "option_39":
            {
                "percentage_piek_usage": 1,
                "battery_capacity_ratio": 1 / 4000,
                "total_reduction_percentage": 40,
                "solar_panels_required": 1.32,
            },
            "option_40":
            {
                "percentage_piek_usage": 1,
                "battery_capacity_ratio": 1 / 4000,
                "total_reduction_percentage": 50,
                "solar_panels_required": 1.87,
            },
            "option_41":
            {
                "percentage_piek_usage": 1,
                "battery_capacity_ratio": 1 / 4000,
                "total_reduction_percentage": 60,
                "solar_panels_required": 2.74,
            },
            "option_42":
            {
                "percentage_piek_usage": 1,
                "battery_capacity_ratio": 1 / 4000,
                "total_reduction_percentage": 70,
                "solar_panels_required": 4.48,
            },
            "option_43":
            {
                "percentage_piek_usage": 0.66,
                "battery_capacity_ratio": 1 / 4000,
                "total_reduction_percentage": 20,
                "solar_panels_required": 0.49,
            },
            "option_44":
            {
                "percentage_piek_usage": 0.66,
                "battery_capacity_ratio": 1 / 4000,
                "total_reduction_percentage": 30,
                "solar_panels_required": 0.8,
            },
            "option_45":
            {
                "percentage_piek_usage": 0.66,
                "battery_capacity_ratio": 1 / 4000,
                "total_reduction_percentage": 40,
                "solar_panels_required": 1.25,
            },
            "option_46":
            {
                "percentage_piek_usage": 0.66,
                "battery_capacity_ratio": 1 / 4000,
                "total_reduction_percentage": 50,
                "solar_panels_required": 2,
            },
            "option_47":
            {
                "percentage_piek_usage": 0.66,
                "battery_capacity_ratio": 1 / 4000,
                "total_reduction_percentage": 60,
                "solar_panels_required": 3.68,
            },
            "option_48":
            {
                "percentage_piek_usage": 0.66,
                "battery_capacity_ratio": 1 / 4000,
                "total_reduction_percentage": 70,
                "solar_panels_required": 19.30,
            },
            "option_49":
            {
                "percentage_piek_usage": 0.33,
                "battery_capacity_ratio": 1 / 4000,
                "total_reduction_percentage": 20,
                "solar_panels_required": 0.55,
            },
            "option_50":
            {
                "percentage_piek_usage": 0.33,
                "battery_capacity_ratio": 1 / 4000,
                "total_reduction_percentage": 30,
                "solar_panels_required": 1.04,
            },
            "option_51":
            {
                "percentage_piek_usage": 0.33,
                "battery_capacity_ratio": 1 / 4000,
                "total_reduction_percentage": 40,
                "solar_panels_required": 2.06,
            },
            "option_52":
            {
                "percentage_piek_usage": 0.33,
                "battery_capacity_ratio": 1 / 4000,
                "total_reduction_percentage": 50,
                "solar_panels_required": 6.4,
            },
            "option_53":
            {
                "percentage_piek_usage": 0.33,
                "battery_capacity_ratio": 1 / 4000,
                "total_reduction_percentage": 60,
                "solar_panels_required": None,
            },
            "option_54":
            {
                "percentage_piek_usage": 0.33,
                "battery_capacity_ratio": 1 / 4000,
                "total_reduction_percentage": 70,
                "solar_panels_required": None,
            },
}



def input_reduction_find_solar_amount(
        percentage_piek_usage,
        battery_ratio,
        total_reduction,
        find_solar_panel_amount_dict,
):
    for option in find_solar_panel_amount_dict:
        option = find_solar_panel_amount_dict[option]
        print(option, percentage_piek_usage, battery_ratio, total_reduction)
        if (option["percentage_piek_usage"] == percentage_piek_usage and
            option["battery_capacity_ratio"] == battery_ratio and
            option["total_reduction_percentage"] == total_reduction*100
        ):
            return option["solar_panels_required"] if option["solar_panels_required"] is not None else 999999
    raise("No option found")

def input_solar_ratio_find_reduction(
        percentage_piek_usage,
        battery_ratio,
        solar_ratio,
        find_total_reduction_percentage_dict
):
    for option in find_total_reduction_percentage_dict:
        option = find_total_reduction_percentage_dict[option]
        if (option["percentage_piek_usage"] == percentage_piek_usage and
            option["battery_capacity_ratio"] == battery_ratio and
            option["solar_panel_ratio"] == solar_ratio
        ):
            return option["total_reduction_percentage"] if option["total_reduction_percentage"] is not None else 999999
    raise("No option found")

# notes that heatpump isnt part of energy consumption but reduces costs by 20% or more
#buttons
## calculate necessary amount of panels
## calculate total reduction with ratio

# display table
## options
## output
## besparing
## total investment
## TvT

# display financing plot
# update function

dropdown_input_column = dbc.Col(
    [
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.P("Piek usage percentage")
                    ]
                ),
                dbc.Col(
                    [
                        dcc.Dropdown(
                            options=[
                                {"label": "33%", "value": 0.33},
                                {"label": "66%", "value": 0.66},
                                {"label": "100%", "value": 1},
                            ],
                            id="percentage_piek_usage",
                            value=0.66
                        )
                    ]
                )
            ]
        ),
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.P("Battery Ratio")
                    ]
                ),
                dbc.Col(
                    [
                        dcc.Dropdown(
                            options=[
                                {"label": "1/1500", "value": 1/1500},
                                {"label": "1/2000", "value": 1/2000},
                                {"label": "1/4000", "value": 1/4000},
                            ],
                            id="battery_ratio",
                            value=1/2000
                        )
                    ]
                )
            ]
        ),
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.P("Enable heatpump")
                    ]
                ),
                dbc.Col(
                    [
                        dcc.Dropdown(
                            options=[
                                {"label": "Yes", "value": "Yes"},
                                {"label": "No", "value": "No"},
                            ],
                            id="enable_heatpump",
                            value="No"
                        )
                    ]
                )
            ]
        ),
        dbc.Row(
            [
                dbc.Col(
                    [
                        dbc.Button(
                            "Calculate amount of panels based on reduction",
                            n_clicks=0,
                            id="calculate_panels_based_on_reduction",
                            className= "me-2",
                            color = "dark",
                            outline=True
                        )
                    ]
                )
            ]
        ),
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.P("Reduce electricity usage percentage")
                    ]
                ),
                dbc.Col(
                    [
                        dcc.Dropdown(
                            options=[
                                {"label": "20%", "value": 0.20},
                                {"label": "30%", "value": 0.30},
                                {"label": "40%", "value": 0.40},
                                {"label": "50%", "value": 0.50},
                                {"label": "60%", "value": 0.60},
                                {"label": "70%", "value": 0.70},
                            ],
                            id="total_Reduction_percentage",
                            value=0.20
                        )
                    ]
                )
            ]
        ),
        dbc.Row(
            [
                dbc.Col(
                    [
                        dbc.Button(
                            "Calculate reduction based on panel to kWh ratio",
                            n_clicks=0,
                            id="calculate_reduction_based_on_panel_ratios",
                            className="me-2",
                            color = "dark",
                            outline = True
                        )
                    ]
                )
            ]
        ),
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.P("Solar panel ratio")
                    ]
                ),
                dbc.Col(
                    [
                        dcc.Dropdown(
                            options=[
                                {"label": "1/4", "value": 1 / 4},
                                {"label": "1/3", "value": 1 / 3},
                                {"label": "1/2", "value": 1 / 2},
                                {"label": "2/3", "value": 2 / 3},
                                {"label": "3/4", "value": 3 / 4},
                                {"label": "1", "value": 1},
                            ],
                            id="solar_ratio",
                            value=2 / 3
                        )
                    ]
                )
            ]
        )
    ]
)

number_input_column = dbc.Col(
    [
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.P("Total_electricity_usage (kWh)")
                    ]
                ),
                dbc.Col(
                    [
                        dbc.Input(
                            type="number",
                            id="kwh_usage",
                            placeholder="50000",
                        )
                    ]
                ),
            ]
        ),
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.P("Cost piekhours per kWh (euro)")
                    ]
                ),
                dbc.Col(
                    [
                        dbc.Input(
                            type="number",
                            id="piekhours_costs",
                            placeholder= 0.18
                        )
                    ]
                )
            ]
        ),
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.P("Cost dalhours per kWh (euro)")
                    ]
                ),
                dbc.Col(
                    [
                        dbc.Input(
                            type="number",
                            id="dalhours_costs",
                            placeholder= 0.15
                        )
                    ]
                )
            ]
        ),
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.P("Total gas usage (m3)")
                    ]
                ),
                dbc.Col(
                    [
                        dbc.Input(
                            type="number",
                            id="total_gas_usage",
                            placeholder= 1
                        )
                    ]
                )
            ]
        ),
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.P("Gas price per m3 (euro)")
                    ]
                ),
                dbc.Col(
                    [
                        dbc.Input(
                            type="number",
                            id="gas_price",
                            placeholder= 1.45
                        )
                    ]
                )
            ]
        ),
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.P("Cost per 450 wp panel (euro)")
                    ]
                ),
                dbc.Col(
                    [
                        dbc.Input(
                            type="number",
                            id="cost_per_panel",
                            placeholder= 405
                        )
                    ]
                )
            ]
        ),
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.P("Cost per kwh batery capacity (euro)")
                    ]
                ),
                dbc.Col(
                    [
                        dbc.Input(
                            type="number",
                            id="cost_battery_capacity",
                            placeholder=350
                        )
                    ]
                )
            ]
        ),
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.P("Heatpump price (euro)")
                    ]
                ),
                dbc.Col(
                    [
                        dbc.Input(
                            type="number",
                            id="heatpump_price",
                            placeholder=10000
                        )
                    ]
                )
            ]
        ),
    ]
)


# layout
dbc_layout = dbc.Container(
    [
        dcc.Store(id="store", data={
            "find_total_reduction_percentage_dict": find_total_reduction_percentage_dict,
            "find_solar_panel_amount_dict": find_solar_panel_amount_dict,
            "kwh_usage": 50000,
            "piekhours_costs": 0.18,
            "dalhours_costs": 0.15,
            "total_gas_usage": 1,
            "gas_price": 1.45,
            "cost_per_panel": 405,
            "cost_battery_capacity": 350,
            "total_Reduction_percentage": 0.20,
            "percentage_piek_usage": 0.66,
            "battery_ratio": 1/2000,
            "enable_heatpump": "No",
            "heatpump_price": 10000,
            "solar_ratio": 2/3,

        }),
        
        dbc.Row(
            [
                number_input_column,
                dropdown_input_column,
            ]
        ),
        # displays
        dbc.Row(
            [
                dbc.Col(
                    [
                        dbc.Table(
                            id="table",
                            bordered=True,
                            hover=True,
                            responsive=True
                        )
                    ]
                ),
                dbc.Col(
                    [
                        dcc.Graph(
                            id="financing_plot",
                        )
                    ]
                )
            ]
        )
    ]
)


def create_output_dict(
        kwh_usage,
        piekhours_costs,
        dalhours_costs,
        total_gas_usage,
        gas_price,
        cost_per_panel,
        cost_battery_capacity,
        total_Reduction_percentage,
        percentage_piek_usage,
        battery_ratio,
        enable_heatpump,
        heatpump_price,
        solar_ratio,
):

    print(
        kwh_usage,
        piekhours_costs,
        dalhours_costs,
        total_gas_usage,
        gas_price,
        cost_per_panel,
        cost_battery_capacity,
        total_Reduction_percentage,
        percentage_piek_usage,
        battery_ratio,
        enable_heatpump,
        heatpump_price,
        solar_ratio,
    )
    average_price_per_kwh = piekhours_costs * percentage_piek_usage + dalhours_costs * (1 - percentage_piek_usage)
    total_amount_of_solar_panels = (kwh_usage / 1000) * solar_ratio
    total_amount_of_batteries = (kwh_usage * battery_ratio)
    electricity_savings = kwh_usage * total_Reduction_percentage * average_price_per_kwh
    gas_usage = total_gas_usage if enable_heatpump == "No" else total_gas_usage * 0.1
    gas_savings = (total_gas_usage * 0.2 * gas_price) if enable_heatpump == "Yes" else 0
    total_savings = gas_savings + electricity_savings
    total_cost_of_batteries = (kwh_usage * battery_ratio) * cost_battery_capacity
    total_cost_of_solar_panels = (kwh_usage / 1000) * solar_ratio * cost_per_panel
    total_investment_cost = total_cost_of_batteries + total_cost_of_solar_panels + (heatpump_price if enable_heatpump == "Yes" else 0)
    time_to_return = total_investment_cost / total_savings

    output_dict = {
        "percentage_piek_usage": percentage_piek_usage,
        "battery_capacity_ratio": battery_ratio,
        "solar_panels_per_1000kwh": solar_ratio,
        "total_reduction_percentage": total_Reduction_percentage,
        "total_amount_of_solar_panels": total_amount_of_solar_panels,
        "total_amount_of_battery_capacity": total_amount_of_batteries,
        "heatpump_enabled": enable_heatpump,
        "total_gas_usage": gas_usage,
        "total_gas_savings": gas_savings,
        "total_electricity_savings": electricity_savings,
        "total_savings": total_savings,
        "total_cost_of_batteries": total_cost_of_batteries,
        "total_cost_of_solar_panels": total_cost_of_solar_panels,
        "total_cost_of_heatpump": heatpump_price,
        "total_investment_cost": total_investment_cost,
        "time_to_return": time_to_return,
    }
    return output_dict
def calculate_panels_based_on_reduction(
        kwh_usage,
        piekhours_costs,
        solar_ratio,
        dalhours_costs,
        total_gas_usage,
        gas_price,
        cost_per_panel,
        cost_battery_capacity,
        total_Reduction_percentage,
        percentage_piek_usage,
        battery_ratio,
        enable_heatpump,
        heatpump_price,
        find_solar_panel_amount_dict,
        find_total_reduction_percentage_dict,
):
    solar_panel_amount = input_reduction_find_solar_amount(
        percentage_piek_usage,
        battery_ratio,
        total_Reduction_percentage,
        find_solar_panel_amount_dict
    )
    output_dict = create_output_dict(
        kwh_usage,
        piekhours_costs,
        dalhours_costs,
        total_gas_usage,
        gas_price,
        cost_per_panel,
        cost_battery_capacity,
        total_Reduction_percentage,
        percentage_piek_usage,
        battery_ratio,
        enable_heatpump,
        heatpump_price,
        solar_panel_amount,
    )

    return output_dict

def calculate_reduction_based_on_panel_ratios(
        kwh_usage,
        piekhours_costs,
        dalhours_costs,
        total_gas_usage,
        gas_price,
        cost_per_panel,
        cost_battery_capacity,
        percentage_piek_usage,
        battery_ratio,
        enable_heatpump,
        heatpump_price,
        solar_ratio,
        total_Reduction_percentage,
        find_total_reduction_percentage_dict,
        find_solar_panel_amount_dict,
):
    total_reduction = input_solar_ratio_find_reduction(
        percentage_piek_usage,
        battery_ratio,
        solar_ratio,
        find_total_reduction_percentage_dict
    )
    output_dict = create_output_dict(
        kwh_usage,
        piekhours_costs,
        dalhours_costs,
        total_gas_usage,
        gas_price,
        cost_per_panel,
        cost_battery_capacity,
        total_reduction,
        percentage_piek_usage,
        battery_ratio,
        enable_heatpump,
        heatpump_price,
        solar_ratio,
    )
    return output_dict

dropdown_ids = [
    "percentage_piek_usage",
    "battery_ratio",
    "solar_ratio",
    "total_Reduction_percentage",
    "enable_heatpump",
    ]
input_ids = [
    "heatpump_price",
    "kwh_usage",
    "piekhours_costs",
    "dalhours_costs",
    "total_gas_usage",
    "gas_price",
    "cost_per_panel",
    "cost_battery_capacity",
]
to_calculate_ids = [
    "calculate_panels_based_on_reduction",
    "calculate_reduction_based_on_panel_ratios",
]

to_update_ids = [
    "table",
    "financing_plot",
]

button_ids = [
    "calculate_panels_based_on_reduction",
    "calculate_reduction_based_on_panel_ratios",
]

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
def dropdown_callback_factory(input_id, state, value_in_state):
    def dropdown_set_value_in_state(value, state):
        if value is None:
            raise PreventUpdate
        state[value_in_state] = value
        return value, state
    app.callback(
        Output(input_id, "value"),
        Output(state, "data", allow_duplicate=True),
        Input(input_id, "value"),
        State(state, "data"),
        prevent_initial_call=True,
    )(dropdown_set_value_in_state)

def input_callback_factory(input_id, state, value_in_state):
    def input_set_value_in_state(value, state):
        state[value_in_state] = value
        return value, state
    app.callback(
        Output(input_id, "value"),
        Output(state, "data", allow_duplicate=True),
        Input(input_id, "value"),
        State(state, "data"),
        prevent_initial_call=True,
    )(input_set_value_in_state)


for dropdown_id in dropdown_ids:
    dropdown_callback_factory(dropdown_id, "store", dropdown_id)

for input_id in input_ids:
    input_callback_factory(input_id, "store", input_id)


def create_table(output_dict):
    table = dbc.Table(
        [
            html.Thead(
                html.Tr(
                    [
                        html.Th("Total_amount_of_solar_panels"),
                        html.Th("Total battery capacity (kWh)"),
                        html.Th("Total savings (Euro)"),
                        html.Th("Total investment (Euro)"),
                        html.Th("TvT"),
                    ]
                )
            ),
            html.Tbody(
                [
                    html.Tr(
                        [
                            html.Td(round(output_dict["total_amount_of_solar_panels"],1)),
                            html.Td(round(output_dict["total_amount_of_battery_capacity"],1)),
                            html.Td(round(output_dict["total_savings"],1)),
                            html.Td(round(output_dict["total_investment_cost"],1)),
                            html.Td(round(output_dict["time_to_return"],1))
                        ]
                    )
                ]
            )
        ]
    )
    return table

def create_financing_plot(output_dict):
    # a line plot with with the total investment reduced by total savings from year 1
    financing_plot = go.Figure()
    end_value = output_dict["total_investment_cost"] - (int(output_dict["time_to_return"] + 2) * output_dict["total_savings"])
    # find place where line crosses 0
    position_where_0 = output_dict["total_investment_cost"] / output_dict["total_savings"]

    # add vertical red line at position where 0 is crossed with label: break even point
    financing_plot.add_shape(
        dict(
            type="line",
            x0=position_where_0,
            y0=end_value - (output_dict["total_savings"]),
            x1=position_where_0,
            y1=output_dict["total_investment_cost"],
            line=dict(
                color="red",
                width=2,
            )
        )
    )
    # label
    financing_plot.add_annotation(
        x=position_where_0,
        y=output_dict["total_investment_cost"],
        text="Break even point",
        showarrow=True,
        arrowhead=1,
    )
    # dashed horiziointal line at y = 0
    financing_plot.add_shape(
        dict(
            type="line",
            x0=0,
            y0=0,
            x1=int(output_dict["time_to_return"]+2),
            y1=0,
            line=dict(
                color="black",
                width=1,
                dash="dash",
            )
        )
    )


    financing_plot.add_trace(
        go.Scatter(
            x=[0, int(output_dict["time_to_return"]+2)],
            y=[output_dict["total_investment_cost"], end_value],
            mode="lines",
            name="Total investment",
        )
    )
    # add title: financial projection
    # add x axes years
    financing_plot.update_layout(
        title="Financial projection",
        xaxis_title="Years",
        yaxis_title="Cumulative ",
    )
    return financing_plot

def button_callback_factory(button_id, state, calculate_function):
    def button_calculate(n_clicks, state):
        if n_clicks is None:
            raise PreventUpdate
        output_dict = calculate_function(**state)
        table = create_table(output_dict)
        financing_plot = create_financing_plot(output_dict)
        return table, financing_plot
    app.callback(
        Output("table", "children", allow_duplicate=True),
        Output("financing_plot", "figure", allow_duplicate=True),
        Input(button_id, "n_clicks"),
        State("store", "data"),
        prevent_initial_call=True,
    )(button_calculate)

button_callback_factory("calculate_panels_based_on_reduction", "store", calculate_panels_based_on_reduction)
button_callback_factory("calculate_reduction_based_on_panel_ratios", "store", calculate_reduction_based_on_panel_ratios)



app.layout = dbc_layout



if __name__ == "__main__":
    app.run_server(debug=True)
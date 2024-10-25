import os
import numpy as np
import pandas as pd
from dash import Dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import json



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
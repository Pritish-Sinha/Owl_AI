from colour import Color
import altair as alt

def ocean_theme():

    ###### COLORS ######
    aero = "#77B5D9"
    blue = "#14397D"
    white = "#FFFFFF"

    aero_c = Color(aero)
    blue_c = Color(blue)
    white_c = Color(white)

    cont = [str(c) for c in blue_c.range_to(aero_c, 50)]
    div = [str(c) for c in blue_c.range_to(white_c, 25)] + [str(c) for c in
           white_c.range_to(aero_c, 25)]
    disc = ["#C137A2", "#694ED6", "#26D07C", "#009CBD", "#F04E98",
            "#ED8B00", "#FFD100", "#F9423A", "#C7C8CA", "#414141"]


    ###### TEXT ######
    title_font = "Futura"
    title_font_size = 22
    tick_font = "Roboto"
    tick_font_size = 12
    text_font = "Roboto"
    text_font_size = 14

    ###### CONFIGURATION ######
    config = {"config": {
        
            "background": '#FFFFFF',

            "title": {
                "anchor": "middle",
                "font": title_font,
                "fontSize": title_font_size
            },

            # Chart Types
            "arc": {
                "fill": aero,
                "tooltip": True},
            "area": {
                "stroke": blue,
                "fill": aero,
                "tooltip": True},
            "line": {
                "stroke": blue,
                "point": aero,
                "stroke_width": 3,
                "tooltip": True},
            "path": {
                "stroke": blue,
                "tooltip": True},
            "rect": {
                "fill": aero,
                "tooltip": True},
            "shape": {
                "stroke": blue,
                "tooltip": True},
            "symbol": {
                "fill": aero,
                "size": 30,
                "tooltip": True},

            "axis": {
                "domainWidth": 0.5,
                "grid": False,
                "labelPadding": 2,
                "tickSize": 5,
                "tickWidth": 0.5,
                "titleFontWeight": 'normal',
                "titleFont": text_font,
                "titleFontSize": text_font_size,
                "labelFont": tick_font,
                "labelFontSize": tick_font_size,
            },

            "axisBand": {
                "grid": False,
            },

            "legend": {
                "labelFontSize": 12,
                "padding": 1,
                "titleFont": text_font,
                "titleFontSize": text_font_size,
                "labelFont": tick_font,
                "labelFontSize": tick_font_size,
            },

            "range": {
                "category": disc,
                "diverging": div,
                "heatmap": cont,
                "ordinal": cont,
                "ramp": cont,
            },
        }
    }

    return config

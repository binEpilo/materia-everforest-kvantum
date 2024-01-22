#!/bin/python

def parse_colors():
    color_list = []

    with open("MateriaNordDark.kvconfig", "r") as kvconfig:
        for line in kvconfig:
            if '#' in line:
                ort = line.index('#')
                color_code = line[ort:ort+7]
                color_list.append(color_code)
    
    with open("MateriaNordDark.svg", "r") as svg:
        for line in svg:
            if '#' in line:
                ort = line.index('#')
                color_code = line[ort:ort+7]
                color_list.append(color_code)

    color_list_unique = list(set(color_list))
    return color_list_unique

def replace_colors():
    kvconfig_list = []
    with open("MateriaNordDark.kvconfig", "r") as kvconfig:
        for line in kvconfig:
            kvconfig_list.append(line)
    with open("MateriaNordDark.kvconfig", "w") as kvconfig:
        
        for item in kvconfig_list:
            if '#' in item:
                ort = item.index('#')
                if item[ort:ort+7] in ("#383f4e", "#3b4252", "#353b49", "#383f3e", "#2e3440"):
                    item = item[:ort] + "#333c43" + item[ort+7:]
                elif item[ort:ort+7] in "#434c5e":
                    item = item[:ort] + "#3a464c" + item[ort+7:]
                elif item[ort:ort+7] in ("#556076", "#4c556a", "#505b70", "#5b677f", "#434c5e", "#59647c"):
                    item = item[:ort] + "#434f55" + item[ort+7:]
                elif item[ort:ort+7] in "#bf616a":
                    item = item[:ort] + "#e67e80" + item[ort+7:]
                elif item[ort:ort+7] in ("#800080", "#ff00ff", "#b48ead"):
                    item = item[:ort] + "#d699b6" + item[ort+7:]
                elif item[ort:ort+7] in ("#d8dee9", "#e4e5e8", "#eceff4"):
                    item = item[:ort] + "#d3c6aa" + item[ort+7:]
                elif item[ort:ort+7] in ("#6f7d98", "#98a3b8", "#929eb3", "#7b88a1"):
                    item = item[:ort] + "#5d6b66" + item[ort+7:]
                elif item[ort:ort+7] in ("#5e81ac", "#81a1c1", "#88c0d0"):
                    item = item[:ort] + "#7fbbb3" + item[ort+7:]
                elif item[ort:ort+7] in ("#c1c9d7", "#acb1bc", "#bbc3d3", "#7b7b7b", "#787878"):
                    item = item[:ort] + "#9da9a0" + item[ort+7:]
                elif item[ort:ort+7] in "#000000":
                    item = item[:ort] + "#293136" + item[ort+7:]
                elif item[ort:ort+7] in "#484848":
                    item = item[:ort] + "#48584e" + item[ort+7:]
                kvconfig.write(item)
            else:
                kvconfig.write(item)
    svg_list = []
    with open("MateriaNordDark.svg", "r") as svg:
        for line in svg:
            svg_list.append(line)
    with open("MateriaNordDark.svg", "w") as svg:
        for item in svg_list:
            if '#' in item:
                ort = item.index('#')
                if item[ort:ort+7] in ("#383f4e", "#3b4252", "#353b49", "#383f3e", "#2e3440"):
                    item = item[:ort] + "#333c43" + item[ort+7:]
                elif item[ort:ort+7] in "#434c5e":
                    item = item[:ort] + "#3a464c" + item[ort+7:]
                elif item[ort:ort+7] in ("#556076", "#4c556a", "#505b70", "#5b677f", "#434c5e", "#59647c"):
                    item = item[:ort] + "#434f55" + item[ort+7:]
                elif item[ort:ort+7] in "#bf616a":
                    item = item[:ort] + "#e67e80" + item[ort+7:]
                elif item[ort:ort+7] in ("#800080", "#ff00ff", "#b48ead"):
                    item = item[:ort] + "#d699b6" + item[ort+7:]
                elif item[ort:ort+7] in ("#d8dee9", "#e4e5e8", "#eceff4"):
                    item = item[:ort] + "#d3c6aa" + item[ort+7:]
                elif item[ort:ort+7] in ("#6f7d98", "#98a3b8", "#929eb3", "#7b88a1"):
                    item = item[:ort] + "#5d6b66" + item[ort+7:]
                elif item[ort:ort+7] in ("#5e81ac", "#81a1c1", "#88c0d0"):
                    item = item[:ort] + "#7fbbb3" + item[ort+7:]
                elif item[ort:ort+7] in ("#c1c9d7", "#acb1bc", "#bbc3d3", "#7b7b7b", "#787878"):
                    item = item[:ort] + "#9da9a0" + item[ort+7:]
                elif item[ort:ort+7] in "#000000":
                    item = item[:ort] + "#293136" + item[ort+7:]
                elif item[ort:ort+7] in "#484848":
                    item = item[:ort] + "#48584e" + item[ort+7:]
                svg.write(item)
            else:
                svg.write(item)

replace_colors()

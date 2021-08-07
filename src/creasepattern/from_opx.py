from .cp import Cp, CpLine
import defusedxml.ElementTree as ET

def from_opx(infile) -> Cp:
    tree = ET.parse(infile)

    root = tree.getroot()

    xmlLines = root.findall(".//void[@property='lines']//array//object")

    lines = []

    for line in xmlLines:
        try:
            type = int(line.find("./void[@property='type']/int").text)
            x0_el = line.find("./void[@property='x0']/double")
            x1_el = line.find("./void[@property='x1']/double")
            y0_el = line.find("./void[@property='y0']/double")
            y1_el = line.find("./void[@property='y1']/double")

            x0 = float(x0_el.text) if x0_el != None else 0.0
            x1 = float(x1_el.text) if x1_el != None else 0.0
            y0 = float(y0_el.text) if y0_el != None else 0.0
            y1 = float(y1_el.text) if y1_el != None else 0.0

            cp_line = CpLine(type, x0, y0, x1, y1)
            lines.append(cp_line)
        except:
            pass  # This line is invalid

    return Cp(lines)
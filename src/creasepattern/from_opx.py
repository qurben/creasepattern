from .cp import Cp, CpLine, CpLineType
import defusedxml.ElementTree as ET


def from_opx(infile: str) -> Cp:
    tree = ET.parse(infile)

    root = tree.getroot()

    xml_lines = root.findall(".//void[@property='lines']//array//object")

    lines = []

    for line in xml_lines:
        try:
            line_type = int(line.find("./void[@property='type']/int").text)

            if line_type == 0:
                line_type = 4

            x0_el = line.find("./void[@property='x0']/double")
            x1_el = line.find("./void[@property='x1']/double")
            y0_el = line.find("./void[@property='y0']/double")
            y1_el = line.find("./void[@property='y1']/double")

            x0 = float(x0_el.text) if x0_el is not None else 0.0
            x1 = float(x1_el.text) if x1_el is not None else 0.0
            y0 = float(y0_el.text) if y0_el is not None else 0.0
            y1 = float(y1_el.text) if y1_el is not None else 0.0

            cp_line = CpLine(CpLineType(line_type), x0, y0, x1, y1)
            lines.append(cp_line)
        except:
            pass  # This line is invalid

    return Cp(lines)

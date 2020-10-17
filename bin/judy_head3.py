#!/usr/bin/env python
import sys

extra_table = {"LWA01": 15.582,
               "LWA02": 15.465,
               "T1M01": 23.686,
               "T1M02": 23.675,
               "T1M03": 22.143,
               "T1M04": 25.180,
               "T1M05": 25.119,
               "T1M06": 22.144,
               "T1M07": 23.675,
               "T1M08": 23.686,
               "U0S01":  1.264,
               "U0S02":  1.263,
               "JGP01": 32.785,
               "T5D01": 26.504,
               "T5D02": 32.284,
               "HWH01":  8.790,
               "T2J01": 45.171,
               "T0V01": 14.729,
               "T0V02": 29.347,
               "U1V01": -1.606,
               "T6701": 35.322,
               "T6702": 41.262,
               "T8P01": 39.813,
               "T8P02": 26.973,
               "T7S01": 22.400,
               "T4Y01": 29.714,
               "T4Y02": 29.247,
               "T4Y03": 22.980
               }


class Conformer:
    def __init__(self, line):
        fields = line.split()
        self.iconf = fields[0]
        self.conformer = fields[1]
        self.fl = fields[2]
        self.occ = fields[3]
        self.crg = fields[4]
        self.em0 = fields[5]
        self.pka0 = fields[6]
        self.ne = fields[7]
        self.nh = fields[8]
        self.vdw0 = fields[9]
        self.vdw1 = fields[10]
        self.tors = fields[11]
        self.epol = fields[12]
        self.dsolv = fields[13]
        self.extra = fields[14]
        self.history = fields[15]
        self.flag = fields[16]

    def writeme(self):
        return("%s %s %s %4s %6s %5s %5s %2s % 2s %7s %7s %7s %7s %7s %7s %10s %s\n" % (self.iconf,
                                     self.conformer,
                                     self.fl,
                                     self.occ,
                                     self.crg,
                                     self.em0,
                                     self.pka0,
                                     self.ne,
                                     self.nh,
                                     self.vdw0,
                                     self.vdw1,
                                     self.tors,
                                     self.epol,
                                     self.dsolv,
                                     self.extra,
                                     self.history,
                                     self.flag))

if __name__ == "__main__":
    """
    This program takes head3.lst and 
    1. alter extra column according to extra_table{}, 
    2. set vdw0, tors, epol to 0
    3. set dummy to "t 0.00"
    """

    # Translate to dummy table
    dummy_table = []
    for key in extra_table.keys():
        dummy_name = "%sDM" % key[:3]
        if dummy_name not in dummy_table:
            dummy_table.append(dummy_name)

    print(dummy_table)

    head3_lines = open("head3.lst").readlines()
    newlines = [head3_lines.pop(0)]
    for line in head3_lines:
        conf = Conformer(line)
        confname = conf.conformer[:5]
        if confname in extra_table:
            conf.extra = "%.3f" % extra_table[confname]
            conf.vdw0 = "0.000"
            conf.tors = "0.000"
            conf.epol = "0.000"
        if confname in dummy_table:
            conf.fl = "t"
            conf.occ = "0.00"
        newlines.append(conf.writeme())

    sys.stdout.writelines(newlines)
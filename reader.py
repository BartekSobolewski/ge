import pandas as pd
def csv_reader(plik):
    table=pd.read_csv(plik, delimiter=" ")
    table = table.iloc[:, :-1]
    table.columns=['Zlocation','ZVelocity','AnaloginVoltage','BTDetect','TankWaterTemp','TankWaterDlint','BTVelRatio','BTVoltageRatio',
                   'PumpPressuerActual','ActiveRecipe','PfmOnTime','PfmOffTime','EdmCurrentHMI','EdmCapacitance','SpindleTargetSpeed',
                   'ElectrodeGap','ZWorkPosition','Holeprogresstrackingvariable','PumpPressureSpindle','BTVoltageStdDev','Averagefeedrate']
    return table
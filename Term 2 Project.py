#We chose to test 2 from each
#- Variable/Lists
PTC = ["BPCM","BPSH","RTMS","RTLM"] #Phone/Tablet Code
PTD = ["Compact","Clam Shell","RoboTab – 8-inch screen and 64GB memory","RoboTab – 10-inch screen and 128GB memory"] #Phone/Tablet Description
PTP = [29.99, 49.99, 149.99, 299.99] #Phone/Tablet Price
#-
ScC = ["SMNO","SMPG"] #Sim Card Code
ScD = ["SIM Free (no SIM card purchased)","Pay As You Go (SIM card purchased)"] #Sim Card Description
ScP = [0, 9.99] #Sim Card Price
#-
CCC = ["CSST","CSLX","CGCR","CGHM"] #Case/Charger Code
CCD = ["Standard","Luxury","Car","Home"] #Case/Charger Description
CCP = [0, 50, 19.99, 15.99] #Case/Charger Price
#-
Total = float(0)
Extra_Devices = -1
Answer = 1
Items_Purchased = []
#----------

#- Actal Code starts here
while Answer == 1:
  DeviceC = input("Please enter the device's (Phone/Tablet) Code: ") #Device Code
  Device_Index = int(PTC.index(DeviceC)) #Find the number position of the device
  Total = Total+float(PTP[Device_Index]) #Adds the price to the total
  Items_Purchased.append(DeviceC)
  #-
  SimC = input("Please enter the SIM Card's Code: ") #Sim Code
  Sim_Index = int(ScC.index(SimC)) #Find the number position of the SIM Card
  Total = Total+float(ScP[Sim_Index]) #Adds the price to the total
  Items_Purchased.append(SimC)
  #-
  CaseC = input("Please enter the Case's Code: ") #Case Code
  Case_Index = int(CCC.index(CaseC)) #Find the number position of the Case
  Total = Total+float(CCP[Case_Index]) #Adds the price to the total
  Items_Purchased.append(CaseC)
  #-
  Answer2 = int(input ("Do you want a charger?\nYes:1 \nNo: 2\n"))
  while Answer2 == 1:
    ChargerC = input("Please enter the Charger's Code: ") #Chager Code
    Charger_Index = int(CCC.index(ChargerC)) #Find the number position of the device
    Total = Total+float(CCP[Charger_Index]) #Adds the price to the total
    Items_Purchased.append(ChargerC)
    Answer2 = int(input ("Do you want a another charger?\nYes:1 \nNo: 2\n"))
  #-
  Extra_Devices = Extra_Devices + 1
  Answer = int(input ("Do you want a another Device?\nYes:1 \nNo: 2\n"))
#----------

#- Calculating Discount
if Extra_Devices > 0:
  Discount = int(Extra_Devices*10)
  Final_Price = float(Total-(Total*Discount)/100)
  Amount_Saved = float(Total-Final_Price)
#----------

#- Outputting
print ("Items Purchased:", Items_Purchased)
if Extra_Devices > 0:
  print("Final Price:", round(Final_Price,2)) #Rounds to 2 dp
  print ("Amount Saved:", round(Amount_Saved,2)) #Rounds to 2 dp
else:
  print (round(Total,2)) #Rounds to 2 dp
#----------

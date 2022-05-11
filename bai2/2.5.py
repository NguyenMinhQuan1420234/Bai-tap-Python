LaiSuat = eval(input("Lai suat 1 nam (%): \n"))
SoTienGui = eval(input("So tien gui: \n"))
SoThangGui = eval(input("So Thang gui: \n"))

Tienlai = (SoTienGui*SoThangGui)*(LaiSuat/12)
print("Tien lai = (%i*%i)*(%.2f/12) = " %(SoTienGui,SoThangGui,LaiSuat), (SoTienGui*SoThangGui)*(LaiSuat/12))
print("Tien lai = ({:,d}*{:,d})*({:,.2f}/12) = {:,.2f}".format(SoTienGui,SoThangGui,LaiSuat,Tienlai)) 
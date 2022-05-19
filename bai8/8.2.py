#tinh chi so BMI

def BMI (height, weight):
    value = weight / (height*height)
    print(f"Chỉ số BMI của bạn: {value:.2f}")
    if value < 18.5:
        print("Kết quả: Bạn gầy")
    elif value >= 25:
        print("Kết quả: Bạn thừa cân")
    else:
        print("Bạn bình thường")

weight = float(input("Nhập cân nặng (kg): \n"))
height = float(input("Nhập chiều cao (m): \n"))
BMI(height,weight) 
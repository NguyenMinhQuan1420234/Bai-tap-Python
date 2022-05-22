
#Mở file 
f = open("baihat.txt","w", encoding="utf-8")  #lưu ý quan trọng, phải lưu tập tin chọn chế độ utf-8 (lưu chế độ nào thì mở chế đó, nếu k nó sẽ báo lỗi )
print("Xem thuộc tính: ")
print(f.closed,'\t', f.mode,'\t', f.name)    #xem các thuộc tính

# f.seek(0)
# print("Vị trí hiện hành của con trỏ" , f.tell())
# Đọc file
# noidung = f.read()
# print(noidung) # không có dữ liệu vì mở chế độ này con trỏ này nằm cuối file, nếu muốn đọc từ đầu phải dùng lệnh f.seek(0)
# print("Vị trí hiện hành của con trỏ" , f.tell())

noidung = """GỢI NHỚ QUÊ HƯƠNG
Quê em hai mùa mưa nắng,
Hai thôn nghèo nối liền bờ đê,
Từng lũy tre xanh nghiêng nghiêng chiều hè,
Như bức tranh gợi tình quê đậm đà.
Lời ru con tiếng võng đong đưa.
Ai chờ ai thương giòng nước u buồn.
"""
f.write(noidung)    #Ghi vào cuối file
f.close()


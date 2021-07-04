from numpy.lib.arraysetops import union1d
import pandas as pd
import numpy as np
'''
Pandas basic
'''

# read_csv() : Đọc dữ liệu từ file trong đường dẫn
df = pd.read_csv('chipotle.tsv', sep = "\t")

# Xuất 5 kí tự đầu tiên của bảng dữ liệu vừa được đọc:
# print(df.head())

# Xuất số hàng và số cột trong dataset: 
# print(df.shape)
# print(df.info())

# Trả về tên tất cả các cột
# print(df.columns)

'''
Location vs Index Location 
loc[] vs iloc[[]]
'''
# select trong dataset, những phần tử nào trùng với diều kiện
# print(df.loc[(df.quantity == 2) & (df.item_name == 'Nantucket Nectar'), ['order_id', 'quantity', 'item_name']])
# print(df.iloc[3:11])

'''
Data Manipulation
Làm việc với dữ liệu trong dataframe
'''

'''
.dtype will return data type of data:
'b' boolean
'i' (signed) integer
'u' unsigned integer
'f' floating-point
'c' complex-floating point
'O' object
'S' (byte) string
'U' Unicode
'V' raw data (void)
'''
'''
Sẽ rất khó để thao tác với dữ liệu khi trong dữ liệu có chưa ký tự đặc biệt như tỏng cột item_price
cho nên cân fdugf hàm apply() để format lại dữ liệu có trong cột thành dạng số.
'''
df.item_price = df.item_price.apply(lambda x : float(x.replace('$', '')))

# Tạo một colums mới:
df['total_price'] = df['quantity']*df['item_price']
#print(df.head())

# Tổng toàn bộ của một cột:
df['total_price'].sum()

'''
Group By
'''
s = df.groupby('item_name')['quantity'].sum()

'''
Sort : Hàm sort_value() trong pandas chỉ sắp xếp từ nhỏ tới lớn, muốn thay đổi thì phải đổi ascending = False
ex: Xuất ra nhưng món có số lượng mua nhiều nhất.
'''
sort = s.sort_values(ascending=False)
#print(sort.head()) 

'''
Unique value: Những giá trị không trùng nhau (value_counts())
ex: có bao nhiêu mặt hàng khác nhau đã được bán, 
- Đầu tiên, dùng value_counts() để tìm những mặt hàng không tùng tên
- Sau đó dùng hàm count() để cộng hết rất cả lại.

Hoặc dùng hàm .nunique()
'''
unique = df.item_name.value_counts().count()
print(unique)
print(df.item_name.nunique())
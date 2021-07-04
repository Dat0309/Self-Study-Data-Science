import numpy as np

'''
Numpy Basic
Thêm một mảng :
'''
a = np.array([[1, 2, 3], [4, 5, 6]])

'''
shape: trả về số hàng và số cột của mảng
ndim: Trả về số chiều của mảng, vd mảng 1 chiều, 2 chiều
dtype: Trả về kiểu dữ liệu trong mảng
size: Trả về size của mảng
'''

'''
Creating Numpy Arrays from Scratch
zeros, ones, full, arange, linspace
'''
# Tạo mảng toàn số 0
np.zeros(a)

# Tạo 1 mảng toàn số 1
np.ones(a)

# Tạo 1 mảng theo ý muốn, gồm một range từ x -> y
np.arange(1,10,2) # start = 1, end = 10, step = 2

# Tạo numpy array và fill theo ý muốn
np.full((3,5), 6.9) #size = 3x5, fill = 6.9

# Tạo mảng có chứa điểm đầu và điểm cuối cho trước, khoảng cách tuyến tính của nó
np.linspace(0, 1, 5) # start = 0, end = 1, step = 5

'''
random : trả lại một mảng numpy có số dòng và số cột cho trước, và random số thực trong khoảng 0.0 -> 1.0
Seed: những con số ngẫu nhiên của mỗi lần random sẽ không thay dổi
randint: random những số nguyên
'''
np.random.random((3, 3))
np.random.seed(0)
np.random.randint(0, 10, (4, 5))

'''
Array Indexing & Slicing
'''
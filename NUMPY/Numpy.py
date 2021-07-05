import numpy as np

'''
Numpy Basic
Thêm một mảng :
'''
a = np.array([1, 2, 3])

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
# One - dimensional subarray:
#a[4], a[0], a[-1]

# Multi - Dimaensional array:
#a[1,2]

'''
Slicing: 
x[start : stop : step]
'''
#a[0 : 2 : 1]

'''
Reshaping of arrays & Transpose
'''
grid = np.arange(1,10)
#print(grid.shape)
#print(grid.reshape((3,3)).shape)
#print(grid.shape)
 # Transpose: .T : Đổi cột thành hàng, hàng thành cột
 # a.T

'''
Array Concattenation and Splitting : 
Nối 2 arr với nhau
'''
x = np.array([1,2,3])
y = np.array([3,2,1])
z = np.concatenate((x,y))
#print(z)

# vstack, hstack : Nối 2 mảng theo hàng, cột
#print(np.vstack((x, y)))

'''
Broadcasting and Vectorized operations
add, sub, multi, dev, ...
'''
#print(a + 5)
#print(a * x)

'''
Standard Deviation and Variance: Độ lệch chuẩn và phương sai, kích thước đó độ phân tán của gí trị,
giúp ta hiểu rõ hơn về dữ liệu của mình thông qua những con số.
Cách tính: tính trung bình cộng của dữ liệu.
Lấy dữ liệu thật trừ đi dữ liệu trung bình sẽ ra độ lệch
lấy độ lệch bình phương, tính trung bình cộng sẽ ra phương sai
căn bậc 2 của phương sai sẽ là độ lệch chuẩn.

Điểm hay là giupos cho ta coi những dữ liệu trong dataset, cái nào là normal, extra large, extra small.
np.std()
np.sqrt()
np.var()

'''
dog_height = [600, 470, 170, 430, 300]
dog_height = np.array(dog_height)

# độ lệch chuẩn
# print(np.std(dog_height))
# Phương sai
# print(np.var(dog_height))

'''
Sorting Arrays: Quick Sort 
np.sort Sắp xếp tăng dần
np.argsort() : trả về vị trí của các phần từ trong mảng đã sort

'''
# Sort along rows of colums
# matA = np.random.seed(42)
# np.sort(matA, axis=0) # Xếp tăng dần theo cột
# np.sort(matA, axis=1) # Xếp tăng theo hàng

'''
Linear Algebra : Đại số tuyến tính
'''
A = np.array([[1,2,3], [4,5,6], [7,8,6]])
B = np.array([[6,5], [4,3], [2,1]])
A.dot(B) # Tích vô hướng 2 ma trận



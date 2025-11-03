import matplotlib.pyplot as plt
x1=[1,2,2,3]
y1=[2,3,1,2]
x2=[6,7,8,7]
y2=[7,6,8,5]
x3=[1,8,7,3]
y3=[2,6,1,5]
x4=[1,2,2,3]
y4=[2,6,1,2]
plt.scatter(x1,y1,color="red",label="Class A")
plt.scatter(x2,y2,color="blue",label="Class B")
plt.scatter(x3,y3,color="green",label="Class C")
plt.scatter(x4,y4,color="yellow",label="Class D")
x_line=[0,10]
y_line=[4,4]
plt.plot(x_line,y_line,'k--',label="Seperating line")
plt.title("Simple example")
plt.xlabel("X-axis")
plt.ylabel("y-axis")
plt.legend()
plt.show()
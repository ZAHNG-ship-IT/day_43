import matplotlib.pyplot as plt   ###将这个库名字命名为plt
input_value = [1,2,3,4,5]
squares = [1,4,9,16,25]

fig, ax = plt.subplots()    ###变量fig表示由生成的一系列绘图构成的整个图形
ax.plot(input_value,squares, linewidth = 3)#宽度加粗

ax.set_title("squaers Nums",fontsize = 24)  #font字号，显示文字的大小
ax.set_xlabel("value",fontsize = 14)
ax.set_ylabel("square of value",fontsize = 14)

ax.tick_params(labelsize = 14)




plt.show()###打开查看器，并显示绘图

###绘制的第一个折线图


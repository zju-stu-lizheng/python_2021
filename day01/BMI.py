height = eval(input('你的身高(/m)'))
weight = eval(input('你的体重(/kg)'))
BMI = weight / (height*height)
if BMI < 18.5:
    print('过轻')
elif BMI < 25:
    print('正常')
elif BMI < 28:
    print('过重')
elif BMI < 32:
    print('肥胖')
else:
    print('严重肥胖')
input('谢谢你的信任，按ENTER键结束')

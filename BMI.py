Height = input ('請輸入身高(單位公尺): ')
Height = float (Height)
Weight = input ('請輸入體重(單位公斤): ')
Weight = float (Weight)
BMI = Weight / (Height * Height)
print ('你的BMI是: ', BMI)
if BMI >= 24 and BMI < 27:
	print('過重')
elif BMI >= 27 and BMI < 30:
	print('輕度肥胖')
elif BMI >= 30 and BMI < 35:
	print('中度肥胖')
elif BMI >= 35:
	print('重度肥胖')
else:
	print('正常')
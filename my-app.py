#можно преобразовать столбец в one-hot вид без использования get_dummies. 
#Воспользуемся методом pd.get_dummies и выполним необходимые шаги:

import pandas as pd

# Ваш код для создания DataFrame
random.seed(42)
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})
data.head()

#Теперь, чтобы преобразовать столбец 'whoAmI' в one-hot кодировку

# Преобразование в one-hot кодировку
one_hot_encoded = pd.get_dummies(data['whoAmI'], prefix='whoAmI')

# Склеим исходные данные с новыми столбцами one-hot
data_one_hot = pd.concat([data, one_hot_encoded], axis=1)

# Удалим исходный столбец 'whoAmI'
data_one_hot = data_one_hot.drop('whoAmI', axis=1)

data_one_hot.head()

#В результате data_one_hot будет содержать столбцы one-hot кодировки для столбца 'whoAmI'.
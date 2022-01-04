import pandas as pd
#import csv
#a = csv.excel_tab()
data = {'product_name': ['laptop', 'printer', 'tablet', 'desk', 'chair'],
        'price': [1200, 150, 300, 450, 200]
        }
df = pd.DataFrame(data, index=['product_1','product_2','product_3','product_4','product_5'])
print (df)

df = pd.DataFrame(data)
print (df)





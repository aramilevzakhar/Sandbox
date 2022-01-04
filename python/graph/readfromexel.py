#Here is a simple example using ordinary least squares
import pandas as pd
df = pd.read_excel (r'Path where the Excel file is stored\File name.xlsx')
print (df)

#Note that for an earlier version of Excel, you may need to use the file extension of ‘xls’
#And if you have a specific Excel sheet that you’d like to import, you may then apply:
import pandas as pd
df = pd.read_excel (r'Path where the Excel file is stored\File name.xlsx', sheet_name='your Excel sheet name')
print (df)


#ptional Step: Selecting subset of columns
#Now what if you want to select a specific column or columns from the Excel file?
#For example, what if you want to select only the Product column? If that’s the case, you can specify this column name as captured below:
import pandas as pd
data = pd.read_excel (r'C:\Users\Ron\Desktop\Product List.xlsx') 
df = pd.DataFrame(data, columns= ['Product'])
print (df)



#You can specify additional columns by separating their names using a comma, so if you want to include both the Product and Price columns, you can use this syntax:
import pandas as pd
data = pd.read_excel (r'C:\Users\Ron\Desktop\Product List.xlsx') 
df = pd.DataFrame(data, columns= ['Product','Price'])
print (df)


import pandas as pd

df = pd.read_csv (r'C:\Users\Ron\Desktop\Clients.csv')
#read the csv file (put 'r' before the path string to address any special characters in the path, such as '\'). Don't forget to put the file name at the end of the path + ".csv"
print (df)


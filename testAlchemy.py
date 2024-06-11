import pandas as pd
import sqlalchemy
from sqlalchemy import create_engine

#create an engine that will open the file and point to it
engine = create_engine('sqlite:///testdb.sqlite')

#create a query
query = "SELECT * FROM member WHERE full_name='Abdullah';"

#convert the query in datafram
df = pd.read_sql(query, engine)
#If you like, you can say read_sql_table...
#df = pd.read_sql_table('member', engine)
#you can print
print (df)
print (len(df))

#You can read column
df_column = pd.read_sql_table('member', engine)
print (df_column)

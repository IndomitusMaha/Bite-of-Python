"""import glob
import os

list_of_files = glob.glob('C://Users//7//Desktop//М.М.Zh//Python Makha//ListOfFiles*') # * means all if need specific format then *.csv
latest_file = max(list_of_files, key=os.path.getctime)
print (latest_file)
#os.startfile(latest_file)
"""""

import os

path = 'data'
os.chdir('C://Users//7//Desktop//М.М.Zh//Python Makha//ListOfFiles')
files = sorted(os.listdir(os.getcwd()), key=os.path.getmtime)

oldest = files[0]
newest = files[-1]

print ("Oldest:", oldest)
print ("Newest:", newest)
print ("All by modified oldest to newest:", files)
os.startfile(newest)
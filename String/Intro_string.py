# String is a data type in python
# String is a sequance of characters enclosed in quotes
# We can primarily write an string in these three ways
a = 'Syed'          #Single quoted string
b = "Muhammad"      #Double quoted string
c = '''Aamer'''     #Triple quoted string
print(a+b+c)

# Slice String / String Slicing
name = "syedmuhammadaamer"
nameshort = name[4:12] # start from index 4 to all the way till 11 (excl 11)
print(nameshort)

# Negative Slicing
print(name[-13:-5])
print(name[12:18])
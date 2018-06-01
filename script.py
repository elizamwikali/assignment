Python 3.6.5 (v3.6.5:f59c0932b4, Mar 28 2018, 16:07:46) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> list1 = [1,2,42,62,73,29,45]
>>> type(list1)
<class 'list'>
>>> list2 = ['education','career','sports','family']
>>> type(list2)
<class 'list'>
>>> list3 = ['U.S.','Kenya', 294,'South Africa','China',400,600]
>>> type(list3)
<class 'list'>
>>> tuple1(1,7,3,'june','september','lamborghini',592,'abc')
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    tuple1(1,7,3,'june','september','lamborghini',592,'abc')
NameError: name 'tuple1' is not defined
>>> tuple1 = (1,7,3,'june','september','lamborghini',592,'abc')
>>> type(tuple1)
<class 'tuple'>
>>> set1 = {'mango','avocado','watermelon','vans','kids'}
>>> type(set1)
<class 'set'>
>>> dict1 = {'Name':'Elizabeth','Nationality':'Kenyan','Age':20,'Gender':'Female','Address':'Embakasi'}
>>> type(dict1)
<class 'dict'>
>>> print(list1,list2,list3,tuple1,set1,dict1)
[1, 2, 42, 62, 73, 29, 45] ['education', 'career', 'sports', 'family'] ['U.S.', 'Kenya', 294, 'South Africa', 'China', 400, 600] (1, 7, 3, 'june', 'september', 'lamborghini', 592, 'abc') {'watermelon', 'avocado', 'kids', 'vans', 'mango'} {'Name': 'Elizabeth', 'Nationality': 'Kenyan', 'Age': 20, 'Gender': 'Female', 'Address': 'Embakasi'}
>>> 

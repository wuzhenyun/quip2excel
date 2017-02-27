file_object=open('contact.txt')
contents=file_object.readlines()
persons=list()
person={}
for line in contents :
	items=line.split("：")
	if len(items)==1:
		if person:
			persons.append(person)
		person={}
		continue
	person[items[0]]=items[1]
	print(persons)

import pandas
pandas.DataFrame(persons)
df=pandas.DataFrame(persons)
writer=pandas.ExcelWriter('abc.xlsx')
df.to_excel(writer,'sheet1')
writer.save()

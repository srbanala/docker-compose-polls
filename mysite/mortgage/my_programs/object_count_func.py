# This program calculates the object count between two uploaded files.

det object_count_func (file_name1,file_name2):
	import os,openpyxl
	os.chdir(C:\\Users\\anred\\Downloads')
	prod=open('prod.txt','r')
	stage=open('stage.txt','r')
    	prod_data=prod.readlines()
	stage_data=stage.readlines()
	prod_output=[]
    	stage_output=[]
    	prod.close()
    	stage.close()
	for data in prod_data:
		if '\n' in data:
			prod_output.append(data.strip('\n'))
       		else:
			prod_output.append(data)
	for data in stage_data:
		if '\n' in  data:
			stage_output.append(data.strip('\n'))
		else:
			stage_output.append(data)
    	my_file=open('output.txt','w')
    	wb=openpyxl.Workbook()
    	sheet=wb['Sheet']
    	sheet.title='Count'
    	print("|{0:15s}|{1:20s}|{2:^10s}|".format('Schema_name','Object_name','Difference'))
    	x="|{0:15s}|{1:20s}|{2:^10s}|".format('Schema_name','Object_name','Difference')
    	sheet.cell(row=1,column=1).value='Schema_name'
    	sheet.cell(row=1,column=2).value='Object_type'
    	sheet.cell(row=1,column=3).value='Difference'
    	#wb.save('Object_count.xlsx')
    	my_file.write(x)
    	count=0
    	for data in prod_output:
		prod_output1=data.split(',')
		for item in stage_output:
			stage_output1=item.split(',')
            		#print(prod_output1,stage_output1)
            		#print("|{0:15s}|{1:20s}|{2:^10s}|".format('Schema_name','Object_name','Difference'))
                                   
            		if prod_output1[0]==stage_output1[0] and  prod_output1[1]==stage_output1[1]:
                		#print(prod_output1[2].strip(),stage_output1[2].strip())
                		x="|{0:15s}|{1:20s}|{2:^10d}|".format(prod_output1[0],prod_output1[1],int(prod_output1[2])-int(stage_output1[2]))
                		print(x)
                		my_file.write(x)
                		sheet.cell(row=count+2,column=1).value=prod_output1[0]
                		sheet.cell(row=count+2,column=2).value=prod_output1[1]
                		sheet.cell(row=count+2,column=3).value=int(prod_output1[2])-int(stage_output1[2])
                		count=count+1
                
    	wb.save('Object_count.xlsx')          
    	my_file.close()
    	my_data=open('output.txt','r')
    	#print(my_data.read())
   
    return None
print(object_count_func(file_name1,file_name2))
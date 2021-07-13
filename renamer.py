import os
path=os.chdir("D:\\jaysh\\7th SEM\\Summer internship\\Covid-resources\\CovidDataset\\Train\\Covid")
i = 1
for old_name in os.listdir(path):
    print(old_name)
    new_name = "COVID{}.mkv".format(i)
    # os.rename(old_name,new_name)
    # print()
    i+=1
    print(i)
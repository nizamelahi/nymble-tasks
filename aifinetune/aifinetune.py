import openai
import csv
import jsonlines
with jsonlines.open('/media/nizam/OS/nymble-tasks/aifinetune/output.jsonl', mode='w') as writer:
    with open('/media/nizam/OS/nymble-tasks/aifinetune/smallset.csv', newline='') as csvfile:
                temp=[]
                temp2=[]
                tempdict={}
                row = csv.reader(csvfile, delimiter=',',quotechar='|')  
                for data in row:

                    if len(data)>3:
                        del data[0]
                        tempdict["prompt"]=data[0]+(" ->\n\n###\n\n")
                        
                        del data[0]
                        tempdict["completion"]=" "+','.join(data).strip("\"").replace(" ,",",")
                        print (tempdict["completion"])
                        writer.write(tempdict)
                        temp2.append(tempdict)
                        # print(temp2)
                        tempdict.clear()
            
                
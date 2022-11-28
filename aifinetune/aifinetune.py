import csv
import jsonlines
import pathlib
import os
inputfilename=f'smallset.csv'
print("current input file:" + inputfilename)
with jsonlines.open(os.path.join(pathlib.Path(__file__).parent.resolve(),f'FineTuneFile.jsonl'), mode='w') as writer:
    with open(os.path.join(pathlib.Path(__file__).parent.resolve(),inputfilename), newline='') as csvfile:
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
                        writer.write(tempdict)
                        temp2.append(tempdict)
                        tempdict.clear()
                
                print("output saved to FineTuneFile.jsonl in current directory")
            
                
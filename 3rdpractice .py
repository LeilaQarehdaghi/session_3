import pandas as pd

#create data frame

data = {'A': ['#','#','0','0','0','0','#','0','0','0'],
        'B': ['0','0','#','#','0','0','0','#','0','0'],
        'C': ['0','0','0','0','0','#','0','0','#','0'],
        'D': ['0','0','0','0','#','0','0','0','0','#'],
        }
df = pd.DataFrame(data)
print(df)
#create a empty list

result_test = []

#create a function
        
def quiz_correction (question ,keyword ,dataframe, answer_sheet):
    #a for loop that refer to each student

    for student in range(answer_sheet):
        t=0
        f=0
        keyword = str(keyword)
        #a for loop that refer to each row of questions

        for first_index in df.index.values.tolist():
            count = 0
            #convert elements of keyword to column's index

            key_word = keyword[first_index]

            if key_word == 'A':
                key_result = 0
            elif key_word == 'B':
                key_result = 1
            elif key_word == 'C':
                key_result = 2
            elif key_word == 'D':
                key_result = 3


            print(key_word,key_result)
            
            #loop in columns
                                            
            for col in range(0,4):
                print(first_index, col,df.iloc[first_index][col] )
                if df.iloc[first_index][col] == '#'  :
                    count = count+1
                    print('count= ',count)
                    #condition that match keyword with col

                    if col== key_result:
                        t += 1
                    else:
                        f +=1
                        
            if count ==0 :
                t=0
                f=0
            elif count != 1:
                t=0
                f=1
            
        result = (3*t)-f
        result_test.append(result)
        return result_test
print(quiz_correction(question= 10,keyword = 'AABBDCABCD',dataframe=df,answer_sheet=1 ))        
        
        

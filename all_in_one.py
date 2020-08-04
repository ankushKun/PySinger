import os

for root,dirs,files in os.walk('./data/'):
    for f in files:
        if os.path.join(root,f).endswith('.txt'):
            with open(os.path.join(root,f),'r') as ly:
                print(f">> processing {files.index(f)}/{len(files)} : {f}")
                with open('./INPUT_DATA.txt','a') as a:
                    a.write(ly.read()+'\n\n\n')

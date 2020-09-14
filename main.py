import os

def createIFnotExist(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)   #makedirs helps to make directory or folders as req.

def  move(folderName, files):
    for file in files :
        os.replace(file, f"{folderName}/{file}")   


if __name__ == "__main__":
    files = os.listdir()
    files.remove('main.py')       

    createIFnotExist('Images')
    createIFnotExist('Docs')
    createIFnotExist('Media')
    createIFnotExist('Others')


    imgExts = ['.png' , '.jpg' , '.jpeg']
    images = [file for file in files if os.path.splitext(file)[1].lower() in imgExts]

    docExts = ['.txt' , '.docx' , '.pdf' , 'doc']
    docs = [file for file in files if os.path.splitext(file)[1].lower() in docExts]


    mediaExts = ['.mp4' , '.mp3' , '.flv']
    medias = [file for file in files if os.path.splitext(file)[1].lower() in mediaExts] 

    others = []
    for file in files:
        ext = os.path.splitext(file)[1].lower()
        if (ext not in mediaExts) and (ext not in imgExts) and (ext not in docExts) and os.path.isfile(file): #os.path.isfile() will make sure that only files get transfered not folders
            others.append(file)

    move ("Images", images)
    move ("Docs", docs)
    move ("Media", medias)
    move ("Others", others)



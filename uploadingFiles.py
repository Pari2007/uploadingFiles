from os import access
import dropbox

class Transferdata:
    def __init__(self,access_token):
        self.access_token = access_token

    def uploadFiles(self,files_from, files_to):
        
        dbx = dropbox.Dropbox(self.access_token)

        with open(files_from, "rb") as f:
            dbx.files_upload(f.read(), files_to)

def main():
    access_token = "sl.AxQzEf6hB1RvOY8mCJOw9aIy0PKr-fEmxcWSXnbmFLVj3rB6i5t2gYZ10MpNb6ow8je5yvyXrEi0tRVe9c1uZDrJbRj4krQG64cZtkXAxBekQzSAk48zrC3yJ-ZqCmrU9uvdkmY"
    transferData = Transferdata(access_token)

    files_from = input("Enter the file's path to transfer:  ")
    files_to = input("Enter the full path to upload the file to: ")

    transferData.uploadFiles(files_from,files_to)

if __name__ == "__main__":
    main()
    

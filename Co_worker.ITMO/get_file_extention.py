# defiation function
def get_file_extention(file_name):
    file_extention = file_name[len(file_name)-3:]
    return file_extention

# call function
print(get_file_extention("video.mp4"))

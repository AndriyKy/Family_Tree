# # importing Image class from PIL package  
# from PIL import Image 
   
# # creating a object  
# image = Image.open("D:/Оброблені/Гало/IMG_7205.jpg")
# im_size = image.size

# if im_size[0] > im_size[1]:
#     MAX_WIDTH = 175
#     MAX_HEIGHT = (MAX_WIDTH * im_size[1]) // im_size[0] 
# elif im_size[0] < im_size[1]:
#     MAX_HEIGHT = 175
#     MAX_WIDTH = (MAX_HEIGHT * im_size[0]) // im_size[1]
# else:
#     MAX_WIDTH = MAX_HEIGHT = 175

# image.thumbnail((MAX_WIDTH, MAX_HEIGHT))
# print(type(image))
# # image.show()


lst = ["test", "sets"]
print(lst[0][0])
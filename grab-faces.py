from PIL import Image
import face_recognition
import os, sys

if len(sys.argv) < 2:
    print("ENTER A DIRECTORY OF IMAGES.")
    quit()

# directory of images to extract the faces from.
directory = sys.argv[1]

# create
if not os.path.exists("./faces"):
    os.mkdir("./faces")
    
savepath = "./faces"

nof = 0

for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    # checking if it is a file
    if os.path.isfile(f):
        print(f)
        if f.endswith(".png") or f.endswith(".jpg") or f.endswith(".jpeg"):

            # Load the jpg file into a numpy array
            image = face_recognition.load_image_file(f)

            # Find all the faces in the image using the default HOG-based model.
            # This method is fairly accurate, but not as accurate as the CNN model and not GPU accelerated.
            # See also: find_faces_in_picture_cnn.py
            face_locations = face_recognition.face_locations(image)

            print("I found {} face(s) in this photograph.".format(len(face_locations)))

            for face_location in face_locations:
                nof = nof + 1       # increment the "number of faces" counter
                # Print the location of each face in this image
                top, right, bottom, left = face_location
                print("A face is located at pixel location Top: {}, Left: {}, Bottom: {}, Right: {}".format(top, left, bottom, right))

                # You can access the actual face itself like this:
                face_image = image[top:bottom, left:right]
                pil_image = Image.fromarray(face_image)
                #pil_image.show()
                pil_image.save(savepath + "/face_" + str(nof) + ".png", format='png')
                print("FACE " + str(nof) + " saved.")

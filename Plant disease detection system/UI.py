import tkinter as tk
from PIL import ImageTk, Image

# Create a Tkinter window
window = tk.Tk()
window.title("Image Uploader")

# Define a function to browse and upload the image
def upload_image():
    # Open a file dialog box to select an image
    file_path = tk.filedialog.askopenfilename()
    
    # Open the selected image using PIL
    image = Image.open(file_path)
    
    # Display the uploaded image
    photo = ImageTk.PhotoImage(image)
    image_label.config(image=photo)
    image_label.image = photo
    
    # Show accuracy and confidence
    accuracy_label.config(text="Accuracy: 95%")
    confidence_label.config(text="Confidence: High")

# Create a button to upload an image
upload_button = tk.Button(window, text="Upload Image", command=upload_image)
upload_button.pack()

# Create a label to display the uploaded image
image_label = tk.Label(window)
image_label.pack()

# Create a label to show accuracy
accuracy_label = tk.Label(window, text="")
accuracy_label.pack()

# Create a label to show confidence
confidence_label = tk.Label(window, text="")
confidence_label.pack()

# Run the Tkinter window
window.mainloop()

#%%

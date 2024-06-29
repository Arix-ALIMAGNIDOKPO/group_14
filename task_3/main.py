import customtkinter as ctk
import tkinter
from PIL import Image, ImageTk, ImageSequence
from diffusers import StableDiffusionPipeline # pip install diffusers transformers accelerate
import torch # pip install torch
import threading

""" Crée une variable globale animation_running pour activer ou désactiver l'animation du spinner """
global animation_running 
global images
animation_running = False
images = []

"""
la méthode show_spinner, permet d'animer le spinner pendant la génération de l'image, elle vérifie si la variable 
globale animation_running est True avant d'animer le spinner, le fichier spinner.gif contient un spinner animé, on 
crée une liste des frames des séquences du GIF, considérez que chaque déplacement du spinner est un frame, le spinner 
n'est pas tout juste affiché à l'utilisateur, il est animé par le programme même, on prend chaque frame des séquences 
du spinner puis on les affiche un à un après une durée donnée, mais la permutation de frame est tellement fluide qu'on
ne se rend pas compte que c'est plusieurs séquences qui sont en train d'être affichées tour à tour
"""
def show_spinner(frame_index=0):
    global animation_running
    if animation_running:
        canvas.delete("all")
        image = Image.open("spinner.gif")

        # Charger toutes les frames du GIF
        frames = [frame.copy() for frame in ImageSequence.Iterator(image)]

        frame = frames[frame_index]
        tk_image = ImageTk.PhotoImage(frame)

        # Disposer le spinner au milieu du canvas
        canvas_width = canvas.winfo_reqwidth()
        canvas_height = canvas.winfo_reqheight()
        image_width = tk_image.width()
        image_height = tk_image.height()
        x = (canvas_width - image_width) // 2
        y = (canvas_height - image_height) // 2
        image_id = canvas.create_image(x, y, anchor=tkinter.NW, image=tk_image)

        canvas.itemconfig(image_id, image=tk_image)
        canvas.image = tk_image

        # Passer à la frame suivante
        frame_index = (frame_index + 1) % len(frames)
        root.after(50, show_spinner, frame_index)


"""
La méthode generate est la méthode qui permet de générer l'image, elle crée une liste vide d'images, utilise le model 
choisi pour l'utilisateur, crée une boucle en fonction du nombre d'images choisi par l'utilisateur mais plus le nombre 
d'images est beaucoup, plus la génération d'images prendra du temps, et à chaque fois qu'une image est prête, on 
l'ajoute à la liste des images puis on l'affiche pendant que les autres images sont en train d'être chargées en arrière plan
"""
def generate():
    global animation_running
    global images
    
    images = []
    

    """
    update_image permet la permutation des images, après 3 secondes, on crée dans le canva une image de l'une des images de la
    liste images en fonction de l'index donné en paramètre à la méthode, ce qui remplace l'image actuel dans le canva et ainsi
    de suite jusqu'à finir la liste et reprendre du début
    """
    def update_image(index=0):
        if len(images) >= 1:
            canvas.image = images[index]
            canvas.create_image(0, 0, anchor="nw", image=images[index])
            index = (index + 1) % len(images) 
            canvas.after(3000, update_image, index)

    model = model_dropdown.get()
    if(model == "tiny-stable-diffusion-pipe"):
        pipe = StableDiffusionPipeline.from_pretrained("hf-internal-testing/tiny-stable-diffusion-torch")
    elif model == "tiny-sd":
        pipe = StableDiffusionPipeline.from_pretrained("segmind/tiny-sd")
    
    pipe = pipe.to("cuda" if torch.cuda.is_available() else "cpu")
    user_prompt = prompt_entry.get("0.0", tkinter.END).strip()
    num_images = int(number_slider.get())

    """
    Cette boucle permet de génerer une ou plusieurs images en fonction du nombres d'images spécifiées par 
    l'utilisateur et d'ajouter le(s) images à la liste images et elle(s) sera/seront directement affichée(s) 
    """
    for _ in range(num_images):
        # Generate the image
        image = pipe(user_prompt).images[0]
        image_resize = image.resize((canvas.winfo_width(),canvas.winfo_height()))
        
        # Convert PIL Image to PhotoImage
        photo_image = ImageTk.PhotoImage(image_resize)
        images.append(photo_image)
        update_image()
        animation_running = False

"""
Commande pour le bouton generate, lorsque l'utilisateur clique sur le bouton generate, on met la variable animation_runing à 
True  on crée un nouveau thread pour séparer 
"""
def on_click():
    global animation_running
    animation_running = True
    threading.Thread(target=generate).start()  # Lancer la génération dans un thread séparé
    show_spinner()  # Démarrer le spinner

root = ctk.CTk()
root.title("AI Image Generator")

ctk.set_appearance_mode("dark")

input_frame = ctk.CTkFrame(root)
input_frame.pack(side="left", expand=True, padx=20, pady=20)

prompt_label = ctk.CTkLabel(input_frame, text="Prompt")
prompt_label.grid(row=0, column=0, padx=10, pady=10)
prompt_entry = ctk.CTkTextbox(input_frame, height=10)
prompt_entry.grid(row=0, column=1, padx=10, pady=10)

model_label = ctk.CTkLabel(input_frame, text="Model")
model_label.grid(row=1, column=0, padx=10, pady=10)
model_dropdown = ctk.CTkComboBox(input_frame, values=["tiny-stable-diffusion-pipe", "tiny-sd"])
model_dropdown.grid(row=1, column=1, padx=10, pady=10)

number_label = ctk.CTkLabel(input_frame, text="# Images")
number_label.grid(row=2, column=0)
number_slider = ctk.CTkSlider(input_frame, from_=1, to=4, number_of_steps=3)
number_slider.grid(row=2, column=1)

generate_button = ctk.CTkButton(input_frame, text="Generate", command=on_click)
generate_button.grid(row=3, column=0, columnspan=2, sticky="news", padx=10, pady=10)

canvas = tkinter.Canvas(root, width=512, height=512)
canvas.pack(side="left")

root.mainloop()
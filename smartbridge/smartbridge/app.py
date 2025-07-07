from flask import Flask, render_template, request, url_for
import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)


model = load_model('model/my_model.keras')

class_names = ['Coccidiosis', 'Salmonella', 'Healthy', 'Newcastle Disease']

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict_page')
def predict_page():
    return render_template('prediction_page.html', prediction=None)

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return render_template('prediction_page.html', prediction="No file uploaded.")

    file = request.files['file']

    if file.filename == '':
        return render_template('prediction_page.html', prediction="No file selected.")

    if file:
        
        upload_folder = 'static'
        if not os.path.exists(upload_folder):
            os.makedirs(upload_folder)

        
        filename = secure_filename(file.filename)
        file_path = os.path.join(upload_folder, filename)
        file.save(file_path)

        try:
            
            img = image.load_img(file_path, target_size=(2, 5)) 
            img_array = image.img_to_array(img)

            gray = np.mean(img_array, axis=2)

            
            img_vector = gray.flatten()

            img_vector /= 255.0

            
            input_vector = np.expand_dims(img_vector, axis=0)

            prediction = model.predict(input_vector)
            predicted_value = prediction[0][0]

            predicted_index = int(round(predicted_value))
            if 0 <= predicted_index < len(class_names):
                predicted_label = class_names[predicted_index]
            else:
                predicted_label = f"Value: {predicted_value:.2f}"

            return render_template('prediction_page.html', prediction=predicted_label)

        except Exception as e:
            print(f"Error: {e}")
            return render_template('prediction_page.html', prediction="Error processing image.")

    return render_template('prediction_page.html', prediction="Unexpected error.")

if __name__ == '__main__':
    app.run(debug=True)

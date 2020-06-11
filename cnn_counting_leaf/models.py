from django.db import models
from django.urls import reverse

import numpy as np
from keras.preprocessing import image
from tensorflow.python.keras.models import load_model, model_from_json
from tensorflow.python.keras.initializers import glorot_uniform
from keras.utils import CustomObjectScope
from keras import backend as K

# Create your models here.
class Regression(models.Model):

    img = models.ImageField(upload_to='images')
    prediction = models.CharField(max_length=200, blank=True)

    def predict(self):

        K.reset_uids()

        model = 'cnn_counting_leaf/model/model.json'
        weights = 'cnn_counting_leaf/model/weights_model.h5'

        with CustomObjectScope({'GlorotUniform': glorot_uniform()}):
            with open(model, 'r') as f:
                model = model_from_json(f.read())
                model.load_weights(weights)

        img = image.load_img(self.img, target_size=(299, 299))

        img = image.img_to_array(img)
        img /= 255
        img = np.expand_dims(img, axis=0)

        result = model.predict(img)

        return "{}".format(result.flatten()[0])


    def save(self, *args, **kwargs):
        self.prediction = self.predict()
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('list')
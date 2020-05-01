from django.db import models

class router(models.Model):
    name : str
    id : int
    d_speed : int
    u_speed : int
    graph_img : str


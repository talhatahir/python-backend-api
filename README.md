# python-backend-api
This is a Python practice project using Python Django Rest API Framework which contains the following Model Entites: 

class images(models.Model):
    image_url = models.CharField(max_length=150)
        
class users(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.CharField(max_length=20)
    cell=  models.CharField(max_length=20)
    user_id= models.IntegerField()

class listings(models.Model):
    title = models.CharField(max_length=50)
    price= models.IntegerField()
    description= models.CharField(max_length=200)
    listing_id=models.IntegerField()
    image =  models.ForeignKey(images, on_delete=models.CASCADE,related_name='image') 
    user =  models.ForeignKey(users, on_delete=models.CASCADE)   
    
    
This API is powering data for a front-end React App
  

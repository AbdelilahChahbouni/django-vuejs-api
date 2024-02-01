import os , django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()

from course.models import Course , Categories , Reviews
import random
from faker import Faker

cat = ["IT" , "DEVELOPMENT" , "MANAGMENT"]
images = os.listdir("media/course_images")
prices = [10 , 20 , 40]

def seek_categorie(number):
    fake = Faker()
    for _ in range(number):
        Categories.objects.create(
            name = fake.name()
        )
    print(f"{number} of categories is Created")


def seek_course(number):
    fake = Faker()
    for _ in range(number):
        Course.objects.create(
            name = fake.name() ,
            subtitle = fake.text(max_nb_chars=50),
            description = fake.text(max_nb_chars=200),
            #price = round(random.uniform(40.99 , 99.99),2),
            price = prices[random.randint(0,2)],
            categorie =Categories.objects.get(id=random.randint(1,3)),
            image ="course_images/"+images[random.randint(0,2)])
    
    print(f"{number} of courses is created successfully")

    











#seek_categorie(30)
seek_course(12)







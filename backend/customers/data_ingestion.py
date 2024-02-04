from django.utils import timezone
from .models import Customer
from faker import Faker
import random
from .choices import GENDER_CHOICES

# Create a Faker instance
fake = Faker()

def seed_db(n):
    for _ in range(n):
        # Generate fake data
        name = fake.name()
        gender = random.choice([choice[0] for choice in GENDER_CHOICES])
        age = random.randint(18, 80)
        favorite_number = random.randint(1, 100)
        # created = timezone.now()

        # Create a Customer object and save it to the database
        customer = Customer.objects.create(
            name=name,
            gender=gender,
            age=age,
            favorite_number=favorite_number,
            # created=created
        )
        print(f"Customer created: {customer}")

# Example usage:
# seed_db(10)  # This will seed the database with 10 records

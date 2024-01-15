from faker import Faker


def make_new_fake_data():
    fake = Faker(locale="ru_RU")
    fake_email = fake.ascii_free_email()
    fake_password = fake.job()
    fake_name = fake.first_name()

    fake_data = {
        "email": fake_email,
        "password": fake_password,
        "name": fake_name
    }

    return fake_data

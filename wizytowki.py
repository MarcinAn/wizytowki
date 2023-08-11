from faker import Faker

fake = Faker()


class BaseContact:
    def __init__(self, name, surname, phone, email_address):
        self.name = name
        self.surname = surname
        self.phone = phone
        self.email_address = email_address
        self._label_len = len(f"{self.name} {self.surname}")

    def contact(self):
        print(f"Wybieram numer {self.phone} i dzwonię do {self.name} {self.surname}")

    def __str__(self):
        return f"{self.name} {self.surname} {self.phone} {self.email_address}"

    @property
    def label_length(self):
        return self._label_len


class BusinessContact(BaseContact):
    def __init__(self, position, company_name, work_phone, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.position = position
        self.company_name = company_name
        self.work_phone = work_phone

    def contact(self):
        print(
            f"Wybieram numer {self.work_phone} i dzwonię do {self.name} {self.surname}"
        )

    def __str__(self):
        return f"{self.name} {self.surname} {self.position} {self.company_name} {self.work_phone} {self.email_address}"


def create_contacts(contact_type, number_of_contacts_to_generate):
    contacts = []
    if contact_type == "base":
        for i in range(number_of_contacts_to_generate):
            contacts.append(
                BaseContact(
                    fake.first_name(),
                    fake.last_name(),
                    fake.phone_number(),
                    fake.ascii_email(),
                )
            )
    elif contact_type == "business":
        for i in range(number_of_contacts_to_generate):
            contacts.append(
                BusinessContact(
                    fake.job(),
                    fake.company(),
                    fake.phone_number(),
                    fake.first_name(),
                    fake.last_name(),
                    fake.phone_number(),
                    fake.ascii_email(),
                )
            )
    return contacts


if __name__ == "__main__":
    base = create_contacts("base", 5)
    for contact in base:
        print(contact)
    business = create_contacts("business", 5)
    for contact in business:
        print(contact)

from faker import Faker

fake = Faker()


class BaseContact:
    def __init__(self, name, surname, phone, email_address):
        self.name = name
        self.surname = surname
        self.phone = phone
        self.email_address = email_address
        self.label_len = len(f"{self.name} {self.surname}")

    def contact(self):
        print(f"Wybieram numer {self.phone} i dzwonię do {self.name} {self.surname}")

    @property
    def label_length(self):
        return self.label_len


class BusinessContact(BaseContact):
    def __init__(self, position, company_name, work_phone, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.position = position
        self.company_name = company_name
        self.work_phone = work_phone
        self.label_len = len(f"{self.name} {self.surname}")

    @property
    def label_length(self):
        return self.label_len


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
    base_contacts = [
        BaseContact("Bryan", "Tackett", "123-234-3456", "BryanNTackett@dayrep.com"),
        BaseContact("Steven", "Richard", "234-345-4567", "StevenRRichard@teleworm.us"),
        BaseContact("Bessie", "Gilbert", "345-456-5678", "BessieCGilbert@rhyta.com"),
        BaseContact("Maryjane", "Lee", "456-567-6789", "MaryjaneJLee@armyspy.com"),
        BaseContact("Deanna", "Smith", "567-678-7890", "DeannaDSmith@teleworm.us"),
    ]
    business_contacts = [
        BusinessContact(
            "Passenger booking clerk",
            "Wag",
            "201-729-4926",
            "Irene",
            "Richardson",
            "111-111-1111",
            "IreneGRichardson@jourrapide.com",
        ),
        BusinessContact(
            "Pilates instructor",
            "Jay Jacobs",
            "208-352-0154",
            "Theodore",
            "Sutton",
            "222-222-2222",
            "TheodoreSSutton@armyspy.com",
        ),
        BusinessContact(
            "Support specialist",
            "Red Bears Tavern",
            "812-553-2570",
            "William",
            "Turner",
            "333-333-3333",
            "WilliamNTurner@jourrapide.com",
        ),
        BusinessContact(
            "Illustrator",
            "Del Farm",
            "773-678-5460",
            "Donald",
            "Albright",
            "444-444-4444",
            "DonaldDAlbright@teleworm.us",
        ),
        BusinessContact(
            "Business management consultant",
            "Mr. Clark's Appliances",
            "918-384-6852",
            "Florence",
            "Goodwin",
            "555-555-5555",
            "FlorenceMGoodwin@teleworm.us",
        ),
    ]

    generate_contact = create_contacts("base", 5)
    generate_contact[1].contact()

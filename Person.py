from datetime import date

class Person:
    def __init__(self, name, country, dob_year, dob_month, dob_day):
        self.name = name
        self.country = country
        self.dob = date(dob_year, dob_month, dob_day)

    def age(self):
        today = date.today()
        years = today.year - self.dob.year

        # if birthday hasn’t happened yet this year
        if (today.month, today.day) < (self.dob.month, self.dob.day):
            years -= 1

        return years


if __name__ == "__main__":
    p = Person("Aaron", "Ireland", 2004, 1, 1)
    print("Age:", p.age())
class Contact:
    """classes generate new instances of contacts
    __init__ method allows us to define properties for our objects.
    methods have an extra variable added to the beginning of the variable i.e self.
    """
    contact_list = [] 
    def __init__(self, first_name,last_name,phone_number,email):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.email = email
# BDD of contacts
#create new contacts with properties
#save,display,delete and dispaly contacts

def setUp(self):
    self.new_contact = Contact("mary", "chuda", "0712345678", "jkim@co.ke")
    
def test_init(self):
    self.assertEqual(self.new_contact.first_name,"mary")
    self.assertEqual(self.new_contact.last_name,"chuda")
    self.assertEqual(self.new_contact.phone_number,"0712345678")
    self.assertEqual(self.new_contact.email,"jkim@co.ke")
    
if __name__ ==  '__main__':
    unittest.main()
        
    
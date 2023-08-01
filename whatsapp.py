import pywhatkit
# sending whatsapp message to a contact
# pywhatkit.sendwhatmsg(
#     phone_no="+91 9xxxxxxxxx",
#     message="Test",
#     time_hour=16,
#     time_min=41
# )
phone_number = input("Enter phone number")
pywhatkit.sendwhatmsg(phone_number, "Test", 17, 16)
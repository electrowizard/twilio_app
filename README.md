## Flask and Twilio Text Messaging Demo

A bare minimal Flask python application that receives a text message and responds by notifying the country with which the originating number is registered.

1. Create a free account on [Twilio](http://twilio.com/) and log into your [console](http://twilio.com/console). Get an available number with SMS capabilities from the [Buy a Number](https://www.twilio.com/console/phone-numbers/search) section on the dashboard. Even though the number says it costs $1, you can purchase it using the free account.

2. The free account will allow you to test only with pre-verified numbers, and hence prevent spam. To verify the number you are testing with, go to [Verified Caller IDs](https://www.twilio.com/console/phone-numbers/verified) and add your number that you are using to test. The Twilio service is capable of sending either a text message or a voice call to complete the verification. Once the verification is complete, you can use your verified number to test with the number you have selected from Twilio.

3. Install the dependencies 

   `pip install twilio flask`

4. Download [ngrok](https://ngrok.com/download) and run on the same port as the Python Flask instance.

    `./ngrok http 8888` 

   The ngrok should return generate a URL

   ![alt text](https://raw.githubusercontent.com/electrowizard/twilio_app/master/img/ngrok_image.png)

5. Note down the ngrok URL generated after starting ngrok and update this URL after adding `/sms` route in the Twilio portal. 

   - Go [here](https://www.twilio.com/console/phone-numbers/incoming) and select the number you have obtained from Twilio. 
   - In the Messaging tab, choose **Webhook** and add the URL, which should be something like `http://xxxxxxxx.ngrok.io/sms`

6. Note the `account_sid`, `auth_token` and `phone number` from the [Twilio console](https://www.twilio.com/console)

   ![alt text](https://raw.githubusercontent.com/electrowizard/twilio_app/master/img/auth_image.png)

7. At this point, the Twilio service is all set. You can run the python application.

   ```bash
   python send_sms.py
   ```

8. To test your service, you can send a text message a.k.a. [SMS](https://en.wikipedia.org/wiki/SMS) from your verified number to the Twilio number, with any random body in the text. You should get a response from Twilio mentioning which country your phone number is registered in.



#### Troubleshooting Tips

- Ensure that your webhook is correctly setup. If you are using the free ngrok account, then every time you restart the ngrok service, the URL will change. You have to remember to update the webhook [here](https://www.twilio.com/console/phone-numbers/incoming).
- You can set `debug = False` on the Flask App. This will throw any exceptions during the execution of the flask handlers.
- Instead of sending an SMS every time to test your application, you can go to your ngrok's default **Inspect**  URL, which is usually `http://localhost:4040/inspect/http`. You can then use the replay option on ngrok to simulate an incoming SMS to your python app. SWEET!  
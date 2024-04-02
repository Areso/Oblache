---
Case ID: TC1
Module: /register
Description: Successful registration of new user
Priority (High, Medium, Low): High
Preconditions: user credentials from service admin
Test Data: login = actual email, password = valid password

---
**Steps**
1. Open https://oblache.areso.pro/
2. Click "Register" button.
3. Click "Register" tab in Registration form.
4. Fill in "Email" field with actual user email.
5. Fill in "Password" field with password
6. Click on checkbox "Terms of Use"
7. Click "Register" button

**Expected Result**
1. Page https://oblache.areso.pro/ is opened
2. Registration form is opened
3. Registration form with checkbox "Terms of Use" and "Register" button is opened
4. Inputted email is displayed in "Email" field
5. Password-mask is displayed in "Password" field
6. Checkbox is checked
7. Message "registered successfully" is displayed
   
**Link to Report**
https://areso.github.io/Oblache/


---
Case ID: TC2
Module: /register
Description: Failed registration of new user with invalid password
Priority: High
Preconditions: user credentials from service admin
Test Data: login = actual email, password = invalid password

---

**Steps**
1. Open https://oblache.areso.pro/
2.Click "Register" button.
3.Click "Register" tab in Registration form.
4.Fill in "Email" field with actual user email.
5.Fill in "Password" field with invalid password.
6.Click on checkbox "Terms of Use".
7.Click "Register" button.

**Expected Result**
1. Page https://oblache.areso.pro/ is opened. 2.Registration form is opened. 3.Registration form with checkbox "Terms of Use" and "Register" button is opened. 4.Inputted email is displayed in "Email" field. 5.Password-mask is displayed in "Password" field. 6.Checkbox is checked. 7.Message "Registration failed. The email is taken" is displayed.
Link to Report: https://areso.github.io/Oblache/

---
Case ID: TC3
Module: /register
Description: Failed registration of new user with taken email
Priority: High
Preconditions: user credentials from service admin
Test Data: login = already used actual email, password = valid password

**Steps**
1.Open https://oblache.areso.pro/  2.Click "Register" button. 3.Click "Register" tab in Registration form. 4.Fill in "Email" field with already taken email. 5.Fill in "Password" field with valid password 6.Click on checkbox "Terms of Use". 7.Click "Register" button.
**Expected Result**
1. Page https://oblache.areso.pro/ is opened. 2.Registration form is opened. 3.Registration form with checkbox "Terms of Use" and "Register" button is opened. 4.Inputted email is displayed in "Email" field. 5.Password-mask is displayed in "Password" field. 6.Checkbox is checked. 7.Message "Registration failed. The email is taken" is displayed.
Link to Report: https://areso.github.io/Oblache/

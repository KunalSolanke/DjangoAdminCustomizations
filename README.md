

# Django Admin Customization

Imp files 
- AdminCutomzation/admin.py
  - this file has the custom admin site class extending from the django admin site class
     New url and actions for admin are in this file 
     For example fuctions page and the send mail action,Also the backend code of user metrics
     
 - templates 
   - admin/function.html
      this is the functions page of the site from which mails to all users can be sent
   - admin/index.html
       jinga code for user metrics added 
       
 - accounts
     - models : User model
     - managers.py : UserManager
     - modeladmin : UserAdmin which has code for change status action
     
     
     


### Useful pics

#### Functions page
<img src= "./Screenshots/functions_page.png"></img>
#### send mail
<img src= "./Screenshots/send_mail.png"></img>

#### Mail Form
<img src= "./Screenshots/mail_form.png"></img>

#### User Metrics
<img src= "./Screenshots/user_metrics.png"></img>


#### Change Status

<img src= "./Screenshots/change_status.png"></img>
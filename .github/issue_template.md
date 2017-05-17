### Task
---
To create a way to enter and store a customer's payment information using the Bangazon CLI App.

### Context
---
An option for entering customer payment options is needed in the Bangazon CLI so that customers can pay for their order with their preferred payment method. If you need to refer to the project ERD then click [here](https://github.com/EducatedCamels/Educated_Camels_Company_Docs/blob/master/resources.md).
### The process 
---
- [ ] If you do not have the current master, pull down CLI-Bangazon-App Project onto your local computer and create a new git branch
- [ ] In the appropriate file, create Payment class with properties listed in ERD. Assign the following related methods to AdminTask Class: addPaymentType, deletePaymentType, others TBD.
- [ ] Be sure to include properties for "Payment Type" and "Payment Account Number." Both should accept a string.
-  [ ] In testing file, create unit tests to test every method relevant to the Payment Class.
-  [ ] Run tests to ensure that all methods relevant to Payment Class pass and return what you expect them to.

### Outcome/expected behavior
---
User should be able to add a payment option type once they have chosen an "Active Customer."

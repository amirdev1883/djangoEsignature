# Python assignment

## Requirements

The objective of this assignment is to develop a small Django application that integrates with a 3rd party
API in order to handle the process of creating, signing, and storing digitally managed agreements.

### 3rd Party API Information

* The service provider is called Docusign, it provides solutions for drafting contracts and
    sending them to the signing parties to collect digital signatures
  *  Link to useful documentations

     https://developers.docusign.com/docs/esign-rest-api/

     https://developers.docusign.com/docs/esign-rest-api/how-to/ 


* Sample code by Docusign: https://developers.docusign.com/docs/esign-rest-api/how-
to/code-launchers/
▪ The direct Git Repo link:
• https://github.com/docusign/code-examples-python

### Tasks at hand

#### Django App: Contract Signing Platform

### Brief Description of Tasks
The objective is to create a Django app that enables a user to register, log in, and sign a pre-defined contract. The contract will have two signing parties:
- The first party is the user who logs in and signs the contract.
- The second party is invited via email to sign the contract.

---

## User Stories

### 1. User Registration
**As a user, I want to register, so that I can log in to use the signing features of the app.**

#### Acceptance Criteria
- Basic Django authentication (session authentication) is sufficient.
- Username and password are enough for registration.
- No extra validation is required for password or username.
- Upon logging in, the user should be directed to the **Contract Instantiation Page**.

---

### 2. User Login
**As a user, I want to log in, so that I can use the signing features of the app.**

#### Acceptance Criteria
- Log in using a username and password.
- No extra validation is required for password or username.
- Upon logging in, the user should be directed to the **Contract Instantiation Page**.

---

### 3. Contract Instantiation
**As a user, I want to instantiate a new contract, so that I can define its signing parties (signatories) and have it signed.**

#### Acceptance Criteria
- The contract instantiation is done on a page view (**Contract Instantiation Page**) that:
  - Displays the contract made up of placeholder text (`"Lorem Ipsum..."`).
  - Includes three empty fields for recipients to fill in: 
    - Full name
    - Date
    - Signature
  - Automatically includes the logged-in user as one of the signatories.
  - Collects an email address for the second signatory (invited via email).

---

### 4. User Signs the Agreement
**As a user, I want to sign the agreement after it’s instantiated, so that I can complete it digitally and send it out to the other recipient for signing.**

#### Acceptance Criteria
- After instantiating the contract on the **Contract Instantiation Page**, the user is directed to a page displaying the **Docusign Agreement**.
- The page shows the agreement with:
  - Placeholder text (`"Lorem Ipsum..."`)
  - Empty fields for the user’s:
    - Full name
    - Date
    - Signature
- Upon completing the agreement:
  - The user is redirected to another page showing a success message.
  - The second signatory receives an email with a link to sign the agreement.
